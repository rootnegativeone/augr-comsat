import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init
from travelDuration import light_travel_time
from tqdm import tqdm
import time

# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for the client
client_color = random.choice(colors)

# server's IP address
# if the server is not on this machine,
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = "3.99.240.72"
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

# SETUP
print("Enter callsign, origin, and destination to open an communication channel.")
callsign = input("Callsign: ")
originLocation = input("Origin: ")
destinationLocation = input("Destination: ")

# TIME CALCULATION(S)
travelTime = light_travel_time(originLocation, destinationLocation)

# Reflect configuration to user
# Convert to whole minutes and remaining seconds
minutes = int(travelTime)
seconds = int((travelTime - minutes) * 60)

print("Callsign", "|", "Origin", "|", "Destination", "|", "Travel Time")
print(callsign, "|", originLocation, "|", destinationLocation, "|", f"{minutes}m {seconds}s")

# RECEIVING
def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

# SENDING
while True:
    # input message we want to send to the server
    to_send =  input()
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {callsign}{separator_token}{to_send}{Fore.RESET}"
    # finally, send the message
    s.send(to_send.encode())

    # Simulate delay using tqdm progress bar
    for _ in tqdm(range(minutes * 60 + seconds), desc="Message Progress"):
        time.sleep(1)  # Sleep for 1 second between iterations

# close the socket
s.close()

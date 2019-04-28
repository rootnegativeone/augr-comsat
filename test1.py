#! C:\Anaconda\envs\web\python.exe
# coding: utf-8
# **Web Control**


from selenium import webdriver
import time

# Using Chrome to access web
# The executable path is wherever you saved the chrome webdriver
chromedriver = "C:\\Anaconda\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver)

# test 1 
# test parameter definitions
Prediction = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N"
Delay = "06/01/2019"
Email = "name@domain.com"

# open the website
driver.get("http://outis.io")

# find prediction box and enter test string
PredictionText = driver.find_element_by_name("prediction")
PredictionText.send_keys(Prediction)

# find delay box and enter time in the future
DelayText = driver.find_element_by_name("delay")
DelayText.send_keys(Delay)

# find email box and enter email address
EmailText = driver.find_element_by_name("email")
EmailText.send_keys(Email)

# fix HTML so that commit button has ID
# find and click "Commit" button
#CommitButton = driver.find_element_by_id('<what is the name of this button>')
#CommitButton.click()

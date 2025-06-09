import time 
import pyautogui

def take_screenshot():

    name =int(round(time.time()*1000))  # Get the current time in milliseconds
    name= 'C:/Users/YASIR787/Downloads/python learning/New folder/screenshot/screenshot/screenshots data/{}.png'.format(name)  # Format the path for the screenshot and also the name of the screenshot file

    time.sleep(5)  # Wait for 5 seconds before taking the screenshot
    img= pyautogui.screenshot(name)  # Take a screenshot

    img.show()  # Display the screenshot
    
    
take_screenshot()  # Call the function to take a screenshot
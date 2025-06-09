import time 
import pyautogui
import tkinter as tk



def take_screenshot():

    name =int(round(time.time()*1000))  # Get the current time in milliseconds
    name= 'C:/Users/YASIR787/Downloads/python learning/New folder/screenshot/screenshot/screenshots data/{}.png'.format(name)  # Format the path for the screenshot and also the name of the screenshot file

    time.sleep()  # Wait for 5 seconds before taking the screenshot
    img= pyautogui.screenshot(name)  # Take a screenshot

    img.show()  # Display the screenshot
    
    
root = tk.Tk()  # Create a Tkinter window
frame = tk.Frame(root)  # Create a frame in the window
frame.pack()  # Pack the frame into the window
button = tk.Button(frame, text='Take Screenshot', command=take_screenshot)  # Create a button that will take a screenshot when clicked
button.pack(side=tk.LEFT )  # Pack the button into the frame
close = tk.Button(frame, text='Close', command=quit)  # Create a button to close the application
close.pack(side=tk.LEFT)  # Pack the close button into the frame
root.mainloop()  # Start the Tkinter event loop
# The code creates a simple GUI application using Tkinter that allows the user to take a screenshot after a 5-second delay.

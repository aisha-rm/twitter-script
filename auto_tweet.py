"""Program to send a tweet on Twitter using Python"""

import webbrowser   # to launch default browser
import time  #to create little delays between keys
import win32com.client  # to establish shell

#Creating a connection to Windows shell.
shell = win32com.client.Dispatch("WScript.Shell")

tweet = """First attempt at automated tweet using Python #Coding #Python """

#launch twitter and allow some delay
webbrowser.open("https://twitter.com")
time.sleep(7)

#new tweet window, allow 1 second delays to allow browser register key strokes
shell.SendKeys("n", 0)  #n is shortcut for new tweet on twitter
time.sleep(1)

#typing new tweet 
shell.SendKeys(tweet, 0)
time.sleep(1)

#send the new tweet
shell.SendKeys("^{ENTER}", 0)   #CTRL + ENTER sends tweet
time.sleep(1)


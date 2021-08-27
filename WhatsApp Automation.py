
# Make sure to close all the tabs in safari except WhatsApp Web
# The code that helps to print the position of the mouse pointer are as follows,
#time.sleep(10)
#print(pyautogui.position())
# place the curser in the position for 10sec in the desired location to get its x and y coordinates.


# Contact List Starts.

all_contacts = {'Amma': 'Amma', 'Daddy': 'Daddy',
                'Akash Thambi': 'bro', 'Selvi Bedha': 'Bedha', 'Avva': 'Avva', # Bedhadaddy???
                'Nandha': 'Nandha', 'Bharathi Anni': 'Anni', 'Malliga Athai': 'Athai',
                'Poornima': 'Poorni', 'Rajeshwari Athai': 'Athai',
                'Ramya Akka': 'Ramya Akka', 'Nishanth': 'Nishanth',
                'Mohan (Monny)': 'Mohan', 'Swetha Akka': 'Swetha Akka', 'Chandru Uncle': 'Chandru Uncle', 'Uma Aunty': 'Uma Aunty', 'Sandeep Swetha': 'Sandeep anna',
                'Ramesh Chithappa': 'Chithappa', 'Jayanthi Chithi': 'Chithi', 'Naveen Bro': 'Naveen',
                'Rajesh Anna': 'Rajesh Anna', 'Ramya Rajesh': 'Ramya Akka', 'Bagyam Bedha': 'Bedha', 'Prabakar Bedhadaddy': 'Bedhadaddy',
                'Sabari Anna': 'Sabari Anna', 'Karuna Aunty': 'Karuna Aunty', 'Kasthuri Avva': 'Kachavva',
                'Shankar Ganesh': 'Dude', 'Karuppusamy': 'Karuppa', 'Panda': 'Panda', 'RamPrakash': 'Ram ji', 'Rahul': 'Rahul', 'Kavin': 'Kavin', 'Gokul (SRV)': 'Gokul',
                'Praveen Bro': 'Bro', }


# Contact List Ends.


import pyautogui   # It is important to import this module. You can install it using "pip install pyautogui" in terminal
import webbrowser
import time

webbrowser.open('https://web.whatsapp.com')

# This for-loop will run through every name in the send_to variable.
for i, j in send.items():               # the .items() is important to unpack values from a dictionary
    message = (f"Hi {j}, pimbilikka pilaapi.")
    time.sleep(10)                       # Waiting time till the browser loads
    pyautogui.click(143, 186)           # Open contact search bar
    pyautogui.typewrite(i)              # Type names
    time.sleep(3)                       # Waiting time for contact to load
    pyautogui.click(134, 319)           # Open specific contact
    pyautogui.click(599, 798)           # Click on input field
    pyautogui.typewrite(message)        # Message typed in
    time.sleep(1)                       # Waiting time
    # pyautogui.click(1403, 793)          # Send message
    pyautogui.click(401, 191)           # Close contact search bar


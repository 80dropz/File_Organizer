import time
from discord_webhook import DiscordWebhook
import random
import os
webhook = input("Paste your webhook here: ")
print("sending test")
code = random.randint(1000, 9999)
codes = str(code)
sendhook = DiscordWebhook(url=webhook, content=code)
sendhook.execute()
print(code)
check = input("Enter code: ")
checker = f"Enter code: {code}"
if codes in check:
    logf = open("log.txt", "w")
    logf.write(f"Webhook: {webhook}")
else:
    print("Wrong code")
    exit()

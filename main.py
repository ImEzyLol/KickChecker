import tls_client
import json

def validate_kick_username(username, webhook_url=None):
    session = tls_client.Session(client_identifier="chrome112")
    r = session.get(f"https://kick.com/api/v2/channels/{username}")

    if r.status_code == 404:
        message = f"[Ezy's Checker] | Username '{username}' is claimable."
        send_to_webhook(message, webhook_url)
        print(message)
        return False

    message = f"[Ezy's Checker] | Username '{username}' is not claimable."
    send_to_webhook(message, webhook_url)
    print(message)
    return True

def send_to_webhook(message, webhook_url):
    if webhook_url:
        data = {
            "content": message
        }
        session = tls_client.Session(client_identifier="chrome112")
        session.post(webhook_url, json=data)


with open("users.txt", "r") as file:
    usernames = file.read().splitlines()

print("[Ezy's Checker] | If you like this please join : discord.gg/meSxCAWXvQ\n")
webhook_url = input("[Ezy's Checker] | Enter webhook URL (optional): ")


for username in usernames:
    validate_kick_username(username, webhook_url)

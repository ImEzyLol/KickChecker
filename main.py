
import tls_client
import concurrent.futures

def validate_kick_username(username, webhook_url=None):
    r = session.get(f"https://kick.com/api/v2/channels/{username}")

    if r.status_code == 404:
        message = f"[Ezy's Checker] | Username '{username}' is claimable."
        print(message)
        if webhook_url:
            send_to_webhook(message, webhook_url)
        return False

    message = f"[Ezy's Checker] | Username '{username}' is not claimable."
    print(message)
    return True

def send_to_webhook(message, webhook_url):
    data = {
        "content": message
    }
    session.post(webhook_url, json=data)

if __name__ == "__main__":
    with open("users.txt", "r") as file:
        usernames = file.read().splitlines()

    print("[Ezy's Checker] | If you like this please join : discord.gg/meSxCAWXvQ\n")
    webhook_url = input("[Ezy's Checker] | Enter webhook URL (optional): ")

    # Create a session object
    session = tls_client.Session(client_identifier="chrome112")

    # Use ThreadPoolExecutor for concurrent processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit username validations to the executor
        futures = [executor.submit(validate_kick_username, username, webhook_url) for username in usernames]

        # Wait for all validations to complete
        concurrent.futures.wait(futures)

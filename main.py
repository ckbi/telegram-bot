import time
import requests
import json

def send_message():
    
    bot_token = 'your bot token here'
  
    chat_id = 'your chat id here'
    message = 'Your message here'

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'}) 
#here it prints into the terminal to show the results
    if response.status_code != 200:
        print(f"something went wrong message didnt send : {response.text}")
    else:
        print("message sent successfully")

while True:
    send_message()
    time.sleep(6000)

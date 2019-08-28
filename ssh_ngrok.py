import telegram
import subprocess
import requests
import json
import time
import psutil

if __name__ == '__main__':
    PROCNAME = "ngrok"

for proc in psutil.process_iter():
	if proc.name() == PROCNAME:
		proc.kill()
    
ngrok = subprocess.Popen(['ngrok','tcp','22'], 
                             stdout=subprocess.PIPE)
time.sleep(3)
localhost_url = "http://localhost:4040/api/tunnels"
tunnel_url = requests.get(localhost_url).text 
j = json.loads(tunnel_url)
tunnel_url = j['tunnels'][0]['public_url'] 

def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    
test = telegram_bot_sendtext(tunnel_url)


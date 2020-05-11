## Remote SSH (with no port fordwarding)
A little python script which lets you ssh into your device without configuring port forwarding. This isn't a viable solution for manage servers and it only should be used in testing environments, you should always configure port forwarding and firewall according to your needs.

## How does it work?
Basically Ngrok allows you to create secure tcp tunnels to ports on your server without needing to configure the port forwarding rules. In fact this isn't a proper SSH connection, but it's more a shell over https. I'm using Telegram cause it's free and it's a good way to communicate the address to SSH too. Theoretically you can even use Twilio APIs to send a SMS but it's not free hence me choosing Telegram. I used to use this to manage my grandma's Ubuntu Laptop since we lived in different cities.

## Getting Started

### Requirements

* A SSH server running on a Linux machine on port 22.
* `telegram` Python library.
* `psutil` Python library.
* A `ngrok` account.

### Instructions

* On Telegram create a new bot by using @BotFather and get the Token.
* Click on [this link](https://api.telegram.org/bot(YourBotToken)/getUpdates), substitute the token in the url and refresh the page. You should be getting a JSON: you need to note down the ChatID field.
* Follow the instruction on https://ngrok.com/download (the script assumes that `ngrok` is available in $PATH on Linux),
* Clone the repository: `git clone https://github.com/XxXTommyXxX/RemoteSSH`.
* CD into it: `cd XxXTommyXxX/RemoteSSH`.
* Install `psutil` and `telegram` libraries in your home project `pip3 install psutil telegram`.
* Edit the script variables `bot_token`, `bot_chatID`.
* Start the bot on Telegram.
* Run the script: `python3 ssh_ngrok.py`.
* A tcp://foo.bar:12345 should pop up.
* Now you can ssh to your device: `ssh user@foo.bar -p 12345`.

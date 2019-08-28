# Project Title

RemoteSSH

## Description

A little python script which lets you ssh into your device without configuring port forwarding.

## Getting Started

### Dependencies

* `telegram` Python library.
* `psutil` Python library.

### Instruction

* On Telegram create a new bot by using @BotFather and get the Token.
* Browse on https://api.telegram.org/bot<YourBOTToken>/getUpdates and get the chatid variable.
* Follow the instruction on https://ngrok.com/download (the script assumes that `ngrok` is available in $PATH on Linux)
* Clone the repository: `git clone https://github.com/XxXTommyXxX/RemoteSSH`.
* CD into it: `cd XxXTommyXxX/RemoteSSH`.
* Install `psutil` and `telegram` libraries: `pip3 install psutil telegram`.
* Edit the script variables `bot_token`, `bot_chatID`.
* Start the bot on Telegram.
* Run the script: `python3 ssh_ngrok.py`.
* A tcp://foo.bar:1234 should pop up.

## Author

[@xo.chiti](https://www.instagram.com/xo.chiti/)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

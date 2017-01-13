# Simple python Telegram bot

## _Important thing to start_

To start working with bot, first you need is to add file config.py with two main variables: <br>
```python
URL = 'http://api.telegram.org/bot' # to send request to Telegram server
TOKEN = <Bot_token_from_@BotFather> # Token to connect to your bot
ADMIN_ID = (list with group admins id)
ADMIN_NAME = <creator's name string>
```
_Make sure that you have fortune._
```bash
pacman -S fortune-mod # Arch
sudo apt-get install fortune # Ubuntu
```
## _Dependencies_

```bash
pip install requests --upgrade
pip install PyGithub --upgrade
pip install sqlite3 --upgrade
```

## _Help (Features)_

__/user_repos <Git_user>__ — print all user's repositories. _Format: id: "full/name" (fork*)_ <br>
__/important__ — most important news by admin<br>
__#важно__ — admin can set important News for group<br>
__date (дата)__ — print full current date and time.


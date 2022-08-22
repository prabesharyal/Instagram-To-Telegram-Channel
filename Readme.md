# Instagram-To-Telegram-Channel

A bot to scrap your instagram feed and post to your Telegram Channel in certain Interval.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/prabesharyal/Instagram-To-Telegram-Channel/tree/main/)

# Table of Contents
 1. [Introduction](#1)
    1. [About Bot](#1.1)
	2. [Working Principle](#1.2)
 2. [Knowing All Variables](#2)
	1. [BOT Token](#2.1)
    2. [Channel ID](#2.2)
	3. [Other Notable Variables](#2.3)
 4. [Requirements](#3)
    1. [Python](#3.1)
		1. [PIPs](#3.1.1)
 5. [Deploy](#4)
 6. [License](#lic)


# Read this throughly before deploying the bot: <a name="1"></a>

## What is this bot about?<a name="1.1"></a>
This bot is make specifically for one purpose. That is to monitor your Instagram Feed and send defined number of Photos and Videos to you in Telegram at the time interval you specify.

## How does this bot work?<a name="1.2"></a>
> **This bot works in various steps as :**
> - It scrapes your Instagram Feed.
> - Tries to clean captions (beta stage).
> - Send Caption
> - And Sends Separate Album
> - Also, it sends an empty sticker to distinguish between posts.
		
# Get Variables <a name="2"></a>

## Bot Token <a name="2.1"></a>
 - You can get Telegram Bot Token from [BotFather](https://t.me/@BotFather) bot on telegram.
 
## Getting Channel ID <a name="2.2"></a>
- **To get Channel ID, first go to your channel in Telegram and perform steps mentioned below.**
- Send a Message to channel and copy link of that Telegram Channel Post.
> - Then your link looks like this : `https://t.me/c/1617181920/369`
> - Note that long number of 10 digits and add -100 in beginning and it must look like: `-1001617181920`
> - This is your Channel ID (including `-` sign.)

 
## Other Variables <a name="2.3"></a>
There are some other variables which you need to note about.
### Instagram Credentials
- > Instagram Username and Password

### Variables as configured in bot. <a name="environ"></a>
- `ig_username` - Enter your Instagram 'Username'
- `ig_password` - Enter your Instagram 'Password'
- `BOT_API_TOKEN` - Enter Bot API Token which you get from Botfather in Telegram.
- `channel` - Enter [Channel ID](#2.2) of your Telegram Channel where you want to send posts.
- `every_x_minutes` - Enter Time Period at which you want to srape your feed regularly (IN MINUTES)
- `no_of_posts` - Enter how much posts to be scraped at above time.
- `Welcome_Message` - Enter some string or welcome message so that you'll know that bot has started working in your channel.
- `secret_command` - Enter a secret command which you'll send to bot in order to activate. Don't include / here but you must use in Telegram.
- `every_post_caption` - Enter a Caption for every posts you sent to Telegram in image. Can be your channel username or some emoji.

# Required Softwares and Languages <a name="3"></a>

## Python <a name="3.1"></a>
> Download Python From here :
> - [Python Latest Version](https://www.python.org/downloads/)

> *While installing, tick install **path / environment** variables whatever is given*

### Python Snippets <a name="3.1.1"></a>
- **Install required python modules using commands below:**
> - `pip install instaloader`
> - `pip install python-telegram-bot --pre`

- __Install all above modules using :__
> - `pip install -r requirements.txt`


# Deploying the bot <a name="4"></a>

## Deploying Locally
- Install Python, PIPs using [above methods](#3)
- Download all files in this repo.
- Replace variables at the top of `bot.py` file with your ones, removing `os.environ.get('name')` commands.

> Type ***any one*** of the following command on terminal to run bot:
> - `py bot.py`
> - `python bot.py`
> - `python3 bot.py`

## Deploying to HEROKU :
Press the button below or at the top of this readme and insert necessary [environment variables](#environ) and you're done.
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/prabesharyal/Instagram-To-Telegram-Channel/tree/main/)

# License <a name="lic"></a>
> Distributed Under GPL or MIT License by [@PrabeshAryalNP](https://t.me/prabesharyalnp) on [social](https://twitter.com/prabesharyalnp) or [@PrabeshAryal](https://github.com/prabesharyal) on code sites.
		
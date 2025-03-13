# SoundCloud Download Bot
![SoundCloud Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Soundcloud_logo.svg/2880px-Soundcloud_logo.svg.png)
A Telegram bot for downloading tracks from SoundCloud, developed in Python using aiogram 3 and SQLite3.

## Description

This bot allows users to download tracks from SoundCloud directly through Telegram. It provides an easy and convenient way to access music without leaving the chat.

## Features

- Track download from SoundCloud
- User-friendly Telegram interface
- SQLite3 database for storing user data and history
- Error handling and logging

## Technologies

- Python 3.x
- aiogram 3
- SQLite3

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/jamshid6573/SoundCloud-Downloader.git
```

2. Navigate to the project directory:

```bash
cd SoundCloudDownloader
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # for Linux
venv\Scripts\activate  # for Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Set up your Telegram bot token and SoundCloud API credentials in the `.env` file.

6. Run the bot:

```bash
python bot.py
```

## Usage

- Send a SoundCloud track link to the bot
- The bot will download and send the track back to you

## License

MIT License

## Contact

If you have any questions or suggestions, contact me at: [jamshid125200@gmail.com](mailto:jamshid125200@gmail.com)

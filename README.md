# Telegram Bot for Downloading Tracks from SoundCloud

![SoundCloud Logo](https://upload.wikimedia.org/wikipedia/commons/7/78/Soundcloud_logo.svg)  
*Download music from SoundCloud directly via Telegram!*

This project is a Telegram bot that allows users to download tracks from SoundCloud by simply sending a link to the track. The bot processes the request, downloads the audio file, and sends it back to the user in the chat.

## Features
- Download tracks using a direct SoundCloud link.
- Support for public tracks (private tracks may require authentication).
- Simple and user-friendly Telegram interface.
- Fast request processing.

## Installation

To deploy the bot on your server or locally, follow these steps:

### Prerequisites
- Python 3.8 or higher installed.
- A Telegram account and a bot token from [@BotFather](https://t.me/BotFather).
- A SoundCloud account and API key (Client ID) for track access (if required).

### Setup Steps
1. **Clone the repository:**
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
Install dependencies:



pip install -r requirements.txt
Configure environment variables: Create a .env file in the root directory and add the following lines:

TOKEN=your_token_from_BotFather


### Usage

Send the bot a SoundCloud track link, for example:


https://soundcloud.com/artist/track-name
Wait for processing — the bot will send you the audio file or an error message if the track is unavailable.
Example
User:

https://soundcloud.com/odesza/a-moment-apart

Bot:

Downloading...

(After a few seconds, sends the file a-moment-apart.mp3).

Dependencies
AIOGRAM 3 — for interacting with the Telegram API.
python-dotenv — for managing environment variables.
Full list of dependencies is available in requirements.txt.

Limitations
The bot works only with public SoundCloud tracks.
Some tracks may require SoundCloud API authentication (in development).
Telegram limits file sizes to 50 MB for bots (without Telegram Premium).
Contributing
If you’d like to contribute to the project:

Fork the repository.
Create a new branch (git checkout -b feature/your-idea).
Make your changes and commit them (git commit -m "Added new feature").
Push to your fork (git push origin feature/your-idea).
Create a Pull Request.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code, provided authorship is credited.

Contact
For questions or suggestions, reach out:

Email: jamshid125200@gmail.com
Telegram: @jama_omonov
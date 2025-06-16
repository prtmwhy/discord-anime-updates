# Discord Anime Updates

A small Python bot for Discord that posts anime release information into a channel.

## Features

- Fetches and posts latest anime episode releases
- Configurable via `.env` for Discord token, channel ID, update interval, etc.
- Simple, small project for personal learning

## Installation

1. Clone the repository:
   git clone https://github.com/prtmwhy/discord-anime-updates.git
   cd discord-anime-updates

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file with the required variables:
   DISCORD_TOKEN=your_bot_token
   CHANNEL_ID=your_channel_id
   UPDATE_INTERVAL=60  # in minutes

## Usage

Run the bot:
   python bot.py

The bot will connect to Discord and send anime updates periodically in the specified channel.

## Notes

- Make sure the bot has permission to post messages in the channel.
- You need a working internet connection for fetching updates.

## License

This project is licensed under the MIT License.

## Disclaimer

This is a personal project created solely for learning and experimentation purposes.  
I do not take any responsibility for any misuse or damage caused by others using this code.  
Use it at your own risk.

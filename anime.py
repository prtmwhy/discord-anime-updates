import discord
from discord.ext import tasks, commands
import requests

# Replace TOKEN and JIKAN_API wit your own data.

TOKEN = '[Tama Token]'

ANNOUNCEMENT_CHANNEL_ID = '[Tama channel ID]'  

JIKAN_API = "https://api.jikan.moe/v4/seasons/now"

announced_episodes = set()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def fetch_ongoing_anime():
    try:
        response = requests.get(JIKAN_API)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(f"Unable to fetch ongoing anime (status code: {response.status_code})")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

@tasks.loop(minutes=30)
async def check_anime_updates():
    print("Checking for anime updates.")
    ongoing_anime = fetch_ongoing_anime()
    
    if ongoing_anime:
        channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
        
        for anime in ongoing_anime:
            title = anime['title']
            episodes = anime.get('episodes', None)
            airing_date = anime.get('airing_start', 'Unknown')
            season_year = anime.get('year', None)
            season_name = anime.get('season', None)
            thumbnail = anime['images']['jpg'].get('image_url', None)
            
            current_episode_info = anime.get('broadcast', {}).get('string', 'Unknown')
            
            genres = ', '.join(genre['name'] for genre in anime.get('genres', [])) if anime.get('genres') else None
            status = anime.get('status', None)

            if title not in announced_episodes:
                log_message = (
                    f"\033[96mNew Updates: Eps {episodes}\033[0m, \033[92m{title}\033[0m"
                )
                print(log_message)

                embed = discord.Embed(title=f"New Episode: {title}!", color=0x00ff00)

                if episodes:
                    embed.add_field(name="Episodes", value=episodes, inline=True)
                if season_name:
                    embed.add_field(name="Season", value=season_name, inline=True)
                if season_year:
                    embed.add_field(name="Year", value=season_year, inline=True)
                if genres:
                    embed.add_field(name="Genre", value=genres, inline=True)
                if status:
                    embed.add_field(name="Status", value=status, inline=True)
                if current_episode_info and current_episode_info != 'Unknown':
                    embed.add_field(name="Next Episode Airing", value=current_episode_info, inline=False)
                if thumbnail:
                    embed.set_image(url=thumbnail)

                await channel.send(embed=embed)

                announced_episodes.add(title)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    check_anime_updates.start()

bot.run(TOKEN)

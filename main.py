import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

music_queue = []

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def play(ctx, url):
    if not ctx.author.voice:
        await ctx.send("You must be in a voice channel to use this command!")
        return

    if not ctx.voice_client:
        channel = ctx.author.voice.channel
        await channel.connect()

    ydl_opts = {'extract_flat': 'in_playlist', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    if 'entries' in info:
        for entry in info['entries']:
            music_queue.append(entry['url'])
        await ctx.send(f"🎶 Playlist added to queue: {info['title']} ({len(info['entries'])} songs)")
    else:
        music_queue.append(url)
        await ctx.send(f"🎶 Song added to queue: {info['title']}")

    if not ctx.voice_client.is_playing():
        await play_next(ctx)


async def play_next(ctx):
    if len(music_queue) > 0:
        url = music_queue.pop(0)
        ydl_opts = {'format': 'bestaudio'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']

        voice_client = ctx.voice_client
        source = await discord.FFmpegOpusAudio.from_probe(url2)
        voice_client.play(source, after=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx), bot.loop))
    else:
        await ctx.voice_client.disconnect()


@bot.command()
async def queue(ctx):
    if len(music_queue) == 0:
        await ctx.send("The queue is empty! Add songs with the command `!play`.")
    else:
        queue_list = "\n".join([f"{i + 1}. {url}" for i, url in enumerate(music_queue)])
        await ctx.send(f"🎶 **Songs Queue:**\n{queue_list}")


@bot.command()
async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await play_next(ctx)
        await ctx.send("⏭ Song skipped!")
    else:
        await ctx.send("There is no song playing at the moment.")


@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Bot Information",
        description="Details about the bot",
        color=discord.Color.blue()
    )
    embed.add_field(name="Name", value=bot.user.name, inline=False)
    embed.add_field(name="Function", value="Plays music on your Discord server", inline=False)
    embed.add_field(name="Status", value="Under Development 🚧", inline=False)
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else "")

    await ctx.send(embed=embed)


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)

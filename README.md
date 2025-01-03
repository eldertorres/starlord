# Starlord - Discord Music Bot 🎵

**Status**: 🚧 Under Development 🚧

Welcome to **Starlord**, a Discord music bot project designed for learning and experimentation! While it is functional, there are known issues that need improvement (see below). Feel free to use this project to learn about Discord bot development or contribute enhancements.

---

## Features
- 🎶 **YouTube Support**: Plays individual songs or entire playlists.
- 📝 **Queue Management**: Allows users to queue and manage songs.
- 🐳 **Dockerized**: Run in an isolated environment for easy deployment.
- 📚 **Learning-Oriented**: Built with simplicity to help developers understand how bots work.

---

## Prerequisites
- [Docker](https://www.docker.com/) (Only if you want to deploy with docker)
- A [Discord Developer Account](https://discord.com/developers/applications) to create a bot token.

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/starlord.git
cd starlord
```

### 2. Set Up Environment Variables
Create a `.env` file in the project directory and add your bot token:
```env
DISCORD_TOKEN=your_bot_token_here
```

### 3. Build the Docker Image
```bash
docker build -t starlord .
```

### 4. Run the Bot
```bash
docker run --env-file .env starlord
```

---

## Commands
- `!play <URL>`: Adds a song or playlist to the queue and starts playing.
- `!queue`: Displays the current music queue.
- `!skip`: Skips the currently playing song.
- `!stop`: Stops playback and disconnects the bot.

---

## Known Issues
- [ ] **Music queue is not cleared**: Songs remain in memory after playback.
- [ ] **No stream buffering**: Causes latency issues while playing songs.
- [ ] **Unlimited queue**: The queue does not enforce a maximum number of songs.
- [ ] **Playback stops mid-song**: Songs occasionally stop abruptly during playback.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! If you encounter a bug or have a feature request, feel free to open an issue or submit a pull request. Since this project is a learning exercise, your improvements can help others.

---

## Acknowledgements
This bot was built as part of a learning journey. Special thanks to the developers of:
- [discord.py](https://github.com/Rapptz/discord.py)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

Happy coding! 🚀


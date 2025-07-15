import os
import asyncio
import discord

TOKEN       = os.environ["DISCORD_TOKEN"]          # set in GitHub Secrets
CHANNEL_ID  = int(os.environ["CHANNEL_ID"])        # set in GitHub Secrets
FRAME_DELAY = float(os.getenv("FRAME_DELAY", "0.5"))  # optional secret

intents = discord.Intents.default()
client  = discord.Client(intents=intents)

def load_frames(path: str = "frames.txt"):
    with open(path, encoding="utf-8") as f:
        blocks = f.read().split("===\n")
    return [b.strip() for b in blocks if b.strip()]

@client.event
async def on_ready():
    print(f"[+] Logged in as {client.user}")
    chan = client.get_channel(CHANNEL_ID)
    if chan is None:
        print("[!] Channel not found. Check CHANNEL_ID.")
        await client.close()
        return

    frames = load_frames()
    msg = await chan.send("Loading animation…")
    while True:                           # loop forever
        for frame in frames:
            await msg.edit(content=f"```\n{frame}\n```")
            await asyncio.sleep(FRAME_DELAY)

client.run(TOKEN)

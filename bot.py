import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ANNOUNCE_CHANNEL_ID = 1454435955795824735
ANNOUNCE_ROLE = "Admin"

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="announce", description="Send scrims announcement")
@discord.app_commands.checks.has_role(ANNOUNCE_ROLE)
async def announce(interaction: discord.Interaction, message: str):
    channel = bot.get_channel(ANNOUNCE_CHANNEL_ID)
    if channel is None:
        await interaction.response.send_message("❌ Channel not found", ephemeral=True)
        return

    embed = discord.Embed(
        title="📢 SCRIMS ANNOUNCEMENT",
        description=message,
        color=0x8e44ad
    )
    embed.set_footer(text="Nexora Scrims")

    await channel.send(embed=embed)
    await interaction.response.send_message("✅ Announcement sent!", ephemeral=True)

bot.run(os.environ["TOKEN"])

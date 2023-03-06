import discord

client = discord.Client()

client.run('<YOUR_TOKEN_HERE>')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!mute'):
        user = message.mentions[0]
        muted_role = discord.utils.get(message.guild.roles, name="Muted")
        await user.add_roles(muted_role)
        dm_channel = await user.create_dm()
        await dm_channel.send("You have been muted. Please quiet down and follow the rules.")
        await message.delete()

# import discord
# import responses
# from discord.ext import commands

# TARGET_USER_TAG = 'hjonker'
# SPECIFIC_MESSAGE = 'hello cutie'

# async def send_message(message, user_message, is_private):
#     try:
#         response = responses.handle_response(user_message)
#         await message.author.send(response) if is_private else await message.channel.send(response)
#     except Exception as e:
#         print(e)

# def run_discord_bot():
#     TOKEN = 'MTE2NTQxODA0MjEwNTI4NjY3Ng.G33qk0.MKt__iW9cbxRraeOYYHRlagvilpjMUEpYaU0SA'    
#     intents = discord.Intents.default()
#     intents.message_content = True
#     client = discord.Client(intents=intents)

#     @client.event
#     async def on_ready():
#         print(f"{client.user}' is now running!")

#     @client.event
#     async def on_message(message):
#         if message.author == client.user:
#             return
        
#         username = str(message.author)
#         user_message = str(message.content)
#         channel = str(message.channel)

#         print(f"{username} said '{user_message}' ({channel})")

#         if user_message[0] == '?':
#             user_message = user_message[1:]
#             await send_message(message, user_message, is_private=True)
#         else:
#             await send_message(message, user_message, is_private=False)

#     client.run(TOKEN)





import discord
import responses
from discord.ext import commands

TARGET_USER_TAG = 'hjonker'
SPECIFIC_MESSAGE = 'what message'





async def send_message_to_target_user(client, content, targetUser):
    print("HERE???")
    for guild in client.guilds:
        for member in guild.members:
            if str(member) == targetUser:
                await member.send(content)
                return

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if response:  # Only send a response if there's one
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE2NTQxODA0MjEwNTI4NjY3Ng.Gs4fwk.bB5130m-rkMKQm43khd0lYuwL2P61QwCTN00R4'  # Make sure to keep your token private and not expose it in code
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user}' is now running!")
        # Send a message to the target user when the bot starts
        await send_message_to_target_user(client, "bot is live", "aladougi")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said '{user_message}' ({channel})")

        # if user_message == SPECIFIC_MESSAGE:
        #     target_user = discord.utils.get(message.guild.members, name=TARGET_USER_TAG)
        #     if target_user:
        #         await target_user.send(f"Hey, someone said '{SPECIFIC_MESSAGE}' in {channel}!")
        #     else:
        #         print(f"User with tag {TARGET_USER_TAG} not found.")
        #     return
        if user_message == SPECIFIC_MESSAGE:
            target_user = discord.utils.get(bot.guilds[0].members, name="hjonker")
            print("lard lard")
            await target_user.send("the code works")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
    return client

        # You can call run_discord_bot() to start the bot





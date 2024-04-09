import requests
import discord
import randfacts
import random
import re
from requests import get
from discord.ext import commands
from randfacts import get_fact

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

resetVal = 100
currVal = resetVal
swears = ['fuck', 'shit']
# Enter Discord User IDs that will be able to use "Alphabet" command
alphabetPrime = []
alphabet = ['https://tenor.com/view/a-dancing-dancing-a-pesing-gif-18704788',
            'https://tenor.com/view/letter-b-dancing-gif-9063746',
            'https://tenor.com/view/letter-c-dancing-gif-9063747',
            'https://tenor.com/view/letter-d-dancing-gif-9063748',
            'https://tenor.com/view/letter-e-gif-9063749',
            'https://tenor.com/view/letter-f-gif-9063750',
            'https://tenor.com/view/g-letter-dance-cartoon-gif-13894794',
            'https://tenor.com/view/letter-h-gif-9063752',
            'https://tenor.com/view/letter-i-gif-9063753',
            'https://tenor.com/view/letter-j-dance-gif-9063754',
            'https://tenor.com/view/letter-k-gif-9063755',
            'https://tenor.com/view/red-alphabet-letter-dancing-letter-l-cartoons-gif-12084376',
            'https://tenor.com/view/letter-m-dance-happy-gif-9063757',
            'https://tenor.com/view/letter-n-gif-9063758',
            'https://tenor.com/view/letter-o-gif-9063759',
            'https://tenor.com/view/letter-p-gif-9063760',
            'https://tenor.com/view/letter-q-gif-9063761',
            'https://tenor.com/view/letter-r-gif-9063762',
            'https://tenor.com/view/letter-s-gif-9063763',
            'https://tenor.com/view/letter-t-gif-9063764',
            'https://tenor.com/view/letter-u-gif-9063765',
            'https://tenor.com/view/letter-v-gif-9063766',
            'https://tenor.com/view/letter-w-gif-9063767',
            'https://tenor.com/view/letter-x-gif-9063768',
            'https://tenor.com/view/letter-y-gif-9063769',
            'https://tenor.com/view/letter-z-gif-9063770']

funfacts = [
            'Running gags call for Donald (Hal Sparks) to be called "out-of-shape" and Chase (Billy Unger) to be '
            'called a weakling nerd; however, these are arguably the two most in-shape athletic people in the show ('
            'only approached by Kelli Berglund\'s accomplishments as a multi-style dancer). Sparks practices kung fu '
            'and has earned several martial art black-belts while Unger studies and participates in extreme martial '
            'arts, advanced stunting, motocross, surfing and skateboarding. These two provide most of the shows '
            'physical comedy, with their physical agility making it look easy.',
            'In "Robot Fight Club," the actors had to build their own robots.',
            'In seasons 1 and 2, Leo was the shortest in the family, but in seasons 3 and 4, Leo is second tallest.',
            'Season 2 is the only season without a one hour season premiere.',
            'Despite the show\'s name, the term "Lab Rats" is only used once in the show itself in the very first '
            'episode. In all the other episodes they\'ve been referred to as "Adam, Bree and Chase", "The Kids", '
            'and "Bionic Super-humans".',
            'no fuck you'
            ]

@bot.command()
async def dm_user(ctx, user_id: int, *, message: str):
    # Find the user by their ID
    user = bot.get_user(user_id)

    if user:
        # Send a direct message to the specified user
        try:
            await user.send(message)
            await ctx.send(f"Sent a DM to {user.name}: {message}")
        except discord.Forbidden:
            await ctx.send(f"Could not send a DM to {user.name}. They might have DMs disabled or blocked the bot.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send(f"Could not find a user with the ID {user_id}.")

@bot.event
async def on_ready():
    print(f'Connected - {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # This pattern matches 'https://twitter.com' or 'https://x.com' only when they are not part of another word
    pattern = r'\b(https://twitter\.com|https://x\.com)\b'

    # Check if the pattern is in the message content
    if re.search(pattern, message.content):
        # Replace 'https://twitter.com' or 'https://x.com' with 'https://fxtwitter.com'
        new_content = re.sub(pattern, 'https://fxtwitter.com', message.content)
        await message.channel.send(new_content)

    if 'sandvich' in message.content.lower():
        await message.channel.send('https://media.tenor.com/images/37aec00973460e984b0c8f48729eb5c5/tenor.gif')

    if 'horny' in message.content.lower():
        await message.channel.send(':newspaper2::anger:')

    if 'gay' in message.content.lower():
        await message.channel.send("^ hey, that's you!")

    if ':dobbert:' in message.content.lower():
        await message.channel.send('<:shootballs:895453687466586122><:dobbert:799180093682483240>')

    if ':monki:' in message.content.lower():
        await message.channel.send('<:monkipog:799839451043856404>')

    if ':monkipog:' in message.content.lower():
        await message.channel.send('<:monki:799838975476498433>')

    if 'show me a magic trick' in message.content.lower():
        await message.channel.send('https://images-na.ssl-images-amazon.com/images/I/71bfmnDpidL._AC_SL1500_.jpg')

    if ':monkinose:' in message.content.lower():
        await message.channel.send('https://media.tenor.com/images/f8275fe31d37d85cc085d0f0bb79c2d5/tenor.gif')

    if 'sus' in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/emojis/803061956290019328.png?v=1')

    if 'vote red' in message.content.lower():
        await message.channel.send('https://media.discordapp.net/attachments/692845310262771823/804878116534616095/image0-20.gif')

    if 'loss' in message.content.lower():
        await message.channel.send("~~.:|:;~~")

    if 'horse plinko' in message.content.lower():
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/828928627998982144/886286351400587284/image0.gif")
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/828928627998982144/886286351765499994/image1.gif")
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/828928627998982144/886286352138776616/image2.gif")
        await message.channel.send("https://tenor.com/view/skeleton-burning-hell-pain-gif-17379863")

    if 'sadie' in message.content.lower():
        await message.channel.send(
            '<:shootballs:895453687466586122> <:sadie:876348224892448778> <:shootdick:895453828965621791>')

    if 'watch me' in message.content.lower():
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/788219343220506644/934199972071624775/ezgif-3-df032e241058.gif')

    if 'gman' in message.content.lower():
        await message.channel.send(
            'https://media.discordapp.net/attachments/1122722391978672180/1155764249252069446/IMG_4239.gif')

    if 'kitty pets' in message.content.lower():
        await message.channel.send(
            'https://media.discordapp.net/attachments/956347274051608616/1198864968142045304/ououououu.gif')

    if 'two of us' in message.content.lower():
            num = random.randint(1,1)
            if(num == 1):
                await message.channel.send(
                    'https://tenor.com/view/2ofus-gif-26564704'
                )
                await message.channel.send(
                    'https://tenor.com/view/2ofus-gif-26564701'
                )

    for i in swears:
        if i in message.content.lower():
            num = random.randint(0,1000)
            if(num == 1):
                await message.channel.send('language')

    if 'alphabet time please and thank you' in message.content.lower() and message.author.id in alphabetPrime:
        i = 0
        while i < len(alphabet):
            rtn = str(alphabet[i])
            await message.channel.send(rtn)
            i += 1

    ### Cryslyn's Bully ###

    global currVal
    if message.author == bot.user:
        return
    if message.author.id == 719393295352070165:
        x = random.randint(1, currVal)
        print(f'\nx: {x}')
        print(f'max: {currVal}')
        print(f'message: {message.content}\n')
        if x == currVal:
            await message.channel.send('hi luci :)')
            print(f'\nBot triggered, resetting to {resetVal}\n')
            currVal = resetVal
        currVal -= 1

    await bot.process_commands(message)

@bot.command()
async def mcip(ctx):
    ip = requests.get('https://api.ipify.org').text
    await ctx.send(f'Current Server ip: {ip}')

@bot.command()
async def labfact(ctx):
    fact = randfacts.get_fact(filter_enabled=False)
    num = random.randint(0, 100)
    if num <= 1:
        fact = random.choice(funfacts)
    await ctx.send(fact)


# Your Discord bot token goes here
#bot.run('')

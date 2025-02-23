import discord
from discord.ext import commands
import random

# intents and client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# confirmation in terminal that bot is logged in
@client.event
async def on_ready():
    print('{0.user} at the ready :D'.format(client))

# adding roles on reaction
@client.event
async def on_raw_reaction_add (payload):

    message_id = payload.message_id

    # portfolio roles 
    message_id_portfolio_roles = 840670003707510784 # message in information channel of EWB server

    # if the user is reacting to the roles message
    if message_id == message_id_portfolio_roles:
        guild_id = payload.guild_id
        guild = discord.utils.find (lambda g : g.id == guild_id, client.guilds)

        # determine the role they should be given
        if payload.emoji.name == 'CEDR_logo':
            role = discord.utils.get(guild.roles, name='CEDR')
        elif payload.emoji.name == 'IR_logo':
            role = discord.utils.get(guild.roles, name='IR')
        elif payload.emoji.name == 'LPA_logo':
            role = discord.utils.get(guild.roles, name='LPA')
        elif payload.emoji.name == 'PA_logo':
            role = discord.utils.get(guild.roles, name='PA')
        elif payload.emoji.name == 'SEJ_logo':
            role = discord.utils.get(guild.roles, name='SEJ')
        elif payload.emoji.name == 'YE_logo':
            role = discord.utils.get(guild.roles, name='YE')
        else:
           role = None
       
        # assign the role accordingly
        if role is not None:
            member = guild.get_member(payload.user_id) # determine member to be assigned the role
            if member is not None: 
                await member.add_roles(role)
            else:
                print("Member not found")
        else:
            print("Role not found")
    
    # Discord + Retreat + F!rosh planning
    message_id_planning = 845280023039705095 # message in ewb-execs-2021-2022 channel of EWB server

    # if the user is reacting to the roles message
    if message_id == message_id_planning:
        guild_id = payload.guild_id
        guild = discord.utils.find (lambda g : g.id == guild_id, client.guilds)
        print ("hello")
        # determine the role they should be given
        if payload.emoji.name == "👾":
            role = discord.utils.get(guild.roles, name='Discord Planning')
        elif payload.emoji.name == "🏕️":
            role = discord.utils.get(guild.roles, name='Retreat Planning')
        elif payload.emoji.name == "💜":
            role = discord.utils.get(guild.roles, name='F!rosh Planning')
        else:
           role = None
           print (payload.emoji.name)
       
        # assign the role accordingly
        if role is not None:
            member = guild.get_member(payload.user_id) # determine member to be assigned the role
            if member is not None: 
                await member.add_roles(role)
            else:
                print("Member not found")
        else:
            print("Role not found")
     

@client.event
async def on_raw_reaction_remove (payload):
    message_id = payload.message_id
    message_id_portfolio_roles = 840670003707510784 # message in information channel of EWB server
    await client.wait_until_ready()
    
    # if the user is reacting to the roles message
    if message_id == message_id_portfolio_roles:
        guild_id = payload.guild_id
        guild = discord.utils.find (lambda g : g.id == guild_id, client.guilds)

        # determine the role to be removed
        if payload.emoji.name == 'CEDR_logo':
            role = discord.utils.get(guild.roles, name='CEDR')
        elif payload.emoji.name == 'IR_logo':
            role = discord.utils.get(guild.roles, name='IR')
        elif payload.emoji.name == 'LPA_logo':
            role = discord.utils.get(guild.roles, name='LPA')
        elif payload.emoji.name == 'PA_logo':
            role = discord.utils.get(guild.roles, name='PA')
        elif payload.emoji.name == 'SEJ_logo':
            role = discord.utils.get(guild.roles, name='SEJ')
        elif payload.emoji.name == 'YE_logo':
            role = discord.utils.get(guild.roles, name='YE')
        else:
            role = None
       
        # remove the role
        if role is not None:
            member = guild.get_member(payload.user_id) # determine the member whose role is to be removed
            if member is not None: 
                await member.remove_roles(role)
            else:
                print("UhOh. Member not found")
        else:
            print("UhOh. Role not found")
    
    # Discord + Retreat + F!rosh planning
    message_id_planning = 845280023039705095 # message in ewb-execs-2021-2022 channel of EWB server

    # if the user is reacting to the roles message
    if message_id == message_id_planning:
        guild_id = payload.guild_id
        guild = discord.utils.find (lambda g : g.id == guild_id, client.guilds)
        print ("hello")
        # determine the role they should be given
        if payload.emoji.name == "👾":
            role = discord.utils.get(guild.roles, name='Discord Planning')
        elif payload.emoji.name == "🏕️":
            role = discord.utils.get(guild.roles, name='Retreat Planning')
        elif payload.emoji.name == "💜":
            role = discord.utils.get(guild.roles, name='F!rosh Planning')
        else:
           role = None
           print (payload.emoji.name)
       
        # assign the role accordingly
        if role is not None:
            member = guild.get_member(payload.user_id) # determine member to be assigned the role
            if member is not None: 
                await member.remove_roles(role)
            else:
                print("Member not found")
        else:
            print("Role not found")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # general fun commands
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('$jo'):
        await message.channel.send('Hello!')
    elif message.content.startswith ('catpic'):
        print ('pic incoming')
        await message.channel.send(file=discord.File('Images/cats/barns.png'))
    elif message.content.startswith ('cowpic'):
        print ('pic incoming')
        await message.channel.send(file=discord.File('Images/cows/cowcow.png'))
   
    # kommutor gang commands
    # can also use .startswith
    if str(message.guild.name) == 'Yua(n)rantined Yomutor Yang':
        if 'curious' in message.content:
            await message.channel.send("george")
        elif message.content.startswith ('catpic'):
            await message.channel.send(file=discord.File('barns'))
        elif message.content.startswith ('i am'):
            num = random.randint(0,10)
            if num == 0:
                msg = message.content
                msg = msg.strip ('i am ')
                await message.channel.send('hello '+ msg)
        elif message.content.startswith ("i'm "):
            num = random.randint(0,10)
            if num == 0:
                msg = message.content
                msg = msg.strip ("i'm ")
                await message.channel.send('hello '+ msg)
        elif 'Suprabhat' in message.content or 'suprabhat' in message.content:
            await message.channel.send('Suprabhat')
        elif message.content.startswith ("I am "):
            num = random.randint(0,10)
            if num == 0:
                msg = message.content
                msg = msg.strip ("I am ")
                await message.channel.send('hello '+ msg)
        elif message.content.startswith ("I'm "):
            num = random.randint(0,10)
            if num == 0:
                msg = message.content
                msg = msg.strip ("I'm ")
                await message.channel.send('hello '+ msg)
        elif message.content == 'monke':
            await message.channel.send('see monke do')   
        elif 'morgan' in message.content:
            num = random.randint(0,1)
            if num == 0:
                await message.channel.send('and the fork ran away with the spoon')
            elif num == 1:
                await message.channel.send('aaaaaaah')
        elif 'david' in message.content:
            await message.channel.send ('https://gfycat.com/allcheeryalaskajingle')
        elif 'kermit' in message.content:
            await message.channel.send('frog')
        elif 'julianne' in message.content:
            await message.channel.send('A flower cannot blossom without sunshine, and man cannot live without love')
        elif 'ewb' in message.content:
            await message.channel.send('EWBe your EWBest EWBot')
        elif 'jo' in message.content:
            num = random.randint(0,10)
            if num == 0:
                await message.channel.send('bot')
            elif num == 1:  
                await message.channel.send('just jo-king')
        elif 'bot' in message.content:
            await message.channel.send('bot is me. me is bot.')
        elif 'morning' in message.content:
            num = random.randint(0,10)
            if num == 0:
                await message.channel.send('starshine, the earth says hello!')
            elif num == 1:  
                await message.channel.send('good morning, morning person')
            elif num == 2:  
                name = str(message.author.display_name)
                await message.channel.send('good morning '+ name)
            else:
                pass

client.run('AUTHTOKEN')
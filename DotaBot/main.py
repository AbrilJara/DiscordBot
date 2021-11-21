import discord
import random
import pyttsx3
import gtts
import os

client = discord.Client()
toronto = ['TON', 'TO', 'TORON']

def random_toronto():
	msg = 'TORONTO'
	cantidad = random.randint(1,15)
	for n in range(cantidad):
		random.choice(toronto)
		msg += random.choice(toronto)
	return msg + 'TOKYO'

def save_msg_gtts(msg):
	tts = gtts.gTTS(msg.lower(), lang='pt')
	tts.save('sounds/tts.mp3')

def save_msg_pyttsx3(msg):
	engine = pyttsx3.init()
	engine.setProperty('voice', 'spanish')
	engine.save_to_file(msg.lower(), 'sounds/tts.mp3')
	engine.runAndWait()
	

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	
	#Refactorizar y fijarse que si estoy en canales diferentes al bot no se rompa
	if message.content.startswith('-toronto'):
		msg = random_toronto()
		save_msg_pyttsx3(msg)
		if (message.author.voice):
			channel = message.author.voice.channel
			if(client.voice_clients):
				channel_client = client.voice_clients[0]
			else:
				channel_client = await channel.connect()
			channel_client.play((discord.FFmpegPCMAudio('sounds/tts.mp3')))
		await message.channel.send(msg)
		

	if message.content.startswith('-gabi'):
		if (message.author.voice):
			channel = message.author.voice.channel
			if(client.voice_clients):
				channel_client = client.voice_clients[0]
			else:
				channel_client = await channel.connect()
			channel_client.play((discord.FFmpegPCMAudio('sounds/coming_through_with_the_woooo.mp3')))
		else:
			await message.channel.send('No estas conectadx a ningun canal de voz')

	if message.content.startswith('-desconectar'):
		if (message.author.voice):
			channel = message.author.voice.channel
		if(any(member.bot for member in channel.members)):
			for member in channel.members:
				if member.bot:
					await member.move_to(None)

client.run('ODk4MzM5NDU2MzEzMDkwMTI4.YWix0A.lznw6eE3Y0uBf29oPnSet3URABU')

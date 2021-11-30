import os
import json
import time
import config
import discord
import requests
import pyfiglet
import platform
import subprocess

from termcolor import colored, cprint

class MyClient(discord.Client):
	async def on_ready(self):
		if platform.system() == 'Linux':
			clear = 'clear'
		else:
			clear = 'cls'
		os.system(clear)
		f = pyfiglet.Figlet(font=config.font)
		cprint(f.renderText(" Taylor  Robot"),'red')
		print(f' [+] Bot Version: {colored(config.__version__, "red")}')
		print(f' [+] Developed By {colored(config.__author__, "red")}')
		print(' _____________________________________________________________________')

	async def on_message(self, msg):
		texto = str(msg.content)

		if msg.author == self.user:
			return

		if texto == '!start':
			await msg.channel.send('Olá, Sou o Robô Taylor!\n\nDigite `!cmd` para conhecer meus comandos disponíveis.\n\nLink: https://discordapp.com/api/oauth2/authorize?client_id=432989654799613962&permissions=8&scope=bot')

		if texto == '!cmd':
			await msg.channel.send('''
**📖|Comandos Disponíveis**:

**!me** -> Exibe as suas informações.
**!start** -> Inicia o Bot.
**!print** `[URL]` -> Manda um print da URL fornecida.
**!regras** -> Visualiza as regras salvas.
**!chat_id** -> Retorna o id do chat.
**!dfregras** -> Define as regras do canal.

**[Reações]:**

**!flip**
**!homo**
**!look**
**!shots**
**!lenny**
**!shrug**
**!nugget**
**!facepalm**

**[OBS]**:

- Utilize **"!ajuda [comando]"** para obter ajuda de um ítem.
- Não coloque **"[]"** ou **"<>"** nos comandos.

Exemplo: `!ajuda !start`
''')

		if texto == '!info':
			await msg.channel.send(f'''
Bot: Taylor Robot
Dev: {config.__author__}
Github: {config.__github__}
Versão: {config.__version__}''')

		if texto.startswith('!ajuda'):
			texto = str(texto.replace('!ajuda ', ''))
			if texto in config.commands:
				await msg.channel.send(config.commands[texto.lower()])
			else:
				await msg.channel.send('Envie o **"!ajuda"** seguido do comando.\nExemplo: **!ajuda !cmd**')

		if texto == '!chat_id':
			await msg.channel.send('Chat_ID: ' + msg.channel.id)

		if texto == '!me':
			await msg.channel.send(f"""
**Id:** `{ msg.author.id}`
**Nome:** `{ msg.author }`""")

		if texto.startswith('!print'):
			text = msg.content
			text = text.replace('!print ','')
			url  = str(config.api['print'].format(config.keys['print'], str(text)))
			r    = requests.get(url)
			with open("image.jpg", "wb") as code:
				code.write(r.content)
			await msg.channel.send(file=discord.File('image.jpg'))
			time.sleep(3)
			os.remove('image.jpg')
		
		if texto.startswith('!ip'):

			texto2 = texto.split(' ', 1)[1].replace(' json','')
			req    = requests.get('http://ip-api.com/json/{}'.format(texto2))
			data   = json.loads(req.text)
			if 'json' in texto2:
				if str(texto).split(' ')[2] == 'json':
					await msg.channel.send(str(data).replace(',',',\n').replace(':',' : '))
			else:
				await msg.channel.send(f"""
**Informações {texto2}:**

**ip:** `{data['query']}`
**cidade:** `{data['city']}` - `{data['region']}`
**estado:** `{data['country']}`
**zip code:** `{ data['zip']}`

hospedado por `{data['isp']}`

**organização:** {data['org']}
**fuso horário:**  `{data['timezone']}`
""")

		if texto == '!speedtest':
			await bot.send_message(msg.channel, 'Iniciando teste...')
			sub = subprocess.getstatusoutput("speedtest-cli --share")[1]
			sub = str(sub)
			sub = sub.replace('Download', '🔻Download')
			sub = sub.replace('Upload', '🔺Upload')
			await msg.channel.send(sub)

		if texto in config.reactions:
			await msg.channel.send(config.reactions[texto])

client = MyClient()
client.run(config.TOKEN)
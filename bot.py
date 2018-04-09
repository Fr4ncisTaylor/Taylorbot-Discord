#-*- coding:utf-8 -*-
import discord, pyfiglet, asyncio, requests, urllib, json, os, time, sys, config, aiml, subprocess

bot      = discord.Client()
db	     = config.db
commands = config.commands
kernel   = aiml.Kernel()

###### [ AIML ]
kernel.learn("mae.xml")
kernel.respond("taylor")



@bot.event
async def on_ready():
    f = pyfiglet.Figlet(font=config.font)
    f.renderText(bot.user.name)
    print('__________________________________________________________________________________'*2)
    
def keepcalmm(a,b,c):
	if c == 'amarelo':
		url   = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['amarelo']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'vermelho':
		url  = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['vermelho']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'verde':
		url  = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['verde']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'rosa':
		url  = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['rosa']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'cyan':
		url  = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['cyan']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'azul':
		url  = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['azul']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'verde2':
		url  = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['verde cana']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'vermelho2':
		url = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['vermelho2']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'cinza':
		url = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['cinza']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'violeta':
		url = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['violeta']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	if c == 'roxo':
		url = 'http://www.keepcalmstudio.com/-/p.php?t=%EE%BB%AA%0D%0AKEEP%0D%0ACALM%0D%0A%3E%3Eand%0D%0A'+str(a)+'%0D%0A'+str(b)+'&bc='+config.cor['roxo']+'&tc=FFFFFF&cc=FFFFFF&uc=true&ts=true&ff=PNG&w=300&ps=sq'
	return url

def add(msg):
	get   = db.get('hanking'+str(msg.channel.id)+str(msg.author.id))
	
	try:
		total = int(get) +1
	except:
		total = 1
	db.set('hanking'+str(msg.channel.id)+str(msg.author.id), str(total))

@bot.event
async def on_message(msg):
	add(msg)
	texto = str(msg.content)

	if texto == '!start':

		await bot.send_message(msg.channel, 'Olá, Sou o Robô Taylor!\n\nDigite `!cmd` para conhecer meus comandos disponíveis.\n\nLink: https://discordapp.com/api/oauth2/authorize?client_id=432989654799613962&permissions=8&scope=bot')

	if texto == '!cmd':

		await bot.send_message(msg.channel, '''
*📖|Comandos Disponíveis*:

`!start` -> Inicia o Bot.
`!id` -> Exibe as suas informações.
`!print` [URL] -> Manda um print da URL fornecida.
`!dfregras` -> Define as regras do canal.
`!regras` -> Visualiza as regras salvas.
`!ia` [on/off] -> Controle da I.A. no seu canal.
`!keepcalm` <texto1, texto2> [cor] -> Confecciona um banner KeepCalm.
`!audio` [URL Youtube/Texto] -> baixa um video do youtube em formato "*.mp3*".
`!tts` [Texto] -> Transforma texto em voz.
`!chat_id` -> Retorna o id do chat.
*__________________________________________________________________________________*
OBS: 

[*] Utilize "!ajuda [comando]" para obter ajuda de um ítem;
[*] Não coloque "[]" ou "<>" nos comandos;

Exemplo: `!ajuda !start`
''')

	if texto == '!info':
		await bot.send_message(msg.channel, '''

BotName: {}
BotVersion: {}

Github: {}'''.format(bot.user.name, config.__version__, config.__github__, config.__author__))

	if texto.startswith('!ajuda'):
		texto = str(texto.replace('!ajuda ', ''))
		if texto in config.commands:
			await bot.send_message(msg.channel, config.commands[texto.lower()])

	if texto == '!chat_id':
		await bot.send_message(msg.channel, 'Chat_ID: ' + msg.channel.id)

	if texto.startswith('!dfregras'):
		regras = msg.content
		regras = regras.replace('!dfregras ','')

		db.set('regras{}'.format(msg.channel.id), str(regras))
		await bot.send_message(msg.channel, 'Regras definidas com sucesso!\n{}'.format(regras))

	if texto == '!regras':
		mssg = db.get('regras{}'.format(str(msg.channel.id)))
		print(mssg)
		await bot.send_message(msg.channel, mssg)

	if texto == '!id':
		nome = str(msg.author).split('#')[0]
		id 	 = msg.author.id
		get   = db.get('hanking'+str(msg.channel.id)+str(msg.author.id))
		print(get)
		try:
			total = int(get) +1
		except:
			total = 1

		MSSG = '''
Nome: {}
Id: {}
Mensagens: {}
'''.format(nome,id, total)
		await bot.send_message(msg.channel, MSSG)

	if texto.startswith('!youtube'):

		texto = texto.replace('!youtube ','')

		if '[' in texto and ']' in texto:
			texto, b = texto.split('[')
			b = b.replace(']','')

		else:
			b = 0
		b = int(b)
		
		request = requests.get(config.api['youtube'].format(config.keys['youtube'], texto))
		text    = request.text
		result  = json.loads(text)
		
		t0  = result['items'][b]['snippet']['title']
		l0  = 'https://www.youtube.com/watch?v='+str(result['items'][b]['id']['videoId'])

		await bot.send_message(msg.channel, str(l0))

	if texto.startswith('!audio'):
		txt = texto.replace('!audio ','')
		if txt.startswith('http://') or txt.startswith('https://'):
			url = txt
		else:
			request = requests.get(config.api['youtube'].format(config.key['youtube'], txt))
			text    = request.text
			result  = json.loads(text)
			url  = 'https://www.youtube.com/watch?v='+str(result['items'][0]['id']['videoId'])
		
		url  = 'https://www.convertmp3.io/fetch/?format=JSON&video='+url
		r    = requests.get(url)
		text = json.loads(r.text)
		nome = text['title']
		link = text['link']


		await bot.send_message(msg.channel, 'Baixando mp3...')
		r   = requests.get(link)
		with open(nome+'.mp3', "wb") as code:
			code.write(r.content)
		if str(os.path.getsize(nome+'.mp3')) > '5000000':
			await bot.send_message(msg.channel, 'O arquivo ultrapassou o limite máximo permitido pelo discord.\nTamanho do arquivo: {}'.format(config.convert(os.path.getsize(nome+'.mp3'))))
		else:
			await bot.send_file(msg.channel, open(nome+'.mp3', 'rb'))
			time.sleep(3)
			os.remove(nome+'.mp3')

	if texto.startswith('!keepcalm'):
		
		text = msg.content
		text = text.replace('!keepcalm ','')
		try:
			a, b, c = str(text).split()
		except:
			try:
				a, b = str(text).split()
				c    = 'cyan'
			except:
				a = str(text)
				b = ''
				c = 'cyan'
		url = keepcalmm(a,b,c)
		r    = requests.get(url)
		with open("image.jpg", "wb") as code:
			code.write(r.content)
		await bot.send_file(msg.channel, open('image.jpg', 'rb'))
		os.remove('image.jpg')

	if texto.startswith('!print'):
		url  = str(config.api['print'].format(config.keys['youtube']))
		text = msg.content
		text = text.replace('!print ','')
		text = str(text)
		url  = url+text
		r    = requests.get(url)
		with open("image.jpg", "wb") as code:
			code.write(r.content)
		await bot.send_file(msg.channel, open('image.jpg', 'rb'))
		time.sleep(3)
		os.remove('image.jpg')

	if texto == '!shrug':
		await bot.send_message(msg.channel, config.reactions['shrug'])

	if texto == '!flip':
		await bot.send_message(msg.channel, config.reactions['flip'])
	
	if texto.startswith('!ip'):

		texto2 = texto.split(' ', 1)[1].replace(' json','')
		req    = requests.get('http://ip-api.com/json/{}'.format(texto2))
		data   = json.loads(req.text)
		if 'json' in texto2:
			if str(texto).split(' ')[2] == 'json':
				await bot.send_message(msg.channel, str(data).replace(',',',\n').replace(':',' : '))
		else:
			pais   = data['city']
			estado = data['country']
			osp    = data['isp']
			cidade = data['regionName']
			ip     = data['query']
			lat    = data['lat']
			lon    = data['lon']
			hora   = data['timezone']
			cep    = data['zip']
			org    = data['org']
			reg    = data['region']
			mssg   = """
Informações {}:

ip: `{}`
cidade: `{}` - `{}`
país: `{}`
estado: `{}`
zip code` {}`
hospedado por `{}`
organização:
{}
fuso horário: 
`{}`""".format(texto ,ip, pais, reg, estado, reg, cep, osp, org, hora)

			await bot.send_message(msg.channel, str(mssg))

	if texto == '!restart':
		if msg.author.id == config.sudo:

			await bot.send_message(msg.channel, 'Reiniciando')
			
			os.system('cls')
			await bot.send_message(msg.channel, 'started');os.execl(sys.executable, sys.executable, *sys.argv)
	
	if texto.startswith('!tts'):
		texto = texto.replace('!tts ','')
		url   = "https://code.responsivevoice.org/getvoice.php?tl=pt-BR&t="+str(texto)
		r     = requests.get(url)
		with open("voice.ogg", "wb") as code:
			code.write(r.content)
		await bot.send_file(msg.channel, open('voice.ogg', 'rb'))

	

	if texto == '!speedtest':
		await bot.send_message(msg.channel, 'Iniciando teste...')
		sub = subprocess.getstatusoutput("speedtest-cli --share")[1]
		sub = str(sub)
		sub = sub.replace('Download', '🔻Download')
		sub = sub.replace('Upload', '🔺Upload')
		await bot.send_message(msg.channel, sub)

	else:
		if str(texto) not in commands:
			if 'taylor ' in texto.lower() or ' taylor' in texto.lower() or ' taylor ' in texto.lower():
				if msg.author.id != config.APLICATION_ID:
					resposta = kernel.respond(str(texto).replace('taylor ','').replace(' taylor ','').replace(' taylor ',''))
					for i in resposta.split('#'):
						i = i.replace('$name', msg.author.name)
						await bot.send_message(msg.channel, i)


bot.run(config.TOKEN)


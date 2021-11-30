# -*- coding: utf-8 -*-
import redis
import math
import sys

#####################################################################################################
#																									#
#        Please keep the data in [INFORMATION SORCE] to assist with developer development.      	#
#																									#
#####################################################################################################

requeriment = 'discord.py redis pyfiglet requests python-aiml speedtest-cli' # DON'T USE ','

#########[ INFORMATION SORCE] # [ DONT REPLACE ]
__version__ = '1.0.1'
__author__ 	= 'FrancisTaylor#5810'
__github__ 	= 'https://github.com/Francis-Taylor'

#########[ DB ]
try:
	db = redis.StrictRedis(host='localhost', port=6379, db=0) # Redis Config
except:
	print('Erro no redis, certifique-se se você tem o Redis-cli instalado.')
	sys.exit()
#########[ BOT CONFIG ]
TOKEN 			= '_aplicationToken_' # Replace for Aplication Token
APLICATION_ID 	= '_aplicationId_'    # Replace for a ID of aplication

#########[ ADMNISTRATION ]
sudo  = '_owner_id' # Replace for you ID.

#########[ FIGLET ]
printer = True # True or false.
font 	= 'doom' # Search for more fonts in google.

#########[ DB MANAGER]
class Redis:
	def hgetall(key1, key2):
		get = db.hget(str(key1))[str(key2)]
		return get.encode('utf-8')

	def get(key1):
		get = db.get(str(key1))
		temp = get.decode('utf-8')
		return 

	def set(key1, key2):
		get = db.set(str(key1), str(key2))
		temp = get.decode('utf-8')
		return temp

	def add(key0, key1):
		try:
			get = db.get(str(key0)+str(key1))
			if len(get)>0:
				have = True
			else:
				have = False
		except:
			have = False

		if have == True:
			get   = db.get(str(key0)+str(key1))
			total = int(get) +1
			db.set(str(key0)+str(key1), str(total))
			return total
########################################### [ BETA STAGE]
reactions = {
	'!lenny'    : "( ͡° ͜ʖ ͡°)",

	'!flip'     : "(╯°□°）╯︵ ┻━┻",

	'!shots'    : "SHOTS FIRED",

	'!homo'     : "┌（┌　＾o＾）┐",

	'!shrug'    : "¯\_(ツ)_/¯",

	'!look'     : "ಠ_ಠ",

	'!facepalm' : "(－‸ლ)",

	'!nugget'   : "chicken nugger",


}

##################[ HELP COMMANDS ]
commands = {
			
			'!start' 	: '''
Mensagem inicial do bot.

Exemplo de uso: 

`!start`''',

			'!id'    	: '''
Retorna os dados do seu perfil.

Exemplo de uso:

`!id`''',   
			'!restart' 	: None,
			'!flip'	  	: None,
			'!print'  	: '''
Retorna uma captura de tela do site fornecido.

Exemplo de uso:

`!print https://google.com`''',
			'!regras' 	: '''
Exibe as regras do chat.

Exemplo de uso:

`!regras`''',
			'!dfregras' : '''
Define as regras do chat.

OBS: Suporte ao Markdown!!!

Exemplo de uso:

`!dfregras proibido flood!`''',
			'!audio' : '''
Retorna um arquivo `.mp3` do link *do youtube* ou texto fornecido.

Exemplo de uso:

`!audio Ed Sheeran perfect`.''',
			'!youtube' : '''
Retorna o link de um vídeo do youtube de acordo com o texto fornecido.

Exemplo de uso:

`!youtube Ed Sheeran perfect`.

OBS: Você também pode mudar o resultado utilizando um número de *um* (1) à *cinco* (5).

Exemplo:

`!youtube Ed Sheeran Perfect 2`''',
			'!tts' : '''
Transforma texto em voz:

Exemplo de uso:

`!tts olá`''',
		'!chat_id' : '''
Retorna o ID do chat:

Exemplo de uso:

`!chat_id`
		''', 



}
########## [ APIS ]
api = {
	'print'   : "https://api.screenshotmachine.com/?key={}&url={}&dimension=1024x768",

}

keys = {
	'print'   : '061f9b',
}
########## [ colors ]
cor = {
	'amarelo'    : 'FFFF00',
	'vermelho'   : 'E31F17',
	'verde'      : '037d12',
	'rosa'       : 'e3068d',
	'cyan'       : '0cc0fd',
	'azul'       : '1b037d',
	'verde cana' : '7D7500',
	'vermelho2'  : '7D0606',
	'cinza'      : '6E6E6E',
	'violeta'    : 'DD00FF',
	'roxo'       : '9900FF',
}

class colors:
	class lg:
		black 	= '0'
		blue  	= '9'
		verde 	= 'A'
		cyan	= 'B'
		red 	= 'C'
		purple 	= 'D'
		yellow 	= 'E'
		white 	= 'F'


########## [ CONVERT SIZE_BYTES]
def convert(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])
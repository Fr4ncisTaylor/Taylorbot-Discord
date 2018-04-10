# -*- coding: utf-8 -*-

#############################
# INSTALL TAYLOR BOT SISTEM #
#############################

import  os, sys,  time, platform

if platform.system() == 'Linux':
	clear = 'clear'
else:
	clear = 'clear'

try:
	import pyfiglet
except:

	os.system('pip install pyfiglet')
	os.system(clear)
	import pyfiglet

__version__ = '1.0.0 [Beta]'
__author__ 	= '@FrancisTaylor'
__github__ 	= 'https://github.com/Francis-Taylor'
requeriment = 'discord.py redis pyfiglet requests python-aiml speedtest-cli' # DON'T USE ','

def figlets():
	#########################################
	print('System Powered by ')				#
	f = pyfiglet.Figlet(font='doom')	#
	print(f.renderText("Cybion"))			#
	print('Author: '+__author__)		#
	print('Version: '+__version__)   #
	print('Git: '+ __github__)    	#
	print('='*110+'\n')						#
	#########################################



os.system(clear)
figlets()

requeriment = 'discord.py redis pyfiglet requests python-aiml speedtest-cli' # DON'T USE ','

pergunta = input('\nDo you want to start the installation? [Y/N]\n>>> ')

if pergunta.lower() != 'y':
	sys.exit()

else:
	print('\nStarting!...\n')
	
	print('Listing Modules...\n')
	modules = requeriment
	print(modules.replace(' ','\n'))
	
	print('\nRunning the Pip to install modules...')
	os.system('pip install '+ modules)

	pergunta = input('\nThe system was successfully installed! Do you want to start the bot? [Y/N]\n\n>>> ')
	if pergunta.lower() != 'y':
		print('\nCybion thanks for using our system!')
		sys.exit()
	else:
		print('\nCybion thanks for using our system! The system will start in 5 seconds ...')
		time.sleep(1)
		print(5)
		time.sleep(1)
		print(4)
		time.sleep(1)
		print(3)
		time.sleep(1)
		print(2)
		time.sleep(1)
		print(1)
		time.sleep(1)
		os.system(clear)
		os.system('python bot.py')



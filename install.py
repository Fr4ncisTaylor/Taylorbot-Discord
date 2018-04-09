# -*- coding: utf-8 -*-

#############################
# INSTALL TAYLOR BOT SISTEM #
#############################

import config, os, sys, pyfiglet, time

def figlets():
	#########################################
	print('System Powered by ')				#
	f = pyfiglet.Figlet(font=config.font)	#
	print(f.renderText("Cybion"))			#
	print('Author: '+config.__author__)		#
	print('Version: '+config.__version__)   #
	print('Git: '+ config.__github__)    	#
	print('='*110+'\n')						#
	#########################################



os.system('CLS')
figlets()

pergunta = input('\nDo you want to start the installation? [Y/N]\n>>> ')

if pergunta.lower() != 'y':
	sys.exit()

else:
	print('\nStarting!...')
	
	print('Listing Modules...')
	modules = config.requeriment
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
		os.system('CLS')
		os.system('python bot.py')



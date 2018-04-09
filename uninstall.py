# -*- coding: utf-8 -*-

#############################
# UNINSTALL TAYLOR BOT SISTEM #
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

pergunta = input('\nDo you want to start the uninstallation? [Y/N]\n>>> ')

if pergunta.lower() != 'y':
	sys.exit()

else:
	print('\nStarting!...')
	
	print('Listing Modules...\n')
	modules = config.requeriment
	print(modules.replace(' ','\n'))
	
	print('\nRunning the Pip to uninstall modules...')
	os.system('pip uninstall '+ modules)

	print('\nThe system was successfully uninstalled!')
	

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
	sys.exit()



#############################
# INSTALL TAYLOR BOT SISTEM #
#############################

import os, sys,  time, platform, config

clear = 'clear' if platform.system() == 'Linux' else 'cls'

try:
	import pyfiglet
except:
	os.system('pip install pyfiglet termcolor')
	os.system(clear)

import pyfiglet
from termcolor import colored, cprint

__version__ = '1.0.1'
__author__ 	= 'FrancisTaylor#5810'
__github__ 	= 'https://github.com/Francis-Taylor'
requeriment = 'discord.py termcolor redis pyfiglet requests python-aiml speedtest-cli' # DON'T USE ','

def figlets():
	cprint('System Powered by ', 'cyan')
	f = pyfiglet.Figlet(font='doom')
	cprint(f.renderText("Cybion"), 'blue')
	print(' [+] Git: '     + colored(__github__, 'cyan'))
	print(' [+] Author: '  + colored(__author__, 'cyan'))
	print(' [+] Version: ' + colored(__version__, 'cyan'))
	print(' ', end='')
	print('='*110+'\n')

os.system(clear)
figlets()

requeriment = 'discord.py redis pyfiglet requests python-aiml speedtest-cli' # DON'T USE ','

pergunta = input(f'\n [+] Do you want to start the installation? { colored("[Y/N]", "cyan") }\n\n >>> ')

if pergunta.lower() != 'y':
	sys.exit()

else:
	print('\n [+]Starting!...\n')
	
	print(' [+] Listing Modules...\n')
	modules = requeriment
	for i in modules.split():
		print(f'  -  {i}')
	
	print('\n [+] Running the Pip to install modules...')
	os.system('pip install '+ modules)

	pergunta = input(f'\n [+] The system was successfully installed! Do you want to start the bot? {colored("[Y/N]", "green")}\n\n  >>> ')
	if pergunta.lower() != 'y':
		print('\n [+] Cybion thanks for using our system!')
		sys.exit()
	else:
		print('\n [+] Cybion thanks for using our system! The system will start in 5 seconds ...')
		time.sleep(5)
		os.system(clear)
		os.system('python main.py')



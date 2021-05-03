import time
import os
from threading import Thread
import pymem
from pymem import process
import pymem.process
import requests
import keyboard
from colorama import init
from colorama import Fore

init()

offsets = 'https://raw.githubusercontent.com/kadeeq/ProjectX/main/offsets/offsets.json'
response = requests.get( offsets ).json()

dwForceJump = int( response["signatures"]["dwForceJump"] )
dwLocalPlayer = int( response["signatures"]["dwLocalPlayer"] )
m_fFlags = int( response["netvars"]["m_fFlags"] )


def bhop():
	try:
		pm = pymem.Pymem("csgo.exe")
		client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
		engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

		os.system("cls")

		print(Fore.CYAN + "Author: Clancy \nYouTube: https://www.youtube.com/c/ClancyCheats \n\nDonate: \nQIWI: DEVCLANCY \nDonationAlerts: https://www.donationalerts.com/r/theclancy")

		while True:
			player = pm.read_int(client + dwLocalPlayer)
			if keyboard.is_pressed( "space" ):
				force_jump = client + dwForceJump
				on_ground = pm.read_int( player + m_fFlags )
				if player and on_ground == 257 or on_ground == 263:
					pm.write_int( force_jump, 6 )
	except Exception as E:
		print("[SimpleBH] Произошла ошибка!")


main = Thread(target = bhop)
main.start()

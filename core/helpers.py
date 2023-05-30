from colorama import Fore, Style, init
import random, time, os
import subprocess

init()

# the class for the input/output functions
class IOFuncs:


	class Verbose:
		def printError(Error: str, Exeption: str) ->  str: print(f"{Fore.RED} + [ERROR] --> {Error} \nExeption --> {Exeption}{Style.RESET_ALL}") 
		def printSuccess(Success: str) ->  str: print(f"{Fore.GREEN} + [SUCCESS] --> {Success}{Style.RESET_ALL}") 
		def printInfo(Info: str) ->  str: print(f"{Fore.BLUE} + [INFO] --> {Info}{Style.RESET_ALL}") 
		def getUserInput(Input: str) ->  str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} y/n: {Style.RESET_ALL}") 

	class Debug:
		def printError(Error: str, Exeption: str) ->  str: print(f"{Fore.RED} + [ERROR] --> {Error} \nExeption --> {Exeption}{Style.RESET_ALL}") 
		def printSuccess(Success: str) ->  str: print(f"{Fore.GREEN} + [SUCCESS] --> {Success}{Style.RESET_ALL}") 
		def printInfo(Info: str) ->  str: print(f"{Fore.BLUE} + [INFO] --> {Info}{Style.RESET_ALL}") 
		def getUserInput(Input: str) ->  str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} y/n: {Style.RESET_ALL}") 

	class Default:
		def printError(Error: str) ->  str: print(f"{Fore.RED} + [ERROR] --> {Error}{Style.RESET_ALL}") 
		def printSuccess(Success: str) ->  str: print(f"{Fore.GREEN} + [SUCCESS] --> {Success}{Style.RESET_ALL}") 
		def printInfo(Info: str) ->  str: print(f"{Fore.BLUE} + [INFO] --> {Info}{Style.RESET_ALL}") 
		def getUserInput(Input: str) ->  str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} y/n: {Style.RESET_ALL}") 
		def getMultiOptionInput(Input: str, q1, q2, q3) ->  str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} ({q1} or {q2} or {q3}): {Style.RESET_ALL}") 
		def getTextInput(Input: str) -> str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input}: {Style.RESET_ALL}")



# the class for the menu
class Menu:
    
	arrayOfLogos = [
    
    
    
    r"""
	____  __.                       __      __ ______________________ 
	|    |/ _| __ __ _______   ____ /  \    /  \\__    ___/\__    ___/ 
	|      <  |  |  \\_  __ \ /  _ \\   \/\/   /  |    |     |    |    
	|    |  \ |  |  / |  | \/(  <_> )\        /   |    |     |    |    
	|____|__ \|____/  |__|    \____/  \__/\  /    |____|     |____|    
			\/                             \/                          
						( Web Testing Tool )	
    
    @devkuro - GH: im-kuro      
          													
    """,
    
	r"""
	888 88P                            Y8b Y8b Y888P 88P'888'Y88 88P'888'Y88 
	888 8P  8888 8888 888,8,  e88 88e   Y8b Y8b Y8P  P'  888  'Y P'  888  'Y 
	888 K   8888 8888 888 "  d888 888b   Y8b Y8b Y       888         888     
	888 8b  Y888 888P 888    Y888 888P    Y8b Y8b        888         888     
	888 88b  "88 88"  888     "88 88"      Y8P Y         888         888                                                  
						( Web Testing Tool )	
    
    @devkuro - GH: im-kuro   
    
	""",
	r"""
	dP     dP                            dP   dP   dP d888888P d888888P 
	88   .d8'                            88   88   88    88       88    
	88aaa8P'  dP    dP 88d888b. .d8888b. 88  .8P  .8P    88       88    
	88   `8b. 88    88 88'  `88 88'  `88 88  d8'  d8'    88       88    
	88     88 88.  .88 88       88.  .88 88.d8P8.d8P     88       88    
	dP     dP `88888P' dP       `88888P' 8888' Y88'      dP       dP    
						( Web Testing Tool )	
    
    @devkuro - GH: im-kuro  
    
	"""
    ]

	def startupMenu(arrayOfLogos):
		""" show the startup menu

		Args:
			arrayOfLogos (_type_): array of logos
		"""
		randLogo = random.choice(arrayOfLogos)

		for line in randLogo.splitlines():
			print(Fore.RED +  line)
			time.sleep(0.2)
		
	def getSessionConfig():
		""" ask the user all needed questions to get config

		Returns:
			_type_: _description_
		"""
		# Function to get user input and validate against the options
		def getValidInput(prompt, *options):
			while True:
				user_input = IOFuncs.Default.getMultiOptionInput(prompt, options[0][0], options[1][0], options[2][0]).strip().lower()
				for option in options:
					if user_input == option[0].lower() or user_input == option[1].lower():
						return option[1]
				print("Error: Invalid input. Please try again.")

		# Prompt for Attack Mode
		sessionMode = getValidInput("Attack Mode (Agressive/a, Silent/s, Default/d)",
									("Agressive", "A"), ("Silent", "S"), ("Default", "D"))

		# Prompt for Attack Speed
		attackSpeed = getValidInput("Attack Speed (Slow/s, Medium/m, Fast/f)",
									("Slow", "S"), ("Medium", "M"), ("Fast", "F"))

		# Prompt for Verbose Level
		verboseLevel = getValidInput("Verbose Level (Low/l, Medium/m, High/h)",
								("Low", "L"), ("Medium", "M"), ("High", "H"))


		useNmap = IOFuncs.Default.getUserInput("Use Nmap? (https://nmap.org/)")
		useNikto = IOFuncs.Default.getUserInput("Use Nikto? (https://cirt.net/Nikto2)")
		useWfuzz = IOFuncs.Default.getUserInput("Use Wfuzz? (https://www.kali.org/tools/wfuzz/)")
		useDirb = IOFuncs.Default.getUserInput("Use Dirb? (https://tools.kali.org/web-applications/dirb)")
		useWpscan = IOFuncs.Default.getUserInput("Use Wpscan? (https://wpscan.org/)")
		useWapiti = IOFuncs.Default.getUserInput("Use Wapiti? (https://wapiti.sourceforge.io/)")
		useJoomscan = IOFuncs.Default.getUserInput("Use Joomscan? (https://www.kali.org/tools/joomscan/)")

		return {"sessionMode": sessionMode, "attackSpeed": attackSpeed, "verboseLevel": verboseLevel, "useNmap": useNmap, "useNikto": useNikto, "useWfuzz": useWfuzz, "useDirb": useDirb, "useWpscan": useWpscan, "useWapiti": useWapiti, "useJoomscan": useJoomscan}


	def checkForTools() -> bool:
		""" Checks for all needed tools to run, and if theyre not there it will install them
	
		Returns:
			bool: true = worked false = no workeded
		"""
		arrOfTools = ["nmap", "nikto", "wfuzz", "dirb", "wpscan", "wapiti", "joomscan"]
		uninstalledTools = []

		for x in arrOfTools:

			if os.path.exists(f"/usr/bin/{x}"):
				continue
			else:
				uninstalledTools.append(x)

				
		if not uninstalledTools:
			IOFuncs.Default.printSuccess("Looks like you have all needed tools!")
		else:
			userAns = IOFuncs.Default.printError("Looks like your missing some tools, would you like to install them now? (you may need to re-run with sudo)")
			if userAns == "y" or "Y":
				for x in uninstalledTools:
					print(Fore.GREEN + " + [INFO] Installing --> " + x )
					try:
						z = subprocess.check_output(f"sudo apt install {x}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
						print(Fore.GREEN + " + [INFO] Success installing! --> " + x )
					except subprocess.CalledProcessError: IOFuncs.Default.printError("Error installing tool. Please try again later.")
						







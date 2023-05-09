from colorama import Fore, Style, init
import random, time
init()

# the class for the input/output functions
class IOFuncs:

	class Debug:
		def printError(Error: str, Exeption: str) -> bool: print(f"{Fore.RED} + [ERROR] --> {Error} \nExeption --> {Exeption}{Style.RESET_ALL}"); return True
		def printSuccess(Success: str) -> bool: print(f"{Fore.GREEN} + [SUCCESS] --> {Success}{Style.RESET_ALL}"); return True
		def printInfo(Info: str) -> bool: print(f"{Fore.BLUE} + [INFO] --> {Info}{Style.RESET_ALL}"); return True
		def getUserInput(Input: str) -> bool: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} y/n: {Style.RESET_ALL}"); return True

	class Default:
		def printError(Error: str) -> bool: print(f"{Fore.RED} + [ERROR] --> {Error}{Style.RESET_ALL}"); return True
		def printSuccess(Success: str) -> bool: print(f"{Fore.GREEN} + [SUCCESS] --> {Success}{Style.RESET_ALL}"); return True
		def printInfo(Info: str) -> bool: print(f"{Fore.BLUE} + [INFO] --> {Info}{Style.RESET_ALL}"); return True
		def getUserInput(Input: str) -> bool: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} y/n: {Style.RESET_ALL}"); return True
		def getMultiOptionInput(Input: str, q1, q2, q3) -> bool: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} ({q1} or {q2} or {q3}): {Style.RESET_ALL}"); return True





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
			print(line)
			time.sleep(0.1)
		
	def getSessionConfig():
		"""_summary_

		Returns:
			_type_: _description_
		"""
  
		sessionMode = IOFuncs.Default.getMultiOptionInput("Attack Mode", "Agressive/A", "Silent/S", "Quiet/Q")
		attackSpeed = IOFuncs.Default.getMultiOptionInput("Attack Speed", "Slow/S", "Medium/M", "Fast/F")
		verboseLevel = IOFuncs.Default.getMultiOptionInput("Verbose Level", "Low/L", "Medium/M", "High/H")
		useNmap = IOFuncs.Default.getUserInput("Use Nmap? (https://nmap.org/)")
		useNikto = IOFuncs.Default.getUserInput("Use Nikto? (https://cirt.net/Nikto2)")
		useWfuzz = IOFuncs.Default.getUserInput("Use Wfuzz? (https://www.kali.org/tools/wfuzz/)")
		useDirb = IOFuncs.Default.getUserInput("Use Dirb? (https://tools.kali.org/web-applications/dirb)")
		useGobuster = IOFuncs.Default.getUserInput("Use Gobuster? (https://tools.kali.org/web-applications/gobuster)")
		useWpscan = IOFuncs.Default.getUserInput("Use Wpscan? (https://wpscan.org/)")
		useWapiti = IOFuncs.Default.getUserInput("Use Wapiti? (https://wapiti.sourceforge.io/)")
		useJoomscan = IOFuncs.Default.getUserInput("Use Joomscan? (https://www.kali.org/tools/joomscan/)")
		useW3af = IOFuncs.Default.getUserInput("Use W3af? (https://www.kali.org/tools/w3af/)")
  
		return {"sessionMode": sessionMode, "attackSpeed": attackSpeed, "verboseLevel": verboseLevel, "useNmap": useNmap, "useNikto": useNikto, "useWfuzz": useWfuzz, "useDirb": useDirb, "useGobuster": useGobuster, "useWpscan": useWpscan, "useWapiti": useWapiti, "useJoomscan": useJoomscan, "useW3af": useW3af}

	def saveSessionConfig():
		pass
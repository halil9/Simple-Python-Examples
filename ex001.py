 #/
 # ==========================================================================
 #                     Filename:     ex001.py
 #                     Description:  Port Checker
 #                     Created:      02.05.2017
 #
 #         Author:  Ümit Öztürk
 #
 # ==========================================================================
 #/

import ipaddress 		## Adding ipaddress module ▬▶ IP VALIDICATION
from socket import * 	## Adding socket module	▬▶ SOCKET OPERATION
from sys import exit 	## Adding exit function
from time import sleep 	## Adding sleep function


def get_IP():
	try:
		targetIP = input("Target IP: ")		## Get target IP
		ip = ipaddress.ip_address(targetIP)	## ▬▶ IP Validication
		print("\033[32m ▬▶ %s \033[33m IPv:%s \n \033[37m" %(ip, ip.version))
		return targetIP
	except:
		print("\033[31mPlease enter a valid ip \033[37m")
		sleep(3)
		get_IP()


def port_Input():
	try:
		f_port = int(input("Enter the first port ▬▶ ")) ## Get first port
		if f_port < 0 or f_port > 65535:	## Port Check
			raise Exception("\033[31mPort number must be between 1 and 65535 \033[37m")
			sleep(3)
			port_Input()
	except:
		print("\033[31mPlease enter a correct port \033[37m")
		sleep(3)
		port_Input()
	try:
		l_port = int(input("Enter the last port ▬▶ ")) ## Get last port
		if l_port < 0 or l_port > 65535:
			raise Exception("\033[31mPort number must be between 1 and 65535  \033[37m")
			sleep(3)
			port_Input()
	except:
		print("\033[31mPlease enter a correct port \033[37m")
		sleep(3)
	return f_port, l_port

def port_Checker(first, last, ip):
	try:
		for i in range(first, last+1): ## Range function does not contain last element
			try:
				portSocket = socket(AF_INET, SOCK_STREAM)	## Creating a Socket
				portSocket.settimeout(0.05)
				con = portSocket.connect((ip, i)) ## Connection Port With Socket
				if con is None:
					print("\033[32m ▬▶ Port %s is OPEN! \033[37m" %(i))
				portSocket.close()
			except:
				print("\033[31m Port %s CLOSED  \033[37m" %(i))
	except:
		print("\033[31m Opss. Something Wrong ... I should exit. \033[37m")
		sleep(1)
		exit()

def main():
	targetIP = get_IP()
	first, last = port_Input()
	port_Checker(first, last, targetIP)

if __name__ == "__main__":
	main()
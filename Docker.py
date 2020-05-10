import os
import getpass 

while True:
	print ("press 1 for continue 0 for exit")
		
	c=input()
	if int(c) == 1:
		os.system("clear")
		os.system("tput setaf 3")
		print("\t\t\t ====================================================")
		os.system("tput setaf 1")
		print("\t\t\t\t DOCKER PROGRAM THAT HELPS EASY TO WORK")
		os.system("tput setaf 3")
		print("\t\t\t ====================================================")
		
		passwd = getpass.getpass("Enter your passwerd : ")
		mypass = "doc"
		if passwd != mypass:
			print("Incorrect password")
			exit()
			
		os.system("tput setaf 2")
		print("Press 1 for Docker configuration")
		print("Press 2 for Docker all info")
		print("Press 3 for To see Docker Image")
		print("Press 4 for To See Docker all running process")
		print("Press 5 for To download new image from docker")
		print("Press 6 for To enable docker permanently")
		print("Press 7 for To disable docker permanently")
		print("Press 8 for docker status")
		print("Press 9 for To run os on docker ")
		print("Press 10 for our own docker image")
		print("Press 11 for exit")			
		os.system("tput setaf 1")
		ch=input()
		if int(ch) == 3:
			print("\ncreate yum repositery copy the string\t\"[Docker] \n baseurl=https://download.docker.com/linux/centos/7/xx86_64/stable/ \n gpgheck=0\t \" on docker repository")	
			os.system("cd /etc/yum.repos.d/ && gedit km.repo && ls")
		elif int(ch) == 2:
			os.system("docker version & docker info")					
		elif int(ch) == 3:
			os.system("docker images")
		elif int(ch) == 4:
			os.system("docker ps -a")
		elif int(ch) == 5:
			print("Which image you want to download use systex \n\" docker pull <OS nme> \" \nwrite")
			os.system(input())	
		elif int(ch) == 6:
			os.system("systemctl enable docker")
		elif int(ch) == 7:
			os.system("systemctl disable docker")
		elif int(ch)== 8:
			os.system("systemctl status docker")		
		elif int(ch) == 9:
			print("Write syntex with os image name\" docker run -it <os name>:version\"")
			os.system(input())
		elif int(ch) == 10:
			print("Write syntex \" docker commit <os name>  <image name(by user)>\"")
			os.system(input())
		elif int(ch) == 11:			
			os.system("tput setaf 7")				
			exit()		
	elif int(c) == 0:
		os.system("tput setaf 7")
		break





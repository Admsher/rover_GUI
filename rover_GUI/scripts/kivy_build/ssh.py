#!/usr/bin/env python3
import rospy
# import getpass
# from fabric import Connection,Config

# password=getpass(input("enter your root passcode:"))
# # config=Config(overides={'sudo':{'password':password}})
# # conn=Connection('192.168.240.245',user="ishangokhale")

# import paramiko
# output_file = 'paramiko.org'


# def paramiko_GKG(hostname, command):
# 	print('running')
# 	try:
# 		port = '22'
		
# 		# created client using paramiko
# 		client = paramiko.SSHClient()
		
# 		# here we are loading the system
# 		# host keys
# 		client.load_system_host_keys()
		
# 		# connecting paramiko using host
# 		# name and password
# 		client.connect('192.168.240.250', port=22, username='koustav',
# 					password='kratos123')
		
# 		# below line command will actually
# 		# execute in your remote machine
# 		(stdin, stdout, stderr) = client.exec_command("ls")
		
# 		# redirecting all the output in cmd_output
# 		# variable
# 		cmd_output = stdout.read()
# 		print('log printing: ', command, cmd_output)
		
# 		# we are creating file which will read our
# 		# cmd_output and write it in output_file
# 		with open(output_file, "w+") as file:
# 			file.write(str(cmd_output))
			
# 		# we are returning the output
# 		return output_file
# 	finally:
# 		client.close()


# paramiko_GKG('192.168.240.250', 'koustav')

# _____________________________________________________________-

# import paramiko
# import numpy as np
import os
# from pexpect import pxssh
# try:
#     s = pxssh.pxssh()
#     hostname = '192.168.240.250'
#     username = 'koustav'
#     password = 'kratos123'
#     s.login(hostname, username, password)
#     s.sendline("roscore") # run a command
    
#     # s.sendline("gnome-terminal -x bash -c 'source ~/kratos/devel/setup.bash;rosrun urc2022 videofeed1 0'&") # run a command
#     s.prompt()             # match the prompt
#     print(s.after)        # print everything before the prompt. 
#     s.logout()
# except pxssh.ExceptionPxssh as e:
#     print("pxssh failed on login.")
#     print(e)

# os.system("ssh koustav@192.168.240.250 & roscore &")
# os.system("'source ~/kratos/devel/setup.bash;roscore'&")
# os.system("gnome-terminal -- bash -c 'ssh koustav@192.168.240.250'")


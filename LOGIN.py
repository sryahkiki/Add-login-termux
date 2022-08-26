#coding: utf-8
# module
import os,sys,time,getpass

# username
x = "surya"
# paasword
y = "pwemailsurya"

# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)

# login
def login():
  os.system("clear")
  sp("\033[1;92mP")
  sp(" \033[1;92mL")
  sp("  \033[1;92mE")
  sp("   \033[1;92mA")
  sp("    \033[1;92mS")
  sp("     \033[1;92mE . . . . ")
  sp("")
  sp("\033[1;96m   ██      ▐██████  ▐██████   ████  █████  ████   ██")
  sp("   ██      ▐█   ██  ▐█         ██    ███    ██    ██")
  sp("   ██      ▐█   ██  ▐█   ███   ██    ██ █   ██    ██")
  sp("   ██      ▐█▄  ██  ▐█   ██    ██    ██  █  ██    ██")
  sp("   ██  ██  ▐██  ██  ▐██  ██    ██    ██  █  ██    ██")
  sp("   ██  ██  ▐██  ██  ▐██  ██    ██    ██   █ ██      ")
  sp("   ██████  ▐██████  ▐██████   ████  ████   ████   ██")
  sp("")
  sp("\033[1;92m=========================================\033[1;92m")
  sp("")
  sp(" \033[1;97m{\033[1;95m+\033[1;97m} \033[1;93mOwner     \033[1;91m: \033[1;95mMr14")
  sp(" \033[1;97m{\033[1;95m+\033[1;97m} \033[1;93mInstagram \033[1;91m: \033[1;95msryahkiki_")
  sp(" \033[1;97m{\033[1;95m+\033[1;97m} \033[1;93mAge       \033[1;91m: \033[1;95m20")
  sp(" \033[1;97m{\033[1;95m+\033[1;97m} \033[1;93mDevice    \033[1;91m: \033[1;95mRedmi 4x")
  sp("")
  sp("\033[1;92m=========================================\033[1;92m")
  sp(" \033[1;91mWelcome tuan,siap membantu kegiatan kapan pun tuan membutuhkannya")
  sp("")
  username = raw_input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername: ")
  password = getpass.getpass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
  sp("") 
  if username == x and password == y:
    print(" \033[1;92mAccess Granted")
    time.sleep(1)
  else:
    print(" \033[1;91mAccess Denied")
    time.sleep(1)
    login()

login()

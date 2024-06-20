from dhooks import Webhook,Embed
import sys
import os
import time 

from colorama import Fore
from os import system
from time import sleep


system("title " + "WEBHOOK Spammed")

os.system("cls")
def SlowPrint(_str):
    for letter in _str:
        #slowly print out the words 
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.03)

panel="""
$$\       $$\                              
$$ |      \__|                             
$$ |  $$\ $$\ $$$$$$$$\ $$$$$$$$\ $$$$$$\  
$$ | $$  |$$ |\____$$  |\____$$  |\____$$\ 
$$$$$$  / $$ |  $$$$ _/   $$$$ _/ $$$$$$$ |
$$  _$$<  $$ | $$  _/    $$  _/  $$  __$$ |
$$ | \$$\ $$ |$$$$$$$$\ $$$$$$$$\\$$$$$$$ |
\__|  \__|\__|\________|\________|\_______|
                                           
 $$$$$$\                                                                      
$$  __$$\                                                                     
$$ /  \__| $$$$$$\   $$$$$$\  $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  
\$$$$$$\  $$  __$$\  \____$$\ $$  _$$  _$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ 
 \____$$\ $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  \__|
$$\   $$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$ | $$ | $$ |$$   ____|$$ |      
\$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$$\ $$ |      
 \______/ $$  ____/  \_______|\__| \__| \__|\__| \__| \__| \_______|\__|      
          $$ |                                                                
          $$ |                                                                
          \__|                                                                
"""
print(panel)

spam_work = f"""{Fore.RED}

 $$$$$$\                                                      $$\                          $$\                     $$\ 
$$  __$$\                                                     $$ |                         $$ |                    $$ |
$$ /  \__| $$$$$$\   $$$$$$\  $$$$$$\$$$$\         $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$$$$$\    $$$$$$\  $$$$$$$ |
\$$$$$$\  $$  __$$\  \____$$\ $$  _$$  _$$\       $$  _____|\_$$  _|   \____$$\ $$  __$$\ \_$$  _| $$  __$$\ $$  __$$ |
 \____$$\ $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |      \$$$$$$\    $$ |     $$$$$$$ |$$ |  \__| $$ |    $$$$$$$$ |$$ /  $$ |
$$\   $$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |       \____$$\   $$ |$$\ $$  __$$ |$$ |       $$ |$$\ $$   ____|$$ |  $$ |
\$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |      $$$$$$$  |  \$$$$  |\$$$$$$$ |$$ |       \$$$$  |\$$$$$$$\ \$$$$$$$ |
 \______/ $$  ____/  \_______|\__| \__| \__|      \_______/    \____/  \_______|\__|        \____/  \_______| \_______|
          $$ |                                                                                                         
          $$ |                                                                                                         
          \__|                                                                                                         

"""


embed = Embed(
    description='STOP SENDING LOGGERS SKID  GAY :sunglasses:',
    color=0x5CDBF0,
    timetamp='now'
)

webhookk = input("\u001b[32mEntre l'URL du webhook: "f"{Fore.RESET}")
os.system("cls")
hook = Webhook(webhookk)

image2 = 'https://i.imgur.com/K7hZxcm.png'
image3 = 'https://pbs.twimg.com/media/Bpvdm-QIgAAsoX5.jpg'
image4 = 'https://i.imgur.com/uAP2Ctf.jpg'
image5 = 'https://i.imgur.com/IY3kK8M.jpg'
embed.set_author(name='By|kizzouille#6969| You are CLOWN ', icon_url=image4)
embed.add_field(name='YOURE A FUCKING CLOWN', value='NOOBY NULLOS SOUS MERDE')
embed.set_footer(text='FUCK YOU', icon_url=image3)
embed.set_footer(text='ur so bad', icon_url=image5)
embed.set_thumbnail(image2)
embed.set_image(image5)

#spam pannel show
print(spam_work)
testboucle = 0
while testboucle < 30:
        hook.send(embed=embed)
        testboucle += 1
        result = str(testboucle)
        if testboucle % 10 == 0:
            print("Succesfully spammed", testboucle, "times!")
time.sleep(2)
SlowPrint("\u001b[31mRestart for more spam!\n")
SlowPrint(f"{Fore.RESET}Credit to kizzouille | Have good day !")
time.sleep(3)

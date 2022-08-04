# By Joji - 8/4/22
# Uploaded at 3:58 PM
# If you have any questions comment and if I remember I shall reply
import dhooks
import colorama
from dhooks import Webhook
from colorama import Fore, Back, Style

colorama.init()

Auth1 = ['Admin', 'Password']


val = input('Username: ')
val1 = input('Password: ')

hook = Webhook("Your_Webhook_Here")
LoggedIn = False

if val == Auth1[0]:
    
    if val1 != Auth1[1]:
        print(Fore.RED + 'Invalid Password')
        val
    
    elif val1 == Auth1[1]:
        print("Logged In")
        LoggedIn = True
        val2 = input(Fore.LIGHTYELLOW_EX + 'Send A Message To The Creator: ')
        hook.send(val2)
        print(Fore.GREEN + 'Message Has Been Sent!')




######NOTES############
#if LoggedIn == False:
 #    exit()
# if LoggedIn == True:
  #  val2
   # hook.send(val2)



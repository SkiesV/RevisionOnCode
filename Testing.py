import dhooks
import colorama
from dhooks import Webhook
from colorama import Fore, Back, Style

colorama.init()

Auth1 = ['Admin', 'Password']
Auth2 = ['Joji', 'Joji123']


val = input('Username: ')
val1 = input('Password: ')

hook = Webhook("https://discord.com/api/webhooks/1004815385616466002/JBNpnd4U7DP5_x11vx51JbSWDbNhhCnS13J8jtkbC8Fepzxj6wL1wAqCOcv4lK91cjYz")
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



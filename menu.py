import shutil,os,crawler2,sys,random,time
from threading import Thread as th
from crawler2 import HANDLER,MENU
from termcolor import colored,cprint
cores=['red','yellow','green','cyan','grey','white']
urlusar=0
obj=[]
listaurl=[]
os.system("clear")
url=input(colored('Qual é o url?',random.choice(cores)))
if "http" not in url:
    if 'https' not in url:
        while 1:
            prefixo=input("HTTP ou HTTPS?")
            if prefixo.lower() == "http":
                url="http://"+url
                break
            if prefixo.lower() == "https":
                url = "https://"+url
                break
            else:
                continue
obj.append(HANDLER(url))
listaurl.append(url)
obj[urlusar].read()
objmenu=MENU(urlusar,1)
objmenu.atualizalista(url)
varth = th(target=objmenu.menu)
varth.daemon=True
varth.start()

def poupa():
    objmenu.stop()
    time.sleep(0.2)
    os.system("clear")




while 1:
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    lines = lines//2
    opc=input()
    if opc == "1":
        print("WIP")
        poupa()
        obj[urlusar].iniciathread()
        #objmenu.start()
    elif opc == "2":
        print("WIP")
    elif opc == "3":
        print("WIP")
    elif opc == "4":
        print("WIP")
    elif opc == "5":
        print("WIP")
    elif opc == "6":
        poupa()
        url = input(colored("Qual é o url?",random.choice(cores)))
        if "http" not in url:
            if 'https' not in url:
                while 1:
                    prefixo=input("HTTP ou HTTPS?")
                    if prefixo.lower() == "http":
                        url="http://"+url
                        break
                    if prefixo.lower() == "https":
                        url = "https://"+url
                        break
                    else:
                        continue
        objmenu.atualizalista(url)
        objmenu.start()
        listaurl.append(url)
        obj.append(HANDLER(url))
        obj[len(obj)-1].read()
    elif opc == "7":
        poupa()
        i=1
        print("\n"*lines)
        for x in listaurl:
            print(colored((str(i)+" "+x).center(columns),random.choice(cores)))
            i+=1
        urlusar=int(input("Qual é o id do url?"))-1
        objmenu.atualiza(urlusar)
        objmenu.start()

    elif opc == "sair":
        objmenu.stop()
        time.sleep(0.2)
        os.system("clear")
        print("Adeus!")
        time.sleep(1)
        os.system("clear")
        sys.exit(1)
    else:
        continue

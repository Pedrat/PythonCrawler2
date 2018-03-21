import requests,os,sys,shutil,random,time
from bs4 import BeautifulSoup
from termcolor import colored,cprint
from threading import Thread as th

class HANDLER:
    def __init__(self,url):
        self.url = url
        self.listadork=[]
        self.listadork2=[]
        self.listadorks=[self.listadork,self.listadork2]
        self.listadorksvalidos=[]
        self.threads=[]
    def read(self):
        tamanho=0
        i=0
        for x in open("dorks.txt",'r'):
            tamanho+=1
        for x in open("dorks.txt",'r'):
            if i<=(tamanho//2):
                self.listadork.append("/"+x.replace("\n",''))
                i+=1
            else:
                self.listadork2.append("/"+x.replace("\n",''))
                i+=1

    def iniciathread(self):
        for i in range(0,2):
            self.threads.append(th(target=self.crawler,args=str(i)))
        self.start()
    def start(self):
        for x in self.threads:
            x.daemon=True
            x.start()

    def crawler(self,i):

        lista=self.listadorks[int(i)]
        if "http" not in self.url:
            if "https" not in self.url:
                self.url= "http://"+self.url
                url2 = self.url + x + "1'"
            else:
                url2 = self.url + x + "1'"
        if "https://" in self.url:
            url=self.url.split("https://")
        elif "http://" in self.url:
            url=self.url.split("http://")
        self.cria(url[1])
        for x in lista:
            #if valida == 1:
            #ry:
            if 1==1:

                page= requests.get(url2)
                contents=page.text
                if 'deprecated' in contents  :
                    self.listadorksvalidos.append(x)
                    cprint("vulnerabilidade encontrada!",'red')
                    self.save(url[1],x)
                elif 'You have an error in your SQL syntax' in contents:
                    self.listadorksvalidos.append(x)
                    self.save(url[1],x)
                    cprint("vulnerabilidade encontrada!",'red')
                elif 'Query fail' in contents:
                    self.listadorksvalidos.append(x)
                    self.save(url[1],x)
                    cprint("vulnerabilidade encontrada!",'red')
            #except:
                #    cprint("Ocorreu um erro (Time out talvez?)",'red')
                #    continue
        sys.exit(1)

    def cria(self,url):
        nome=url+".txt"
        file=open(nome,'w')
        file.write("Começou."+'\n')
        file.close()


    def save(self,url,dork):
        nome=url+".txt"
        file=open(nome,'a')
        file.write(dork+'\n')
        file.close()

    def pelica(self,url):
        if 'https' not in self.url:
            if 'http' not in self.url:
                while 1:
                    prefix=input("É http ou https?\n")
                    if prefix == "http":
                        prefix='http://'
                        self.url = prefix + self.url
                        break
                    elif prefix == "https":
                        prefix ='https://'
                        self.url = prefix + self.url
                        break
                    else:
                        cprint("Invalido!",'red')
        cprint(self.url,'magenta')
        page=requests.get(self.url+"'")
        contents=page.text
        if 'deprecated' in contents  :
            cprint("Vulneravel",'red')
        elif 'You have an error in your SQL syntax' in contents:
            cprint("Vulneravel",'red')
        elif 'Query fail' in contents:
            cprint("Vulneravel",'red')
        else:
            cprint("Não foi encontrada vulnerabilidade",'green')

    def subfinder(self):
        try:
            prefixo=""
            url = input("URL do website:\n")
            if "http" not in self.url:
                if "https" not in self.url:
                    antes = input("HTTP ou HTTPS?\n")
                    if antes == "https":
                        prefixo = 'https://'
                    elif antes == "http":
                        prefixo = 'http://'
            sufixo = '/'
            r = requests.get(prefixo + self.url + sufixo)
            data = r.text
            sopa = BeautifulSoup(data, "lxml")
            nome=self.url.split(".")
            nomecompleto = (nome[1]+".txt")
            for x in sopa.find_all('a'):
                print(x.get('href'))
                f = open(nomecompleto,"a")
                f.write("\n"+x.get('href'))
                f.close()
        except:
            cprint('Ocorreu um erro!\n','red')


class MENU:
    def __init__(self,urlusar,valida):
        self.listaurl=[]
        self.urlusar = urlusar
        self.valida=valida


    def menu(self):
        cores=['red','yellow','green','cyan','grey','white']
        while 1:
            if self.valida==1:
                time.sleep(0.2)
                columns = shutil.get_terminal_size().columns
                lines = shutil.get_terminal_size().lines
                os.system("clear")
                calma=''
                menu=['1-Crawler', '2-Pelica', '3-Google Dork Search', '4- Crawler pelo ficheiro',"5-Directory Finder",'6-Adicionar URL','7-Mudar de Url', 'Escreva sair', 'Opção:']
                lines= (lines//2)-(len(menu)//2)-1
                print("\n"*lines)
                print(colored("URL a usar: "+self.listaurl[int(self.urlusar)],random.choice(cores)))
                for x in menu:
                    print(colored(x,random.choice(cores)).center(columns))
            else:# self.valida==0:
                a=2
    def atualiza(self,urlusar):#,valida):
        self.urlusar=urlusar
        #self.valida=valida
    def atualizalista(self,lista):
        self.listaurl.append(lista)
    def start(self):
        self.valida=1
    def stop(self):
        self.valida=0

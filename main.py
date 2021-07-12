import requests
from bs4 import *
import time
import colorama
from colorama import Fore
colorama.init()

print(Fore.BLUE+'''
    ____  ____  ____ _  ____  __   
   / __ \/ __ \/ __ \ |/ /\ \/ /   
  / /_/ / /_/ / / / /   /  \  /    
 / ____/ _, _/ /_/ /   |   / /     
/_/   /_/ |_|\____/_/|_| _/_/   __ 
                  / /   (_)____/ /_
                 / /   / / ___/ __/
                / /___/ (__  ) /_  
               /_____/_/____/\__/  ::::::
                                   
''')

def write_proxies_to_file(proxy, output_file):
    with open(output_file, 'a') as fp:
        fp.write(proxy + '\n')
        fp.close()

print(Fore.CYAN+'::::::::::::::::::::::')
print(Fore.CYAN+'::::::::::::::::::::::')
print(Fore.GREEN+"\nListing Proxy IPs.......\n\n")
time.sleep(1)
print("Here is the list--")

ProxyList = "https://free-proxy-list.net/"

data1 = requests.get(ProxyList)
data2 = data1.content

soup =BeautifulSoup(data2, 'html.parser')

html_table = soup.find('table', {'id' : 'proxylisttable'})
table = html_table.find_all('tr')

for row in table:
    column = row.find_all('td')
    try:
        print(Fore.GREEN+"IP Address : "+column[0].get_text(), Fore.YELLOW + "    Port : "+column[1].get_text(), Fore.GREEN + "    Country : "+column[3].get_text(), Fore.RED + "    Anonymiy : "+column[4].get_text())
        inf = "IP Address : "+column[0].get_text()+"    Port : "+column[1].get_text()+"    Country : "+column[3].get_text()+"    Anonymiy : "+column[4].get_text()
        write_proxies_to_file(inf, "ProxyList.txt")
    except:
        pass

input("\nProxyListing Finished!!\n")
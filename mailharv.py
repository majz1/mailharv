import requests
import re
from bs4 import BeautifulSoup
import tldextract
print("""  __  __          _____ _      _    _          _______      __
 |  \/  |   /\   |_   _| |    | |  | |   /\   |  __ \ \    / /
 | \  / |  /  \    | | | |    | |__| |  /  \  | |__) \ \  / / 
 | |\/| | / /\ \   | | | |    |  __  | / /\ \ |  _  / \ \/ /  
 | |  | |/ ____ \ _| |_| |____| |  | |/ ____ \| | \ \  \  /   
 |_|  |_/_/    \_\_____|______|_|  |_/_/    \_\_|  \_\  \/    
                                                              
                                                      

Developed by majz1 



                                                                                      """)
def search_mail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            subdomain = tldextract.extract(url).subdomain
            soup = BeautifulSoup(response.text, 'html.parser')
            for tag in soup.find_all(text=re.compile('@')):
                words_with_at = re.findall(r'\S+@\S+', tag)
                if words_with_at:
                    print(f'[+] Printing emails or similars that contains "@" in {url} (subdomain {subdomain}):')
                    for word in words_with_at:
                        print(word)

            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith('http') and subdomain in href:
                    search_mail(href)

        else:
            print(f'[+] Error at obtaining the content of the page {url}. Status code: {response.status_code}')
    except Exception as e:
        print(f'[+] An error ocurred: {e}')

if __name__ == "__main__":
    url = input("[+] Introduce the URL of the website\n[-] ")
    search_mail(url)

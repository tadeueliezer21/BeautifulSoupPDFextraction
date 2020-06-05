from tqdm import tqdm #progressbar
import requests
from bs4 import BeautifulSoup as bs

#your URL_BASE
#exemple: 'https://mywebsite.com.br/'
URL = ''

#file type
FILETYPE = '.pdf'

#your css selector
#exemple: 'body > .container > .row .col-sm-6 .panel > .panel-collapse > .panel-body > ul > li > a'
CSS_SELECTOR = ''

def get(url):
    content = bs(requests.get(url).text, 'html.parser')
    return content.select(CSS_SELECTOR)

def getFiles():
    c = [x for x in get(URL)]
    for i in tqdm(range(len(c)), ascii=True, desc="Downloading"):
        
        file_link = c[i].get('href')
        file_name = c[i].text
        
        if FILETYPE in file_link:
            response = requests.get(URL+file_link)
            
            if file_name.find("/"):
                file_name = file_name.replace("/", "-")

            open(file_name+'.pdf', 'wb').write(response.content)
            
    print("Finish!")

if __name__ == '__main__':
    getFiles()
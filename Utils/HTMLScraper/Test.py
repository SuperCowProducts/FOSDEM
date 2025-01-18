'''
TODO 

- €
 - find out how random scale machine works (may need to find a way to scrape javascript instead of just html)
 - make your own random scale machine
 



'''
# https://stackoverflow.com/questions/66109042/how-do-i-copy-the-html-code-of-a-website-to-a-text-file-in-python

import requests
from bs4 import BeautifulSoup
import bs4

headers = {
    
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15"
}

with open("input2.txt", "r", encoding="utf8") as f:
    input2=f.read()

with open("input.txt", "r", encoding="utf8") as f:
    input=f.read()
    #page = requests.get(f"{f}", headers=headers, cookies = {'CONSENT' : 'YES+'}).text
    page = requests.get(f"{input}").text
with open("output.txt", "w", encoding="utf8") as f:
    #https://stackoverflow.com/questions/40255128/how-to-parse-the-website-using-beautifulsoup
    #page = requests.get("https://www.therandomscalemachine.com/", headers=headers, cookies = {'CONSENT' : 'YES+'}).text

    #https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
    soup = BeautifulSoup(page, "html.parser")
    #https://www.w3schools.com/python/ref_file_write.asp
    f.write(str(soup))
    #f.write(soup.encode('utf8'))
    
    
#https://stackoverflow.com/questions/66128867/retrieving-text-from-specific-class-html-tags-and-storing-into-an-array-in-pytho
    
    
def get_titles(soup):
    pbe_titles = soup.find_all(attrs={'class': f'{input2}'})
    for tag in pbe_titles :
        yield tag.text.strip()

titles = list(get_titles(soup))
print(titles)


with open("output2.txt", "w", encoding="utf8") as f:
    for i in titles:
        print(i, file=f)
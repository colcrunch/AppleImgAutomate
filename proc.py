from PIL import Image
import re
import glob, os
import requests
from contextlib import closing
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

src = "url_redacted"
regex = r'[S][T][0-9]{8}'
regex2  = ''
binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\firefox.exe")

with closing(Firefox(firefox_binary=binary)) as browser:
    browser.get(src)
    WebDriverWait(browser, timeout=10)
    page_source = browser.page_source

with open("output2.html", "w", encoding="utf-8") as file:
    file.write(page_source)

soup = BeautifulSoup(open("output2.html", encoding="utf-8"), 'html.parser')

dP = soup.find_all("div", "panel")
tS = []
iS = []

for d in dP:
    t = d.find_all("p")
    v = d.find_all("img", {'height': '200px'})
    for w in v:
        i = re.search(regex, w['src'])
        if i is not None:
            iS.append(i[0])
        else:
            iS.append('N')
    for u in t:
        tS.append(u.text)
print(tS)
print(iS)
movs = dict(zip(tS, iS))
print(movs)
    
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    t = im.resize((185, 278), Image.BILINEAR)
    f = im.resize((450, 675), Image.BILINEAR)
    if file in movs:
        print(file + movs[file])
        f.save("sn"+movs[file]+".jpg", "JPEG")
        print(file+" >> "+"s"+movs[file]+".jpg")
        t.save("s"+movs[file]+".jpg", "JPEG")
        print(file+" >> "+"sn"+movs[file]+".jpg")
    else:
        f.save(file+"-_-screen.jpg", "JPEG")
        print(file+" > > "+file+"-_-screen.jpg")
        t.save(file+"-_-movie.jpg", "JPEG")
        print(file+" > > "+file+"-_-movie.jpg")

os.system("move sn*.jpg screens")
os.system("move sS*.jpg movies")
os.system("move *-_-screen.jpg screens")
os.system("move *-_-movie.jpg movies")
os.system("move *.jpg originals")
os.system("del output2.html")

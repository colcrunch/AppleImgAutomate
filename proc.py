from PIL import Image
import re
import glob, os
import requests
import json

src = "http://RTS_SERVER_ID:2235/showtimes.json"

shows = requests.get(src)
json = shows.json()

films = json['films']

tS = []
iS = []

for film in films:
    tS.append(film['name'])
    iS.append(film['RtsCode'])

movs = dict(zip(tS,iS))

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    t = im.resize((185, 278), Image.BILINEAR)
    f = im.resize((450, 675), Image.BILINEAR)
    file = file.upper()
    if file in movs:
        print(file + movs[file])
        f.save("sn"+movs[file]+".jpg", "JPEG")
        print(file+" >> "+"sS"+movs[file]+".jpg")
        t.save("s"+movs[file]+".move", "JPEG")
        print(file+" >> "+"sn"+movs[file]+".jpg")
    else:
        f.save(file+"-_-screen.jpg", "JPEG")
        print(file+" > > "+file+"-_-screen.jpg")
        t.save(file+"-_-movie.jpg", "JPEG")
        print(file+" > > "+file+"-_-movie.jpg")

os.system("move sn*.jpg screens")
os.system("move s*.move movies")
os.system("move *-_-screen.jpg screens")
os.system("move *-_-movie.jpg movies")
os.system("move *.jpg originals")
os.system("cd movies && ren *.move *.jpg")


import os, shutil, re, requests
from bs4 import BeautifulSoup

def move_images():
    src=input("Source folder: ")
    dst=input("Destination folder: ")
    os.makedirs(dst, exist_ok=True)
    moved=0
    for f in os.listdir(src):
        if f.lower().endswith((".jpg",".jpeg")):
            shutil.move(os.path.join(src,f), os.path.join(dst,f))
            moved+=1
    print(f"Moved {moved} image(s).")

def extract_emails():
    path=input("Text file: ")
    with open(path,"r",encoding="utf-8") as fp:
        text=fp.read()
    emails=sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",text)))
    os.makedirs("output",exist_ok=True)
    with open("output/emails.txt","w") as fp:
        fp.write("\n".join(emails))
    print("Saved output/emails.txt")

def scrape_title():
    url=input("URL: ")
    r=requests.get(url,timeout=10)
    r.raise_for_status()
    title=BeautifulSoup(r.text,"html.parser").title.string
    os.makedirs("output",exist_ok=True)
    with open("output/webpage_title.txt","w") as fp:
        fp.write(title or "")
    print(title)

def menu():
    while True:
        print("\n1.Move JPG\n2.Extract Emails\n3.Scrape Title\n4.Exit")
        c=input("Choice: ")
        if c=="1": move_images()
        elif c=="2": extract_emails()
        elif c=="3": scrape_title()
        elif c=="4": break

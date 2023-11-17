
import requests
import os
#from tqdm import tqdm

def download(url, filename=0, subfolder=None):
    if filename==0:
        filename = url.split('/')[-1]
        if "." not in filename:
            filename += ".html"
    #chunk_size = 1024
    req = requests.get(url #, headers={ 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36" }#, stream = True
    )
    #total_size = int(req.headers['content-length'])
    if not subfolder==None:
        ls = os.listdir()
        if subfolder not in ls:
            os.mkdir(subfolder)
        os.chdir(subfolder)
    with open(filename, "wb") as file:
        data =req.content
        #for data in tqdm(iterable=req.iter_content(chunk_size=chunk_size), total = total_size/chunk_size, unit='KB'):
        file.write(data)
    if subfolder!=None:
        os.chdir("..")
#
link = lambda n : f"https://death-note-manga-online.com/manga/death-note-chapter-{n}/"
chapters = [x for x in range(1,111)]
for chapter_number1 in chapters:
    chapter_number3 = f"{chapter_number1:03}"
    folder = "Chapter " + chapter_number3
    os.mkdir(folder)
    os.chdir(folder)
    chapter_link = link(chapter_number1)
    html = requests.get(chapter_link).text
    pages_number = html.count(">PAGE")+1
    pages = [n for n in range(1, pages_number+1)]
    for page_number in pages:
        img_url = f"https://cdn.readdetectiveconan.com/file/mangap/938/10{chapter_number3}000/{page_number}.jpg"
        download(url=img_url, filename=f"c{chapter_number3}p{page_number:02}.jpg")
    os.chdir("..")
input("Done")
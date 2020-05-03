import os

def createIfNoteExist(Folder):
    if not os.path.exists(Folder):
        os.makedirs(Folder)

def mov(folderName,files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")





files = os.listdir()
files.remove("main.py")
createIfNoteExist('Images')
createIfNoteExist('Docs')
createIfNoteExist('Media')
createIfNoteExist('others')
imgExts=[".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
docExts=[".doc",".txt",".pdf",".docx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


mediaExts = [".mp3",".mp4",".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []

for file in files:
    hatao = os.path.splitext(file)[1].lower()
    if (hatao not in mediaExts) and (hatao not in docExts)  and (hatao not in  imgExts) and os.path.isfile(file):
        others.append(file)

mov("Images", images)
mov("Docs", docs)
mov("Media", medias)
mov("others", others)



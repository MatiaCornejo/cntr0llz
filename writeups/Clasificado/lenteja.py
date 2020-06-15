from zipfile import ZipFile
name=1999
new_dir="files/"
while True:
    with open("1000.txt", "r") as file:
        with ZipFile('./files/'+str(name)+'.zip') as zf:
            for line in file:
                try:
                    zf.extract("files/"+str(name-1)+".zip",pwd=bytes(line.strip(),'utf-8'))
                    print("Pass: "+line)
                    print("Name :"+ str(name)+".zip")
                    name-=1
                except Exception as e:
                    pass

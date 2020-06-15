from PIL import Image
img = Image.open("papel_pegado.png").convert('RGB')
pix= img.load()
current=""
qr=[]
for y in range(21):
    for x in range(21):
        pixel=pix[y,x]
        if pixel == (255,255,255):
            current+="_"
        elif pixel == (0,0,0):
            current+="X"
        else:
            current+="?"
    print(current)
    qr.append(current)
    current=""
with open("qr.txt","w") as fl:
    fl.write("\n".join(qr))
img.close()
print("Finalizado")

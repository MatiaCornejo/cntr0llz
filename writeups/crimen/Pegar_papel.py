from PIL import Image
#ruta donde estan las partes de imagen
ruta="./imagenes/{0}-{1}.png"
#Almacen de pixel
pix=""
respaldo = Image.new('RGB', (21, 21), color = 'black')
#Cargar y permitir edicion de pixeles
respaldo2=respaldo.load()
#Pegar
for Xi in range(21):
    for Yi in range(21):
        if Xi < 10 and Yi >=10:
            cXi="0"+str(Xi)
            img = Image.open(ruta.format(Yi,cXi)).convert('RGB')
            pix= img.getcolors()
            img.close()
        if Xi>=10  and Yi<10 :
            cYi="0"+str(Yi)
            img = Image.open(ruta.format(cYi,Xi)).convert('RGB')
            pix= img.getcolors()
            img.close()
        elif Xi<10 and Yi<10:
            cXi="0"+str(Xi)
            cYi="0"+str(Yi)
            img = Image.open(ruta.format(cYi,cXi)).convert('RGB')
            pix= img.getcolors()
            img.close()
        elif Xi >=10 and Yi >=10:
            img = Image.open(ruta.format(Yi,Xi)).convert('RGB')
            pix = img.getcolors()
            img.close()
        #pintar pixel
        pix=pix[0]
        respaldo2[Yi,Xi]=pix[-1]
respaldo.save('papel_pegado.png')
print("Finalizado")

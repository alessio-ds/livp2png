import os
from heic_image_converter.Converter import Converter as converti

listalivp=os.listdir()
print(listalivp)
for e in listalivp:
    if '.py' in e:
        pass
    elif '.' not in e:
        pass
    elif '.livp' in e:
        os.system(f'tar -xf "{e}"')
        #os.system(f'del "{e}"') 
        # remove the "#" on the previous line if you wish to delete the livp file in the current folder after unpacking it
    else:
        pass
listaspacchettati=os.listdir()
percorso=os.getcwd()
ImgConverter = converti(percorso)
ImgConverter.convert_files()
for e in listaspacchettati:
    if '.mov' in e or ".heic" in e:
        pass
        os.system(f'del "{e}"')
    elif '.py' in e:
        pass
    elif '.' not in e:
        pass
    elif 'png' in e:
        pass
    else:
        pass

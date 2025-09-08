#Importar modulos necesarios
import os
import shutil

#Definimos las extensiones por tipo

tipos={
    "Imagenes":[".jpg",".jpeg",".png",".gif"],
    "Documentos":[".pdf",".docx",".txt",".xlsx"],
    "Videos":[".mp4",".avi",".mov",".mkv"]
}

#Crear subcarpetas si no existen
def crear_subcarpetas(destino,categorias):
    for categoria in categorias:
        ruta=os.path.join(destino,categoria)
        if not os.path.exists(ruta):
            os.makedirs(ruta)
    #Carpeta "Otros"
    otros=os.path.join(destino,"Otros")
    if not os.path.exists(otros):
        os.makedirs(otros)
        
#Clasificar y mover archivos
def organizar_archivos(carpeta):
    crear_subcarpetas(carpeta,tipos.keys())
    
    for archivo in os.listdir(carpeta):
        ruta_archivo= os.path.join(carpeta,archivo)
        
        if os.path.isfile(ruta_archivo):
            extension=os.path.splitext(archivo)[1].lower()
            destino= None
            for categoria, extensiones in tipos.items():
                if extension in extensiones:
                    destino= os.path.join(carpeta,categoria)
                    break
            if destino is None:
                destino= os.path.join(carpeta,"Otros")
                
            shutil.move(ruta_archivo,os.path.join(destino,archivo))
#Ejecutar el script
if __name__=="__main__":
    carpeta_descargas="descargas"
    organizar_archivos(carpeta_descargas)
    print("Archivos organizados Correctamente.")
    
#Importar modulos necesarios
import os
import shutil
import time
import schedule
from datetime import datetime

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
    try:
        crear_subcarpetas(carpeta,tipos.keys())
        
        archivos_movidos = 0
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
                archivos_movidos += 1
        
        # Log de la actividad
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Organización completada. {archivos_movidos} archivos movidos.")
        
    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Error: {e}")

# Función para ejecutar la organización
def ejecutar_organizacion():
    carpeta_descargas="descargas"
    organizar_archivos(carpeta_descargas)

# Configurar tareas programadas
def configurar_automatizacion():
    # Ejecutar cada 30 minutos
    schedule.every(30).minutes.do(ejecutar_organizacion)
    
    # Ejecutar cada hora
    # schedule.every().hour.do(ejecutar_organizacion)
    
    # Ejecutar todos los días a las 9:00 AM
    # schedule.every().day.at("09:00").do(ejecutar_organizacion)
    
    print("Organizador automático iniciado...")
    print("Presiona Ctrl+C para detener")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

#Ejecutar el script
if __name__=="__main__":
    # Ejecutar una vez inmediatamente
    ejecutar_organizacion()
    
    # Configurar automatización
    configurar_automatizacion()

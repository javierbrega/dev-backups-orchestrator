import os
import zipfile
from datetime import datetime
from dotenv import load_dotenv

# 1. Cargar variables de entorno (Seguridad y Configuración)
load_dotenv()

def compress_folder(source_dir, output_filename):
    """
    Lógica de compresión: Camina por la carpeta origen y mete todo en un ZIP.
    Usa rutas relativas para que el ZIP sea limpio al descomprimirlo.
    """
    try:
        # Creamos el archivo ZIP con compresión deflated (estándar)
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # El arcname evita que se guarde toda la ruta C:/Users/... dentro del zip
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
        return True
    except Exception as e:
        print(f"❌ Error en la compresión: {e}")
        return False

def main():
    print("--- 🚀 Dev Backups Orchestrator ---")
    
    # 2. Capturar rutas del .env
    source = os.getenv("SOURCE_PATH")
    dest_folder = os.getenv("BACKUP_DESTINATION")
    
    # Validación técnica: Si falta algo en el .env, frenamos.
    if not source or not dest_folder:
        print("🚨 Error: Revisá tu archivo .env. Faltan SOURCE_PATH o BACKUP_DESTINATION.")
        return

    # 3. Generar nombre único: backup_2026-03-26_16-45.zip
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"backup_{timestamp}.zip"
    full_path = os.path.join(dest_folder, filename)

    print(f"📦 Iniciando backup de: {source}...")
    
    # 4. Ejecución del proceso modular
    if compress_folder(source, full_path):
        print(f"✅ Proceso completado exitosamente.")
        print(f"📂 Archivo generado: {full_path}")
    else:
        print("⚠️ El proceso de backup no pudo finalizar.")

if __name__ == "__main__":
    main()
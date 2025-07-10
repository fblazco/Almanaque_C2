import os
import sys

if len(sys.argv) != 2:
    print("Uso: python3 renombrar_con_a.py /ruta/a/la/carpeta")
    sys.exit(1)

carpeta = sys.argv[1]

if not os.path.isdir(carpeta):
    print("La carpeta no existe.")
    sys.exit(1)

for nombre_archivo in os.listdir(carpeta):
    # Ignora archivos ocultos (como .DS_Store o .file)
    if nombre_archivo.startswith('.'):
        continue
    if nombre_archivo.startswith('test.py'):
        continue
    ruta_actual = os.path.join(carpeta, nombre_archivo)

    if os.path.isfile(ruta_actual) and os.access(ruta_actual, os.W_OK):
        nombre_base, extension = os.path.splitext(nombre_archivo)
        nuevo_nombre = nombre_base + "-2015-2" + extension
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)
        os.rename(ruta_actual, nueva_ruta)
    else:
        print(f"Saltado: {nombre_archivo} (no es archivo o sin permiso)")

print("Renombrado completo.")


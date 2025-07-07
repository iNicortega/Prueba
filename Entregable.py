# Activar entorno virtual desde la terminal: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Librerías necesarias.
import pandas as pd
import json
from faker import Faker # Faker se usa para la generación de datos simulados
import random

# ==============================================================================
# SCRIPT 1: CREACIÓN DE LA BASE DE DATOS DE CLIENTES (DATOS SIMULADOS)
# ==============================================================================

archivo_ventas = 'ventas_challenge.csv'
archivo_clientes_generados = 'clientes_challenge.csv'

# --- Lectura de archivo de ventas y extracción de id_clientes ---
try:
    df_ventas = pd.read_csv(archivo_ventas)
    clientes_unicos = df_ventas['id_cliente'].unique()
    print(f"Se encontraron {len(clientes_unicos)} id_clientes en '{archivo_ventas}'.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_ventas}'. El archivo debe estar en la misma carpeta con el script.")
    exit()

# --- Generar datos de clientes simulados ---
fake = Faker('es_ES')
lista_contactos = []

for i, cliente_id in enumerate(clientes_unicos):
    nombre = fake.first_name()
    apellido = fake.last_name()
    if i % 4 == 0:
        correo = f"{nombre.lower().replace(' ', '')}.{apellido.lower().replace(' ', '')}@alianzateam.com"
    else:
        correo = fake.email()
    telefono = f"3{random.randint(10, 22)}{random.randint(1000000, 9999999)}"
    lista_contactos.append({
        'id_cliente': cliente_id, 'nombre': nombre, 'apellido': apellido, 'correo': correo, 'telefono': telefono
    })

# --- Guardar los clientes generados en un archivo CSV ---
df_clientes_generados = pd.DataFrame(lista_contactos)
df_clientes_generados.to_csv(archivo_clientes_generados, index=False)
print(f"Se ha creado el archivo '{archivo_clientes_generados}' con los datos simulados.")
print("-" * 50)


# ==============================================================================
# SCRIPT 2: PROCESAMIENTO Y CREACIÓN DEL REPORTE
# ==============================================================================

# --- Simulación de la API ---
def simular_api(email):
    if isinstance(email, str) and email.lower().endswith('@alianzateam.com'):
        return True
    return False

# Lexctura de archivo CSV Clientes
try:
    df_contactos = pd.read_csv(archivo_clientes_generados)
    print(f"\nArchivo '{archivo_clientes_generados}' leído con exito.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_clientes_generados}'.")
    exit()

# Inicializar listas y contadores
contactos_existentes = []
nuevos = []
contactos_incompletos = []

# Procesar los contactos
for index, row in df_contactos.iterrows():
    if row.isnull().any():
        contactos_incompletos.append(row.to_dict())
    else:
        email = row['correo']
        if simular_api(email):
            contactos_existentes.append(row.to_dict())
        else:
            nuevos.append(row.to_dict())

print("Procesamiento de contactos finalizado.")

# --- Creación de JSON ---
json_filename = 'nuevos_contactos.json'
with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(nuevos, json_file, indent=4, ensure_ascii=False)
print(f"Se ha creado el archivo '{json_filename}'.")

# --- Creación de Excel ---
df_resumen = pd.DataFrame({
    'Métrica': ['Total de nuevos contactos', 'Contactos existentes', 'Contactos con datos incompletos'],
    'Cantidad': [len(nuevos), len(contactos_existentes), len(contactos_incompletos)]
})
df_nuevos = pd.DataFrame(nuevos)
df_nuevos['Estado'] = 'Nuevo'
df_existentes = pd.DataFrame(contactos_existentes)
df_existentes['Estado'] = 'Existente'
df_detalle_contactos = pd.concat([df_nuevos, df_existentes], ignore_index=True)

excel_filename = 'reporte_final_clientes.xlsx'
with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
    df_resumen.to_excel(writer, sheet_name='Resumen', index=False)
    df_detalle_contactos.to_excel(writer, sheet_name='Detalle de Contactos', index=False)

print(f"Se ha creado el reporte '{excel_filename}'.")
print("-" * 50)
print("\n¡Proceso completado! Revisa los archivos generados en la carpeta del proyecto.")
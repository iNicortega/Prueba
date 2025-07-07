# Prueba Práctica - TS Automatización e Integración de API Simulada

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Objetivo del Proyecto

Este proyecto es la solución a una prueba técnica para el cargo de Analista de Datos e Insight Junior. El objetivo es desarrollar un script en Python que simule un proceso de ETL (Extracción, Transformación y Carga) para la validación, analisis, limpieza e integración de datos de nuevos clientes en un sistema CRM, automatizando la clasificación de registros y la creación de reportes clave.

## Contexto de la prueba

La tarea consiste en:
> Simular una integración entre un sistema externo y un CRM como HubSpot, sin acceso real.
> 
> * Parte A: Simular una validación de contactos existentes con una "API ficticia".
>
> * Parte B: Generar un archivo JSON con los nuevos contactos "a crear".
>
> * Parte C: Crear un archivo Excel con un resumen de la información cuantificada de los contactos.

## Aplicación

* Generación de Datos Simulados: Al no contar con una base de datos de clientes, el script evalua un dataset de ventas (ventas_challenge.csv), extrae los id de clientes únicos y genera una base de datos de clientes ficticia (clientes_challenge.csv) utilizando la librería Faker.

* Procesamiento y Clasificación: El script principal, lee los datos de clientes y los procesa fila por fila con el fin de identificar y separar registros con datos incompletos y utilizar una función que simula una API para validar si un contacto ya existe (basado en el dominio del correo @alianzateam.com). De igual forma, clasifica los contactos en "Nuevos" o "Existentes".

* Generación de Entregables:

    1.  Archivo JSON: Crea un archivo nuevos_contactos.json listo para integrarse en otro sistema o API.
    2.  Reporte en Excel: Genera un reporte (reporte_final_clientes.xlsx) con dos hojas:
        * Resumen: Una tabla con el total de contactos nuevos, existentes e incompletos.
        * Detalle de Contactos: Una lista completa de todos los contactos procesados (nuevos y existentes) y una columna de "Estado".

Juan Nicolás Ortega Giraldo  
**[LinkedIn](https://www.linkedin.com/in/juan-nicolas-ortega-giraldo-485985265/)**

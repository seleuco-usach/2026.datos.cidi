import pyodbc
import pandas as pd
import numpy as np
from datetime import date


con_1 = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER=158.170.66.56,{1433};"
    f"DATABASE=PROC01ESTUDIO;"
    f"UID=proceso;"
    f"PWD=Estudio.2024;")

print("Conexión exitosa")

####listado de tablas
cursor_1 = con_1.cursor()
cursor_1.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.\
                 TABLES WHERE TABLE_TYPE = 'BASE TABLE';")


for t in cursor_1.fetchall():
    print(t)

####listado de campos

cursor_1 = con_1.cursor()
columnas=cursor_1.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.\
                          COLUMNS WHERE TABLE_NAME='DEMRE_E_2014_2025';")

for c in columnas.fetchall():
    print(c)



pd.read_sql("""SELECT 
                m.ANHO_MU, 
                m.COD_SIES,
                m.NIV_GLO,
                m.COD_SIES,
                m.primer_anio,
                m.FOR_ING_ACT,
                c.FACULTAD,
                m.ANHO_SIES_CAR,
                m.UNICIT,
                m.VIG,
                COUNT(DISTINCT m.N_DOC) AS tot
            FROM TABLA_MU_2016_2026 m
            LEFT JOIN CPP_DR2 c
            ON CONCAT(ANHO, '-',c.SIES_CAR) = m.ANHO_SIES_CAR
            GROUP BY 
            m.ANHO_MU, 
            m.COD_SIES, 
            m.primer_anio,
            m.FOR_ING_ACT,
            m.NIV_GLO, 
            c.FACULTAD,
            m.ANHO_SIES_CAR,
            m.UNICIT,
            m.VIG
            """, con_1).to_clipboard(index=False)

pd.read_sql("""SELECT 
            ano,
            nivel_formacion_esp_med,
            jce,
            ccc_contrato,
            COUNT(DISTINCT clave_ano) AS tot,
            principal_unidad_academica_contrato
            FROM PAC_2008_2025
            group by 
            ano,
            nivel_formacion_esp_med,
            jce,
            ccc_contrato,
            principal_unidad_academica_contrato""", con_1).to_clipboard(decimal=',', index=False)



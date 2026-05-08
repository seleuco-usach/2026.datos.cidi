import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(layout="wide")

st.title("CIDI Indicadores Financieros")

df =pd.read_csv("tabla_cidi.csv")
df_rev =pd.read_csv("tabla_cidi_rev.csv")



df['AÑO'] = df['AÑO'].astype(str)

df.rename(columns={'AÑO':'anho', 
                   'FACULTAD':'fac',
                   'TOTAL ALUMNOS PREGRADO':'mat',
                   'ALUMNOS NUEVOS PREGRADO':'mat_1er',
                   'JCE DR/JCE (i)':'jce_doc',
                   'N° DE CARRERAS DIURNAS':'n_carreras_j1',
                   'TASA DE TITULACIÓN':'tit',
                   'TASA DE RETENCIÓN 1ER AÑO':'ret_1',
                   'N° DE PROYECTOS ANID':'n_anid',
                   'N° PUBLICA WOS Y SCIELO':'n_pub_wos_scielo'}, inplace=True)

df = df.drop('id', axis=1)

#for i in df.columns:
 #   print(i)

#sel =st.multiselect("Selecciona facultad:", df['AÑO'].unique(), 
 #                                  default=df['AÑO'].unique()[0])
tab1, tab2 = st.tabs(["indicadores financieros", "revision"])

with tab1:

    sel=st.selectbox("Selecciona año:", 
         list(df['anho'].unique()), 
         index=None)

    if sel:
        df_filtrada = df[df['anho'].isin([sel])]
    else:    
        df_filtrada = df
    

    seleccion_depto = st.multiselect("Selecciona facultad:", 
                                df_filtrada['fac'].unique())

    if seleccion_depto:
        df_final = df_filtrada[(df_filtrada['anho'].isin([sel])) & (df_filtrada['fac'].isin(seleccion_depto))]
    else:    
        df_final = df_filtrada



    st.dataframe(df_final, use_container_width=True)
    
    #st.info(f"Se cuentan {len(df_final)} registros de este programa")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("mat total", f"{round(df_final['mat'].sum(),0)}")
        
    with col2:
        st.metric("mat 1 año", f"{round(df_final['mat_1er'].sum(),0)}")
        
    with col3:
        st.metric("n_carrera diurnas", f"{round(df_final['n_carreras_j1'].sum(),0)}")
    
with tab2:
    
    st.dataframe(df_rev, use_container_width=True)
    #st.metric("mat_1er total: {df_final['mat_1er'].sum()}")
    #st.metric("n_carreras_j1 total: {df_final['n_carreras_j1'].sum()}")
    
  


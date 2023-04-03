"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    df.reset_index(inplace=True, drop=True)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],dayfirst=True)

    df.dropna(axis="index",inplace=True)
    df.drop_duplicates(inplace=True)
       
    # Minusculas 
    df['sexo'] = df['sexo'].str.lower().astype(str).str.strip()
    df['barrio'] = df['barrio'].str.lower().astype(str)
    df['línea_credito'] = df['línea_credito'].str.lower().astype(str)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.lower().astype(str)
           
    # Espacios en blanco y guiones
    df['barrio'] = df['barrio'].str.replace('-',' ').str.replace('_',' ')
    df['idea_negocio'] = df['idea_negocio'].str.replace('-',' ').str.replace('_',' ').str.strip()
    df['línea_credito'] = df['línea_credito'].str.replace('-',' ').str.replace('_',' ').str.strip()
    
    #Reemplazos de valores especificos
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').str.strip().astype(float)
   
    #df['línea_credito'] = df['línea_credito'].str.replace('[^a-zA-Z0-9 \n\.]', ' ',regex=True)
    #df['línea_credito'].replace({'soli diaria':'solidaria'}, inplace=True)
    #df['idea_negocio'] = df['idea_negocio'].str.replace('[^a-zA-Z0-9 \n\.]', ' ',regex=True)
    #df['idea_negocio'].replace({'organizaci n y':'organizacion y','pa alera':'panalera'}, inplace=True)
    #df['barrio'] = df['barrio'].str.replace('[^a-zA-Z0-9 \n\.]',' ',regex=True)
    #df["barrio"].replace({"antonio nari o": "antonio narino","antonio nari  o": "antonio narino", "antonio nari¿o": "antonio narino",'bel n':'belen',"bel¿n": "belen",'san jos  de la monta a':'san jose de la montana'}, inplace=True)
               
    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)
       
    #print(df.sexo.value_counts())
    #print(df.tipo_de_emprendimiento.value_counts())
    #print(df.barrio.value_counts())
    #print(df.estrato.value_counts())
    #print(df.fecha_de_beneficio.value_counts())
    #print(df.monto_del_credito.value_counts())
    #print(df.línea_credito.value_counts())

    #df.to_excel("solicitudes_credito_clean.xlsx", index=False)
   

    return df



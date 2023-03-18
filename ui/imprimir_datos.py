def corregir_datos(columna):
    columna = columna.str.replace('[a-zA-Z]', '', regex=True)
    columna = columna.str.replace('<', '')
    columna = columna.str.replace(',', '.')
    return columna.astype(float)

def get_medianas(datos):
    medianas = {'ph': 0, 'fosforo': 0, 'potasio': 0}
    medianas['ph'] = (round(corregir_datos(datos['ph_agua_suelo_2_5_1_0']).median(), 2))
    medianas['fosforo'] = (round(corregir_datos(datos['f_sforo_p_bray_ii_mg_kg']).median(), 2))
    medianas['potasio'] = (round(corregir_datos(datos['potasio_k_intercambiable_cmol_kg']).median(), 2))
    return medianas

def imprimir_tabla(datos):
    medianas = get_medianas(datos)
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(
        "Departamento", "Municipio", "Cultivo", "Topología", "ph (mediana)",
        "Fósforo (mediana)", "Potasio (mediana)"))
    for fila in range (len(datos)) :
        print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format(
            datos.iloc[fila]['departamento'], datos.iloc[fila]['municipio'], 
            datos.iloc[fila]['cultivo'], datos.iloc[fila]['topografia'], 
            medianas['ph'], medianas['fosforo'], medianas['potasio'])) 
        
        
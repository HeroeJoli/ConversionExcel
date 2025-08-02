import pandas as pd

# Leer Excel
tabla_input = input("Nombre de la Tabla(con .xlsx): ")
tabla = pd.read_excel(tabla_input)

# Dejar las columnas de identificación (las primeras 3)
id_vars = []
nm_colmnas_idnt = input("Pon el *numero* de columnas de identificación:")
for i in range(int(nm_colmnas_idnt)):
    columna = input(f"Por el nombre de la columna identificatioria numero {i+1}: ")
    id_vars.append(columna)
#id_vars = ["letra", "patron", "patron"]

# Renombrar

#num_total_columnas = len(tabla.columns)
#n_w = num_total_columnas - nm_colmnas_idnt  # las primeras 3 son letra + 2 patrones
#tabla.columns = ["letra", "patron1", "patron2"] + [f"w{i+1}" for i in range(n_w)]

# Transformar de formato ancho a largo
tabla_largo = tabla.melt(id_vars=id_vars, 
                    var_name="w", 
                    value_name="qty")

# Guardar en nuevo Excel
nombre_nuevoexcl = input("Nombre del nuevo excel (sin .xlsx): ")
tabla_largo.to_excel(f"{nombre_nuevoexcl}.xlsx", index=False)

print("Transformación completada. Guardado como 'tabla_convertida.xlsx'")
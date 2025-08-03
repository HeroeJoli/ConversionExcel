from flask import Flask, request, render_template, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        archivo = request.files["archivo"]
        nombre_archivo = archivo.filename
        terminacion = nombre_archivo.split('.')[-1] #e.g. xlsx
        # Parámetros de transformación
        num_cols = int(request.form["num_cols"])
        id_vars = [request.form[f"id_col_{i}"] for i in range(num_cols)]
        valor_col = request.form["valor_col"]
        nombre_salida = request.form["nombre_salida"]

        # Leer y transformar
        if terminacion == "xlsx":
            df = pd.read_excel(archivo)
        else:
            df = pd.read_csv(archivo)
        df_largo = df.melt(id_vars=id_vars, var_name="w", value_name=valor_col)

        # Guardar en memoria (no disco)
        output = io.BytesIO()
        if terminacion == "xlsx":
            df_largo.to_excel(output, index=False)
        else:
            df_largo.to_csv(output, index=False)
        output.seek(0)

        if terminacion == "xlsx":
            download_name = f"{nombre_salida}.xlsx"
        else: 
            download_name = f"{nombre_salida}.csv"

        return send_file(output,
                        download_name=download_name,
                        as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)  

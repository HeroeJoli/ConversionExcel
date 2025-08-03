from flask import Flask, request, render_template, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        archivo = request.files["archivo"]

        # Parámetros de transformación
        num_cols = int(request.form["num_cols"])
        id_vars = [request.form[f"id_col_{i}"] for i in range(num_cols)]
        valor_col = request.form["valor_col"]
        nombre_salida = request.form["nombre_salida"]

        # Leer y transformar
        df = pd.read_excel(archivo)
        df_largo = df.melt(id_vars=id_vars, var_name="w", value_name=valor_col)

        # Guardar en memoria (no disco)
        output = io.BytesIO()
        df_largo.to_excel(output, index=False)
        output.seek(0)

        # Descargar archivo transformado
        return send_file(output,
                        download_name=f"{nombre_salida}.xlsx",
                        as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  

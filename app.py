from flask import Flask,render_template,request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "Bienvenido...."
    return render_template("home.html",titulo=titulo)

@app.route("/acercade")
def acerca():
    titulo = "Acerca de"
    return render_template("acercade.html",titulo=titulo)

@app.route("/",methods=["POST"])
def clasificacion():
    titulo = "Clasificacion de flor...."
    inputs = {
        'SepalLengthCm': [request.form.get('SepalLengthCm')],
        'SepalWidthCm': [request.form.get('SepalWidthCm')],
        'PetalLengthCm': [request.form.get('PetalLengthCm')],
        'PetalWidthCm': [request.form.get('PetalWidthCm')]
    }
    inp = pd.DataFrame(inputs)
    ia = pickle.load(open("model.pkl","rb"))
    resultados = ia.predict(inp)
    resultados = resultados[0]
    src = ''
    if (resultados == "Iris-setosa"):
        src = "https://m.media-amazon.com/images/I/61pLvdbjC7L._AC_SX466_.jpg"
    if (resultados == "Iris-virginica"):
        src = "https://www.fs.fed.us/wildflowers/beauty/iris/Blue_Flag/images/iris_virginica/iris_virginica_virginica_lg.jpg"
    if (resultados == "Iris-versicolor"):
        src = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Iris_versicolor_4.jpg/1200px-Iris_versicolor_4.jpg"
    return render_template("clasificacion.html",titulo=titulo,resultados=resultados,src=src,inputs=inputs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
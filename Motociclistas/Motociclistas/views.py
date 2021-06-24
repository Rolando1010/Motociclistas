from werkzeug.utils import redirect
from Motociclistas import app
from flask import render_template, request, redirect, url_for
from Motociclistas import model

@app.route("/", methods=["POST","GET"])
def index():
    #model.reiniciarArchivo()
    if(request.method=="POST"):
        return redirect(url_for(".motociclistas",nombre = request.form["nombre"]))
    return render_template("login.html")

@app.route("/<nombre>", methods=["POST","GET"])
def motociclistas(nombre):
    if(request.method=="POST"):
        if "data" in request.form:
            datos = request.form["data"].split("|")
            pos = int(datos[0])
            tomar = True if datos[1] == "true" else False
            model.seleccionarMoto(pos,tomar)
            model.tomarQuitarMoto(pos, nombre, tomar)
    return render_template("motociclistas.html", motos = model.obtenerMotociclistas(), tomados = model.obtenerTomadosUsuario(nombre),nombre = nombre)
from flask import request, abort, jsonify
from .. import db
from . import api
from ..models import Amigo

@api.route("/amigo/<int:id>")
def get_amigo(id):
    """
    Retorna JSON con información sobre el amigo cuyo id recibe como parámetro
    o un error 404 si no lo encuentra.
    """
    amigo = Amigo.query.get_or_404(id)
    amigodict = {'id': amigo.id, 'name': amigo.name,
                 'lati': amigo.lati, 'longi': amigo.longi}
    return jsonify(amigodict)

@api.route("/amigo/byName/<name>")
def get_amigo_by_name(name):
    """
    Busca el amigo por su nombre en la base de datos. Si no lo encuentra
    retorna un error 404. Si lo encuentra retorna el JSON con sus datos
    """
    amigo = Amigo.query.filter_by(name = name).first()
    if not amigo:
        abort(404, "No se encuentra ningún amigo con ese nombre")
    amigodict = {'id': amigo.id, 'name': amigo.name,
                 'lati': amigo.lati, 'longi': amigo.longi}
    return jsonify(amigodict)

@api.route("/amigos")
def list_amigos():
    # 1. Consultar todos los amigos guardados en la base de datos
    amigos = Amigo.query.all()
    
    # 2. Convertir la lista de objetos SQLAlchemy a una lista de diccionarios Python
    resultado = [
        {'id': a.id, 'name': a.name, 'lati': a.lati, 'longi': a.longi}
        for a in amigos
    ]
    
    # 3. Convertir la lista de diccionarios a JSON y retornarla
    return jsonify(resultado)

@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    """
    Modifica en la base de datos el amigo cuyo id recibe como parámetro.

    Retorna el JSON con el amigo tras la modificación
    """
    # Obtenemos el amigo a partir de su ID
    amigo = Amigo.query.get_or_404(id)

    # Comprobamos que hemos recibido JSON como parte del PUT
    if not request.json:
        abort(422, "No se ha enviado JSON")

    # Intentamos extraer campos del JSON (si no están presentes)
    # la extracción retornará None
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")
    # Usamos los campos que estén presentes para actualizar el objeto amigo
    if name:
        amigo.name = name
    if lati:
        amigo.lati = lati
    if longi:
        amigo.longi = longi

    # Finalmente, si hemos cambiado algo en el objeto amigo, hacemos
    # el commit a la base de datos para que se guarden las modificaciones
    if name or lati or longi:
        db.session.commit()

    # Y retornamos el JSON con los nuevos datos
    amigodict = {"id": amigo.id, "name": amigo.name,
                 "longi": amigo.longi, "lati": amigo.lati }
    return jsonify(amigodict)

@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    """
    Elimina un amigo cuyo id recibe como parámetro de la base de datos.
    """
    # 1. Obtenemos el amigo de la base de datos o devolvemos un error 404 si no existe
    amigo = Amigo.query.get_or_404(id)
    
    # 2. Eliminamos el objeto de la sesión de SQLAlchemy y guardamos los cambios en MariaDB
    db.session.delete(amigo)
    db.session.commit()
    
    # 3. Retornamos respuesta vacía con código HTTP 204 "No content"
    return ('', 204)

@api.route("/amigos", methods=["POST"])
def new_amigo():
    """
    Modifica en la base de datos añadiendo un amigo cuyos datos
    recibe en JSON.
    Retorna el JSON con el amigo tras la creación, para que el cliente
    pueda conocer el id del amigo recién creado.
    """
    # Comprobamos que hemos recibido JSON como parte del POST
    if not request.json:
        abort(422, "No se ha enviado JSON")

    # Intentamos extraer campos del JSON (si no están presentes, retornará None)
    name = request.json.get("name")

    # Si no hay nombre, rechazamos la petición
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")

    # Si el nombre ya existe en la base de datos, también lo rechazamos
    amigo = Amigo.query.filter_by(name=name).first()
    if amigo:
        abort(422, "Ya existe un amigo con ese nombre")

    # En caso contrario, tomamos latitud y longitud. Si no vienen les damos valor "0"
    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")

    # Creamos un nuevo amigo con esos datos
    amigo = Amigo(name=name, lati=lati, longi=longi)
    db.session.add(amigo)
    db.session.commit()

    # Retornamos el JSON con los datos del nuevo amigo
    amigodict = {
        "id": amigo.id,
        "name": amigo.name,
        "longi": amigo.longi,
        "lati": amigo.lati,
    }
    return jsonify(amigodict)

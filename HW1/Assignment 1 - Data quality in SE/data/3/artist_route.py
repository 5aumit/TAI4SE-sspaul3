from flask import Blueprint, request, jsonify, redirect, url_for, session
from services.artist_service import ArtistService

artist_bp = Blueprint("artist_bp", __name__)


@artist_bp.route('/list', methods=["GET"])
def list():
    return jsonify(ArtistService().list())


@artist_bp.route('/create', methods=["GET"])
def create():
    context = request.args
    return ArtistService().create(context)


@artist_bp.route('/delete', methods=["GET"])
def delete():
    return ArtistService().delete()


@artist_bp.route('/login', methods=["POST"])
def login():
    form = request.form
    artist_info = ArtistService().login(form)

    if artist_info is not None:
        session["id"] = artist_info["id"]
        session["name"] = artist_info["name"]
        session["surname"] = artist_info["surname"]
        session["type"] = "artist"
        session["state"] = True

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

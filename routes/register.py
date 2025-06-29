from flask import Blueprint, request, jsonify, render_template
import sqlite3
from utils import hash_password

registro_bp = Blueprint('register', __name__)

@registro_bp.route('/register', methods=['GET'])
def registro_form():
    return render_template('register.html')

@registro_bp.route('/register', methods=['POST'])
def registro():
    data = request.form or request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    contraseña_hash = hash_password(contraseña)

    try:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, contraseña_hash) VALUES (?, ?)', 
                       (usuario, contraseña_hash))
        conn.commit()
        conn.close()
        return "✅ Usuario registrado exitosamente", 201
    except sqlite3.IntegrityError:
        return "⚠️ Usuario ya existe", 409

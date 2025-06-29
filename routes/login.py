from flask import Blueprint, request, jsonify, render_template
import sqlite3
from utils import hash_password

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.form or request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    contraseña_hash = hash_password(contraseña)

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM usuarios WHERE usuario = ? AND contraseña_hash = ?', 
                  (usuario, contraseña_hash))
    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template('tareas.html')  # redirige a tareas si login exitoso
    else:
        return "❌ Usuario o contraseña inválidos", 401

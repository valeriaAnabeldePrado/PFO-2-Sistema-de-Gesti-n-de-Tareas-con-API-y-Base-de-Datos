from flask import Flask
from routes.login import login_bp
from routes.register import registro_bp
from routes.task import tareas_bp
from db import init_db

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(registro_bp)
app.register_blueprint(tareas_bp)

if __name__ == '__main__':
    init_db()
    print("🚀 Iniciando servidor Flask en puerto 3000...")
    app.run(debug=True, port=3000)

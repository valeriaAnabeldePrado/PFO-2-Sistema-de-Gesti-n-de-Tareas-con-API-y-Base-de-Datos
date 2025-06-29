from flask import Blueprint, render_template

tareas_bp = Blueprint('task', __name__)

@tareas_bp.route('/task')
def tareas():
    return render_template('tasks.html')

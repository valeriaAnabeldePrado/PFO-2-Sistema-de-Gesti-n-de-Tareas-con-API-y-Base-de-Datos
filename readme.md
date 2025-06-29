# 🗂️ Sistema de Gestión de Usuarios y Tareas con Flask

Este proyecto es una pequeña aplicación web hecha en **Flask** que permite registrar usuarios, iniciar sesión y acceder a una pantalla de bienvenida. Utiliza formularios HTML y base de datos SQLite. Todo está organizado en módulos para mantener una estructura limpia y escalable.

---

## Tecnologías utilizadas

- Python 3.x
- Flask
- SQLite
- HTML/CSS 

---

## 📁 Estructura del proyecto

mi_app/
├── app.py 
├── db.py 
├── utils.py
├── templates/ 
│ ├── login.html
│ ├── register.html
│ └── tasks.html
├── routes/ 
│ ├── login.py
│ ├── register.py
│ └── task.py
└── tasks.db # Base de datos SQLite (se crea automáticamente


---

## Instalación y ejecución

1. **Clonar el repositorio** (o descargar los archivos manualmente):

   ```bash
   git clone https://github.com/valeriaAnabeldePrado/PFO-2-Sistema-de-Gesti-n-de-Tareas-con-API-y-Base-de-Datos.git
   cd flask-usuarios-tareas

2. **Instalar dependencias**
   
   pip install flask

3. **Ejecutar la aplicación**

    python app.py

4. **3. **Ejecutar la aplicación****

    Registro: http://localhost:3000/register

    Login: http://localhost:3000/login

    Página de tareas (luego del login): http://localhost:3000/task

---

## Funcionalidades
Registro de usuario con verificación de duplicados

Login con validación de credenciales

Formularios HTML estilizados de forma simple

Redirección a pantalla de bienvenida tras el login

Contraseñas almacenadas de forma segura usando SHA-256

## Desarrollado por Valeria Anabel de Prado
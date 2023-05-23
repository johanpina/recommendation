# Sistema de Recomendación de Empleos

Este repositorio contiene el código para un sistema de recomendación de empleos. El sistema fue desarrollado como parte de una prueba técnica para un puesto de desarrollador de Inteligencia Artificial.

## Descripción

El sistema de recomendación utiliza un modelo de lenguaje grande para generar recomendaciones de empleo basadas en la información del usuario. Las recomendaciones se generan comparando la información del usuario con una base de datos de ofertas de empleo.

El sistema está construido con Python y FastAPI, y utiliza la biblioteca OpenAI para trabajar con el modelo de lenguaje grande.

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

- `main.py`: El punto de entrada para la aplicación FastAPI. Define las rutas para obtener recomendaciones y crear usuarios.
- `schemas.py`: Define los modelos Pydantic para los datos del usuario, las ofertas de trabajo y las recomendaciones.
- `crud.py`: Simula las operaciones CRUD para la base de datos de usuarios y ofertas de trabajo.
- `large_language_model.py`: Contiene las funciones para generar recomendaciones utilizando el modelo de lenguaje grande.
- `database.py`: Simula la conexión, estructura y carga de la base de datos.



## Instalación

Para instalar las dependencias del proyecto, necesitarás tener Python instalado en tu máquina. Puedes instalar las dependencias utilizando pip, el administrador de paquetes de Python. En la raíz del repositorio, ejecuta el siguiente comando:

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Ejecución
Para ejecutar el sistema de recomendación, debes ejecutar el archivo main.py. Puedes hacerlo con el siguiente comando:
```bash
python main.py
```

Una vez que la aplicación esté en ejecución, puedes hacer una solicitud **`GET`** a **`/recommendations/{user_id}`** para obtener las recomendaciones para un usuario, o puedes hacer una solicitud **`POST`** a **`/create/user/`** para crear un nuevo usuario y obtener recomendaciones para él.
## Sistema desoplegado con Azure:
[Hunty recommendation API](https://huntyappreco.azurewebsites.net/docs)

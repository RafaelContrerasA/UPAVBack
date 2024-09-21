# Proyecto UPAV

## Requisitos 
- Python 
- pip (gestor de paquetes de Python) 

## Instalación 
### 1. Clonar el repositorio 
```git clone https://gitlab.com/webscraping9105015/web-scraping-back.git```

### 2. Instalar venv (si no está instalado)  
##### En Windows 
```pip install virtualenv ``` 

### 3. Crear y activar un entorno virtual. 
##### En Windows 
Crear
```python -m venv venv``` 

Activar
```.\venv\Scripts\activate ``` 

### 4. Instalar las dependencias Una vez que el entorno virtual está activado, instala las dependencias del proyecto utilizando el archivo `requirements.txt`. 
```pip install -r requirements.txt ``` 

### 5. Instalar Tesseract-OCR 
Para que PyTesseract funcione, necesitas instalar Tesseract-OCR. Descarga el instalador de Tesseract para Windows desde [este enlace](https://github.com/UB-Mannheim/tesseract/wiki).

### 6. Configurar la ruta de Tesseract 
Después de instalar Tesseract-OCR, agrega la ruta de instalación dentro del archivo "apis/signals.py". Normalmente, la ruta es `C:\Program Files\Tesseract-OCR\tesseract.exe'`.

```pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' ``` 


### 7. Configurar la conexión a la base de datos 
Abre el archivo `gob/settings.py` y encuentra la sección `DATABASES`. Aquí puedes configurar la conexión a la base de datos. 
```DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'nombre_bd', 'USER': 'usuario', 'PASSWORD': 'contraseña', 'HOST': 'localhost', 'PORT': '5432', } } ``` 

### 8. Aplica las migraciones para configurar la base de datos. 
```python manage.py migrate ``` 

### 9. Crear un superusuario.  
```python manage.py createsuperuser ``` 

### 10. Iniciar el servidor de desarrollo.
```python manage.py runserver ``` 

Abre tu navegador web y ve a `http://127.0.0.1:8000/` para ver tu aplicación en funcionamiento. 


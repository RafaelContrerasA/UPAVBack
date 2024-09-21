import pytesseract
import requests
from PIL import Image as PILImage
from io import BytesIO
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Image, Publicacion, Dependencia
import bleach
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        img = PILImage.open(BytesIO(response.content))
        text = pytesseract.image_to_string(img)

        return text
    except requests.exceptions.RequestException as e:
        return f"Error downloading image: {e}"
    except Exception as e:
        return f"Error processing image: {e}"

#Sanitizar campos antes de guardarlos
@receiver(pre_save, sender=Publicacion)
def sanitize_publicacion_text(sender, instance, **kwargs):
    instance.text = bleach.clean(instance.text, strip=True)


@receiver(pre_save, sender=Dependencia)
def sanitize_dependencia_text(sender, instance, **kwargs):
    instance.nombre = bleach.clean(instance.nombre, strip=True)
    instance.pagina_fb = bleach.clean(instance.pagina_fb, strip=True)
    instance.siglas = bleach.clean(instance.siglas, strip=True)

@receiver(post_save, sender=Image)
def update_extracted_text(sender, instance, **kwargs):
    # Extraer el texto de la imagen
    text = extract_text_from_image(instance.url)
    
    # Actualizar el campo extracted_text y guardar la instancia de nuevo
    if text != instance.extracted_text:
        instance.extracted_text = bleach.clean(text, strip=True)
        instance.save()
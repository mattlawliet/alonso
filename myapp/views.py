import os
from django.conf import settings
from django.shortcuts import render

# Create your views here.
def home(request):
    # Define the folder containing images
    img_folder = os.path.join(settings.STATIC_ROOT, 'myapp/img/')
    
    # List to hold the image URLs
    img_list = []

    # Loop through the folder and get all image file paths
    for filename in os.listdir(img_folder):
        if filename.endswith(('tn.jpg', 'tn.jpeg')):  # Filter image types
            img_list.append(f'myapp/img/{filename}')

    context = {
        'section_title' : 'Muebles tipo',
        'images': img_list,

        'about_us_title' : 'Acerca de nosotros',
        'about_us' : 'Con más de 50 años de experiencia en el arte de la ebanistería, nuestra empresa ha sido pionera en la creación de muebles únicos y personalizados. Nos dedicamos a transformar espacios con piezas de alta calidad y diseño a medida, cuidando cada detalle para lograr la satisfacción de nuestros clientes.',

        'mission_title' : 'Nuestra misión',
        'mission' : 'Convertimos la madera en arte, creando muebles duraderos y bellos que reflejan la esencia y visión de nuestros clientes. Nos esforzamos por mantener la tradición artesanal mientras incorporamos innovaciones que nos permitan entregar siempre lo mejor.',

        'story_title' : 'Historia',
        'story' : 'Fundada por Alonso hace más de cinco décadas, la empresa nació de una pasión por la ebanistería y un compromiso con la excelencia.',
        
        'team_title' : 'Equipo',
        'team' : 'Nuestro equipo está compuesto por artesanos dedicados y apasionados por su trabajo. Cada miembro aporta su experiencia y habilidad para asegurar que cada pieza supere las expectativas de cada cliente.',
        
        'quality_title' : 'Compromiso de calidad',
        'quality' : 'La calidad es nuestra prioridad. Desde la selección de los mejores materiales hasta los acabados más finos, nos aseguramos de que cada detalle cumpla con los más altos estándares, garantizando la satisfacción y durabilidad de nuestros productos.',
        
        'sustain_title' : 'Sostenibilidad',
        'sustain' : 'Nos comprometemos con la sostenibilidad y el respeto por el medio ambiente. Utilizamos madera de fuentes responsables y aplicamos prácticas ecológicas para reducir nuestro impacto ambiental, asegurando un futuro mejor para todos.',
        
        'contact_title' : '¡Hablemos de tus ideas!',
        'contact' : 'Estamos aquí para ayudarte a hacer realidad tus proyectos en madera. Completa el formulario con tu nombre, correo electrónico y un mensaje detallado sobre lo que necesitas. Nos pondremos en contacto contigo lo antes posible para discutir cómo podemos trabajar juntos.',

        'map_street' : ':)'
    }
    return render(request, 'myapp/index.html', context)

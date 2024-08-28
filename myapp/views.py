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
        'images': img_list
    }
    return render(request, 'myapp/index.html', context)

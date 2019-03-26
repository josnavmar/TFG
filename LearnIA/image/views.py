from django.shortcuts import render

def image_index(request):
    return render(request, "image.html")

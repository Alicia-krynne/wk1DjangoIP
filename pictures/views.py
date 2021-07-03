from django.shortcuts import render
import pictures
from pictures.models import Images
from django.shortcuts import render
from django.http  import HttpResponse,Http404
from decouple import config,Csv


# Create your views here.
def my_gallery(request):
    images = Images.my_gallery()
    return render(request, 'pics/home.html', {"images":images})

def show_images(request):
   
    try:
        images = Images.objects.all()
        ALLOWED_HOSTS = config('ALLOWED_HOSTS')

    except Images.DoesNotExist:
        raise Http404()
    return render(request,"pics/my_gallery.html", {"images":images, "ALLOWED_HOSTS":ALLOWED_HOSTS})
   
   
def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'pics/search.html',{"message":message,"gallery": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'pics/search.html',{"message":message})







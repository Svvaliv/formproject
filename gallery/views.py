from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import GalleryUploadForm
from .models import Gallery


# Create your views here.


class GalleryView(View):
    def get(self, request):
        form = GalleryUploadForm
        return render(request, "gallery/load_file.html", {"form": form})

    def post(self, request):
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Gallery(image=form.cleaned_data['image'])
            new_image.save()
            return HttpResponseRedirect('load_image')
        return render(request, "gallery/load_file.html", {"form": form})

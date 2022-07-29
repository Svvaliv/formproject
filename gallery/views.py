from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Gallery
from .forms import GalleryUploadForm


# Create your views here.

class ListGallery(ListView):
    model = Gallery
    template_name = "gallery/images_list.html"
    context_object_name = 'records'


# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm
#         return render(request, "gallery/load_file.html", {"form": form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, "gallery/load_file.html", {"form": form})


class CreateGalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    context_object_name = 'form'
    template_name = 'gallery/load_file.html'
    success_url = '/load_image'

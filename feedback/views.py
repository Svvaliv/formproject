from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import FeedbackForm
from .models import Feedback


# Create your views here.

# class FeedBackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, "feedback/feedback.html", context={
#             "form": form
#         })
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/done")
#         return render(request, "feedback/feedback.html", context={
#             "form": form
#         })

class FeedBackView(FormView):
    form_class = FeedbackForm
    template_name = "feedback/feedback.html"
    success_url = "/done"

    def form_valid(self, form):
        form.save()
        return super(FeedBackView, self).form_valid(form)

    # def post(self, request):
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/done")
    #     return render(request, "feedback/feedback.html", context={
    #         "form": form
    #     })

class FeedbackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, "feedback/feedback.html", context={
            "form": form
        })

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/{id_feedback}")
        return render(request, "feedback/feedback.html", context={
            "form": form
        })


class DoneView(TemplateView):
    template_name = "feedback/done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Ivanov I.I."
        context["date"] = "27.06.2022"
        return context


class ListFeedBack(ListView):
    template_name = "feedback/list_feedback.html"
    model = Feedback
    context_object_name = "feedbacks"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class DetailFeedBack(DetailView):
    template_name = "feedback/detail_feedback.html"
    model = Feedback

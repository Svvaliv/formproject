from django.contrib import admin
from django.urls import path
from .views import DoneView, FeedBackView, FeedbackUpdateView, ListFeedBack, DetailFeedBack

urlpatterns = [
    path('done', DoneView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<int:pk>', DetailFeedBack.as_view()),
    path('', FeedBackView.as_view()),
    # path('<int:id_feedback>', FeedbackUpdateView.as_view()),
    path('update/<int:pk>', FeedbackUpdateView.as_view()),
]
from django.urls import path
from .app.views.view_book import CreateBookAPIView


app_name = 'main'

urlpatterns = [
    path('/create', CreateBookAPIView.as_view()),
]

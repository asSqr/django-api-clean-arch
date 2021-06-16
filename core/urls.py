from django.urls import include, path

app_name = 'core'
from .app.views.view_order_cart import CreateOrderCartAPIView

urlpatterns = [
    path('/create', CreateOrderCartAPIView.as_view()),
]

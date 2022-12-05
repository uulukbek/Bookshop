from django.urls import path
from applications.product.views import ListCreateBookApiView, RetUpdDelBookApiView

urlpatterns = [
    path('', ListCreateBookApiView.as_view()),
    path('<int:pk>/', RetUpdDelBookApiView.as_view())
]
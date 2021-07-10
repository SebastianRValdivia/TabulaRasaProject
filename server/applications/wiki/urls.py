from django.urls import path

from applications.wiki.views import WikiPageDetailView

urlpatterns = [
    path('<int:pk>/', WikiPageDetailView.as_view(), name="wikipage")
]

from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('wiki/', include('applications.wiki.urls'))
]

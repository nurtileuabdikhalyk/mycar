from django.urls import path
from .views import index, detailcar, servicesview, carsview, about, blog, contact, addreview, Search

urlpatterns = [
    path('', index, name='index'),
    path('cars/', carsview, name='cars'),
    path('cars/<slug:slug>/', detailcar, name='detailcar'),
    path("search/", Search.as_view(), name='search'),
    path('services/', servicesview, name='services'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path("review/", addreview, name="addreview"),
    path('contact/', contact, name='contact'),
]

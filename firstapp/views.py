from itertools import chain

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Vehicle, Reviews, Service, Blog
from .forms import ReviewForm


def index(request):
    vehicles = Vehicle.objects.order_by('name')[:3]
    vcount = Vehicle.objects.all().count()
    services = Service.objects.all()[:3]
    reviews = Reviews.objects.order_by('-publish')[:3]
    blogs = Blog.objects.order_by('-data')[:3]

    context = {'title': 'Главная', 'vehicles': vehicles, 'services': services, 'reviews': reviews, 'blogs': blogs,
               'vcount': vcount}
    return render(request, 'firstapp/index.html', context)


def detailcar(request, slug):
    question = get_object_or_404(Vehicle, slug=slug)
    context = {'vehicle': question}
    return render(request, 'firstapp/detailcar.html', context)


def servicesview(request):
    services = Service.objects.all()
    context = {'title': 'Сервисы', 'services': services}
    return render(request, 'firstapp/services.html', context)


def carsview(request):
    vehicles = Vehicle.objects.all()
    context = {'title': 'Машины', 'vehicles': vehicles}
    return render(request, 'firstapp/cars.html', context)


# class ServicesView(ListView):
#     model = Service
#     template_name = 'firstapp/services.html'
#     context_object_name = 'services'


def about(request):
    context = {'title': 'Про нас'}
    return render(request, 'firstapp/about.html', context)


def blog(request):
    context = {'title': 'Блог'}
    return render(request, 'firstapp/blog.html', context)


def contact(request):
    form = ReviewForm()
    context = {'title': 'Контакты', 'form': form}

    return render(request, 'firstapp/contact.html', context)


def addreview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('contact')


class Search(ListView):
    template_name = 'firstapp/search.html'

    def get_queryset(self):
        return Vehicle.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Поиск'
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

# class ReviewView(View):
#     model = Reviews
#
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         movie = Vehicle.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             if request.POST.get("parent", None):
#                 form.parent_id = int(request.POST.get("parent"))
#             form.movie = movie
#             form.save()
#         return redirect(movie.get_absolute_url())

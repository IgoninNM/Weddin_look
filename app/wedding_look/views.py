from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from users.models import User

from .models import *


class IndexView(TitleMixin, TemplateView):
    template_name = 'wedding_look/index.html'
    title = 'Wedding Look'


class Wedding_dressesListView(TitleMixin, ListView):
    model = Product
    template_name = 'wedding_look/wedding.html'
    paginate_by = 6
    title = 'Wedding Look - Свадебные платья'

    def get_queryset(self):
        queryset = super(Wedding_dressesListView, self).get_queryset().filter(type__name="Свадебные платья")
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Wedding_dressesListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


class EveningListView(TitleMixin, ListView):
    model = Product
    template_name = 'wedding_look/evening.html'
    paginate_by = 6
    title = 'Wedding Look - Вечерние платья'

    def get_queryset(self):
        queryset = super(EveningListView, self).get_queryset().filter(type__name="Вечерние платья")
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


class AccessoriesListView(TitleMixin, ListView):
    model = Product
    template_name = 'wedding_look/accessories.html'
    paginate_by = 6
    title = 'Wedding Look - Аксессуары'

    def get_queryset(self):
        queryset = super(AccessoriesListView, self).get_queryset().filter(type__name="Аксессуары")
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


class AboutView(TitleMixin, TemplateView):
    template_name = 'wedding_look/about.html'
    title = 'Wedding Look - Свадебный дом'


class ServicesView(TitleMixin, TemplateView):
    template_name = 'wedding_look/services.html'
    title = 'Wedding Look - Наши услуги'


class ContactsView(TitleMixin, TemplateView):
    template_name = 'wedding_look/contacts.html'
    title = 'Wedding Look - Контакты'


class BlogListView(TitleMixin, ListView):
    model = Blog
    template_name = 'wedding_look/blog.html'
    title = 'Wedding Look - Блог'


class About_usView(TitleMixin, TemplateView):
    template_name = 'wedding_look/about_us.html'
    title = 'Wedding Look - О нас'


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

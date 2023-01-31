from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from wedding_look.views import (AboutView, AccessoriesListView, ContactsView,
                                EveningListView, IndexView, ServicesView,
                                Wedding_dressesListView, BlogListView, About_usView)
from . import views

add_name = 'wedding_look'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('wedding/', Wedding_dressesListView.as_view(), name='wedding_dresses'),
    path('evening/', EveningListView.as_view(), name='evening_dresses'),
    path('accessories/', AccessoriesListView.as_view(), name='accessories_dresses'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about_us/', About_usView.as_view(), name='about_us'),
    path('category/<int:category_id>', Wedding_dressesListView.as_view(), name='category'),
    path('wedding/page/<int:page>', Wedding_dressesListView.as_view(), name='paginator'),
    path('evening/page/<int:page>', EveningListView.as_view(), name='paginator_evening'),
    path('accessories/page/<int:page>', AccessoriesListView.as_view(), name='paginator_accessories'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('blog/', BlogListView.as_view(), name='blog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

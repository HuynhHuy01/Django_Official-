from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


app_name = 'book'
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),
    path('', home, name='home'),
    path('search/',search,name ='search'),
    path('<int:pk>/details', bookDetails, name='details'),
    path('<int:pk>/shop-item', shopDetails, name='shop_details'),
    path('cart/',views.cart, name='cart'),
    path('checkout/', checkoutBookView, name='checkout'),
    path('update_item/',updateItem,name ='update_item'),
    path('book-lists/', login_required_book_lists, name='books'),
    path('profile/', profile, name='users-profile'),
    path("<int:pk>/update/", userProfileUpdateView, name='update_user'),
    path('user-lists/', UserListView.as_view(), name='user_lists'),
    path("create/", CreateUserView.as_view(), name='create_user'),
    path('about/', views.about, name='about'),
    path('process_order/',processOrder,name ='process_order'),
    path('chat/',views.ChatBot,name = 'chat'),
    path('chatbot/',views.chatBot,name ='ChatBot')
]

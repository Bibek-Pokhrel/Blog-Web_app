from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('base',views.base),
    path('home',views.home,name='home'),
    path('',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('searchbar',views.searchbar,name='searchbar'),
    path('searchprofile/<pk>',views.searchprofile,name='searchprofile'),
    path('comment/<pk>',views.blogcomment,name='commentpost'),
    path("delete/<pk>",views.cmtdelete,name='delete'),
    path("editcmt/<pk>",views.cmtedit,name='editcmt'),
    path('profile',views.profile,name='profile'),
    path('register',views.register,name='register'),
    path('login',views.userlogin,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('usertag',views.usertag1,name='usertag'),
    path('bio/<pk>',views.bio,name='bio'),
    path('tagu/<pk>',views.tagu,name='tagu'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

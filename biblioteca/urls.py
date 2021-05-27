# Los enlaces que manejo de las paginas a las que acceden

from django.urls import path

from . import views


urlpatterns = [
    path('registro/', views.registerPage, name ='registro'),
    path('login/', views.loginPage, name ='login'),
    path('logout/', views.logoutUser, name ='logout'),

    path('', views.home, name = 'inicio'),
    path('user/', views.userPage, name ='pagina-usuario'),
    path('cuenta/', views.accountSettings, name ='cuenta'),
    path('productos/', views.products, name ='productos'),
    path('clientes/<str:pk_test>/', views.customer, name = 'clientes'),

    path('crearPedido/<str:pk>/',views.createOrder, name = 'crearPedido'),
    path('actualizarPedido/<str:pk>/',views.updateOrder, name = 'actualizarPedido'),
    path('eliminarPedido/<str:pk>/',views.deleteOrder, name = 'eliminarPedido'),

]

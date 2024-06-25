from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index,login,loginaction,customer_view,addproduct,addproductaction,viewproduct,edit_product
from .views import editproduct_action,delete_product
urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login" ),
    path("loginaction/", loginaction, name="loginaction"),
    path("customer_view/", customer_view, name="customer_view"),
    path("addproduct/", addproduct, name="addproduct"),
    path("addproductaction/", addproductaction, name="addproductaction"),
    path("viewproduct/", viewproduct, name="viewproduct"),
    path('edit_product<int:id>/', edit_product, name="edit_product"),
    path("editproduct_action/", editproduct_action, name="editproduct_action"),
    path("delete_product<int:id>/", delete_product, name="delete_product"),
    
   
   
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
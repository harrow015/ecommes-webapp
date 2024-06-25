from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import signup,signupaction,customerview,addtocart,cartaction,viewcart,deleteitem,orderaction,payment
from .views import paymentaction,viewdetails,details,cancelorder
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signupaction/", signupaction, name="signupaction"),
    path("customerview/", customerview, name="customerview"),
    path("addtocart<int:id>/", addtocart, name="addtocart"),
    path("cartaction/", cartaction, name="cartaction"),
    path("viewcart/", viewcart, name="viewcart"), 
    path("deleteitem<int:id>/", deleteitem, name="deleteitem"),  
    path("orderaction/", orderaction, name="orderaction"),
    path("payment<int:id>/", payment, name="payment"),
    path("paymentaction/", paymentaction, name="paymentaction"),
    path("viewdetails/", viewdetails, name="viewdetails"),
    path("details<int:id>", details, name="details"),
    path("cancelorder<int:id>/", cancelorder, name="cancelorder"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
"""
URL configuration for GearGarage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.SignupView.as_view(),name="signup"),
    path("", views.SignInView.as_view(), name="signin"),
    path("home/",views.HomeView.as_view(),name="home"),
    path("selling/bike/",views.AddingBikeView.as_view(),name="sellbike"),
    path("myvehicle/",views.MyVehicleView.as_view(),name="myvehicle"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("vehicle/<int:pk>",views.VehicleDetailView.as_view(),name="vehicle-detail"),
    path("vehicle/<int:pk>/addtowishlist/",views.AddtoWishlistView.as_view(),name="add-to-wishlist"),
    path('wishlist/items/all',views.WhislistItemView.as_view(),name="whishlist-basket"),
    path("vehicle/<int:pk>/notifications/",views.NotificationView.as_view(), name="notification"),
    path('vehicle/owner/text/',views.VehicleNotificationView.as_view(),name="name"),
    path("vehicle/message/<int:pk>/", views.Enquiry.as_view(), name = "enquiry"), 
    path("vehicle/reply/list/", views.ReplyList.as_view(), name="reply-list"),
    path("vehicle/reply/<int:pk>/", views.Reply.as_view(), name = "reply"),
    path("vehicle/message/list/", views.MessageList.as_view(), name = "message-list"),
    path('signout/',views.SignOutView.as_view(),name='signout'),
    path('wishlist/item/<int:pk>/remove',views.WishlistItemRemoveView.as_view(),name="wishlistitem-remove"),
    
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



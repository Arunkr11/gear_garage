from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib.auth import login, logout, authenticate

from store.forms import RegistrationForm,LoginForm,BikeAddingForm
from store.models import Vehicle,Brand,Wishlist,Notification

# Create your views here.

class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"login.html",{"form":form})

class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {"form":form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
           u_name=form.cleaned_data.get("username")
           pwd=form.cleaned_data.get("password")
           user_object=authenticate(request, username=u_name, password=pwd)
           if user_object:
               login(request, user_object)
               return redirect("index")
        else:
            return render(request,'login.html', {"form":form})
        
class HomeView(View):
    def get(self,request,*args,**kwargs):
        
        return render(request,"home.html")
    
class AddingBikeView(View):
    def get(self,request,*args,**kwargs):
        form=BikeAddingForm()
        return render(request,"bikeadd.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BikeAddingForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.owner=request.user
            form.save()
            return redirect("index")
        else:
            return render(request,"bikeadd.html",{"form":form})
class MyVehicleView(View):
    def get(self,request,*args,**kwargs):
        qs=Vehicle.objects.filter(owner=request.user)
        return render(request,"myvehicle.html",{"da":qs})
    
class IndexView(View):
    def get(self,request,*args,**kwargs):
        qs=Vehicle.objects.all()
        qsss=Vehicle.objects.filter(owner=request.user)
        return render(request,"index.html",{"data":qs,"veh":qsss})
    
class VehicleDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicle.objects.get(id=id)
        return render(request,"vehiche_detail.html",{"data":qs})
    
class AddtoWishlistView(View):
  
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        vehicle_obj=Vehicle.objects.get(id=id)
        request.user.wishlist.vehicle_objects.add(vehicle_obj)
        # to fetch wishlist object of authenticated user
        # request.user.wishlist.vehicle_objects.all()
        return redirect("whishlist-basket")
    
class WhislistItemView(View):
    def get(self,request,*args,**kwargs):
        qs=request.user.wishlist.vehicle_objects.all()
        return render(request,"wishlist.html",{"data":qs})
    

class WishlistItemRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        wishlist_item_object=Wishlist.objects.get(id=id)
        wishlist_item_object.delete()
        return redirect("whishlist-basket")
    

class NotificationView(View):
    template_name = "notification.html"  # Specify your template name here

    def get(self, request, *args, **kwargs):
        # Handle GET request logic here (if needed)
        id = kwargs.get("pk")
        qs = Vehicle.objects.get(id=id)  # Retrieve the Vehicle object
        return render(request, self.template_name, {"data": qs})

    def post(self, request, *args, **kwargs):
        # Handle POST request logic here
        id = kwargs.get("pk")
        qs = Vehicle.objects.get(id=id)  # Retrieve the Vehicle object
        # print(request.POST.get("question"))
        Notification.objects.create(
            vehicle_object=qs,
            user_object=request.user,
            message=request.POST.get("question")            
            )
        return render(request, self.template_name, {"data": qs})
    
class VehicleNotificationView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        vehi_obj=Vehicle.objects.filter(id=id)
        qs=Notification.objects.filter(vehicle_object=vehi_obj)
        return render(request,"text.html",{"data":qs,"vehi":vehi_obj})
    
   






    

    


    
    

    


    

    

    

    

    

        
        


    


    
        


        


        






            


    

 



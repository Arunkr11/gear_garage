from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,TemplateView
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from store.forms import RegistrationForm,LoginForm,BikeAddingForm
from store.models import Vehicle,Brand,Wishlist,Notification
from store.decorators import signin_required

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
        
@method_decorator([signin_required,never_cache],name="dispatch") 
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
        
@method_decorator([signin_required,never_cache],name="dispatch") 
class MyVehicleView(View):
    def get(self,request,*args,**kwargs):
        qs=Vehicle.objects.filter(owner=request.user)
        return render(request,"myvehicle.html",{"da":qs})
    
@method_decorator([signin_required,never_cache],name="dispatch") 
class IndexView(View):
    def get(self,request,*args,**kwargs):
        qs=Vehicle.objects.all()
        qsss=Vehicle.objects.filter(owner=request.user)
        return render(request,"index.html",{"data":qs,"veh":qsss})

@method_decorator([signin_required,never_cache],name="dispatch")     
class VehicleDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicle.objects.get(id=id)
        return render(request,"vehiche_detail.html",{"data":qs})
 
@method_decorator([signin_required,never_cache],name="dispatch")    
class AddtoWishlistView(View):
  
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        vehicle_obj=Vehicle.objects.get(id=id)

        request.user.wishlist.vehicle_objects.add(vehicle_obj)
        # to fetch wishlist object of authenticated user
        # request.user.wishlist.vehicle_objects.all()
        return redirect("whishlist-basket")

@method_decorator([signin_required,never_cache],name="dispatch")    
class WhislistItemView(View):
    def get(self,request,*args,**kwargs):
        qs=request.user.wishlist.vehicle_objects.all()
        return render(request,"wishlist.html",{"data":qs})
    
# @method_decorator([signin_required,never_cache],name="dispatch") 
# class WishlistItemRemoveView(View):
#     def get(self, request, *args, **kwargs):
#         # Get the primary key from the URL kwargs
#         id = kwargs.get("pk")
        
#         # Get the Wishlist item object based on the primary key
#         wishlist_item_object = get_object_or_404(Wishlist, id=id)
        
#         # Delete the Wishlist item
#         wishlist_item_object.delete()
        
#         # Redirect to a specific URL after removing the item
#         return redirect("wishlist-basket")
    

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
# class Reply_list(View):
#     def get(self, request, *args,**kwargs):
        
#         qs = Notification.objects.filter(user_object !=request.user, is_read =False)
#         qs.orderf 
#         return render()
# class ReplyView(View):
#     def get(self, request, *args, **kwargs):
        
#         return render( )
#     def post():
#         id = kwargs.get("pk")
#         qs = Notification.objects.get(id =id)
#         reply = request.POST.get("reply")
#         qs.reply = reply
#         if qs.reply:
#             qs.is_read = True


@method_decorator([signin_required,never_cache],name="dispatch")    
class VehicleNotificationView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        vehi_obj=Vehicle.objects.filter(id=id)
        qs=Notification.objects.filter(vehicle_object=vehi_obj)
        return render(request,"text.html",{"data":qs,"vehi":vehi_obj})
    
@method_decorator([signin_required,never_cache],name="dispatch")    
class Enquiry(View):
    def get(self,request,*args,**kwargs):
        id  = kwargs.get("pk")
        bike_object = Vehicle.objects.get(id = id)
        return render(request, "enquiry.html", {"data":bike_object})
    
    def post(self,request,*args,**kwargs):
        id  = kwargs.get("pk")
        bike_object = Vehicle.objects.get(id = id)
        message = request.POST.get("message")
        Notification.objects.create(user_object =request.user, 
                                    vehicle_object = bike_object, 
                                    message=message)
        return redirect("reply-list")
    
@method_decorator([signin_required,never_cache],name="dispatch")        
class ReplyList(View):
    def get(self,request,*args,**kwargs):
        qs=Notification.objects.filter(vehicle_object__owner = request.user, is_replied = False)
        return render(request, "reply-list.html", {"data":qs})
        
@method_decorator([signin_required,never_cache],name="dispatch") 
class Reply(View):
    def get(self, request,*args,**kwargs):
        id = kwargs.get("pk")
        qs =Notification.objects.get(id =id)
        return render(request, "reply.html", {"data":qs})
    
    def post(self, request,*args,**kwargs):
        id = kwargs.get("pk")
        qs =Notification.objects.get(id =id)
        reply  = request.POST.get("reply") 
        qs.reply = reply
        qs.save()
        if qs.reply:
            qs.is_replied = True
            qs.save()
            
        return redirect("reply-list")         

@method_decorator([signin_required,never_cache],name="dispatch") 
class MessageList(View):
    def get(self, request, *args, **kwargs):
        qs = Notification.objects.filter(user_object = request.user, is_replied  = True, is_read = False)
        return render(request, "message-list.html", {"data":qs})
        
        
        
@method_decorator([signin_required,never_cache],name='dispatch')
class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('signin')
    

    


    
    

    


    

    

    

    

    

        
        


    


    
        


        


        






            


    

 



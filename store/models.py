from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Brand(models.Model):
    name=models.CharField(max_length=200,unique=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="vehicle_images",default="default.jpeg",null=True,blank=True)
    decription=models.TextField(null=True)
   
    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE, related_name="item")
    cat_opt=(
        ("motorbike","motorbike"),
        ("scooter","scooter")
    )
    category=models.CharField(max_length=30,choices=cat_opt,default="motorbike")
    # brand=models.ForeignKey(Brand)
    fuel_opt=(
        ("petrol","petrol"),
        ("electric","electric")
    )
    fuel=models.CharField(max_length=20,choices=fuel_opt,default="petrol")
    kms=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of=(
        ("first_hand","first_hand"),
        ("second_hand","second_hand"),
        ("third_hand","third_hand"),
        ("fourth_hand","fourth_hand"),
        ("other","other")
    )
    owner_type=models.CharField(max_length=200,choices=no_of,default=None)
    price=models.PositiveIntegerField()
    is_sold=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Wishlist(models.Model):
    owner_object=models.OneToOneField(User,on_delete=models.CASCADE,related_name="wishlist")
    vehicle_objects=models.ManyToManyField(Vehicle,related_name="wishlist_item")

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

# class WishlistItem(models.Model):
    # wishlist_object=models.ForeignKey(Wishlist,on_delete=models.CASCADE,related_name="wish_item")
    

    # created_date=models.DateTimeField(auto_now_add=True)
    # updated_date=models.DateTimeField(auto_now=True)
    # is_active=models.BooleanField(default=True)

class Notification(models.Model):
    vehicle_object=models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name="notification")
    user_object=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    message=models.CharField(max_length=200)
    reply=models.CharField(max_length=200,null=True)
    is_read=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    is_replied=models.BooleanField(default=False,null=True)

def create_whislist(sender,instance,created,**kwargs):
    #instance=user_object :ie is the account created user
    #created=T|F
    #sender=User
    if created:
        Wishlist.objects.create(owner_object=instance)
post_save.connect(create_whislist,sender=User)

from django.db import models

# Create your models here.


class admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    ad_username = models.CharField(max_length=100)
    ad_password = models.CharField(max_length=100)
  
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_phone = models.IntegerField()
    customer_email = models.EmailField()
    customer_password = models.CharField(max_length=100)


# PRODUCT--------------------------------------------------------------------------------------------------------

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50 )
    category_image = models.ImageField()
    category_quantity = models.IntegerField()
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=500)
    product_image = models.ImageField()
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)


# PRODUCT / END --------------------------------------------------------------------------------------------------------


# Cart & Wishedlist

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cartproduct_username = models.CharField(max_length=50 ,default=False)
    cartproduct_name = models.CharField(max_length=50, default=False)
    cartproduct_image = models.ImageField(blank=True, null=True ,default=False)
    cartproduct_price = models.IntegerField(default=False)
    cartproduct_quantity = models.IntegerField(default=False)




class Wishedlist(models.Model):
    wishedlist_id = models.AutoField(primary_key=True)
    wishedlist_username = models.CharField(max_length=50, default=False)
    wishedlist_name = models.CharField(max_length=50, default=False)
    wishedlist_image = models.ImageField(blank=True, null=True, default=False)
    wishedlist_price = models.IntegerField(default=False)

# Order & Product Details & Payment

class CustomerOrders(models.Model):
    order_id = models.AutoField(primary_key=True)
    USER = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
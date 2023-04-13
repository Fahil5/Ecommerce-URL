from dataclasses import fields
from django import forms
from . models import*

class adminform(forms.ModelForm):
    class Meta:
        model=admin
        fields=('ad_username','ad_password')
        labels={
            'ad_username':'username',
            'ad_password':'password'
        }


# CUSTOMER--------------------------------------------------------------------------------------------------------


class customerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('customer_name','customer_phone','customer_email','customer_password')
        labels={
            'customer_name':'name',
            'customer_phone':'phone',
            'customer_email':'email',
            'customer_password':'password',
        }
        
class customerformlogin(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('customer_name','customer_password')
        labels={
            'customer_name':'name',
            'customer_password':'password'
        }
        
# CUSTOMER / END --------------------------------------------------------------------------------------------------------



# PRODUCT--------------------------------------------------------------------------------------------------------


class categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=('category_name','category_image','category_quantity')
        labels={
            'category_name':'name',
            'category_image':'image',
            'category_quantity':'quantity',
        }


class productform(forms.ModelForm):
    class Meta:
        model=Product
        fields=('product_name','product_description','product_image','product_price','product_quantity')
        labels={
            'product_name':'name',
            'product_description':'description',
            'product_image':'image',
            'product_price':'price',
            'product_quantity':'quantity',
        }
    
# PRODUCT / END --------------------------------------------------------------------------------------------------------


class cartform(forms.ModelForm):
    class Meta:
        model=Cart
        fields=('cartproduct_username','cartproduct_name','cartproduct_image','cartproduct_price','cartproduct_quantity')
        labels={
            'cartproduct_username':'username',
            'cartproduct_name':'name',
            'cartproduct_image':'image',
            'cartproduct_price':'price',
            'cartproduct_quantity':'quantity',
        }


class CustomerOrdersform(forms.ModelForm):
    class Meta:
        model=CustomerOrders
        fields=('USER','country','name','address','state','postcode','phone','payment_type','product_name','product_price','product_quantity')
        labels={
            'USER':'USER',
            'country':'country',
            'name':'name',
            'address':'address',
            'state':'state',
            'postcode':'postcode',
            'phone':'phone',
            'payment_type':'payment_type',
            'product_name':'product_name',
            'product_price':'product_price',
            'product_quantity':'product_quantity',
        }

class Wishedlistform(forms.ModelForm):
    class Meta:
        model=Wishedlist
        fields=('wishedlist_username','wishedlist_name','wishedlist_image','wishedlist_price')
        labels={
            'wishedlist_username':'username',
            'wishedlist_name':'name',
            'wishedlist_image':'image',
            'wishedlist_price':'price',
        }
    
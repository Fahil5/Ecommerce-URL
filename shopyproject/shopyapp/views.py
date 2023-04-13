from django.shortcuts import redirect, render

from django.contrib import messages

from . models import*
from . forms import*
# Create your views here.


# ADMIN--------------------------------------------------------------------------------------------------------

def adminadd(request):
    form=adminform
    if(request.method=='POST'):
        form=adminform(request.POST)
        if(form.is_valid()):
            username=form.cleaned_data['ad_username']
            password=form.cleaned_data['ad_password']
            result=admin(ad_username=username,ad_password=password)
            result.save()
            return render(request,'adminadd-login.html',{'form':form})
    return render(request,'adminadd-login.html',{'form':form})


def adminlogin(request):
    msg="incorrect username or password"
    form=adminform
    if(request.method=='POST'):
        form=adminform(request.POST)
        if(form.is_valid()):
            username=form.cleaned_data['ad_username']
            password=form.cleaned_data['ad_password']
            c=admin.objects.filter(ad_username=username,ad_password=password)
            if(c):
                request.session['ad_username']=username
                return redirect('shopy:adminhome')
            else:
                return render(request,'adminadd-login.html',{'m':msg,'form':form})
    return render(request,'adminadd-login.html',{'m':msg,'form':form})

def adminhome(request):
    if 'ad_username' in request.session:
        var=request.session['ad_username']
        dict={'var':var}
        return render(request,'adminhome.html',dict)
    else:
        return redirect('shopy:adminhome')


def adminlogout(request):
    if(request.session.has_key):
        del request.session['ad_username']
        request.session.flush()
        return redirect('shopy:adminlogin')


def admincartview(request):
    z=Cart.objects.all()
    dict={'z':z}
    return render(request,'admincartview.html',dict)


def adminwishlistview(request):
    z=Wishedlist.objects.all()
    dict={'z':z}
    return render(request,'adminwishlistview.html',dict)


def adminviewcustomerorder(request):
    z=CustomerOrders.objects.all()
    dict={'z':z}
    return render(request,'adminviewcustomerorder.html',dict)

# ADMIN / END --------------------------------------------------------------------------------------------------------



# CUSTOMER--------------------------------------------------------------------------------------------------------

def customeradd(request):
    form=customerform
    if(request.method=='POST'):
        form=customerform(request.POST)
        if(form.is_valid()):
            name=form.cleaned_data['customer_name']
            phone=form.cleaned_data['customer_phone']
            email=form.cleaned_data['customer_email']
            password=form.cleaned_data['customer_password'] 
            result=Customer(customer_name=name,customer_phone=phone,customer_email=email,customer_password=password)
            result.save()
            return redirect('/shopy/customerlogin')
    return render(request,'login-register.html',{'form':form})


def customerlogin(request):
    msg="incorrect username or password"
    form=customerformlogin
    if(request.method=='POST'):
        form=customerformlogin(request.POST)
        if(form.is_valid()):
            name=form.cleaned_data['customer_name']
            password=form.cleaned_data['customer_password']
            c=Customer.objects.filter(customer_name=name,customer_password=password)
            if(c):
                request.session['customer_name']=name
                return redirect('shopy:customerhome')
            else:
                return render(request,'login-register.html',{'m':msg,'form':form})
    return render(request,'login-register.html',{'m':msg,'form':form})


# def customerhome(request):
#     if 'customer_name' in request.session:
#         var=request.session['customer_name']
#         z = Product.objects.filter(product_category=(int(1)))
#         y = Product.objects.filter(product_category=(int(2)))
#         x = Product.objects.filter(product_category=(int(3)))
#         w = Product.objects.filter(product_category=(int(4)))
#         category = Category.objects.filter(category_name="Laptop")
#         dict={'var':var,'z':z,'y':y,'x':x,'w':w,'category':category}
#         return render(request,'index.html',dict)
#     else:
#         return redirect('shopy:customerhome')


def customerlogout(request):
    if(request.session.has_key):
        del request.session['customer_name']
        request.session.flush()
        return redirect('shopy:customerlogin')

# CUSTOMER / END --------------------------------------------------------------------------------------------------------



# PRODUCT--------------------------------------------------------------------------------------------------------

def categoryadd(request):
    form=categoryform
    if(request.method=='POST'):
        form=categoryform(request.POST,request.FILES)
        if(form.is_valid()):
            name=form.cleaned_data['category_name']
            image=form.cleaned_data['category_image']
            quantity=form.cleaned_data['category_quantity']
            result=Category(category_name=name,category_image=image,category_quantity=quantity)
            result.save()
            return redirect('/shopy/adminhome')
    return render(request,'categoryadd.html',{'form':form})


def productadd(request):
    c=Category.objects.all()
    form=productform
    if(request.method=='POST'):
        ca=Category.objects.only('category_id').get(category_name=request.POST['cat'])
        form=productform(request.POST,request.FILES)
        if(form.is_valid()):
            name=form.cleaned_data['product_name']
            description=form.cleaned_data['product_description']
            image=form.cleaned_data['product_image']
            price=form.cleaned_data['product_price']
            quantity=form.cleaned_data['product_quantity']
            result=Product(product_name=name,product_description=description,product_image=image,
                           product_price=price,product_quantity=quantity,product_category=ca)
            result.save()
            return redirect('/shopy/adminhome')
    return render(request,'productadd.html',{'form':form,'c':c})


# PRODUCT / END --------------------------------------------------------------------------------------------------------


def cartadd(request,product_id):
    a=Product.objects.get(product_id=product_id)
    if 'customer_name' in request.session:
        var2=request.session['customer_name']
    form=cartform
    if(request.method=='POST'):
        form=cartform(request.POST,request.FILES)
        if(form.is_valid()):
            var2=var2
            username=form.cleaned_data['cartproduct_username']
            name=form.cleaned_data['cartproduct_name']
            image=form.cleaned_data['cartproduct_image']
            price=form.cleaned_data['cartproduct_price']
            quantity=form.cleaned_data['cartproduct_quantity']
            result=Cart(cartproduct_username=username,cartproduct_name=name,cartproduct_image=image,cartproduct_price=price,cartproduct_quantity=quantity)
            result.save()
            return redirect('/shopy/customerhome')
    return render(request,'single-product.html',{'form':form,'a':a,'var2':var2})


def cartview(request):
    if 'customer_name' in request.session:
        var2=request.session['customer_name']
    z=Cart.objects.all()
    x=Cart.objects.all().filter(cartproduct_username=var2)
    dict={'x':x,'z':z}
    return render(request,'shopping-cart.html',dict)


def cartdelete(request,cart_id):
    y=Cart.objects.get(cart_id=cart_id)
    y.delete()
    return redirect('shopy:customerhome')



def CustomerOrdersadd(request):
    if 'customer_name' in request.session:
        var2=request.session['customer_name']
    x=Cart.objects.all().filter(cartproduct_username=var2)
    form=CustomerOrdersform
    if(request.method=='POST'):
        form=CustomerOrdersform(request.POST)
        if(form.is_valid()):
            var2=var2
            USER=form.cleaned_data['USER']
            country=form.cleaned_data['country']
            name=form.cleaned_data['name']
            address=form.cleaned_data['address']
            state=form.cleaned_data['state']
            postcode=form.cleaned_data['postcode']
            phone=form.cleaned_data['phone']
            payment_type=form.cleaned_data['payment_type']
            product_name=form.cleaned_data['product_name']
            product_price=form.cleaned_data['product_price']
            product_quantity=form.cleaned_data['product_quantity']
            result=CustomerOrders(USER=USER,country=country,name=name,address=address,state=state,postcode=postcode,
                                    phone=phone,payment_type=payment_type,product_name=product_name,product_price=product_price,
                                    product_quantity=product_quantity)
            result.save()
            return redirect('/shopy/success')
    return render(request,'cart-checkout.html',{'form':form,'x':x,'var2':var2})




def wishlistadd(request,product_id):
    a=Product.objects.get(product_id=product_id)
    if 'customer_name' in request.session:
        var2=request.session['customer_name']
    form=Wishedlistform
    if(request.method=='POST'):
        form=Wishedlistform(request.POST,request.FILES)
        if(form.is_valid()):
            var2=var2
            username=form.cleaned_data['wishedlist_username']
            name=form.cleaned_data['wishedlist_name']
            image=form.cleaned_data['wishedlist_image']
            price=form.cleaned_data['wishedlist_price']
            result=Wishedlist(wishedlist_username=username,wishedlist_name=name,wishedlist_image=image,
                              wishedlist_price=price)
            result.save()
            return redirect('/shopy/customerhome')
    return render(request,'single-product.html',{'form':form,'a':a,'var2':var2})


def wishlistview(request):
    if 'customer_name' in request.session:
        var2=request.session['customer_name']
    x=Cart.objects.all()
    z=Wishedlist.objects.all().filter(wishedlist_username=var2)
    dict={'x':x,'z':z}
    return render(request,'wish-list.html',dict)


def wishlistdelete(request,wishedlist_id):
    y=Wishedlist.objects.get(wishedlist_id=wishedlist_id)
    y.delete()
    return redirect('shopy:customerhome')

def success(request):
    a=('/shopy/customerhome')
    dict={'a':a}
    return render(request,'success.html',dict)


def customerhome(request):
    if 'customer_name' in request.session:
        var=request.session['customer_name']
        z = Product.objects.filter(product_category=(int(1)))
        y = Product.objects.filter(product_category=(int(2)))
        x = Product.objects.filter(product_category=(int(3)))
        w = Product.objects.filter(product_category=(int(4)))
        dict={'var':var,'z':z,'y':y,'x':x,'w':w}
        return render(request,'index.html',dict)
    else:
        return redirect('shopy:customerhome')


def categoryproductone(request):
    z = Product.objects.filter(product_category=(int(1)))
    dict={'z':z}
    return render(request,'shop-1-column.html',dict)

def categoryproducttwo(request):
    y = Product.objects.filter(product_category=(int(2)))
    dict={'y':y}
    return render(request,'shop2-column.html',dict)

def categoryproductthree(request):
    x = Product.objects.filter(product_category=(int(3)))
    dict={'x':x}
    return render(request,'shop-3-column.html',dict)

def categoryproductfour(request):
    w = Product.objects.filter(product_category=(int(4)))
    dict={'w':w}
    return render(request,'shop-4-column.html',dict)

# def collections(request):
#     category = Category.objects.filter(category_name="Laptop")
#     context = {'category':category}
#     return render(request,'collections.html',context)


# def collectionsview(request):
#     product = Product.objects.filter(product_category=(int(1)))
#     context = {'product':product}
#     return render(request,'index11.html',context)





# URGENT

# Image of Product       OR       # wishlist id passing


# NOT URGENT

# multiple product in database
# total amount
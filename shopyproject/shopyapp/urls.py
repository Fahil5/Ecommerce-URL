from django.urls import path
from . import views
app_name='shopy'
urlpatterns = [
    
# ADMIN--------------------------------------------------------------------------------------------------------
    
    path('adminadd',views.adminadd,name="adminadd"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
    path('admincartview',views.admincartview,name="admincartview"),
    path('adminwishlistview',views.adminwishlistview,name="adminwishlistview"),
    path('adminviewcustomerorder',views.adminviewcustomerorder,name="adminviewcustomerorder"),

# ADMIN / END --------------------------------------------------------------------------------------------------------

    
    
# CUSTOMER--------------------------------------------------------------------------------------------------------
    
    path('customeradd',views.customeradd,name="customeradd"),
    path('customerlogin',views.customerlogin,name="customerlogin"),
    path('customerhome',views.customerhome,name="customerhome"),
    path('customerlogout',views.customerlogout,name="customerlogout"),
    
# CUSTOMER / END --------------------------------------------------------------------------------------------------------



# PRODUCT--------------------------------------------------------------------------------------------------------
    
    path('productadd',views.productadd,name="productadd"),
    path('categoryadd',views.categoryadd,name="categoryadd"),
    path('productadd',views.productadd,name="productadd"),

# PRODUCT / END --------------------------------------------------------------------------------------------------------


 
# CART--------------------------------------------------------------------------------------------------------

    path('cartadd/<int:product_id>/',views.cartadd,name="cartadd"),
    path('cartview',views.cartview,name="cartview"),
    path('cartdelete/<int:cart_id>/',views.cartdelete,name="cartdelete"),
    
# CART / END --------------------------------------------------------------------------------------------------------



# WISHLIST--------------------------------------------------------------------------------------------------------

    path('wishlistadd/<int:product_id>/',views.wishlistadd,name="wishlistadd"),
    path('wishlistview',views.wishlistview,name="wishlistview"),
    path('wishlistdelete/<int:wishedlist_id>/',views.wishlistdelete,name="wishlistdelete"),    

# WISHLIST / END --------------------------------------------------------------------------------------------------------

    path('CustomerOrdersadd',views.CustomerOrdersadd,name="CustomerOrdersadd"),
    
    path('success',views.success,name="success"),

    path('categoryproductone',views.categoryproductone,name="categoryproductone"),

    path('categoryproducttwo',views.categoryproducttwo,name="categoryproducttwo"),

    path('categoryproductthree',views.categoryproductthree,name="categoryproductthree"),
    
    path('categoryproductfour',views.categoryproductfour,name="categoryproductfour"),

    # path('collections',views.collections,name="collections"),

    # path('collectionsview',views.collectionsview,name="collectionsview"),

]

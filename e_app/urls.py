from django.urls import path
from . import views
app_name = 'e_app'
urlpatterns = [
    path('',views.all_category_products,name='all_category_products'),
    path('<slug:c_slug>/',views.all_category_products,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.product_view,name='product_view'),
]
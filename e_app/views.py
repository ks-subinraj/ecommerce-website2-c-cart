from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def all_category_products(request,c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products_list = Product.objects.filter(category=c_page,available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list,2)
    page_num = int(request.GET.get('page',1))
    try:
        products = paginator.page(page_num)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request,'index.html',{'category':c_page,'products':products})

def product_view(request,c_slug,product_slug):
    try:
        cat = get_object_or_404(Category,slug=c_slug)
        product = Product.objects.get(category=cat,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

    
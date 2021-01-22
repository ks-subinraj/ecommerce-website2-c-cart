from django.shortcuts import render
from django.db.models import Q
from e_app.models import Product

# Create your views here.
def search_view(request):
    product = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'result.html',{'product':product,'query':query})
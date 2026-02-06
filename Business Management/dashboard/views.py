from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product # We 'import' the storage room

@login_required
def index(request):
    # Logic: Grab all products from the database
    all_products = Product.objects.all()
    
    # Logic: Put them in a 'context' dictionary to send to HTML
    context = {
        'products': all_products,
        'product_count': all_products.count()
    }
    
    return render(request, 'dashboard/index.html', context)
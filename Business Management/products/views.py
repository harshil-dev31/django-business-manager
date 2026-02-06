from django.shortcuts import render, redirect,  get_object_or_404
from .models import Product
def add_product(request):
    if request.method == "POST":
        # Logic: Pull data from the HTML form
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        # Logic: Save it to the Database
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock_quantity=stock
        )
        return redirect('dashboard_index') # Send them home!

    return render(request, 'products/add_product.html')


def delete_product(request, pk):
    # Logic: Find the specific product by its ID (Primary Key)
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('dashboard_index')

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.name = request.POST.get('name')
        # Logic: If description is None, use an empty string ""
        product.description = request.POST.get('description') or "" 
        product.price = request.POST.get('price')
        product.stock_quantity = request.POST.get('stock')
        
        product.save()
        return redirect('dashboard_index')

    return render(request, 'products/edit_product.html', {'product': product})
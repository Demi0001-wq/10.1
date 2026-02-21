from django.shortcuts import render, get_object_or_request_or_404

from catalog.models import Product, Contact

def home(request):
    """
    Controller for the home page.
    Displays all products.
    """
    products_list = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products_list})

def product_detail(request, pk):
    """
    Controller for the single product page.
    Receives product by pk and displays its details.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def contacts(request):
    """
    Controller for the contacts page.
    Handles POST requests from the feedback form.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Display message to console as required in Task 4
        print(f"New contact message:\nName: {name}\nPhone: {phone}\nMessage: {message}")

    contacts_list = Contact.objects.all()
    return render(request, 'catalog/contacts.html', {'contacts': contacts_list})

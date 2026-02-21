from django.shortcuts import render

from catalog.models import Product, Contact

def home(request):
    """
    Controller for the home page.
    """
    latest_products = Product.objects.order_by('-created_at')[:5]
    for product in latest_products:
        print(product)
    return render(request, 'catalog/home.html', {'latest_products': latest_products})

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

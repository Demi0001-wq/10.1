from django.shortcuts import render

def home(request):
    """
    Controller for the home page.
    """
    return render(request, 'catalog/home.html')

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
        return render(request, 'catalog/contacts.html', {'success': True})
    
    return render(request, 'catalog/contacts.html')

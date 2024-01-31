from django.shortcuts import render

# View for the home page
def home_view(request):
    return render(request, 'core/home.html')

# View for the about page
def about_view(request):
    return render(request, 'core/about.html')

# View for the contact page
def contact_view(request):
    return render(request, 'core/contact.html')

# View for the terms page
def terms_view(request):
    return render(request, 'core/terms.html')

# View for the privacy page
def privacy_view(request):
    return render(request, 'core/privacy.html')

# View for the 404 page
def handler404(request, exception):
    return render(request, 'core/404.html', status=404)

# View for the 500 page
def handler500(request):
    return render(request, 'core/500.html', status=500)



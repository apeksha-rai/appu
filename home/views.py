from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
def portfolio(request):
    return render(request,'portfolio.html')
def price(request):
    return render(request,'price.html')
def blog_home(request):
    return render(request,'blog-home.html')
def blog_single(request):
    return render(request,'blog-single.html')
def elements(request):
    return render(request,'elements.html')
def contact(request):
    return render(request,'contact.html')



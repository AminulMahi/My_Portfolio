from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from .models import contact
from admin_app.models import blog

# Create your views here.

def home(request):
    return render(request, 'index.html')

def user_blog(request): # class name and function name cannot be same
    all_data = blog.objects.all()

    data = {
        'all_blog_data' : all_data,
        }
    return render(request, 'blog.html', data)


def blog_details(request,slug):
    blog_detail = blog.objects.get(slug=slug)
    
    data = {
        'blog_detail' : blog_detail,
    }
    return render(request, 'blog_details.html', data)

def contact_info(request):
    if request.method == 'POST':  # post is secure method
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contactus= contact(name=name,email=email,phone=phone,message=message)
        contactus.save()

        return redirect('home')
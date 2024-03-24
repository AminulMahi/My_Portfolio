from django.shortcuts import render, redirect
from .models import blog, Signup

from django.contrib import messages


# Create your views here.

def admin(request):
    if 'user_id' in request.session:
        print(request.session['user_id'])
        return render(request, 'admin/admin_index.html')
    else:
        return redirect('login')

def admin_blog(request):
    if 'user_id' in request.session:
        all_data = blog.objects.all()
        data = {'all_blog_data' : all_data}
        return render(request, 'admin/admin_blog.html', data)
    messages.error(request, 'Session Expired please login again..!')
    return redirect('login')

def insert_blog(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    date = request.POST.get('date')
    image = request.FILES.get('image')
    description = request.POST.get('description')
    # CreatingVariable = requestMethod.POSTmethod.GetMethod(ValueFromHTMLnameAttribute)

    blog.objects.create(title=title, author=author, date=date, image=image, description=description)
    # blog_obj = blog(
    #     title = title,
    #     author = author,
    #     date = date,
    #     image = image,
    #     description = description
    # )
    # blog_obj.save()
    return redirect('admin_blog')

def delete_blog(request, id):
    all_data = blog.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('admin_blog')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conpw = request.POST.get('conf_password')

        Signup.objects.create(
            name=name,
            phone=phone,
            email=email,
            password=password,
            
        )

    return render(request, 'login.html')
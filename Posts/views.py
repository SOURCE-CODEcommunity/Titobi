from django.shortcuts import render, redirect
from .models import post, init_img, gif, detail, order
from django.contrib import messages
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    init_imgs = init_img.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request, user)
                return redirect('manage posts')
    else:
        form = AuthenticationForm(request)
    
    return render(request, 'login.html', {'form': form, 'init_imgs': init_imgs})
    
def logout_view(request):
    logout(request)
    return redirect('login')

def home_page(request):
    init_imgs = init_img.objects.all()
    gifs = gif.objects.all()
    return render(request, 'home.html', {'init_imgs': init_imgs, 'gifs': gifs})

def featured_items(request):
    posts = post.objects.all().order_by('-date')
    init_imgs = init_img.objects.all()
    return render(request, 'featured items.html', {'posts': posts, 'init_imgs': init_imgs})

def about(request):
    posts = post.objects.all().order_by('-date')
    init_imgs = init_img.objects.all()
    details = detail.objects.all()
    return render(request, 'about.html', {'posts': posts, 'init_imgs': init_imgs, 'details': details})

def Order(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        phone_number = request.POST.get('phone_number')
        contact_method = request.POST.get('contact_method')

        if not phone_number or not contact_method:
            messages.error(request, 'Please fill in the fields')
            return redirect('featured items')
        
        order_ = order(title= title, phone_number= phone_number, contact_method= contact_method)
        order_.save()

        messages.success(
            request, 
            f"Order has successfully been placed. "
            f"{'You will receive a phone call soon for further details' if contact_method != 'Whatsapp' else 'You will receive a WhatsApp message soon for further details'}"
            " Thank you!"
        )

        #messages.success(request, f'Order as successfully been placed {'you will receive a phone call soon on further details' if contact_method!='Whatsapp' else 'you will receive a whatsapp message soon on further details'} Thank you!')
        return redirect('featured items')
    else:
        return redirect('featured items')

@login_required       
def manage_posts(request):
    posts = post.objects.all().order_by('-date')
    init_imgs = init_img.objects.all()
    orders = order.objects.all().order_by('-date')

    return render(request, 'manage posts.html', {'posts': posts, 'init_imgs': init_imgs, 'orders': orders})

def new_post(request):
    init_imgs = init_img.objects.all()
    if request.method == 'POST':
        form = forms.CreatePosts(
            request.POST, request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect('manage posts')
    else:
        form = forms.CreatePosts()
    return render(request, 'new post.html', {'form': form, 'init_imgs': init_imgs})


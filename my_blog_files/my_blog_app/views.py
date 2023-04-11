from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import Post
from .forms import SignUpForm, SignInForm, FeedbackForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError


class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return render(request, 'my_blog_app/contact.html', context={
            'form': form,
            'title': 'Написать мне',
        })

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
           #try:
           #    send_mail(f'От {name} | {subject}', message, from_email, [''])
           #except BadHeaderError:
           #    return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'my_blog_app/contact.html', context={
            'form': form,
        })





class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'my_blog_app/success.html', context={
            'title': 'Спасибо'
        })


class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'my_blog_app/home.html', context={
            'page_obj': page_obj,
        })


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'my_blog_app/post_detail.html', context={
            'post': post,
        })


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'my_blog_app/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            return render(request, 'my_blog_app/signup.html', context={
                'form': form,
            })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'my_blog_app/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'my_blog_app/signin.html', context={
            'form': form,
        })

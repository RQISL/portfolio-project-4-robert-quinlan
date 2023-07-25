from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Post
from order_foods.forms import LoginForm
from django.contrib.auth import login, authenticate, logout


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "contact_and_feedback.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )


class OrderFoods(TemplateView):
    template_name = "order_foods.html"


def sign_in(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts')

        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f'Hi {username.title()}, welcome back!')
                return redirect('posts')

        # either form not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'accounts/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('login')

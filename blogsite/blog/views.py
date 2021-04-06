from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
# Create your views here.

#def home(request):
#    context = {'posts':Post.objects.all()}
#    return render(request, 'blog/home.html', context)

class Postlistview(ListView):
    model=Post
    template_name='blog/home.html' #cbv look for template in format of #<app>/<models>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class Userpostlistview(ListView):
    model=Post
    template_name='blog/user_post.html' #cbv look for template in format of #<app>/<models>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class Postdetailview(DetailView):
    model=Post

class Postcreateview(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self, form): #new post need an author
        form.instance.author=self.request.user
        return super().form_valid(form)

class Postupdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView): #no need for template
    model=Post
    fields = ['title','content']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self): #works with UserPassesTestMixin
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class Postdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url = "/" #after deletion
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
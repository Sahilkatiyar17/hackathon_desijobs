from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import UserRegisterForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Post 
from django.views.generic import ListView , CreateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def Home(request):
    return render(request,"home.html")

def Register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user=User.objects.filter(username=username)
        
        if user.exists():
           # messages.error(request,"Username already exists")
            return redirect('/register/')
        
        
        user=User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.save()
        #messages.success(request,f"Account created for {username}!",)
        return redirect('/login/')
    return render(request,"register.html")
        
    
'''def Register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_vaild():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,"register.html",{'form':form})'''
            
   
    
def Login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid username or password")
            return redirect('/login/')
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("logged in")
            return redirect('/jobs/')
            
        else:
            
            messages.error(request,"Invalid credentials")
            print('invalid credentials')
            return redirect('/login/')
            
    
    return render(request,"Login.html")

def Jobs(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,"jobs.html",context)

class PostListView(ListView):
    model=Post
    template_name="jobs.html"
    context_object_name="posts"
    ordering=["-date_posted"]
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=["author","title","location","content"]
    template_name="post_form.html"
    
    
    def form_vaild(self,form):
        form.instance.author=self.request.user
        return super().form_vaild(form)
    

def logout(request):
    auth.logout(request)
    return render(request,"logout.html")

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name="post_con_del.html"
    success_url="/jobs/"
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDetailView(DetailView):
    model=Post
    template_name="post_detail.html"

def course(request):
    return render(request,"courses.html")

def aboutus(request):
    return render(request,"aboutus.html")
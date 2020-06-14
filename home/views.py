from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def home(request):
    post = Post.objects.filter(published=True).order_by('timeStamp')[:3]
    return render (request, 'home/home.html', {'post': post})

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill in the form correctly")
        else:
            contact = Contact(name=name, email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render (request, 'home/contact.html')
    # return HttpResponse ('This is Contact page')

def about(request):
    return render (request, 'home/about.html')
    # return HttpResponse ('This is About page')

def search(request):
    query = request.GET['query']
    allPost = Post.objects.filter(postSlug__icontains=query)
    params = {'allPost': allPost, 'query':query}
    return render (request, 'home/search.html', params)
    # return HttpResponse ('This is Search')

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        userName = request.POST['userName']    
        fName = request.POST['fName']    
        lName = request.POST['lName']    
        eMail = request.POST['eMail']    
        pass1 = request.POST['pass1']    
        pass2 = request.POST['pass2']

        # Checks fro erronous entries
        if len(userName)>12:
            messages.error(request, "Username must be under 12 Characters")
            return redirect('home')
        if not userName.isalnum():
            messages.error(request, "Username must contained alphabets and numbers. Special characters are not allowed")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Your Password does not match")
            return redirect('home')

        # Create the users
        myUser = User.objects.create_user(userName,eMail,pass1)
        myUser.first_name = fName     
        myUser.last_name = lName 
        myUser.save()
        messages.success(request, "Your Maifalit Majhya account has been successfully created")
        return redirect('home')    
    else:
        return HttpResponse ('404- Page not Found')

def handleLogin(request):
    if request.method == "POST":
        loginUser = request.POST['loginUser']
        loginPass = request.POST['loginPass']
        user = authenticate(username=loginUser, password=loginPass)

        if user is not None:
            login(request,user)
            messages.success(request,"You have been successfully logged in")
            return redirect ('home')
        else:
            messages.error(request,"Invalid Credentials, Please Login with correct credentials")
            return redirect ('home')

    return HttpResponse ('404- Page not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "You have been successfully Logged Out")
    return redirect ('home')
from django.shortcuts import render, HttpResponse, redirect
from blog import urls
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post, blogComment
from blog.templatetags import extras
# Create your views here.

def blogHome(request):
    allPost = Post.objects.all()
    context = {'allPost': allPost}
    return render (request, 'blog/blogHome.html',context)

def blogPost(request, slug):
    post = Post.objects.filter(postSlug=slug).first()
    comments = blogComment.objects.filter(post=post, parent=None)
    replies = blogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].apend(reply)
    context = {'post': post, 'comments':comments, 'user':request.user, 'replyDict':replyDict}
    return render (request, 'blog/blogPost.html', context)

def postComment(request):
    if request.method =='POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sNo=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = blogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your Comment has been successfully posted")
        else:
            parent = blogComment.objects.get(sno=parentSno)
            comment = blogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your Reply has been successfully posted")
    
    return redirect(f"/blog/{post.postSlug}")
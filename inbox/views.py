from django.shortcuts import render
from authors.models import single_author
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Inbox
from post.models import Like, Post


# @login_required(login_url='/login/')
# def my_inbox(request,userId):
#     currentAuthor=single_author.objects.filter(uuid=userId).first()
#     currentAuthorInbox = InboxItem.objects.filter(author__uuid=currentAuthor.uuid)
#     return render(request, 'inbox/inbox.html',{
#         "currentAuthorInbox": currentAuthorInbox,
#         "userId": userId
#     })

@login_required(login_url='/login/')
def search_result(request,userId,searched):
    if request.method == "POST":
        result = request.POST['searched']
        find_user = single_author.objects.filter(username = result)
        return render(request, 'search_result.html',{'userId':userId,
                                                    'searched':result, 
                                                    'searchResult':find_user})
    else:
        result = searched
        find_user = single_author.objects.filter(username = result)
        return render(request, 'search_result.html',{'userId':userId,'searched':result,'searchResult':find_user})


@login_required(login_url='/login/')
def my_inbox(request,userId):
    currentAuthor=single_author.objects.get(uuid=userId)
    
    if not Inbox.objects.filter(author=currentAuthor).exists():
        myInbox = Inbox.objects.create(author=currentAuthor,items=None)
        myInbox.save()
    
    all_author_posts = Post.objects.filter(uuid=userId)
    
    #currentAuthorInbox = Inbox.objects.get(author=currentAuthor)
    # bugs here
    currentAuthorInbox =  Inbox.objects.update(author=currentAuthor,items=all_author_posts)
    #currentAuthorInbox.save()
    # currentAuthorInbox = Inbox.objects.get(author=currentAuthor)
    # for post in currentAuthorInbox.items:
    #     postId = post.id
    #     all_likes_from_this_post = Like.objects.filter(object=postId)
    return render(request, 'inbox/inbox.html',{
        # "currentAuthorInbox": currentAuthorInbox,
        "userId": userId,
        # "all_likes_from_this_post": all_likes_from_this_post,
    })
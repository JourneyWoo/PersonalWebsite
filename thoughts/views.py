from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import ThoughtsPost
import markdown
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ThoughtsPostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from comment.models import Comment
from .models import ThoughtsColumn
from comment.forms import CommentForm


def thoughts_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    # tag = request.GET.get('tag')

    thoughts_list = ThoughtsPost.objects.all()

    if search:
        thoughts_list = thoughts_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search = ''

    # if column is not None and column.isdigit():
    #     thoughts_list = thoughts_list.filter(column=column)

    # if tag and tag != 'None':
    #     thoughts_list = thoughts_list.filter(tags__name__in=[tag])

    if order == 'total_views':
        thoughts_list = thoughts_list.order_by('-total_views')

    paginator = Paginator(thoughts_list, 10)
    page = request.GET.get('page')
    thoughts = paginator.get_page(page)

    context = {
        'thoughts': thoughts,
        'order': order,
        'search': search,
        # 'column': column,
        # 'tag': tag,
    }

    return render(request, 'thoughts/list.html', context)


def thoughts_detail(request, id):
    thoughts = ThoughtsPost.objects.get(id=id)
    # comments = Comment.objects.filter(thoughts=id)
    # comment_form = CommentForm()
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    # thoughts.body = md.convert(thoughts.body)

    # context = {'thoughts': thoughts, 'toc': md.toc, 'comments': comments, 'comment_form': comment_form,}
    context = {'thoughts': thoughts, 'toc': md.toc,}
    thoughts.total_views += 1
    thoughts.save(update_fields=['total_views'])

    return render(request, 'thoughts/detail.html', context)


def thoughts_create(request):
    if request.method == "POST":
        thoughts_post_form = ThoughtsPostForm(request.POST, request.FILES)
        if thoughts_post_form.is_valid():
            new_thoughts = thoughts_post_form.save(commit=False)
            new_thoughts.author = User.objects.get(id=request.user.id)
            if request.POST['column'] != 'none':
                new_thoughts.column = ThoughtsColumn.objects.get(id=request.POST['column'])
            new_thoughts.save()
            thoughts_post_form.save_m2m()
            return redirect("thoughts:thoughts_list")
        else:
            return HttpResponse("Form ERROR, please rewrite this form.")
    else:
        thoughts_post_form = ThoughtsPostForm()
        # columns = ThoughtsColumn.objects.all()
        # context = { 'thoughts_post_form': thoughts_post_form, 'columns': columns }
        context = {'thoughts_post_form': thoughts_post_form}
        return render(request, 'thoughts/create.html', context)


@login_required(login_url='/userprofile/login/')
def thoughts_delete(request, id):
    thoughts = ThoughtsPost.objects.get(id=id)
    if request.user != thoughts.author:
        return HttpResponse("Sorry, you don't have the permission to delete this thoughts.")
        thoughts.delete()
    return redirect("thoughts:thoughts_list")


@login_required(login_url='/userprofile/login/')
def thoughts_update(request, id):
    thoughts = ThoughtsPost.objects.get(id=id)
    if request.user != thoughts.author:
        return HttpResponse("Sorry, you don't have the permission to edit this blog.")
    if request.method == "POST":
        thoughts_post_form = ThoughtsPostForm(data=request.POST)
        if thoughts_post_form.is_valid():
            thoughts.title = request.POST['title']
            # thoughts.body = request.POST['body']
            # if request.POST['column'] != 'none':
            #     thoughts.column = ThoughtsColumn.objects.get(id=request.POST['column'])
            # else:
            #     thoughts.column = None
            #     thoughts.save()
            return redirect("thoughts:thoughts_detail", id=id)
        else:
            return HttpResponse("Form Wrong, please re fill")

    else:
        thoughts_post_form = ThoughtsPostForm()
        # columns = ThoughtsColumn.objects.all()
        context = {
            'thoughts': thoughts,
            'thoughts_post_form': thoughts_post_form,
            # 'columns': columns,
        }
        return render(request, 'thoughts/update.html', context)
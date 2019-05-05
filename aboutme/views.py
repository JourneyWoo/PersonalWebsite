from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from .forms import FriendForm
from .utils import PageLinksMixin
from .models import (
    Friend,
)


class FriendList(PageLinksMixin, ListView):
    paginate_by = 100
    model = Friend


class FriendDetail(View):
    def get(self, request, pk):
        friend = get_object_or_404(
            Friend,
            pk=pk
        )

        return render(
            request,
            'aboutme/friend_detail.html',
            {'friend': friend}
        )


class FriendCreate(CreateView):
    form_class =FriendForm
    model = Friend


class FriendUpdate(UpdateView):
    form_class = FriendForm
    model = Friend
    template_name = 'aboutme/friend_form_update.html'


class FriendDelete(View):
    def get(self, request, pk):
        friend = self.get_object(pk)
        return render(
            request,
            'aboutme/friend_confirm_delete.html',
            {'friend': friend}
        )

    def get_object(self, pk):
        friend = get_object_or_404(
            Friend,
            pk=pk
        )
        return friend

    def post(self, request, pk):
        friend = self.get_object(pk)
        friend.delete()
        return redirect('aboutme:friend_list_urlpattern')

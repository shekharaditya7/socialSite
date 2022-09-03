from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from groups.models import Group, GroupMember
# Create your views here.
from django.views.generic.base import RedirectView
from django.db import IntegrityError
from . import models


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
            return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug = self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Already a Member')
        else:
            messages.success(self.request, 'You are Now A Member')

        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
            return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug = self.kwargs.get('slug'))

        try:
            membership = models.GroupMember.objects.filter(user=self.request.user,
            group__slug=self.kwargs.get('slug')).get()

        except models.GroupMemberDoesNotExist:
            messages.warning(self.request, "you aren't a Member")
        else:
            membership.delete()
            messages.success(self.request, 'You Left!')

        return super().get(request, *args, **kwargs)

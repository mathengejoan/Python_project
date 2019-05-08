from django.shortcuts import render
from .models import Member
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
# Create your views here.


class MemberListView(ListView):
    model = Member
    template_name = 'new/index.html'
    context_object_name = 'profiles'
    ordering = ['name']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Member.objects.filter(name__icontains=query) | Member.objects.filter(slogan__icontains=query)
        else:
            return Member.objects.all()

class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'


class MemberUpdateView(UpdateView):
    model = Member
    fields = '__all__'

class MemberDeleteView(DeleteView):
    model = Member
    success_url = '/'
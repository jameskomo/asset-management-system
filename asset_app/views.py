from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import Assets
from .filters import AssetsFilter


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'asset_app/home.html', context)

# List Views for Assets

class AssetsListView(ListView):
    model = Assets
    template_name = 'asset_app/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'assets'
    ordering = ['-date_purchased']


# Detail Views for Assets
class AssetsDetailView(DetailView):
    model = Assets

# Create Views for Assets
class AssetsCreateView(LoginRequiredMixin, CreateView):
    model = Assets
    fields = ['asset_name', 'asset_serial_No', 'asset_manufacturer', 'asset_issued', 'asset_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update Class Views for Assets

class AssetsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Assets
    fields = ['asset_name', 'asset_serial_No', 'asset_manufacturer', 'asset_issued', 'asset_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        assets = self.get_object()
        if self.request.user == asset_assignee:
            return True
        return False


# Delete Class Views for Assets
class AssetsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Assets
    success_url = '/'

    def test_func(self):
        assets = self.get_object()
        if self.request.user == assets.asset_assignee:
            return True
        return False

def about(request):
    return render(request, 'asset_app/about.html', {'title': 'About'})


# Searching Assets


def assetssearch(request):
    assets_list = Assets.objects.all()
    assets_filter = AssetsFilter(request.GET, queryset=assets_list)
    return render(request, 'asset_app/assets-search.html', {'filter': assets_filter})
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
from .models import Post, Neighborhood, Business, Contact
from .filters import ContactFilter, NeighborhoodFilter, BusinessFilter


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'asset_app/home.html', context)

# List Views for Post, Business, Neighborhood and Contact

class PostListView(ListView):
    model = Post
    template_name = 'asset_app/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class NeighborhoodListView(ListView):
    model = Neighborhood
    template_name = 'asset_app/neighborhood_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'neighborhoods'
    ordering = ['neighborhood_name']
    
class BusinessListView(ListView):
    model = Business
    template_name = 'asset_app/business_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'businesses'
    ordering = ['business_name']

class ContactListView(ListView):
    model = Contact
    template_name = 'asset_app/contact_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'contacts'
    ordering = ['contact_name']

# Detail Views for Post, Business, Neighborhood and Contact
class PostDetailView(DetailView):
    model = Post

class NeighborhoodDetailView(DetailView):
    model = Neighborhood

class BusinessDetailView(DetailView):
    model = Business

class ContactDetailView(DetailView):
    model = Contact

# Create Views for Post, Business, Neighborhood and Contact
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NeighborhoodCreateView(LoginRequiredMixin, CreateView):
    model = Neighborhood
    fields = ['neighborhood_name', 'neighborhood_location', 'occupants_count', 'neighborhood_image']

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['business_name', 'business_location', 'business_email', 'business_description', 'business_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['contact_name', 'contact_email', 'contact_number', 'contact_address', 'contact_logo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update Class Views for Post, Business, Neighborhood and Contact

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class NeighborhoodUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Neighborhood
    fields = ['neighborhood_name', 'neighborhood_location', 'occupants_count', 'neighborhood_image']

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)

    def test_func(self):
        neighborhood = self.get_object()
        if self.request.user == neighborhood.admin:
            return True
        return False

class BusinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Business
    fields = ['business_name', 'business_location', 'business_email', 'business_description', 'business_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.user:
            return True
        return False

class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['contact_name', 'contact_email', 'contact_number', 'contact_address', 'contact_logo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object() 
        if self.request.user == contact.user:
            return True
        return False

# Delete Class Views for Post, Business, Neighborhood and Contact
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business
    success_url = '/'

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.user:
            return True
        return False

class NeighborhoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Neighborhood
    success_url = '/'

    def test_func(self):
        neighborhood = self.get_object()
        if self.request.user == neighborhood.admin:
            return True
        return False

class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.user:
            return True
        return False

def about(request):
    return render(request, 'asset_app/about.html', {'title': 'About'})


# Searching Models


def contactsearch(request):
    contact_list = Contact.objects.all()
    contact_filter = ContactFilter(request.GET, queryset=contact_list)
    return render(request, 'asset_app/contact-search.html', {'filter': contact_filter})

def businesssearch(request):
    business_list = Business.objects.all()
    business_filter = BusinessFilter(request.GET, queryset=business_list)
    return render(request, 'asset_app/business-search.html', {'filter': business_filter})

def neighborhoodsearch(request):
    neighborhood_list = Neighborhood.objects.all()
    neighborhood_filter = NeighborhoodFilter(request.GET, queryset=neighborhood_list)
    return render(request, 'asset_app/neighborhood-search.html', {'filter': neighborhood_filter})
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from . models import Post


def home(request):
	context = {
		'posts': Post.objects.all(),
	}
	return render(request,"blog/home.html",context)

def Approve(request):
	approved = 'true'

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = {'-Date_Of_Delivery'}


class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post	
	fields = ['Plant_Model', 'Customer_Name', 'Pre_Order_Sheet_No', 'Random_Key']

	def form_valid(self, form):
		form.instance.Sales_Persons_Name = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post	
	fields = ['Plant_Model', 'Customer_Name', 'Pre_Order_Sheet_No', 'Random_Key']

	def form_valid(self, form):
		form.instance.Sales_Persons_Name = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Sales_Persons_Name or 'AnkurJain':
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Sales_Persons_Name or 'AnkurJain':
			return True
		return False				


class PostApprovedView(DetailView):
	model = Post	
		

def about(request):
	return render(request,"blog/about.html", {'title': 'about'})
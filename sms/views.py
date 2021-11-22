from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, JsonResponse
from.models import Cordinator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .serializers import CordSerializer

# @login_required #used for function based view
def home(request):
	return render(request, 'base.html')

class AddCord(LoginRequiredMixin, CreateView):  #LoginRequiredMixins used for class based view
	model = Cordinator
	template_name = 'add_cord.html'
	# context_object_name=
	fields = '__all__'
	success_url = reverse_lazy('list_cord')
	login_url = reverse_lazy('login')

class DetailCord(LoginRequiredMixin, DetailView):
	model = Cordinator
	template_name = 'detail_cord.html'
	context_object_name= 'cord'
	login_url = reverse_lazy('login')


class DelCord(LoginRequiredMixin, DeleteView):
	model = Cordinator
	success_url = reverse_lazy('list_cord')
	login_url = reverse_lazy('login')



class ListCord(LoginRequiredMixin, ListView):
	model = Cordinator
	template_name = 'list_cord.html'
	context_object_name = 'list_cord'
	login_url = reverse_lazy('login')



class UpdateCord(LoginRequiredMixin, UpdateView):
	model = Cordinator
	template_name= 'update_cord.html'
	fields = '__all__'
	success_url = reverse_lazy('list_cord')
	login_url = reverse_lazy('login')





class LoginView(View):
	def get(self, request):
		form = LoginForm()
		return render(request, 'login.html', {'form':form})

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return redirect('list_cord')
			else:
				return HttpResponse('You are  active.')
		else:
			return HttpResponse('You are not a valid user')
				



    
class LogoutView(View):
	def get(self, request):
		logout(request)
		return redirect('login')


class RegisterView(View):
	def get(self, request):
		form= RegisterForm()
		return render(request, 'register.html',{'form':form})

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(request.POST['password'])
			user.save()
			login(request,user)
			return redirect('list_cord')
		else:
			return render(request, 'register.html', {'form':form})


class APICord(View):
	def get(self, request):
		cord = Cordinator.objects.all()
		seri_cord = CordSerializer(cord, many=True)
		return JsonResponse(seri_cord.data, safe=False)
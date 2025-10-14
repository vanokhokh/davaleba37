from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from user.forms import Userform, Profileform
from user.models import Profile


class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('shop:home')

class Logout(LogoutView):
    next_page = reverse_lazy('user:login')


class Registration(CreateView):
    model = User
    form_class = Userform
    template_name = 'registration.html'
    success_url = reverse_lazy('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['profile_form'] = Profileform(self.request.POST)
        else:
            context['profile_form'] = Profileform()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']

        if profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class Userprofile(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request):
        user_form = Userform(instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = Profileform(instance=profile)
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = Userform(request.POST, instance=request.user)
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = Profileform(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user:profile')
        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})







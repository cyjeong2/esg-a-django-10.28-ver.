from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

login = LoginView.as_view(
    template_name="accounts/login_form.html",
)
logout = LogoutView.as_view(
    nex_page="/accounts/login/",
)
@login_required
def profile(request):

    return render(request, "accounts/profile.html")

signup = CreateView.as_view(
    form_class=UserCreationForm,
    success_url="/accounts/login/",
    template_name = "accounts/signup_form.html",
)



from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm, JobForm, SignupForm

# Signup view
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from .models import Vacancy
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Signup successful. You are now logged in.")
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "website/account/signup.html", {"form": form})


class HomeView(TemplateView):
    template_name = "website/pages/home.html"


class JobsView(ListView):
    model = Vacancy
    template_name = "website/pages/jobs.html"
    context_object_name = "vacancies"

    def get_queryset(self):
        return Vacancy.objects.filter(is_active=True).order_by("-publish_date")


class CandidateView(TemplateView):
    template_name = "website/pages/candidate.html"


class JobDetailView(DetailView):
    model = Vacancy
    template_name = "website/pages/job_single.html"
    context_object_name = "vacancy"
    pk_url_kwarg = "id"

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class ElementsView(TemplateView):
    template_name = "website/pages/elements.html"


class AboutView(TemplateView):
    template_name = "website/pages/about.html"


class BlogView(TemplateView):
    template_name = "website/pages/blog.html"


class SingleBlogView(TemplateView):
    template_name = "website/pages/single-blog.html"


class ContactView(TemplateView):
    template_name = "website/pages/contact.html"


class CustomLoginView(LoginView):
    template_name = "website/account/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class CustomLogoutView(LogoutView):
    template_name = "website/account/logout.html"
    next_page = reverse_lazy("home")


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vacancy
    template_name = "website/pages/job_confirm_delete.html"
    success_url = reverse_lazy("jobs")

    def test_func(self):
        return self.request.user.is_staff


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    form_class = JobForm
    template_name = "website/pages/job_add.html"
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class JobEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vacancy
    form_class = JobForm
    template_name = "website/pages/job_edit.html"
    context_object_name = "form"
    pk_url_kwarg = "pk"

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy("job_single", kwargs={"id": self.get_object().pk})


# /search
# def search_results(request: HttpRequest) -> HttpResponse:
#     results = None

#     query = request.GET.get("q")
#     if query:
#         results = Product.objects.filter(title__icontains=query)
#     else:
#         results = Product.objects.none()

#     return render(
#         request, "website/pages/search_results.html", {"results": results, "query": query}
#     )


# ? error pages
# /404
# def not_found_404(
#     request: HttpRequest, exception: Optional[Exception] = None
# ) -> HttpResponse:
#     return render(request, "website/pages/404.html", status=404)


# # /preview-404
# def preview_404(request: HttpRequest) -> HttpResponse:
#     return not_found_404(request)

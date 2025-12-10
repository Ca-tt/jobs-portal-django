from django.contrib import admin


from django.urls import path, include
from django.conf import settings
from website.views import *


urlpatterns = [
    # pages
    path("signup/", signup, name="signup"),
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("jobs/", JobsView.as_view(), name="jobs"),
    path("job_single/<int:id>/", JobDetailView.as_view(), name="job_single"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("single-blog/", SingleBlogView.as_view(), name="single_blog"),
    path("elements/", ElementsView.as_view(), name="elements"),
    path("candidate/", CandidateView.as_view(), name="candidate"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("delete_job/<int:pk>/", JobDeleteView.as_view(), name="delete_job"),
    path("edit_job/<int:pk>/", JobEditView.as_view(), name="edit_job"),
    # path("search/", page_views.search_results, name="search_results"),
    # path("products/", product_views.products, name="products"),
    # path("products/<slug:slug>/", product_views.single_product, name="product_single"),
    # path("profile/", profile_views.profile, name="profile"),
    # path("preview-404/", page_views.preview_404, name="preview-404"),
]

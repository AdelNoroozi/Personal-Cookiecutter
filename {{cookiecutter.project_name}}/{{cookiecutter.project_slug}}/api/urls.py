from django.urls import path, include

urlpatterns = [
    path('users/', include('{{cookiecutter.project_slug}}.users.urls')),
    path('auth/', include('{{cookiecutter.project_slug}}.authentication.urls')),
]

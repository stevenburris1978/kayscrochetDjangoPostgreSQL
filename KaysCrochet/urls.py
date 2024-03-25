"""
URL configuration for KaysCrochet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import logging
from django.http import HttpResponseServerError

# Create a logger for this module
logger = logging.getLogger(__name__)

urlpatterns = [
    path("", include("kayscrochetapp.urls")),
    path("admin/", admin.site.urls),
    path("", include("pwa.urls")),
]


def handler500(request, *args, **argv):
    # Log an error if a 500 error occurs
    logger.error("An error occurred: Internal Server Error")

    # You can customize the log message and log level based on your needs.

    # Return an error response or handle it as needed
    return HttpResponseServerError("An error occurred. Please try again later.")
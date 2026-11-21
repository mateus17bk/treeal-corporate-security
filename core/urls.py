from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('corporate_intel.urls')),
]

handler404 = 'corporate_intel.views.custom_page_not_found_view'

from django.contrib import admin
from django.urls import path, include

import store


urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),

]

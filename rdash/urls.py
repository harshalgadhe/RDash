from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('', include('authentication.urls'))
]

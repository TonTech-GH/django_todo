from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # どんなURLでも受付ける(この場合は上記 admin/ 以外の全てとなる)
    path('', include('todo.urls'))
]

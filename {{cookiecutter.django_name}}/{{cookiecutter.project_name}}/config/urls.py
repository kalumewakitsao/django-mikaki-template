from django.contrib import admin
from django.urls import include, path

# from chama.common.urls import router as common_router

urlpatterns = [
    path('authy/', include('rest_framework.urls')),
    # path('common/', include(common_router.urls)),
]

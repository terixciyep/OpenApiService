from django.urls import path, include
from rest_framework.routers import SimpleRouter

from openapi.views import FilesViewSet, AllowedHTTPMethodsViewSet, FileDetailAPIView

router = SimpleRouter()
router.register(r'file', FilesViewSet, basename='files')
router.register(r'add_methods', AllowedHTTPMethodsViewSet, basename='methods')

urlpatterns = [
    path('file_detail/<int:pk>', FileDetailAPIView.as_view(), name='FileDetailView'),
    path('', include(router.urls),
)
]
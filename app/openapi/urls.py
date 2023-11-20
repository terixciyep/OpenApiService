from django.urls import path, include
from rest_framework.routers import SimpleRouter

from openapi.views import FilesViewSet, AllowedHTTPMethodsViewSet, FileDetailAPIView

router = SimpleRouter()
router.register(r'file', FilesViewSet, basename='files')
router.register(r'add_methods', AllowedHTTPMethodsViewSet, basename='methods')

urlpatterns = [
    path('methods/<int:pk>', FileDetailAPIView.as_view(), name='methodsView'),
    path('', include(router.urls),
)
]
from django.urls import include, path
from rest_framework import routers
from server.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('markers/', views.handle_markers_request, name='handle-markers-request'),
    path('markers/<int:pk>', views.handle_markers_request, name='handle-markers-request'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views




# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cart', views.CartViewSet)
# router.register(r'cart\delete_cart', views.CartViewSet.delete_cart)
router.register(r'course', views.CourseViewSet)
router.register(r'user/course', views.UserCoursesViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
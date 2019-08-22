from rest_framework import routers
from .views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
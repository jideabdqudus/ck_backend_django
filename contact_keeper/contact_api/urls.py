from rest_framework import routers
from .views import ContactViewSet

router = routers.DefaultRouter()
router.register('api/contacts', ContactViewSet, 'contacts')

urlpatterns = router.urls
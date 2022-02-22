from django.urls import include, path 
from . import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'options', views.OptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('create', views.createTest, name='create'),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
    # path('edit/<int:test_id>', views.edit, name='edit'),
    # path('show/<int:id>',views.show),
    # path('update/<int:test_id>',views.update, name='update'),
    # path('delete/<int:test_id>',views.destroy, name='delete'),
]

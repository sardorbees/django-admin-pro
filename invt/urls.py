from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, CategoryViewSet,
    PowerViewSet, ProductTypeViewSet, BrandViewSet, ProductList,
    SolarPanelListView
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register('power', PowerViewSet, basename='power')
router.register('producttype', ProductTypeViewSet, basename='producttype')
router.register('categories', CategoryViewSet)
router.register('brand', BrandViewSet, basename='brand')

extra_urls = [
    path('products-list/', ProductList.as_view(), name='product-list'),
    path('api/products-page/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('solar-panels/', SolarPanelListView.as_view(), name='solar-panel-list'),
]

urlpatterns = router.urls + extra_urls

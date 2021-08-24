from django.urls import path

from .api_views import CategoryAPIView,SmartphoneListAPI,NotebookListAPI,\
    SmartphoneDetailAPIView,CustomersListAPIView,NotebookDetailAPIView
urlpatterns=[
    path('categories/',CategoryAPIView.as_view(),name='categories_list'),
    path('customers/',CustomersListAPIView.as_view(),name='customers_list'),
    path('smartphones/',SmartphoneListAPI.as_view(),name='smartphones_list'),
    path('notebooks/',NotebookListAPI.as_view(),name='notebooks_list'),
    path('smartphones/<str:id>/',SmartphoneDetailAPIView.as_view(),name='smartphone_detail'),
    path('notebooks/<str:id>/',NotebookDetailAPIView.as_view(),name='notebooks_detail'),
]
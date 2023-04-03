from django.contrib import path
from .views import PackageView,SubscriptionView
urlpatterns = [
    path('packages/',PackageView.as_view())
    path('subscriptions/',SubscriptionView.as_view())
]

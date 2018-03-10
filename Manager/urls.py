from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^goods_manager?', 'Manager.views.goods_manager'),
    url(r'^orders_manage', 'Manager.views.orders_manage'),
    url(r'^manager_info', 'Manager.views.manager_info'),
    url(r'^manager_logout/', 'User.views.manager_logout'),
    # url(r'^manager_logout/', 'User.views.manager_logout'),
    url(r'^redirect_to_goods_manager_page/$',
        RedirectView.as_view(url='/Manager/goods_manager', permanent=False)),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

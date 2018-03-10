from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'SportShop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home_page', 'Goods.views.home_page'),
    url(r'^goods_detail', 'Goods.views.goods_detail'),
    url(r'^goods_list', 'Goods.views.goods_list'),
    url(r'^search', 'Goods.views.search'),
    url(r'^add_to_cart', 'Goods.views.add_to_cart'),
    url(r'^remove_from_cart', 'Goods.views.remove_from_cart'),
    url(r'^cancel_order', 'Goods.views.cancel_order'),
    url(r'^cart', 'Goods.views.cart'),
    url(r'^createOrder', 'Goods.views.createOrder'),
    url(r'^order_success', 'Goods.views.order_success'),
    url(r'^editInfo', 'Goods.views.editInfo'),
    url(r'^order', 'Goods.views.order'),
    url(r'^logout', 'User.views.logout'),
    url(r'^redirect_to_login_page/$',
        RedirectView.as_view(url='/User/login_page', permanent=False)),
    url(r'^redirect_to_goods_detail_page/$',
        RedirectView.as_view(url='/User/index_page', permanent=False)),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'FoodsShop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^User/', include('User.urls')),
    url(r'^Goods/', include('Goods.urls')),
    url(r'^Manager/', include('Manager.urls')),

]

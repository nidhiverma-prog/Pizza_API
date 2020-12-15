from django.conf.urls import url
from pizza_app.views import pizza_list,pizza_detail

urlpatterns = [
    url('pizza/',pizza_list),
    url('detail/(?P<pk>[0-9]+)',pizza_detail),

]
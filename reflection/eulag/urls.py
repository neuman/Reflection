from django.conf.urls import include, url
from sitegate.decorators import redirect_signedin, sitegate_view
import eulag.views

urlpatterns = [
    url(r'sign/$', eulag.views.SignView.as_view(), name="sign"),
]

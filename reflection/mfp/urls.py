from django.conf.urls import include, url
from sitegate.decorators import redirect_signedin, sitegate_view
import views as v
#from api import urls as api_urls

urlpatterns = [
    url(r'vis/', v.VisView.as_view(), name="vis"),

]

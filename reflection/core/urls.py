from django.conf.urls import include, url
from sitegate.decorators import redirect_signedin, sitegate_view
import core.views as cv
#from api import urls as api_urls

urlpatterns = [
    #url(r'api/', include(api_urls)),

]

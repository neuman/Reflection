from django.conf.urls import include, url
from sitegate.decorators import redirect_signedin, sitegate_view
import hello.views

urlpatterns = [
    url(r'entrance/$', hello.views.entrance, name="entrance"),
    url(r'guide/$', hello.views.GuideView.as_view(), name="guide"),
    url(r'selfanalysis/$', hello.views.SelfAnalysisView.as_view(), name="selfanalysis"),
    url(r'dashboard/$', hello.views.DashboardView.as_view(), name="dashboard")
]

from django.conf.urls import patterns, include, url
from django.contrib import admin
from tally_sheet.views import PublicView
from tally_sheet.api import PublicTallyApiView, AddTallyApiView, ChangeBalanceApiView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', PublicView.as_view(), name="public"),
                       url(r'^public/$', PublicView.as_view(), name="public"),

                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
                           name="login"),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'},
                           name="logout"),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'api/public/$', PublicTallyApiView.as_view(), name="public-api"),
                       url(r'api/tally/add/$', AddTallyApiView.as_view(), name="add-tally-api"),
                       url(r'api/balance/change/$', ChangeBalanceApiView.as_view(), name="change-balance-api")
)

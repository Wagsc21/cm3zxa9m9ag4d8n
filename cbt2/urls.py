from django.conf.urls import url



urlpaatterns=[
    url(r'^login/$', 'cbt2.views.login'),
    url(r'^auth/$', 'cbt2.views.auth_view'),
    url(r'^logout/$', 'cbt2.views.logout'),
    url(r'^loggedin/$', 'cbt2.views.loggedin'),
    url(r'^invalid/$', 'cbt2.views.invalid_login'),
        


]
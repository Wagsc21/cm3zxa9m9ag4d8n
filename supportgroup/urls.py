from django.conf.urls import url
#from forum import views
#from forum.api import QueryResource

#query_resource = QueryResource()

urlpatterns = [
	url(r'^home/$','supportgroup.views.home',name='home'),
        url(r'^home/create/$','supportgroup.views.create',name='create'),
        url(r'^home/queries/all/$','supportgroup.views.queries',name='queries'),
        url(r'^home/queries/(?P<query_id>[0-9]+)/$','supportgroup.views.query',name='query'),
        url(r'^home/queries/upvote/(?P<query_id>[0-9]+)/$','supportgroup.views.upvote',name='upvote'),
        url(r'^home/queries/downvote/(?P<query_id>[0-9]+)/$','supportgroup.views.downvote',name='downvote'),
        url(r'^home/queries/add_comment/(?P<query_id>[0-9]+)/$','supportgroup.views.comment',name='comment'),
        url(r'^home/queries/upvotes/(?P<query_id>[0-9]+)/(?P<comment_id>[0-9]+)/$','supportgroup.views.upvote',name='upvote'),
        url(r'^home/queries/downvotes/(?P<query_id>[0-9]+)/(?P<comment_id>[0-9]+)/$','supportgroup.views.downvote',name='downvote'),
        url(r'^home/notifications/$','supportgroup.views.notifications',name='notifications'),
        url(r'^home/latest/$','supportgroup.views.latest',name='latest'),
	#url(r'^home/queries/search/$',views.search_titles,name='search'),
	#url(r'^api/',include(query_resource.urls)),		
]


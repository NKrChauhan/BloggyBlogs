from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path,include
from .views import ( PostListView,
                     AboutView,
                     CreatePostView,
                     PostDetailView,
                     add_comment,
                     UpdatePostView,
                     DraftView,
                     index,
                     comment_remove,
                     DeletePostView,
                     approve_comment,
                     publish_post,
                    )
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^list/',PostListView.as_view(),name='post_list'),
    url(r'^about_page/$',AboutView.as_view(),name='about'),
    url(r'^NewPost/(?P<pk>\d+)/$',CreatePostView.as_view(),name='post_create'),
    url(r'^post/(?P<pk>\d+)/edit/$',UpdatePostView.as_view(),name='post_update'),
    url(r'post/(?P<pk>\d+)/$',PostDetailView.as_view(),name='post_detail'),
    url(r'post/(?P<pk>\d+)/delete$',DeletePostView.as_view(),name='post_delete'),
    url(r'draft/$',DraftView.as_view(),name='draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',add_comment,name='add_comment'),
    url(r'comment/(?P<pk>\d+)/approve/$',approve_comment,name='approve_comment'),
    url(r'comment/(?P<pk>\d+)/delete$',comment_remove,name='comment_remove'),
    url(r'post/(?P<pk>\d+)/publish$',publish_post,name='publish_post'),
    url(r'^logout/',views.LogoutView.as_view(),name='logout',kwargs={'next_page':'blog/post_list'}),
    url(r'^login/',views.LoginView.as_view(),name='login'),
    path('admin/', admin.site.urls),


]

from django.conf.urls import patterns, url
from premises.views import (ContentionDetailView, HomeView,
                            ArgumentCreationView, PremiseCreationView,
                            PremiseDeleteView, ContentionJsonView,
                            PremiseEditView, ArgumentUpdateView,
                            ArgumentPublishView, ArgumentUnpublishView,
                            ArgumentDeleteView, AboutView, NewsView,
                            UpdatedArgumentsView, ReportView, ControversialArgumentsView, TosView, SearchView)


urlpatterns = patterns('',
   url(r'^$', HomeView.as_view(), name='home'),
   url(r'^news$', NewsView.as_view(),
       name='contentions_latest'),
   url(r'^search', SearchView.as_view(),
       name='contentions_search'),
   url(r'^updated$', UpdatedArgumentsView.as_view(),
       name='contentions_updated'),
   url(r'^controversial', ControversialArgumentsView.as_view(),
       name='contentions_controversial'),
   url(r'^about$',
       AboutView.as_view(),
       name='about'),
   url(r'^report$',
       ReportView.as_view(),
       name='report'),
   url(r'^tos$',
       TosView.as_view(),
       name='tos'),
   url(r'^new-argument$',
       ArgumentCreationView.as_view(),
       name='new_argument'),
   url(r'^(?P<slug>[\w-]+)/edit$',
        ArgumentUpdateView.as_view(),
        name='contention_edit'),
   url(r'^(?P<slug>[\w-]+)\.json$',
        ContentionJsonView.as_view(),
        name='contention_detail_json'),
   url(r'^(?P<slug>[\w-]+)$',
        ContentionDetailView.as_view(),
        name='contention_detail'),
   url(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/delete',
        PremiseDeleteView.as_view(),
        name='delete_premise'),
   url(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)/new',
        PremiseCreationView.as_view(),
        name='insert_premise'),
   url(r'^(?P<slug>[\w-]+)/premises/(?P<pk>[0-9]+)',
        PremiseEditView.as_view(),
        name='edit_premise'),
   url(r'^(?P<slug>[\w-]+)/premises/new',
        PremiseCreationView.as_view(),
        name='new_premise'),
    url(r'^(?P<slug>[\w-]+)/publish',
        ArgumentPublishView.as_view(),
        name='contention_publish'),
    url(r'^(?P<slug>[\w-]+)/unpublish',
        ArgumentUnpublishView.as_view(),
        name='contention_unpublish'),
    url(r'^(?P<slug>[\w-]+)/delete',
        ArgumentDeleteView.as_view(),
        name='contention_delete'),
)

"""
Class-based, modern views for elephantblog
==========================================

Use one of those two::

    def elephantblog_entry_url(self):
        from django.core.urlresolvers import reverse
        return reverse('elephantblog_entry_detail', kwargs={
            'year': self.published_on.strftime('%Y'),
            'month': self.published_on.strftime('%m'),
            'day': self.published_on.strftime('%d'),
            'slug': self.slug,
            })

    def elephantblog_category_url(self):
        from django.core.urlresolvers import reverse
        return reverse('elephantblog_category_detail', kwargs={
            'slug': self.translation.slug,
            })

    def elephantblog_entry_url_app(self):
        from feincms.content.application.models import app_reverse
        return app_reverse('elephantblog_entry_detail', 'elephantblog', kwargs={
            'year': self.published_on.strftime('%Y'),
            'month': self.published_on.strftime('%m'),
            'day': self.published_on.strftime('%d'),
            'slug': self.slug,
            })

    def elephantblog_category_url_app(self):
        from feincms.content.application.models import app_reverse
        return app_reverse('elephantblog_category_detail', 'elephantblog', kwargs={
            'slug': self.translation.slug,
            })

    ABSOLUTE_URL_OVERRIDES = {
        'elephantblog.entry': elephantblog_entry_url, # OR elephantblog_entry_url_app,
        'elephantblog.category': elephantblog_category_url, # OR elephantblog_category_url_app,
    }


NOTE! You need to register the app as follows for the application content snippet::

    Page.create_content_type(ApplicationContent, APPLICATIONS=(
        ('elephantblog', _('Blog'), {'url': 'elephantblog.views.cbv.urls'),
        ))

"""

from django.conf.urls.defaults import patterns, include, url

from elephantblog.feeds import EntryFeed
from elephantblog.views.cbv import views


urlpatterns = patterns('elephantblog.views.cbv',
    url(r'^feed/$', EntryFeed()),
    url(r'^$',
        views.ListView.as_view(),
        name='elephantblog_entry_list'),
    url(r'^(?P<year>\d{4})/$',
        views.YearArchiveView.as_view(),
        name='elephantblog_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.MonthArchiveView.as_view(),
        name='elephantblog_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        views.DayArchiveView.as_view(),
        name='elephantblog_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.DateDetailView.as_view(),
        name='elephantblog_entry_detail'),
    url(r'^category/(?P<slug>[-\w]+)/$',
        views.CategoryListView.as_view(),
        name='elephantblog_category_detail'),
)
from django_hosts import patterns, host
from portfolio import settings

host_patterns = patterns('',
        host(r'www', settings.ROOT_URLCONF, name='www'),
        host(r'blog', 'blog.urls', name='blog'),
        )

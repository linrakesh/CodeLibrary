from django.contrib.sitemaps import Sitemap
from .models import code


class CodeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return code.objects.all()

    def lastmode(self, obj):
        return obj.updated_on

from django.shortcuts import render
from django.http import Http404

from dispatch.apps.frontend.themes.default import DefaultTheme

class GuideTheme(DefaultTheme):
    """Theme for the 2016 Ubyssey Guide to UBC."""

    def landing(self, request):
        """The Guide to UBC landing page."""
        return render(request, 'guide/index.html', {})

    def article(self, request, slug=None):
        """Guide article page."""
        try:
            article = self.find_article(request, slug, 'guide')
        except:
            raise Http404('Article could not be found.')

        template_fields = article.get_template_fields()

        try:
            next_a = self.find_article(request, template_fields['next_a'], 'guide')
        except:
            next_a = None

        try:
            next_b = self.find_article(request, template_fields['next_b'], 'guide')
        except:
            next_b = None

        article.add_view()

        context = {
            'title': article.headline,
            'meta': self.get_article_meta(article),
            'article': article,
            'next': [next_a, next_b]
        }

        return render(request, 'guide/article.html', context)
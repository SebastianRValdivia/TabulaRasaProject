from django.views.generic import DetailView
from .models import WikiPage

# Create your views here.
class WikiPageDetailView(DetailView):
    """ Lite detail view of a wiki page
    """

    model = WikiPage
    template_name = 'wiki/wikipage_detail.html'

from django.core.management.base import BaseCommand, CommandError
from core.scrapers import GenericRSSScraper

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        grs = GenericRSSScraper()
        q = grs.scrape_feed('http://www.esquire.com/rss/all.xml')
        q = grs.scrape_feed('http://uploadvr.com/feed/')
        q = grs.scrape_feed('http://espn.go.com/espn/rss/news')
        q = grs.scrape_feed('http://www.popsci.com/syndication/site_default')
        q = grs.scrape_feed('https://www.buzzfeed.com/index.xml')
        q = grs.scrape_feed('http://www.theverge.com/rss/full.xml')
        q = grs.scrape_feed('http://www.forbes.com/real-time/feed2/')
        q = grs.scrape_feed('http://rss.cnn.com/rss/cnn_topstories.rss')
        q = grs.scrape_feed('http://www.polygon.com/rss/index.xml')


import myfitnesspal
import core.models as cm
from django.utils import timezone
from datetime import datetime, timedelta

today = timezone.now()

client = myfitnesspal.Client('eric_neuman')

def store_day(day):
    datum = {}
    datum['meals'] = day.get_as_dict()
    datum['totals'] = day.totals
    datum['goals'] = day.goals
    cm.DataPoint.objects.create(datum=datum, date=day.date)


def scrape_since_last():
    most_recent = cm.get_most_recent_datapoint()
    delta = today - most_recent.created_at
    day_count = delta.days
    scrape_days_back(day_count)

def scrape_days_back(day_count):
    for d in range(day_count):
        date = today - timedelta(days=d)
        day = client.get_date(date.year, date.month, date.day)
        #don't store bad data
        if day.totals != {}:
            store_day(day)

scrape_since_last()

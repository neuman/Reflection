import myfitnesspal
import core.models as cm

from datetime import datetime, timedelta

today = datetime.today()

client = myfitnesspal.Client('eric_neuman')

day = client.get_date(2016, 9, 24)

def store_day(day):
    datum = {}
    datum['meals'] = day.get_as_dict()
    datum['totals'] = day.totals
    datum['goals'] = day.goals
    cm.DataPoint.objects.create(datum=datum, date=day.date)

for d in range(4):
    date = today - timedelta(days=d)
    day = client.get_date(date.year, date.month, date.day)
    store_day(day)
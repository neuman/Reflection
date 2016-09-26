import myfitnesspal

client = myfitnesspal.Client('eric_neuman')

day = client.get_date(2016, 9, 24)
day
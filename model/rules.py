from datetime import date, timedelta

TODAY = date.today()
MIN_AGE = 18
MAX_AGE = 120

MAX_DATE = TODAY - timedelta(days=MIN_AGE * 365)
MIN_DATE = TODAY - timedelta(days=MAX_AGE * 365)

MAX_HEIGHT = 2.50
MIN_HEIGHT = 0.54

MAX_WEIGHT = 635
MIN_WEIGHT = 2
import seasons
from datetime import date, timedelta

def test_get_date():
    assert seasons.get_date("2023-05-22") == date(2023, 5, 22)

def test_get_diff():
    assert seasons.get_diff(date.today(), date.today() + timedelta(days=1)) == -1440
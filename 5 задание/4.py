from datetime import datetime, timedelta
import array
import random

def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def date_differences():
    today = datetime.now()
    five_years_ago = today - timedelta(days=5*365)

    dates = [random_date(five_years_ago, today) for _ in range(10)]
    dates.sort()

    diff_array = array.array('i')

    for i in range(len(dates) - 1):
        delta = dates[i+1] - dates[i]
        days = delta.days
        diff_array.append(days)
        print(f"Разница между {dates[i].strftime('%Y-%m-%d')} и "
              f"{dates[i+1].strftime('%Y-%m-%d')}: {days} дней")

if __name__ == "__main__":
    print("\nЗадание 4:")
    date_differences()
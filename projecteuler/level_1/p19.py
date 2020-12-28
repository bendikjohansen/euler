from functools import reduce

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def counting_sundays():
    months_by_year = [[31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                      for year in range(1901, 2001)]
    months = [month for months in months_by_year for month in months]
    start_of_months = reduce(lambda prev, cur: prev + [cur + prev[-1]], months, [0])
    sundays = [True for day in start_of_months if day % 7 == 0]
    return len(sundays)


if __name__ == "__main__":
    print(counting_sundays())

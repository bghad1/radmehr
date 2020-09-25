from . import jalali
from django.utils import timezone


def persian_number_convert(numbers):
    persian_numbers = {
        '0': '۰',
        '1': '١',
        '2': '٢',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }

    for en_number, fa_number in persian_numbers.items():
        numbers = numbers.replace(en_number, fa_number)

    return numbers


def shamsi_converter(time):
    shamsi_month = [
        'فروردین',
        'اردیبهشت',
        'خرداد',
        'تیر',
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند',
    ]

    time = timezone.localtime(time)

    # time_to_str = f"{time.year} {time.month} {time.day}"
    time_to_str = "{} {} {}".format(time.year, time.month, time.day)
    converted_time_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(converted_time_tuple)
    for index, month in enumerate(shamsi_month):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    converted_time = f"{time_to_list[2]} {time_to_list[1]} {time_to_list[0]}"

    return persian_number_convert(converted_time)

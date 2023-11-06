import datetime

import jpholiday as jph


class TestHoliday1(jph.OriginalHoliday):
    def _is_holiday(self, date):
        if date == datetime.date(2022, 5, 10):
            return True
        return False

    def _is_holiday_name(self, date):
        return '特別休暇1'


class TestHoliday2(jph.OriginalHoliday):
    def _is_holiday(self, date):
        if date == datetime.date(2022, 5, 20):
            return True
        return False

    def _is_holiday_name(self, date):
        return '特別休暇2'


from_day = datetime.date(2022, 5, 1)
to_day = datetime.date(2022, 5, 31)
result = jph.between(from_day, to_day)
print(f'削除前 {from_day.strftime("%Y/%m/%d")}から{to_day.strftime("%Y/%m/%d")}祝日は？:{result}')
for x in result:
    print(x)

jph.OriginalHoliday.unregister(TestHoliday1)
result = jph.between(from_day, to_day)
print(f'削除後 {from_day.strftime("%Y/%m/%d")}から{to_day.strftime("%Y/%m/%d")}祝日は？:{result}')
for x in result:
    print(x)
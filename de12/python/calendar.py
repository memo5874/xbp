import datetime

import jpholiday as jph

#独自の日程を追加
class TestHoliday1(jph.OriginalHoliday):
    def _is_holiday(self, date):
        if date == datetime.date(2023, 11, 23):
            return True
        return False

    def _is_holiday_name(self, date):
        return '振替休日'
class TestHoliday2(jph.OriginalHoliday):
    def _is_holiday(self, date):
        if date == datetime.date(2024, 1, 12):
            return True
        return False

    def _is_holiday_name(self, date):
        return '大学休校※予定'
    #長期休暇の開始と終了の日にちを指定
class longtimeholiday1(jph.OriginalHoliday):
    def _is_holiday(self, date):
        if date.year == 2023 and date.month == 12 and date.day == 23:
            return True
        if date.year == 2024 and date.month == 1 and date.day == 5:
            return True
        return False

    def _is_holiday_name(self, date):
        return "冬休み開始or終了"
class longtimeholiday2(jph.OriginalHoliday):
    def _is_holiday(self, date):
        if date.year == 2024 and date.month == 1 and date.day == 28:
            return True
        if date.year == 2024 and date.month == 4 and date.day == 6:
            return True
        return False

    def _is_holiday_name(self, date):
        return "春休み期間開始or終了"
class longtime3(jph.OriginalHoliday):
    def _is_holiday(self, date):
        if date.year == 2024 and date.month == 1 and date.day == 22:
            return True
        if date.year == 2024 and date.month == 1 and date.day == 27:
            return True
        return False

    def _is_holiday_name(self, date):
        return "テスト期間開始or終了"
#指定する範囲
from_day = datetime.date(2023, 1, 1)
to_day = datetime.date(2024, 4, 20)
result = jph.between(from_day, to_day)
print(f' {from_day.strftime("%Y/%m/%d")}{to_day.strftime("%Y/%m/%d")}:{result}')
import jpholiday
import datetime

class TestHoliday(jpholiday.OriginalHoliday):
    def _is_holiday(self, date):
        if date == datetime.date(2020, 2, 9):
            return True
        return False

    def _is_holiday_name(self, date):
        return '特別休暇'

jpholiday.is_holiday_name(datetime.date(2020, 2, 9))
'特別休暇'

jpholiday.is_holiday(datetime.date(2020, 2, 9))
True
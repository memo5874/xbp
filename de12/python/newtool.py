#時計
import jpholiday
from datetime import datetime
t = datetime.now()
print(t)
#datetimeオブジェクトは日付をyear,month,dayそして時間をhour,minute,second,microsecondで示す
print(t.weekday())
#weekdayは0～6の数字で表され、月～日と対応している
result = jpholiday.year_holidays(2023)
print(result)
#年間の祝日がわかる（使用時はその年の年度に合わせる必要がある）




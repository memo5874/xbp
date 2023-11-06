#時計
import jpholiday as jph
from datetime import datetime
t = datetime.now()
print(t)
#datetimeオブジェクトは日付をyear,month,dayそして時間をhour,minute,second,microsecondで示す
print(t.weekday())
#weekdayは0～6の数字で表され、月～日と対応している
result = jph.year_holidays(2023)
print(result)
#年間の祝日がわかる（使用するときはその年の年度に合わせる必要がある）

  







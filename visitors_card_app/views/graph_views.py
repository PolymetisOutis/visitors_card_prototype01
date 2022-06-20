from django.shortcuts import render
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import calendar
from .. import graph
from ..models import *
import datetime as dt
from django.db.models.functions import TruncDate
from django.db.models import Count

def analysis_index(request):
    today = dt.date.today()
    # 今月
    cm_st = today.replace(day=1)
    nm_st = (today + relativedelta(months=1)).replace(day=1)
    cm_ed = nm_st - timedelta(days=1)
    # 今日から一か月の間の日数で日付を取得
    # date_list = [datetime(2020, 1, 25) + timedelta(days=i) for i in range(10)]
    rm_ed = today - relativedelta(months=1)
    date_list = [today - timedelta(days=i) for i in range(30)]
    print('1か月分の日付時刻取得date_list；', end='')
    print(date_list)
    # 1か月後の日付
    print('1か月後の日付時刻取得；', end='')
    print(rm_ed)
    # 先月
    pm_st = (today - relativedelta(months=1)).replace(day=1)
    pm_ed = cm_st - timedelta(days=1)
    print('これまでの日付取得の様子')
    print('今月：{}～{}'.format(cm_st.strftime('%Y/%m/%d'),cm_ed.strftime('%Y/%m/%d')))
    print('先月：{}～{}'.format(pm_st.strftime('%Y/%m/%d'),pm_ed.strftime('%Y/%m/%d')))
    print(calendar.monthrange(cm_st.year, cm_st.month)[1])
    print('今日の日付取得；', end='')
    print(today)
    print('1か月後の日付取得；', end='')
    print(rm_ed)

    # 期間指定来訪者クエリーセット取得
    qs    = Visitors.objects.filter(date__range=(rm_ed, today)).annotate(visited_date=TruncDate('date')).values('date').annotate(count=Count('pk'))  #モデルクラス(ProductAテーブル)読込
    qs_range    = Visitors.objects.filter(date__range=(rm_ed, today))
    # qs = Visitors.objects.filter(date__lte=today, date__gte=rm_ed)
    print('1か月間期間指定のクエリーセット：', end='')
    print(qs)
    qs_date_list = []
    for i in qs:
        qs_date_list.append(i['date'])
    print('1か月間期間指定のクエリーセットの日付リストqs_date_list：', end='')
    print(qs_date_list)

    """
    x,yのパラメーター代入
    """
    x     = [x for x in reversed(date_list)]           #X軸データ
    print('リストx reversed(date_list)の出力：', end='')
    print(x)
    # y     = [y.Revenue for y in qs]        #Y軸データ

    qs_date_index = []
    for i in qs_date_list:
        if i in x:
            qs_date_index.append(x.index(i))
    print('qs_date_index：', end='')
    print(qs_date_index)

    y = []
    for i in x:
        if i in qs_date_list:
            print(dir(qs_range))
            qs_per_date = qs_range.filter(date=i)
            y.append(len(qs_per_date))
        else:
            y.append(0)

    print('qs_per_date：', end='')
    print(qs_per_date)
    print(y)
    chart = graph.Plot_Graph(x,y)          #グラフ作成
    
    total = len(qs_range)
    context= {
        'chart': chart,
        'total': total,
    }

    return render(request, 'visitors_card_app/analysis/analysis_index.html', context)
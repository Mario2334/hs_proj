from django.shortcuts import render, render_to_response, HttpResponse
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from django.template import Context, Template


# import pandas_datareader.data as web
# Create your views here.


def rendergraph(request):
    style.use('ggplot')

    start = dt.datetime(2015, 1, 1)
    end = dt.datetime.now()

    # # df = web.DataReader("TSLA", 'morningstar', start, end)
    # df = web.get_data_yahoo('CBS', start=start, end=end)

    data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    html = Template(df.to_html())
    return HttpResponse(html.render(Context({"person": "Clarke"})))


def sample1(request):
    return render(request, "sample.html")


def page(request):
    return render(request, "page.html")

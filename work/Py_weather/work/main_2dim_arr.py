#!/usr/bin/env python3

import json
import datetime
from urllib import request


URL_WEATHER = 'https://api.apixu.com/v1/history.json?key={KEY}&q={city}&dt={date}'
API_KEY = '837d8297891746f990b65202191106'

#https://stackoverflow.com/questions/50116416/appending-to-2-dimensional-array-in-python

def main():
    cities = ['Berlin', 'Washington', 'London']
    now = datetime.datetime.now()
    res = [[None,None,None],[]]
    for city in cities:
        i = 3
        # go from 3 to 1, end get weather history for each day (last three days)
        while i > 0:
            date = now - datetime.timedelta(days=i)
            body = request.urlopen(URL_WEATHER.format(city=city, KEY=API_KEY, date=date.strftime('%Y-%m-%d'))).read()
            print(i)
            res.append([i],json.loads(body.decode()))
            A = array([[0, 1, 2], [0, 2, 0]]) 
            newrow = [1,2,3]
            A = numpy.vstack([A, newrow])
            i -= 1
    parse_result(res[1])


def parse_result(data_to_parse):
    res = {}
    for item in data_to_parse:
        # set default keys
        city = item.get('location', {}).get('name', '')
        date = item.get('forecast', {}).get('forecastday', [{}, ])[0].get('date', '')
        hour_history = item.get('forecast', {}).get('forecastday', [{}, ])[0].get('hour', [])
        res.setdefault(city, {})
        res[city].setdefault(date, {})
        # parse hour by hour
        for h_item in hour_history:
            # get time from full data
            str_hour = h_item.get('time', '')[-5:]
            res[city][date][str_hour] = h_item.get('temp_c', 0)
    res_str = json.dumps(res)
    with open('result.json', 'w') as f:
        f.write(res_str)
    print(res)
    print('!!!ALL DATA SAVE IN result.json!!!')


if __name__ == '__main__':
    main()

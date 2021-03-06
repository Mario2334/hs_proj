#!/usr/bin/env python3
import json
import requests
import datetime
import time
import numpy
import pandas
from pandas.io.json import json_normalize

max_count = 20
max_days  = 1

URL_WEATHER = 'https://api.apixu.com/v1/history.json?key={KEY}&q={city}&dt={date}' # string substitution using {}
# https://realpython.com/python-string-formatting/

API_KEY = '837d8297891746f990b65202191106'

my_file_name = "city.dat"
my_cities = []  # open an array with 1 default city !!

PandaMatrix = pandas.DataFrame( [] )
#PandaMatrix.ignore_index=True
#NumPyMatrix = numpy.array([])

def main():
    try:
        my_file = open(my_file_name)
    except IOError:
        print("Can't open " + my_file_name + "!")
        #exit
    get_city_data()
    get_weather_data()

def get_city_data():
    # https://stackoverflow.com/questions/8009882/how-to-read-a-large-file-line-by-line-in-python/801013
    # https://thispointer.com/5-different-ways-to-read-a-file-line-by-line-in-python/
    # https://stackoverflow.com/questions/23459095/check-for-file-existence-in-python-3
    my_cities_raw_data = [] 
    with open(my_file_name, "r") as ins:
        for line in ins:
            my_cities_raw_data.append(line)
        #print( my_cities_raw_data )
        print( "-------------------------------------------------------------------------------------------------------------------my_cities_raw_data" )
        for city_data in my_cities_raw_data:
            index_of_end_of_name = city_data.find( "," )
            if index_of_end_of_name > 0:
                city = city_data[0:(index_of_end_of_name)]
                index_of_end_of_name = city.find(" (")
                if index_of_end_of_name > 0:
                    city = city[0:(index_of_end_of_name)]
                index_of_end_of_name = city.find("[")
                if index_of_end_of_name > 0:
                    city = city_data[0:(index_of_end_of_name)]
                city = city.lower().capitalize()  
                #print( city )
                my_cities.append ( city )  
        print( "-------------------------------------------------------------------------------------------------------------------cities" )
 
def get_weather_data():
    now = datetime.datetime.now()                # use datetime lib to get time of now
    #res = []
    counter = 0
    for city in my_cities:
        if counter > max_count:
            break
        counter += 1
        dict_res = []
        print( "Searching data from " + city + "...")
        time.sleep(2)
        i = max_days
        # go from 3 to 1, and get weather history for each day (last three days)
        while i > 0:
            # calculate 'i' days ago in regard today
            date = now - datetime.timedelta(days=i)
            # add json response to array 'res'  
            
            # example response: {"location":{"name":"London","region":"City of London, Greater London","country":"United Kingdom","lat":51.52,"lon":-0.11,"tz_id":"Europe/London","localtime_epoch":1560273465,"localtime":"2019-06-11 18:17"},"forecast":{"forecastday":[{"date":"2019-06-10","date_epoch":1560124800,"day":{"maxtemp_c":12.7,"maxtemp_f":54.9,"mintemp_c":3.9,"mintemp_f":39.0,"avgtemp_c":11.4,"avgtemp_f":52.4,"maxwind_mph":12.8,"maxwind_kph":20.5,"totalprecip_mm":31.0,"totalprecip_in":1.22,"avgvis_km":9.9,"avgvis_miles":6.0,"avghumidity":79.0,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"uv":0.0},"astro":{"sunrise":"04:44 AM","sunset":"09:16 PM","moonrise":"12:50 PM","moonset":"01:52 AM","moon_phase":"First Quarter","moon_illumination":"51"},"hour":[{"time_epoch":1560121200,"time":"2019-06-10 00:00","temp_c":14.5,"temp_f":58.1,"is_day":0,"condition":{"text":"Patchy rain possible","icon":"//cdn.apixu.com/weather/64x64/night/176.png","code":1063},"wind_mph":2.7,"wind_kph":4.3,"wind_degree":221,"wind_dir":"SW","pressure_mb":1019.0,"pressure_in":30.6,"precip_mm":0.04,"precip_in":0.0,"humidity":69,"cloud":100,"feelslike_c":15.0,"feelslike_f":59.0,"windchill_c":15.0,"windchill_f":59.0,"heatindex_c":14.5,"heatindex_f":58.1,"dewpoint_c":9.0,"dewpoint_f":48.2,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":14.3,"vis_miles":8.0,"gust_mph":3.4,"gust_kph":5.4},{"time_epoch":1560124800,"time":"2019-06-10 01:00","temp_c":14.1,"temp_f":57.4,"is_day":0,"condition":{"text":"Patchy rain possible","icon":"//cdn.apixu.com/weather/64x64/night/176.png","code":1063},"wind_mph":2.5,"wind_kph":4.0,"wind_degree":155,"wind_dir":"SSE","pressure_mb":1018.0,"pressure_in":30.5,"precip_mm":0.02,"precip_in":0.0,"humidity":72,"cloud":100,"feelslike_c":14.7,"feelslike_f":58.5,"windchill_c":14.7,"windchill_f":58.5,"heatindex_c":14.1,"heatindex_f":57.4,"dewpoint_c":9.1,"dewpoint_f":48.4,"will_it_rain":0,"chance_of_rain":"21","will_it_snow":0,"chance_of_snow":"0","vis_km":13.1,"vis_miles":8.0,"gust_mph":3.1,"gust_kph":4.9},{"time_epoch":1560128400,"time":"2019-06-10 02:00","temp_c":13.8,"temp_f":56.8,"is_day":0,"condition":{"text":"Light rain","icon":"//cdn.apixu.com/weather/64x64/night/296.png","code":1183},"wind_mph":2.2,"wind_kph":3.6,"wind_degree":89,"wind_dir":"E","pressure_mb":1018.0,"pressure_in":30.5,"precip_mm":0.57,"precip_in":0.02,"humidity":74,"cloud":100,"feelslike_c":14.4,"feelslike_f":57.9,"windchill_c":14.4,"windchill_f":57.9,"heatindex_c":13.8,"heatindex_f":56.8,"dewpoint_c":9.3,"dewpoint_f":48.7,"will_it_rain":0,"chance_of_rain":"61","will_it_snow":0,"chance_of_snow":"0","vis_km":12.0,"vis_miles":7.0,"gust_mph":2.8,"gust_kph":4.4},{"time_epoch":1560132000,"time":"2019-06-10 03:00","temp_c":13.4,"temp_f":56.1,"is_day":0,"condition":{"text":"Light rain","icon":"//cdn.apixu.com/weather/64x64/night/296.png","code":1183},"wind_mph":2.0,"wind_kph":3.2,"wind_degree":23,"wind_dir":"NNE","pressure_mb":1017.0,"pressure_in":30.5,"precip_mm":0.76,"precip_in":0.03,"humidity":77,"cloud":100,"feelslike_c":14.1,"feelslike_f":57.4,"windchill_c":14.1,"windchill_f":57.4,"heatindex_c":13.4,"heatindex_f":56.1,"dewpoint_c":9.4,"dewpoint_f":48.9,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":10.8,"vis_miles":6.0,"gust_mph":2.5,"gust_kph":4.0},{"time_epoch":1560135600,"time":"2019-06-10 04:00","temp_c":13.0,"temp_f":55.5,"is_day":0,"condition":{"text":"Light rain","icon":"//cdn.apixu.com/weather/64x64/night/296.png","code":1183},"wind_mph":3.5,"wind_kph":5.6,"wind_degree":24,"wind_dir":"NNE","pressure_mb":1017.0,"pressure_in":30.5,"precip_mm":0.38,"precip_in":0.01,"humidity":78,"cloud":98,"feelslike_c":13.2,"feelslike_f":55.7,"windchill_c":13.2,"windchill_f":55.7,"heatindex_c":13.0,"heatindex_f":55.5,"dewpoint_c":9.2,"dewpoint_f":48.6,"will_it_rain":0,"chance_of_rain":"61","will_it_snow":0,"chance_of_snow":"0","vis_km":9.4,"vis_miles":5.0,"gust_mph":4.2,"gust_kph":6.7},{"time_epoch":1560139200,"time":"2019-06-10 05:00","temp_c":12.7,"temp_f":54.8,"is_day":1,"condition":{"text":"Moderate rain","icon":"//cdn.apixu.com/weather/64x64/day/302.png","code":1189},"wind_mph":5.0,"wind_kph":8.0,"wind_degree":25,"wind_dir":"NNE","pressure_mb":1016.0,"pressure_in":30.5,"precip_mm":1.8,"precip_in":0.07,"humidity":79,"cloud":96,"feelslike_c":12.2,"feelslike_f":54.0,"windchill_c":12.2,"windchill_f":54.0,"heatindex_c":12.7,"heatindex_f":54.8,"dewpoint_c":9.1,"dewpoint_f":48.3,"will_it_rain":0,"chance_of_rain":"63","will_it_snow":0,"chance_of_snow":"0","vis_km":8.1,"vis_miles":5.0,"gust_mph":5.9,"gust_kph":9.5},{"time_epoch":1560142800,"time":"2019-06-10 06:00","temp_c":12.3,"temp_f":54.1,"is_day":1,"condition":{"text":"Moderate rain","icon":"//cdn.apixu.com/weather/64x64/day/302.png","code":1189},"wind_mph":6.5,"wind_kph":10.4,"wind_degree":26,"wind_dir":"NNE","pressure_mb":1016.0,"pressure_in":30.5,"precip_mm":2.4,"precip_in":0.09,"humidity":80,"cloud":93,"feelslike_c":11.3,"feelslike_f":52.3,"windchill_c":11.3,"windchill_f":52.3,"heatindex_c":12.3,"heatindex_f":54.1,"dewpoint_c":8.9,"dewpoint_f":48.0,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":6.7,"vis_miles":4.0,"gust_mph":7.6,"gust_kph":12.2},{"time_epoch":1560146400,"time":"2019-06-10 07:00","temp_c":12.4,"temp_f":54.4,"is_day":1,"condition":{"text":"Moderate rain","icon":"//cdn.apixu.com/weather/64x64/day/302.png","code":1189},"wind_mph":6.6,"wind_kph":10.7,"wind_degree":21,"wind_dir":"NNE","pressure_mb":1016.0,"pressure_in":30.5,"precip_mm":1.2,"precip_in":0.05,"humidity":77,"cloud":87,"feelslike_c":11.4,"feelslike_f":52.6,"windchill_c":11.4,"windchill_f":52.6,"heatindex_c":12.4,"heatindex_f":54.4,"dewpoint_c":8.5,"dewpoint_f":47.2,"will_it_rain":0,"chance_of_rain":"63","will_it_snow":0,"chance_of_snow":"0","vis_km":9.1,"vis_miles":5.0,"gust_mph":7.8,"gust_kph":12.6},{"time_epoch":1560150000,"time":"2019-06-10 08:00","temp_c":12.6,"temp_f":54.6,"is_day":1,"condition":{"text":"Patchy light rain","icon":"//cdn.apixu.com/weather/64x64/day/293.png","code":1180},"wind_mph":6.8,"wind_kph":10.9,"wind_degree":17,"wind_dir":"NNE","pressure_mb":1015.0,"pressure_in":30.5,"precip_mm":0.43,"precip_in":0.02,"humidity":74,"cloud":81,"feelslike_c":11.6,"feelslike_f":52.8,"windchill_c":11.6,"windchill_f":52.8,"heatindex_c":12.6,"heatindex_f":54.6,"dewpoint_c":8.0,"dewpoint_f":46.5,"will_it_rain":0,"chance_of_rain":"60","will_it_snow":0,"chance_of_snow":"0","vis_km":11.4,"vis_miles":7.0,"gust_mph":8.1,"gust_kph":13.0},{"time_epoch":1560153600,"time":"2019-06-10 09:00","temp_c":12.7,"temp_f":54.9,"is_day":1,"condition":{"text":"Patchy light rain","icon":"//cdn.apixu.com/weather/64x64/day/293.png","code":1180},"wind_mph":6.9,"wind_kph":11.2,"wind_degree":12,"wind_dir":"NNE","pressure_mb":1015.0,"pressure_in":30.5,"precip_mm":0.58,"precip_in":0.02,"humidity":71,"cloud":75,"feelslike_c":11.7,"feelslike_f":53.1,"windchill_c":11.7,"windchill_f":53.1,"heatindex_c":12.7,"heatindex_f":54.9,"dewpoint_c":7.6,"dewpoint_f":45.7,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":13.8,"vis_miles":8.0,"gust_mph":8.3,"gust_kph":13.3},{"time_epoch":1560157200,"time":"2019-06-10 10:00","temp_c":12.5,"temp_f":54.4,"is_day":1,"condition":{"text":"Patchy light rain","icon":"//cdn.apixu.com/weather/64x64/day/293.png","code":1180},"wind_mph":7.6,"wind_kph":12.2,"wind_degree":9,"wind_dir":"N","pressure_mb":1015.0,"pressure_in":30.4,"precip_mm":0.29,"precip_in":0.01,"humidity":73,"cloud":83,"feelslike_c":11.3,"feelslike_f":52.3,"windchill_c":11.3,"windchill_f":52.3,"heatindex_c":12.5,"heatindex_f":54.4,"dewpoint_c":7.8,"dewpoint_f":46.0,"will_it_rain":0,"chance_of_rain":"60","will_it_snow":0,"chance_of_snow":"0","vis_km":12.6,"vis_miles":7.0,"gust_mph":8.9,"gust_kph":14.4},{"time_epoch":1560160800,"time":"2019-06-10 11:00","temp_c":12.2,"temp_f":54.0,"is_day":1,"condition":{"text":"Moderate rain","icon":"//cdn.apixu.com/weather/64x64/day/302.png","code":1189},"wind_mph":8.3,"wind_kph":13.3,"wind_degree":6,"wind_dir":"N","pressure_mb":1015.0,"pressure_in":30.4,"precip_mm":1.33,"precip_in":0.05,"humidity":75,"cloud":92,"feelslike_c":10.8,"feelslike_f":51.5,"windchill_c":10.8,"windchill_f":51.5,"heatindex_c":12.2,"heatindex_f":54.0,"dewpoint_c":7.9,"dewpoint_f":46.3,"will_it_rain":0,"chance_of_rain":"63","will_it_snow":0,"chance_of_snow":"0","vis_km":11.5,"vis_miles":7.0,"gust_mph":9.6,"gust_kph":15.5},{"time_epoch":1560164400,"time":"2019-06-10 12:00","temp_c":12.0,"temp_f":53.6,"is_day":1,"condition":{"text":"Moderate rain","icon":"//cdn.apixu.com/weather/64x64/day/302.png","code":1189},"wind_mph":8.9,"wind_kph":14.4,"wind_degree":3,"wind_dir":"N","pressure_mb":1014.0,"pressure_in":30.4,"precip_mm":1.78,"precip_in":0.07,"humidity":77,"cloud":100,"feelslike_c":10.4,"feelslike_f":50.7,"windchill_c":10.4,"windchill_f":50.7,"heatindex_c":12.0,"heatindex_f":53.6,"dewpoint_c":8.1,"dewpoint_f":46.6,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":10.3,"vis_miles":6.0,"gust_mph":10.3,"gust_kph":16.6},{"time_epoch":1560168000,"time":"2019-06-10 13:00","temp_c":11.6,"temp_f":52.9,"is_day":1,"condition":{"text":"Moderate rain","icon":"//cdn.apixu.com/weather/64x64/day/302.png","code":1189},"wind_mph":10.2,"wind_kph":16.4,"wind_degree":118,"wind_dir":"ESE","pressure_mb":1014.0,"pressure_in":30.4,"precip_mm":0.89,"precip_in":0.03,"humidity":78,"cloud":100,"feelslike_c":9.8,"feelslike_f":49.6,"windchill_c":9.8,"windchill_f":49.6,"heatindex_c":11.6,"heatindex_f":52.9,"dewpoint_c":8.0,"dewpoint_f":46.4,"will_it_rain":0,"chance_of_rain":"63","will_it_snow":0,"chance_of_snow":"0","vis_km":10.2,"vis_miles":6.0,"gust_mph":12.8,"gust_kph":20.6},{"time_epoch":1560171600,"time":"2019-06-10 14:00","temp_c":11.3,"temp_f":52.3,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":11.5,"wind_kph":18.5,"wind_degree":232,"wind_dir":"SW","pressure_mb":1013.0,"pressure_in":30.4,"precip_mm":1.03,"precip_in":0.04,"humidity":80,"cloud":100,"feelslike_c":9.1,"feelslike_f":48.4,"windchill_c":9.1,"windchill_f":48.4,"heatindex_c":11.3,"heatindex_f":52.3,"dewpoint_c":7.9,"dewpoint_f":46.2,"will_it_rain":1,"chance_of_rain":"92","will_it_snow":0,"chance_of_snow":"0","vis_km":10.0,"vis_miles":6.0,"gust_mph":15.4,"gust_kph":24.7},{"time_epoch":1560175200,"time":"2019-06-10 15:00","temp_c":10.9,"temp_f":51.6,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":12.8,"wind_kph":20.5,"wind_degree":347,"wind_dir":"NNW","pressure_mb":1013.0,"pressure_in":30.4,"precip_mm":1.38,"precip_in":0.05,"humidity":81,"cloud":100,"feelslike_c":8.5,"feelslike_f":47.3,"windchill_c":8.5,"windchill_f":47.3,"heatindex_c":10.9,"heatindex_f":51.6,"dewpoint_c":7.8,"dewpoint_f":46.0,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":9.9,"vis_miles":6.0,"gust_mph":17.9,"gust_kph":28.8},{"time_epoch":1560178800,"time":"2019-06-10 16:00","temp_c":10.2,"temp_f":50.4,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":11.9,"wind_kph":19.1,"wind_degree":348,"wind_dir":"NNW","pressure_mb":1012.0,"pressure_in":30.4,"precip_mm":0.69,"precip_in":0.03,"humidity":84,"cloud":100,"feelslike_c":8.6,"feelslike_f":47.5,"windchill_c":8.6,"windchill_f":47.5,"heatindex_c":11.2,"heatindex_f":52.2,"dewpoint_c":8.7,"dewpoint_f":47.6,"will_it_rain":1,"chance_of_rain":"92","will_it_snow":0,"chance_of_snow":"0","vis_km":8.8,"vis_miles":5.0,"gust_mph":17.1,"gust_kph":27.6},{"time_epoch":1560182400,"time":"2019-06-10 17:00","temp_c":9.6,"temp_f":49.2,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":11.0,"wind_kph":17.6,"wind_degree":349,"wind_dir":"N","pressure_mb":1012.0,"pressure_in":30.4,"precip_mm":2.67,"precip_in":0.1,"humidity":87,"cloud":100,"feelslike_c":8.8,"feelslike_f":47.8,"windchill_c":8.8,"windchill_f":47.8,"heatindex_c":11.6,"heatindex_f":52.8,"dewpoint_c":9.5,"dewpoint_f":49.2,"will_it_rain":1,"chance_of_rain":"92","will_it_snow":0,"chance_of_snow":"0","vis_km":7.6,"vis_miles":4.0,"gust_mph":16.4,"gust_kph":26.4},{"time_epoch":1560186000,"time":"2019-06-10 18:00","temp_c":8.9,"temp_f":48.0,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":10.1,"wind_kph":16.2,"wind_degree":350,"wind_dir":"N","pressure_mb":1012.0,"pressure_in":30.4,"precip_mm":3.56,"precip_in":0.14,"humidity":89,"cloud":100,"feelslike_c":8.9,"feelslike_f":48.0,"windchill_c":8.9,"windchill_f":48.0,"heatindex_c":11.9,"heatindex_f":53.4,"dewpoint_c":10.4,"dewpoint_f":50.7,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":6.5,"vis_miles":4.0,"gust_mph":15.7,"gust_kph":25.2},{"time_epoch":1560189600,"time":"2019-06-10 19:00","temp_c":7.2,"temp_f":45.0,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":10.6,"wind_kph":17.0,"wind_degree":242,"wind_dir":"WSW","pressure_mb":1011.0,"pressure_in":30.3,"precip_mm":1.78,"precip_in":0.07,"humidity":89,"cloud":100,"feelslike_c":7.2,"feelslike_f":45.0,"windchill_c":7.2,"windchill_f":45.0,"heatindex_c":9.9,"heatindex_f":49.8,"dewpoint_c":10.7,"dewpoint_f":51.3,"will_it_rain":1,"chance_of_rain":"92","will_it_snow":0,"chance_of_snow":"0","vis_km":6.5,"vis_miles":4.0,"gust_mph":16.3,"gust_kph":26.3},{"time_epoch":1560193200,"time":"2019-06-10 20:00","temp_c":5.6,"temp_f":42.0,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":11.1,"wind_kph":17.9,"wind_degree":134,"wind_dir":"SE","pressure_mb":1011.0,"pressure_in":30.3,"precip_mm":2.47,"precip_in":0.1,"humidity":90,"cloud":100,"feelslike_c":5.6,"feelslike_f":42.0,"windchill_c":5.6,"windchill_f":42.0,"heatindex_c":7.9,"heatindex_f":46.2,"dewpoint_c":11.1,"dewpoint_f":51.9,"will_it_rain":1,"chance_of_rain":"92","will_it_snow":0,"chance_of_snow":"0","vis_km":6.6,"vis_miles":4.0,"gust_mph":17.0,"gust_kph":27.4},{"time_epoch":1560196800,"time":"2019-06-10 21:00","temp_c":3.9,"temp_f":39.0,"is_day":1,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/day/389.png","code":1276},"wind_mph":11.6,"wind_kph":18.7,"wind_degree":27,"wind_dir":"NNE","pressure_mb":1011.0,"pressure_in":30.3,"precip_mm":3.29,"precip_in":0.13,"humidity":90,"cloud":100,"feelslike_c":3.9,"feelslike_f":39.0,"windchill_c":3.9,"windchill_f":39.0,"heatindex_c":5.9,"heatindex_f":42.6,"dewpoint_c":11.4,"dewpoint_f":52.5,"will_it_rain":0,"chance_of_rain":"0","will_it_snow":0,"chance_of_snow":"0","vis_km":6.6,"vis_miles":4.0,"gust_mph":17.7,"gust_kph":28.4},{"time_epoch":1560200400,"time":"2019-06-10 22:00","temp_c":6.9,"temp_f":44.4,"is_day":0,"condition":{"text":"Moderate or heavy rain with thunder","icon":"//cdn.apixu.com/weather/64x64/night/389.png","code":1276},"wind_mph":11.1,"wind_kph":17.9,"wind_degree":37,"wind_dir":"NE","pressure_mb":1010.0,"pressure_in":30.3,"precip_mm":1.64,"precip_in":0.06,"humidity":91,"cloud":85,"feelslike_c":6.4,"feelslike_f":43.5,"windchill_c":6.4,"windchill_f":43.5,"heatindex_c":8.2,"heatindex_f":46.8,"dewpoint_c":11.5,"dewpoint_f":52.7,"will_it_rain":1,"chance_of_rain":"92","will_it_snow":0,"chance_of_snow":"0","vis_km":6.5,"vis_miles":4.0,"gust_mph":18.0,"gust_kph":28.9},{"time_epoch":1560204000,"time":"2019-06-10 23:00","temp_c":9.9,"temp_f":49.8,"is_day":0,"condition":{"text":"Heavy rain at times","icon":"//cdn.apixu.com/weather/64x64/night/305.png","code":1192},"wind_mph":10.6,"wind_kph":17.0,"wind_degree":46,"wind_dir":"NE","pressure_mb":1010.0,"pressure_in":30.3,"precip_mm":3.53,"precip_in":0.14,"humidity":92,"cloud":69,"feelslike_c":8.9,"feelslike_f":48.0,"windchill_c":8.9,"windchill_f":48.0,"heatindex_c":10.6,"heatindex_f":51.0,"dewpoint_c":11.6,"dewpoint_f":52.9,"will_it_rain":0,"chance_of_rain":"64","will_it_snow":0,"chance_of_snow":"0","vis_km":6.4,"vis_miles":3.0,"gust_mph":18.3,"gust_kph":29.4}]}]}}
            dict_res.append(requests.get(URL_WEATHER.format(city=city, KEY=API_KEY, date=date.strftime('%Y-%m-%d'))).json())
            i -= 1
            # parsing each city separately
            #print ( dict_res )
            #print( "-------------------------------------------------------------------------------------------------------------------res" )
            json_res_after_parse = parse_result(dict_res)
            print ( json_res_after_parse )
            print( "-------------------------------------------------------------------------------------------------------------------res after parsing" )

    #print( PandaMatrix.to_string() ) 
    print( "-------------------------------------------------------------------------------------------------------------------Panda" )

def parse_result(data_to_parse):
    # will final result
    res = {}
    array_res = []
    # item is one response from main def
    for item in data_to_parse:
        # set default keys
        
        # get dict from 'location' key, if it unsset, get epmty dict, that was not error. next get city name or empty str if name is undefined
        city = item.get('location', {}).get('name', '')
        # get dict from 'forecast' key, if it unsset, get epmty dict, next get array of dicts on key 'forecastday' or array with empty dict if 'forecastday' undefined
        
        # call first array element in 'forecastday' and get date or empty str if date is undefined
        date = item.get('forecast', {}).get('forecastday', [{}, ])[0].get('date', '')
        
        # the same as we get date, but if 'hour' is undefined we return empty array. It's need for well done work loop below
        hour_history = item.get('forecast', {}).get('forecastday', [{}, ])[0].get('hour', [])
        
        # set default key with city name and set empty dict on this key. If key in dict, nothing happend. It's need for comfortable expand final result
        res.setdefault(city, {})
        
        # the same. but set date dict in city or do nothing if date isset
        res[city].setdefault(date, {})
        
        # parse hour by hour. hour_history is array forecasts on each hour 00:00/01:00/02:00/03:00...
        for h_item in hour_history:
            # get only time from full data
            str_hour = h_item.get('time', '')[-5:]
            # res['Berlin']['2019-06-10'][01:00] = 30
            res[city][date][str_hour] = h_item.get('temp_c', 0)
            array_res.append( h_item.get('temp_c', 0) )
    
    print ( res )
    print( "-------------------------------------------------------------------------------------------------------------------array_res" )
    print ( array_res )
    print( "-------------------------------------------------------------------------------------------------------------------res" )

    # make json string from res
    str_res = json.dumps(res)

    print ( str_res ) # nothing really changed just when printing out you get " instead of '
    print( "-------------------------------------------------------------------------------------------------------------------res str" )

    norm_json_res = json_normalize( res )
    print ( norm_json_res )
    print( "-------------------------------------------------------------------------------------------------------------------res norm" )

    #rows=list(range(0,len(array_res)))
    #PandaMatrix = pandas.DataFrame( data=array_res, index=rows, columns=[city] )
    
    # https://thispointer.com/python-pandas-how-to-add-new-columns-in-a-dataframe-using-or-dataframe-assign/
    # https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/
    PandaMatrix.insert ( 0, city, array_res, True )
    PandaMatrix.ignore_index=True
    #PandaMatrix.assign ( city=array_res ) # geht nicht
    print( PandaMatrix.to_string() ) 
    print( "-------------------------------------------------------------------------------------------------------------------Panda im loop" )

    #NumPyMatrix = numpy.array( array_res )
    #NumPyMatrix = numpy.vstack([NumPyMatrix, newrow ])
    #NumPyMatrix.append( res )

    # funktioniert
    #numpy.random.seed(25)
    #df = pandas.DataFrame(numpy.random.rand(10, 3), columns =['A', 'B', 'C'])
    #print( df.to_string() ) 

    # save result in file
    filename = city
    with open( 'data/' + filename + '.json', 'w') as f:
        f.write(str_res)
    #print(res)
    #print('!!! ALL DATA SAVED IN result.json !!!')
    return str_res

if __name__ == '__main__':
    main()


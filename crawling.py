import requests
import json
import datetime
import pandas as pd
# __URL = 'http://openAPI.seoul.go.kr:8088/'+self.__KEY+'/json/DailyAverageCityAir/1/25/'

def send_api(self, method, date):
    url = self.__URL + date
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "key1": "value1",
        "key2": "value2"
    }
    try:
        if method == 'GET':
            response = requests.get(url = url)
        elif method == 'POST':
            response = requests.post(url = url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
    except Exception as ex:
        print(ex)
    return response


def DataFrame(self):
    year, days, BASE = self.year, self.days, self.__URL
    start, df = True, None
    startdate = datetime.datetime(year = year, month = 1, day = 1)
    for day in range(days):
        cdate = startdate + datetime.timedelta(days = day)
        cdate = cdate.strftime('%Y%m%d')
        result = self.send_api('GET', cdate)
        jsonresult = result.json()
        if start:
            df = pd.json_normalize(jsonresult['DailyAverageCityAir']['row'])
            start = False
        else:
            try:
                df = pd.concat([df, pd.json_normalize(jsonresult['DailyAverageCityAir']['row'])])
            except:
                continue
    self.df = df
    return df

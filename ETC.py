
# def DataFrame(self):
#     year, days, BASE = self.year, self.days, self.__URL
#     start, df = True, None
#     startdate = datetime.datetime(year = year, month = 1, day = 1)
#     for day in range(days):
#         cdate = startdate + datetime.timedelta(days = day)
#         cdate = cdate.strftime('%Y%m%d')
#         result = self.send_api('GET', cdate)
#         jsonresult = result.json()
#         if start:
#             df = pd.json_normalize(jsonresult['DailyAverageCityAir']['row'])
#             start = False
#         else:
#             try:
#                 df = pd.concat([df, pd.json_normalize(jsonresult['DailyAverageCityAir']['row'])])
#             except:
#                 continue
#     self.df = df
#     return df



# {
#   "MSRDT_DE" : 20220101,
#   "MSRRGN_NM": "도심권",
#   "MSRSTE_NM" : "중구",
#   "O3" : 0.015,
#   "NO2" : 0.5,
#   "CO":0.035,
#   "SO2" : 0.003   
# }
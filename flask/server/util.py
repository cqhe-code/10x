import csv
from datetime import datetime

class WeatherDataReader:
    def __init__(self, path=''):
        self.path = path
        self._colnames = None
        self._data = []
        with open(path) as csvfile:
            rows = csv.reader(csvfile, delimiter=",")
            for n, row in enumerate(rows):
                if n == 0: 
                    #date,precipitation,temp_max,temp_min,wind,weather
                    self._colnames = row
                else:
                    #2012-01-01,0.0,12.8,5.0,4.7,drizzle
                    processed_row = [
                        datetime.strptime(row[0], '%Y-%m-%d'),
                        float(row[1]),
                        float(row[2]),
                        float(row[3]),
                        float(row[4]),
                        row[5]
                    ]
                
                    self._data.append(processed_row)

    def colnames(self):
        return self._colnames
    
    def data(self):
        return self._data
    
class WeatherDataQuery:
    def __init__(self, data=[]):
        self._data = data

    # date,precipitation,temp_max,temp_min,wind,weather
    def query_by_date(self, date: datetime):
        if not date:
            return self
        self._data = [d for d in self.data() if d[0] == date]
        return self
    def query_by_weather(self, type: str):
        if not type:
            return self
        self._data = [d for d in self.data() if d[-1] == type]
        return self
    
    def query_by_limit(self, limit: int):
        if not limit:
            return self
        self._data = self._data[:limit]
        return self
    
    def data(self):
        return self._data
    
    def __str__(self):
        s = ""
        for d in self._data:
            s += f'{d}\n'
        return s
    
if __name__ == "__main__":
    path = "server/data/seattle-weather.csv"
    import os
    print(os.getcwd())
    data_reader = WeatherDataReader(path)
    cname, data = data_reader.colnames, data_reader.data()
    print(cname)
    q = WeatherDataQuery(data)
    unique_weather = set() 
    for d in data:
        unique_weather.add(d[-1])
    print(unique_weather)
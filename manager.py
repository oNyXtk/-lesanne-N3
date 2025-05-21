class MurderStatsManager:
    def __init__(self):
        self.data = {}

    def add_data(self, continent, country, city, count):
        if continent not in self.data:
            self.data[continent] = {}
        if country not in self.data[continent]:
            self.data[continent][country] = {}
        self.data[continent][country][city] = count

    def get_stats(self):
        return self.data

    def get_city_stats(self, continent, country, city):
        try:
            return self.data[continent][country][city]
        except KeyError:
            return f"No data for {city}, {country}, {continent}"

    def remove_city(self, continent, country, city):
        try:
            del self.data[continent][country][city]
        except KeyError:
            return f"City {city} not found in {country}, {continent}"

import os
import requests

class CountryIter:

    def __iter__(self):
        countries_url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
        request = requests.get(countries_url)
        request_json = request.json()
        self.countries_list = []
        for i in range(len(request_json)):
            self.countries_list.append(request_json[i]["translations"]["rus"]["common"])
        self.counter = len(self.countries_list)
        self.count = 0
        return self

    def __next__(self):
        if self.counter <= self.count:
            raise StopIteration
        country_wikipath = f"https://ru.wikipedia.org/wiki/{self.countries_list[self.count]}\n"
        self.count += 1
        return country_wikipath


if __name__ == "__main__":
    filepath = os.path.join(os.getcwd(), 'countriesWikipath.txt')
    with open(filepath, 'a') as file:
        for country in CountryIter():
            file.write(country)
    file.close()

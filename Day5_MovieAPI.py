import requests
from terminaltables import AsciiTable
# to see the structure of the response (json tree)
import pprint


def get_data_from_movie_api(movie_title):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    querystring = {"q": movie_title}

    headers = {
        'x-rapidapi-key': "your_api_key_goes_here",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

    response = requests.request(method="GET", url=url, params=querystring, headers=headers)
    return response


def display_movie_info():
    response = get_data_from_movie_api(input("Find a movie! "))
    response_json = response.json()
    # pprint.pprint(response_json)
    arguments = ['l', 'y', 's']
    # args = ['title', 'cast', 'year']
    table_data = [['Title', 'Year', 'Main cast']]

    for i in range(len(response_json['d'])):
        info = ["", "", ""]
        for a in arguments:
            try:
                data = response_json['d'][i][a]
                info[arguments.index(a)] = data
                # table_data[i+1][arguments.index(a)] = data

            except KeyError:
                # print("no " + str(args[arguments.index(a)]))
                pass
        table_data.append(info)


        # print("{title}: {year}, main cast: {cast}".format(
        #     title=info[0],
        #     year=info[2],
        #     cast=info[1],
        # ))

    table = AsciiTable(table_data)
    print(table.table)

display_movie_info()

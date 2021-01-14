import requests
from terminaltables import AsciiTable

def get_books(author):
    url = '''http://data.bn.org.pl/api/bibs.json?author={author}&amp%3Bkind=
    ksi%C4%85%C5%BCka&fbclid=IwAR3LPbak_U4vrgQs-DpKhIaN35Wpqg1rQC3T7HVF-1sIy-BfK_aQb5ChDWY'''.format(
        author=author
    )

    response = requests.request(method="GET", url=url)
    return response.json()


author = input("Give author: ")
response = get_books(author)
table_data = [['Tytuł', 'Gatunek', 'rok Publikacji']]

info = ["", "", ""]
for i in range(len(response["bibs"])):
    info[0] = response["bibs"][i]["title"]
    info[1] = response["bibs"][i]["genre"]
    info[2] = response["bibs"][i]["publicationYear"]
    table_data.append(info)
    info = ["", "", ""]

table = AsciiTable(table_data)
print(table.table)


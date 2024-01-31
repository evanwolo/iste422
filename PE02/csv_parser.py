import pandas


def json_to_csv():
    
    with open('jsonfile.json', encoding='utf-8') as inputfile:
        df = pandas.read_json(inputfile)
        df.to_csv('csvfile.csv', encoding='utf-8', index=False)




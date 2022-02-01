import pandas as pd
from flask import Flask

app = Flask(__name__)

df = pd.read_csv("/Users/dougl/OneDrive/Documents/PortfolioDashboard/covidData.csv")

#country = 'Brazil'


def get_table(country):
    df_output = df.loc[df['Country_Region'] == country][['Province_State', 'Country_Region', 'Confirmed', 'Lat', 'Long_']]
    df_output = df_output.sort_values('Confirmed', ascending=False)
    df_output.to_csv(country + "Data.csv")

    print("data stored...")

def get_sumary(country):
    df_country = df.groupby(['Country_Region']).sum()
    df_country = df_country[['Confirmed', 'Deaths', 'Recovered', 'Active']]

    dct = {
        "Country": country,
        "Confirmed": df_country.loc[country][0],
        "Deaths": df_country.loc[country][1],
        "Recovered": df_country.loc[country][2],
        "Active": df_country.loc[country][3]
    }
    return dct

def get_geo(country):
    df_country = df.groupby(['Country_Region']).mean()
    df_country = df_country[['Lat', 'Long_', 'Case_Fatality_Ratio']]

    dct = {
        "Country": country,
        "Latitude": df_country.loc[country][0],
        "Longitude": df_country.loc[country][1],
        "Fatality_ratio": df_country.loc[country][2]
    }
    return dct


@app.route('/<country>/sumary')
def sumary(country):
    response_sum = get_sumary(country)
    return response_sum

@app.route('/<country>/geo')
def geo(country):
    response_geo = get_geo(country)
    return response_geo


#get_table(country)
#print(get_sumary(country))

if __name__ == "__main__":
    app.run(debug=True)
import pandas as pd

df = pd.read_csv("/Users/dougl/OneDrive/Documents/PortfolioDashboard/covidData.csv")

country = 'Brazil'

def get_table(country):
    df_output = df.loc[df['Country_Region'] == country][['Province_State', 'Country_Region', 'Confirmed', 'Lat', 'Long_']]
    df_output = df_output.sort_values('Confirmed', ascending=False)
    df_output.to_csv(country + "Data.csv")

    print("data stored...")

def get_sumary(country):
    df_country = df.groupby(['Country_Region']).sum()
    df_country = df_country[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    return df_country.loc[country]


get_table(country)
print(get_sumary(country))

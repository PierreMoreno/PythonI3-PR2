#
import pandas as pd
import plotly.graph_objs as go
import plotly
import plotly_express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

#Lecture du fichier csv
df = pd.read_csv("populations.csv", error_bad_lines=False,skiprows=3)
# Déclaration des list() et des data frames
countries = df['Country Name']
countries_code = df['Country Code']
countries_name_data = list()
countries_code_data = list()
countries_name_data2019 = list()
countries_code_data2019 = list()
countries_data = list()
countries_data_year2019 = list()
years_data = list()
#Liste des années étudiées
years  = ["1960","1961","1962","1963","1964","1965","1966","1967","1968","1969",
"1970","1971","1972","1973","1974","1975","1976","1977","1978","1979",
"1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",
"1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
"2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
"2010","2011","2012","2013","2014","2015","2016","2017","2018","2019",]

#Liste des territoires non étudiés dans mes données 
exclusion = ["Aruba","Le monde arabe","Antigua-et-Barbuda","Europe centrale et les pays baltes","Asie de l’Est et Pacifique (hors revenu élevé)","de dividende précoce démographique",
"Asie de l’Est et Pacifique","Europe et Asie centrale (hors revenu élevé)","Europe et Asie centrale","Zone euro","Union européenne","Fragile et les situations de conflit touchées",
"Revenu élevé","Pays pauvres très endettés (PPTE)","BIRD seulement","BIRD et IDA","IDA totale","IDA mélange","IDA seulement","Non classifié",
"Amérique latine et Caraïbes (hors revenu élevé)","Amérique latine et Caraïbes","Pays les moins avancés : classement de l’ONU","Faible revenu",
"Revenu intermédiaire, tranche inférieure",
"Revenu faible et intermédiaire","de dividende tardif démographique","Afrique du Nord et Moyen-Orient","Revenu intermédiaire","Afrique du Nord et Moyen-Orient (hors revenu élevé)",
"Amérique du Nord","Pays membres de l'OCDE","de Pré-dividende démographique","de Post-dividende démographique","Asie du Sud","Afrique subsaharienne (hors revenu élevé)",
"Afrique subsaharienne","Asie de l’Est et Pacifique (BIRD et IDA)",
"Europe et Asie centrale (BIRD et IDA)","Amérique latine et Caraïbes (BIRD et IDA)","Afrique du Nord et Moyen-Orient (BIRD et IDA)","Asie du Sud (BIRD et IDA)",
"Afrique subsaharienne (BIRD et IDA)","Revenu intermédiaire, tranche supérieure","Monde","Fragile et les situations de conflit touchées"]

#Remplissage des nouvelles data frames (Année en colonne)
for country  in countries:
    try:
        if (country  not in exclusion):
            query=df.query("`Country Name`=='"+country+"'")
            countries_data_year2019.append(query["2019"].array[0])
            countries_name_data2019.append(country)
            countries_code_data2019.append(query["Country Code"].array[0])
    except(SyntaxError):
        print()

    for year in  years:
        try:
            if (country  not in exclusion):
                countries_name_data.append(country)
                countries_code_data.append(query["Country Code"].array[0])
                countries_data.append(query[year].array[0])
                years_data.append(int(year))
        except(SyntaxError):
            print()


#Création des nouvelles data séries des  2 dataframes
df1 = pd.DataFrame(countries_name_data, columns = ['country'])
df1['code'] = countries_code_data
df1['year'] = years_data
df2 = pd.DataFrame(countries_name_data2019, columns=['country'])
df2['code'] = countries_code_data2019
df2['year'] = "2019"
df2['data'] = countries_data_year2019
df1['data'] = countries_data
#print(df1) 
#print(df2)

#Création  du Dash
if __name__ == '__main__':

    app = dash.Dash(__name__) 
#Création  de l'histogramme
    fig = px.histogram(df1, x="year", y="data",
                        hover_name="country") 
#création de la map
    figmap = px.choropleth(df2,
    locations='code',
    color='data',
    color_continuous_scale=px.colors.sequential.Plasma)          


#Disposition de la page sur le dash
    app.layout = html.Div(children=[

                            html.H1(children=f'Evolution de la population de réfugiés dans le monde',
                                        style={'textAlign': 'center', 'color': '#7FDBFF'}), 

                            dcc.Graph(
                                id='graph1',
                                figure=fig
                            ), 
                            dcc.Graph(
                                id='carte1',
                                figure=figmap
                            ), 
                            html.Div(children=f'''
                                L'histogramme ci-dessus nous montre l'évolution de la population de réfugiés dans le monde depuis 1960
                                La carte montre la population de réfugiés en 2019 dans le monde.
                            '''), 

    ]
    )
        #
    # RUN APP
    #

    app.run_server(debug=True) 

import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os

import requests
import plotly.graph_objects as go
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.max_columns", 999)

df = pd.read_csv('WHS8_110.csv')

new_columns = {
    'Country': 'country'
}


VALID_USERNAME_PASSWORD_PAIRS = {
    os.environ['USERNAME']: os.environ['PASSWORD']
}

df.columns = df.iloc[0].values
df = df[1:]
df = df.fillna(0).copy()
df.columns = df.columns.astype(str)
df.columns = [col.replace('.0', '') for col in df.columns]
df.rename(columns=new_columns, inplace=True)

# df_country = df.head(30)
# df_year = df.head(30)

app = dash.Dash()

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

server = app.server

app.layout = html.Div(
    [
        html.H1(
            'Immunization Dashboard',
            style={'text-align': 'center'}
        ),
        html.Div([
            dcc.Dropdown(
                id='year_selection',
                options=[
                    {'label': '2019', 'value': '2019'},
                    {'label': '2018', 'value': '2018'},
                    {'label': '2017', 'value': '2017'},
                    {'label': '2016', 'value': '2016'},
                    {'label': '2015', 'value': '2015'},
                    {'label': '2014', 'value': '2014'},
                    {'label': '2013', 'value': '2013'},
                    {'label': '2012', 'value': '2012'}
                ],
                value='2019'
            ),
            dcc.Graph(id='bargraph'),
            dcc.Dropdown(
                id='country_selection',
                options=[
                    {'label': 'Romania', 'value': 'Romania'},
                    {'label': 'United States of America', 'value': 'United States of America'},
                    {'label': 'France', 'value': 'France'},
                    {'label': 'Hungary', 'value': 'Hungary'},
                    {'label': 'Italy', 'value': 'Italy'},
                    {'label': 'Sudan', 'value': 'Sudan'},
                    {'label': 'Spain', 'value': 'Spain'},
                    {'label': 'Egypt', 'value': 'Egypt'},
                    {'label': 'India', 'value': 'India'},
                ],
                value='Romania'
            ),
            dcc.Graph(id='linegraph'),
        ],
            style={'padding': 10})
    ]
)


@app.callback(
    Output('bargraph', 'figure'),
    [Input('year_selection', 'value')]
)
def retrieve_revenue(year):
    df_country = df['country'].head(20)
    df_year = df[year].head(20)
    datapoints = {'data': [go.Bar(x=df_country, y=df_year)], 'layout': dict(yaxis={'title': 'Vaccination %'}, )}
    return datapoints


@app.callback(
    Output('linegraph', 'figure'),
    [Input('country_selection', 'value')]
)
def retrieve_revenue(country):
    df_country = df[df['country'] == country]
    df_country = df_country.T.drop('country', axis=0)
    df_country.columns = ['rate']
    df_country = df_country.rename(columns={df_country.columns[0]: 'rate'})
    years = list(df_country.index)
    rates = list(df_country['rate'].values)
    datapoints = {'data': [go.Scatter(x=years, y=rates, mode="lines+markers")],
                  'layout': dict(yaxis=dict(range=[0, 100]))}
    return datapoints


if __name__ == '__main__':
    app.run_server(debug=True)

# import plotly.graph_objects as go
# import pandas as pd
#
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import dash_table
# import dash_bootstrap_components as dbc
#
# external_stylesheets = [dbc.themes.LUX]
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# df = pd.read_csv('covid19 updated.csv')
#
# # rename columns
# df.rename(columns={'Intensive Care Unit (ICU)': 'Intensive Care Unit',
#                    'General Wards MOH report': 'General wards',
#                    'In Isolation MOH report': 'In Isolation',
#                    'Total Completed Isolation MOH report': 'Total completed isolation',
#                    'Total Hospital Discharged MOH report': 'Total discharged from hospital',
#                    'Local cases residing in dorms MOH report': 'Local cases residing in dorms',
#                    'Local cases not residing in doms MOH report': 'Local cases not residing in dorms'},inplace=True)
#
# app.layout = html.Div([
#     dbc.Container([
#         dbc.Row([
#             dbc.Col(html.H1("COVID-19 in Singapore at a glance"), className="mb-2")
#         ]),
#         dbc.Row([
#             dbc.Col(html.H6(children='Visualising trends across the different stages of the COVID-19 outbreak in Singapore'), className="mb-4")
#         ]),
#
#         dbc.Row([
#             dbc.Col(dbc.Card(html.H3(children='Latest Update',
#                                      className="text-center text-light bg-dark"), body=True, color="dark")
#                     , className="mb-4")
#         ]),
#
#     dcc.RadioItems(
#         id='table_type',
#         options=[{'label': i, 'value': i} for i in ['Condensed table', 'Full table']],
#         value='Condensed table',
#         labelStyle={'display': 'inline-block'}
#     ),
#     dash_table.DataTable(
#         id='datatable',
#         style_table={'overflowX': 'scroll',
#                         'padding': 10},
#         style_header={'backgroundColor': '#25597f', 'color': 'white'},
#         style_cell={
#             'backgroundColor': 'white',
#             'color': 'black',
#             'fontSize': 13,
#             'font-family': 'Nunito Sans'}),
#
#         dbc.Row([
#             dbc.Col(dbc.Card(html.H3(children='Situation Across Different Periods of the Outbreak',
#                                      className="text-center text-light bg-dark"), body=True, color="dark")
#                     , className="mt-4 mb-5")
#         ]),
#
#     dcc.Dropdown(
#         id='covid_period',
#         options=[
#             {'label': 'Pre-DORSCON Orange', 'value': 'Pre-DORSCON'},
#             {'label': 'DORSCON Orange', 'value': 'DORSCON'},
#             {'label': 'Circuit Breaker', 'value': 'CB'}
#         ],
#         value='CB',
#         style={'width': '48%', 'margin-left':'5px'}
#         ),
#
#     dbc.Row([
#         dbc.Col(html.H5(children='Daily COVID-19 cases in Singapore', className="text-center"),
#                 className="mt-4")
#     ]),
#
#     dcc.Graph(id='graph_by_period',
#               hoverData={'points': [{'x': '11-May'}]}),
#
#     dbc.Row([
#         dbc.Col(html.H5(children='Breakdown of cases: local vs imported', className="text-center"),
#                 width=6, className="mt-4"),
#         dbc.Col(html.H5(children='Breakdown of cases: whether residing in dorms', className="text-center"), width=6,
#                 className="mt-4"),
#         ]),
#     dbc.Row([
#         dbc.Col(
#             dcc.Graph(id='local and imported'), width=6),
#         dbc.Col(dcc.Graph(id='dorms'), width=6)
#     ]),
#
#     dcc.Dropdown(
#         id='choose_hospital_situation',
#         options=[
#             {'label': 'ICU', 'value': 'Intensive Care Unit'},
#             {'label': 'General wards', 'value': 'General wards'},
#             {'label': 'Isolation', 'value': 'In Isolation'},
#             {'label': 'Total completed isolation', 'value': 'Total completed isolation'},
#             {'label': 'Total discharged from hospital', 'value': 'Total discharged from hospital'},
#         ],
#         value=['Intensive Care Unit', 'General wards'],
#         multi=True,
#         style={'width': '70%', 'margin-left':'5px'}
#         ),
#
#     dbc.Row([
#         dbc.Col(html.H5(children='Situation in local hospitals', className="text-center"),
#                 className="mt-4")
#     ]),
#
#     dcc.Graph(id='situation_graph_by_period')
#     ])
#
# ])
#
# # page callbacks
# # choose between condensed table and full table
# @app.callback([Output('datatable', 'data'),
#               Output('datatable', 'columns')],
#              [Input('table_type', 'value')])
#
# def update_columns(value):
#     df2 = df.tail(1)
#     col = ['Daily Imported', 'Daily Local transmission']
#     df2['Daily Confirmed Cases'] = df2[col].sum(axis=1)
#
#     condensed_col = ['Date', 'Daily Confirmed Cases', 'Cumulative Confirmed', 'Daily Discharged',
#                      'Cumulative Discharged', 'Daily Deaths', 'Cumulative Deaths', 'Daily Imported',
#                      'Local cases residing in dorms',
#                      'Local cases not residing in dorms']
#
#     full_col = ['Date', 'Daily Confirmed Cases', 'Cumulative Confirmed', 'Daily Discharged',
#                 'Cumulative Discharged', 'Daily Deaths', 'Cumulative Deaths', 'Daily Imported',
#                 'Local cases residing in dorms', 'Local cases not residing in dorms',
#                 'Intensive Care Unit', 'General wards', 'In Isolation']
#
#     if value == 'Condensed table':
#         columns = [{"name": i, "id": i} for i in condensed_col]
#         data=df2.to_dict('records')
#     elif value == 'Full table':
#         columns = [{"name": i, "id": i} for i in full_col]
#         data=df2.to_dict('records')
#     return data, columns
#
# # allow for easy sieving of data to see how the situation has changed
# # can observe whether government measures are effective in reducing the number of cases
# @app.callback(Output('graph_by_period', 'figure'),
#               [Input('covid_period', 'value')])
#
# def update_graph(covid_period_name):
#     dff = df[df.Period == covid_period_name]
#     # not sure why this doesn't work, Daily Confirmed is an invalid key
#     col = ['Daily Imported', 'Daily Local transmission']
#     dff['total'] = dff[col].sum(axis=1)
#     data = [go.Scatter(x=dff['Date'], y=dff['total'],
#                        mode='lines+markers',name='Daily confirmed')]
#     layout = go.Layout(
#         yaxis={'title': "Cases"},
#         paper_bgcolor = 'rgba(0,0,0,0)',
#         plot_bgcolor = 'rgba(0,0,0,0)',
#         template = "seaborn",
#         margin=dict(t=20)
#     )
#
#     return {'data': data, 'layout': layout}
#
# @app.callback([Output('local and imported', 'figure'),
#                Output('dorms', 'figure')],
#               [Input('graph_by_period', 'hoverData')])
#
# def update_breakdown(hoverData):
#     day = hoverData['points'][0]['x']
#     dff = df[df['Date'] == day]
#
#     fig2 = go.Figure()
#     fig2.add_trace(go.Bar(x=dff['Date'], y=dff['Daily Local transmission'],
#                           name='Local cases'))
#
#     fig2.add_trace(go.Bar(x=dff['Date'], y=dff['Daily Imported'],
#                           name='Imported cases'))
#
#     # edit layout
#     fig2.update_layout(yaxis_title='Cases',
#                        paper_bgcolor='rgba(0,0,0,0)',
#                        plot_bgcolor='rgba(0,0,0,0)',
#                        template = "seaborn",
#                        margin=dict(t=20))
#
#     fig3 = go.Figure()
#     fig3.add_trace(go.Bar(x=dff['Date'], y=dff['Local cases residing in dorms'],
#                           name='Residing in dorms'))
#
#     fig3.add_trace(go.Bar(x=dff['Date'], y=dff['Local cases not residing in dorms'],
#                           name='Not residing in dorms'))
#
#     # edit layout
#     fig3.update_layout(yaxis_title='Cases',
#                        paper_bgcolor='rgba(0,0,0,0)',
#                        plot_bgcolor='rgba(0,0,0,0)',
#                        template = "seaborn",
#                        margin=dict(t=20))
#     return fig2, fig3
#
# # update hospital situation graph
# @app.callback(Output('situation_graph_by_period', 'figure'),
#               [Input('covid_period', 'value'),
#                Input('choose_hospital_situation', 'value')])
#
# def update_situation_graph(covid_period_name, choose_hospital_situation_name):
#     dff = df[df.Period == covid_period_name]
#
#     trace = []
#
#     for i in choose_hospital_situation_name:
#         trace.append(go.Bar(name=i, x=dff['Date'], y=dff[i]))
#
#     data = trace
#
#     layout = go.Layout(
#         yaxis={'title': "Cases"},
#         barmode='stack',
#         paper_bgcolor = 'rgba(0,0,0,0)',
#         plot_bgcolor = 'rgba(0,0,0,0)',
#         template="seaborn",
#         margin=dict(t=20)
#     )
#
#     return {'data': data, 'layout': layout}
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
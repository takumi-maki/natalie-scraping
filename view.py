
import dash
import dash_html_components as html
import pandas as pd
import datetime


df = pd.read_csv('data.csv')
today = datetime.date.today().strftime('%-m月%-d日')

def generate_table(dataframe, max_rows=30):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server 

app.layout = html.Div(children=[
    html.H4(children='Owarai natalie'),
    html.P(children=today),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)

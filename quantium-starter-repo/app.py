
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('./data/processedDF2')

colors = {
    'background': '#fff',
    'text': '#000'
}

fig = px.line(df, x="date", y="sales")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Pink Morsel Sales From October 2020 to Frebruary 2022',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'font-family':'sans-serif'
        }
    ),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

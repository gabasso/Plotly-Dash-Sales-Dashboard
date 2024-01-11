# Load data

import pandas as pd
df=pd.read_excel("Superstore.xlsx",sheet_name="TAD")
# filtro de DF
df=df[(df['Profit Margin']>-2) & (df["Sales"]<5000)]
df['Order_year']=df['Order_Date'].dt.year.astype(int)
# get segments
segments=df['Segment'].unique()
# Order years
order_years=df.Order_year.unique()
max_year=max(order_years)
# colors for plots 
plot_color=["rgb(46, 148, 76)","rgb(128, 171, 203)","rgb(160, 207, 255)","rgb(22, 71, 36)"]

#
import figures as figs

# Dash
from dash import Dash, dcc, html, Input, Output, callback, clientside_callback



app = Dash(__name__)


# Potly

import plotly.express as px


app.layout = html.Div(style={'backgroundColor': 'black',
    'color': 'white',
    'flexDirection': 'row',
    'display':'flex'

   },
    children=[
        html.Div(id="side-panel",
                 children=[
                     html.H2("side panel")
                 ]),
        html.Div(id="main-content",style={
             'padding':'10px',
             'width': '99%',},
                 children=[

        html.H1('Super Store Dashboard', style={'textAlign': 'left',
                                                    "padding":"10px",}),
        

        html.Div(id='slicers',style={
            'display': 'flex',
            'flexDirection': 'row',
             'justifyContent': 'space-between',
             'padding':'10px',
             'width': '49%',},
            children=[
            html.Div(className="slicer",style={'width': '49%',
                                               "margin-right":".5%"},
                     children=[html.H4("Segment",style={"padding":"3px",
                                                        "margin":"2px"}),
                              dcc.Dropdown(options=segments,
                                value='Consumer',
                                id='segment-dropdown',
                                placeholder="Select a segment"
                                )]),
            html.Div(className="slicer",style={'width': '49%',
                                               "margin-right":".5%"},
                     children=[html.H4("Years",style={"padding":"3px",
                                                        "margin":"2px"}),             
                                dcc.Dropdown(options=order_years,
                                value=max_year,
                                id='year-dropdown',
                                placeholder="Select years", 
                                multi=True 
                                        )])
            ]),
        html.Div(style={
            'display': 'flex',
            'flexDirection': 'row',
             'justifyContent': 'space-between',
             'padding':'10px',
             "margin-right":"5px"
             },
            children=[    
                        html.Figure(dcc.Graph(id="scatterplot"),style={'width': '49%',
                                               "margin-right":".5%"}),
                        dcc.Store(id="scatterplot-store"),
                        html.Figure(dcc.Graph(id="Sales-bar-plot"),style={'width': '49%',
                                                                          "margin-right":".5%"})])


])])




@callback(
    #Output('scatterplot-store', 'data'),
    Output('scatterplot','figure'),
    Output('Sales-bar-plot','figure'),
    Input('segment-dropdown', 'value'),
    Input('year-dropdown','value'))

def update_figures(segment,year):
    if type(year)!=list:
        year=[year]
    dff = df[(df['Segment'] == segment)]
             
    fig=figs.sales_vs_magin(dff=dff,segment=segment,year=year)
    fig2=figs.sales_by_year(dff=dff,segmeent=segment)

    return fig, fig2
            



if __name__ == '__main__':
    app.run_server(debug=True)

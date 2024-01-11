# Load data

import pandas as pd
df=pd.read_excel("Superstore.xlsx",sheet_name="TAD")
# filtro de DF
df=df[(df['Profit Margin']>-2) & (df["Sales"]<5000)]
df['Order_year']=df['Order_Date'].dt.year
# get segments
segments=df['Segment'].unique()
# Order years
order_years=df.Order_year.unique()
max_year=max(order_years)
# colors for plots 
plot_color=["rgb(46, 148, 76)","rgb(128, 171, 203)","rgb(160, 207, 255)","rgb(22, 71, 36)"]


# Dash
from dash import Dash, dcc, html, Input, Output, callback, clientside_callback



app = Dash(__name__)


# Potly

import plotly.express as px


app.layout = html.Div(style={'backgroundColor': 'black',
    'color': 'white',

   },
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


])




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
             
    fig = px.scatter(dff[(dff['Order_year'].isin(year))],x='Sales',y='Profit Margin',
                     title=str(segment),
                     color='Order_year',
                     color_discrete_sequence=plot_color
                     )


    fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    modebar=dict(bgcolor='rgba(0, 0, 0, 0)'),
    font=dict(color='white'),
        xaxis=dict(showgrid=False, zeroline=True, showticklabels=True,
        title_text="Sales",  # Replace with your x-axis title
        title_font=dict(size=18, color='white', family="Courier New, monospace"),
    ),
    yaxis=dict(
        tickformat=".0%",
        showgrid=False,
        zeroline=True,
        showticklabels=True,
        title_text="Profit Margin",  # Replace with your y-axis title
        title_font=dict(size=18, color='white', family="Courier New, monospace"),
    ))

    fig2 = px.bar(dff['Sales'].groupby(dff['Order_year']).sum().reset_index(), x='Order_year', y='Sales')
    
    
    fig2.update_xaxes(tickmode='array', tickvals=year)
    fig2.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    modebar=dict(bgcolor='rgba(0, 0, 0, 0)'),
    font=dict(color='white'),
        xaxis=dict(showgrid=False, zeroline=True, showticklabels=True,
        title_text="Year",  # Replace with your x-axis title
        title_font=dict(size=18,
                         color='white',
                         family="Courier New, monospace"),
    ),
    yaxis=dict(
        tickformat=".2s",
        showgrid=False,
        zeroline=True,
        showticklabels=True,
        title_text="Sales",  # Replace with your y-axis title
        title_font=dict(size=18,
                         color='white',
                         family="Courier New, monospace"),
    ))
    fig2.update_traces(marker_color='rgb(39, 124, 64)',hovertemplate='%{y}')
    return fig, fig2
            



if __name__ == '__main__':
    app.run_server(debug=True)

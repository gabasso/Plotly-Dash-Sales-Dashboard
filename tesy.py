# Import necessary libraries
from dash import dash, html, dcc
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div(style={'backgroundColor': '#111111'}, children=[
    html.H1('Sales Report Dashboard', style={'color': '#FFFFFF'}),
    
    # Line graph
    dcc.Graph(
        id='sales-line-graph',
        figure={
            'data': [
                {'x': ['January', 'February', 'March'], 'y': [400, 500, 300], 'type': 'line', 'name': 'Monthly'},
                {'x': ['Week 1', 'Week 2', 'Week 3'], 'y': [100, 150, 200], 'type': 'line', 'name': 'Weekly'}
            ],
            'layout': {
                'title': 'Sales Over Time',
                'plot_bgcolor': '#111111',
                'paper_bgcolor': '#111111',
                'font': {
                    'color': '#FFFFFF'
                }
            }
        }
    ),
    
    # Donut charts
    html.Div([
        dcc.Graph(
            id='total-sales-donut',
            figure={
                'data': [
                    {'values': [450, 300, 250], 'type': 'pie', 'hole': .3}
                ],
                'layout': {
                    'title': 'Total Sales',
                    'annotations': [
                        {'font': {'size': 20}, 'showarrow': False, 'text': 'Total', 'x': 0.50, 'y': 0.5}
                    ],
                    'showlegend': False
                }
            }
        ),
        # Add more donut charts here
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),
    
    # Sales table
    html.Table([
        html.Thead(
            html.Tr([html.Th('Quantity'), html.Th('Item'), html.Th('Total')])
        ),
        html.Tbody([
            html.Tr([html.Td('10'), html.Td('Dallas Gas Dining Table'), html.Td('$2000')]),
            html.Tr([html.Td('5'), html.Td('Bamboo Rocking Chair'), html.Td('$750')]),
            # Add more rows here
        ])
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

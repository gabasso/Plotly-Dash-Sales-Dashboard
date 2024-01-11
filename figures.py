# Potly
import plotly.express as px

color_map={2018:"red",
           2017:"green",
           2016:"pnik",
           2015:"orange",
           "Test":"purpple"}


def sales_vs_magin(dff,segment,year):
    dfff=dff[(dff['Order_year'].isin(year))]
    dfff['Year']=dfff['Order_year'].astype(str)

    fig = px.scatter(dfff,x='Sales',y='Profit Margin',
                     title=str(segment),
                     color='Year',
                     color_discrete_map=color_map
                     #color_discrete_sequence=['red','green','orange','light blue']

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
    return fig

def sales_by_year(dff,segmeent):


    fig2 = px.bar(dff['Sales'].groupby(dff['Order_year']).sum().reset_index(), x='Order_year', y='Sales',
                  title='Sales by year for '+str(segmeent))
    
    
    fig2.update_xaxes(tickmode='array', tickvals=list(dff['Order_year'].unique()))
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

    return fig2
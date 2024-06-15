import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('sales_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Sales Data Visualizer', className='header'),
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        className='radio-buttons'
    ),
    dcc.Graph(id='sales-line-chart', className='line-chart')
], className='container')

# Create a callback to update the graph based on the selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-selector', 'value')]
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales', title=f'Sales in {selected_region.capitalize()} Region')
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales'
    )
    return fig

# CSS styles
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

# Inline CSS for custom styles
app.css.append_css({
    'external_url': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'
})

app.css.append_css({
    'external_url': '/assets/style.css'
})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

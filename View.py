import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import Cloud_Data

# Create the Dash app
app = Dash(__name__)

# Fetch sentiment data by trend
sentiment_by_trend = Cloud_Data.get_sentiment_by_trend()

# Convert the result into a DataFrame
df_trend = pd.DataFrame(sentiment_by_trend)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Sentiment Breakdown by Trend", style={'text-align': 'center'}),

    # Dropdown to select a trend
    dcc.Dropdown(
        id='trend-dropdown',
        options=[{'label': trend['trend'], 'value': trend['trend']} for trend in sentiment_by_trend],
        value=sentiment_by_trend[0]['trend'],  # Default to first trend
        style={'width': '50%', 'margin': 'auto'}
    ),

    # Pie chart displaying sentiment breakdown
    dcc.Graph(id='sentiment-pie-chart')
])

# Callback to update the pie chart when a trend is selected
@app.callback(
    Output('sentiment-pie-chart', 'figure'),
    [Input('trend-dropdown', 'value')]
)
def update_pie_chart(selected_trend):
    # Filter the data for the selected trend
    trend_data = df_trend[df_trend['trend'] == selected_trend].iloc[0]

    # Prepare data for the pie chart
    sentiment_data = {
        'Sentiment': ['Positive', 'Neutral', 'Negative'],
        'Count': [trend_data['positive_count'], trend_data['neutral_count'], trend_data['negative_count']]
    }

    sentiment_df = pd.DataFrame(sentiment_data)

    # Create the pie chart
    fig = px.pie(sentiment_df, values='Count', names='Sentiment', title=f"Sentiment for Trend: {selected_trend}")

    return fig

# Run the app
app.run_server(debug=True)

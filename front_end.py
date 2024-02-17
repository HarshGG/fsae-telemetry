import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import json
import websocket

# Initialize Dash app
app = dash.Dash("http://localhost:3001/FSAE_EV_Telemetry/")

# Layout of the web app
app.layout = html.Div(children=[
    html.H1("Live Telemetry Data"),
    dcc.Graph(id="live-graph"),
])

# Create a WebSocket connection to receive telemetry data from the backend
ws = websocket.WebSocket()
ws.connect("ws://localhost:8050/ws")  # Replace with your backend WebSocket URL

# Callback to update the graph with live data
@app.callback(
    Output('live-graph', 'figure'),
    [Input('live-graph', 'id')]
)
def update_graph(_):
    while True:
        try:
            message = ws.recv()
            data = json.loads(message)['data']
            timestamp, speed, rpm, temperature = data

            # Update the graph
            trace = go.Scatter(
                x=[timestamp],
                y=[speed],
                mode='lines+markers',
                name='Speed'
            )
            layout = go.Layout(
                title='Live Speed Data',
                xaxis=dict(title='Time'),
                yaxis=dict(title='Speed (mph)')
            )
            return {'data': [trace], 'layout': layout}
        except websocket.WebSocketConnectionClosedError:
            pass

if __name__ == '__main__':
    # Run the Dash app
    app.run_server(debug=True)
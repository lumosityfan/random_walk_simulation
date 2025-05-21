import random as r
import math as m
from dash import Dash, dcc, html, Input, Output, State, callback
import plotly.express as px

app = Dash(__name__)

# Sets initial coordinates at origin
x_coord = 0
y_coord = 0
# Sets up initial array of coordinates
steps_x_coords = [0]
steps_y_coords = [0]
# Goes through various steps
for _ in range(0, 1000):
    # Generate x and y differentials
    x_diff = r.uniform(-1.0, 1.0) # Generates random float number
    y_diff = r.uniform(-1.0, 1.0) # Generates random float number

    # Normalize x and y differentials
    length = m.sqrt(m.pow(x_diff, 2) + m.pow(y_diff, 2))
    x_diff = x_diff / length
    y_diff = y_diff / length

    # Changes coordinates
    x_coord += x_diff
    y_coord += y_diff
        
    steps_x_coords.append(x_coord)
    steps_y_coords.append(y_coord)

fig = px.line(x=steps_x_coords, y=steps_y_coords, title="Plot #0", width=800, height=800)
fig.update_layout(xaxis_range=[-40, 40])
fig.update_layout(yaxis_range=[-40, 40])
fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='Black')
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='Black')
app.layout = html.Div(
    [
        html.H3("Random Walk Simulation", style={"textAlign": "center"}),
        html.Button("Generate values", id="random-val", n_clicks=0),
        dcc.Graph(
            id="graph",
            figure=fig,
        ),
    ]
)

@callback(
    Output("graph", "figure"),
    Input("random-val", "n_clicks"),
    prevent_initial_call=True,
)
def update_report(n):
    # Sets initial coordinates at origin
    x_coord = 0
    y_coord = 0
    # Sets up initial array of coordinates
    steps_x_coords = [0]
    steps_y_coords = [0]
    # Goes through various steps
    for _ in range(0, 1000):
        # Generate x and y differentials
        x_diff = r.uniform(-1.0, 1.0) # Generates random float number
        y_diff = r.uniform(-1.0, 1.0) # Generates random float number

        # Normalize x and y differentials
        length = m.sqrt(m.pow(x_diff, 2) + m.pow(y_diff, 2))
        x_diff = x_diff / length
        y_diff = y_diff / length

        # Changes coordinates
        x_coord += x_diff
        y_coord += y_diff
        
        steps_x_coords.append(x_coord)
        steps_y_coords.append(y_coord)

    fig = px.line(x=steps_x_coords, y=steps_y_coords, title=f"Plot #{n}")
    fig.update_layout(xaxis_range=[-40, 40])
    fig.update_layout(yaxis_range=[-40, 40])
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='Black')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='Black')
    return fig

if __name__ == "__main__":
    app.run(debug=True)



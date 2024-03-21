from flask import Flask
from dash import Dash, html


server = Flask(__name__)
app = Dash(__name__, server=server)
app.layout = html.Div(
    html.H1("Hello, google")
)

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8080)
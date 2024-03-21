from flask import Flask
from dash import Dash, html

def main():
    server = Flask(__name__)
    app = Dash(server=server)
    app.layout = html.Div(
        html.H1("Hello, google")
    )
    app.run_server()

if __name__ == "__main__":
    main()
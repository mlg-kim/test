import os

from dash import Dash, dcc, html

from callbacks import get_callbacks
from utils import MBTI

app = Dash(__name__)
server = app.server()


def user_controls():
    return html.Div(
        [
            html.Label("이름"),
            dcc.Input(placeholder="김민규", type="text",id="name-input"),
            html.Label("나이"),
            dcc.Input(placeholder="27", type="number",id="age-input"),
            html.Label("MBTI"),
            dcc.Dropdown(options=MBTI,id="mbti-input"),
            html.Label("아바타 재설정"),
            html.Button("재생성", id = "avatar-button", style={ "font-size": "16px"}),
        ],
        className="three columns div-user-controls",
    )


def profile():
    return html.Div(
        [
            html.Div([
                html.H2("Profile", style={"font-size": "36px"}),
                html.Div([
                    html.H2("이름",id="name"),
                    html.H2("나이",id="age"),
                ]),
                html.Img(id="avatar")
            ]),
            html.H2("MBTI", style={"font-size": "36px"}),
            dcc.Graph(id="mbti"),
        ],
        className="nine columns bg-grey",
        style={
            "display": "flex",
            "flex-direction": "column",
            "flex-grow": 1,
        },
    )


app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                user_controls(),
                profile(),
            ],
        )
    ]
)

get_callbacks(app)

# Remove all svg files is assets folder
for file in os.listdir("assets"):
    if file.endswith(".svg"):
        os.remove(os.path.join("assets", file))


if __name__ == "__main__":
    app.run_server()

import numpy as np

import data_operations
import pandas as pd
import random
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, ctx, dash_table  # pip install dash (version 2.0.0 or higher)
#from dash import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

def generate_random_table(df: pd.DataFrame):
    df_length = df.shape[0]
    random_dict = {}
    for column in df.columns:
        index = random.randint(0, df_length-1)
        print(df[column][index])
        if not isinstance(df[column][index],str):#df[column][index]==np.NaN or len(df[column][index])<1:
            index=random.randint(0,4)
        random_dict[column] = [df[column][index], '']
    df_temp = pd.DataFrame(random_dict)
    # print(df_temp)
    return df_temp


def columns_generate(df):
    columns = []
    for number, column in enumerate(df.columns):
        temp = {"id": number, "name": column}
        columns.append(temp)
    print(columns)
    return columns


def main():
    path = 'data.csv'
    # app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
    app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
    server = app.server
    df = data_operations.import_csv(path)
    df_temp = generate_random_table(df)
    # ------------------------------------------------------------------------------
    # App layout
    app.layout = html.Center([

        html.H1("Get a game idea", style={'text-align': 'center'}),

        dcc.Markdown('''
        Bellow you can see a set of prompts that should help you come up with a game idea. 
        Feel free to base your idea on favourite 3, random 4 or all of them.
        The meaning of each field
         '''),
        html.Br(),

        dcc.Markdown('''
        Free Domain Character - a character who's story can inspire you, they can become main hero of your story, they can just lend you their world or anything else you can think of,
        
        Environment Type - where roughly your game will be taking place,
        
        Game Type - ...the type of game it will be... let's be honest this one is self-explanatory
        
        Established Title Mechanic - think of the game/series you got and take one element from them, it can be very specific (Cyberpunk-like ability to hack things) or very basic (limited inventory of Resident Evil),
        
        Theme - what will be the...general theme??.. again pretty self explanatory
        '''),
        html.Br(),

        dcc.Markdown('''
        Click the 'Generate' button to get a new set       
        '''),
        html.Br(),

        # dcc.Markdown('''
        #         | title one | title two | title three | title four | title five |
        #         |-----------|-----------|-------------|------------|------------|
        #         | 1         | 2         | 3           | 4          | 5          |
        #
        #
        #         '''),

        # dash_table.DataTable(df_temp.to_dict('records'), [{"name": i, "id": i} for i in df_temp.columns]),


        # html.Div(id='output_container', children=[]),
        # html.Br(),

        # html.A(html.Button('Submit', id='submit-val', n_clicks=0),href='/
        #html.Center([
        dash_table.DataTable(
            id='table',
            data=[],#df.to_dict('records'),columns=[{"name": i, "id": i} for i in df.columns]
            # fill_width=False
            style_table = {'width': '80%','color': 'black'},
            style_cell = {'text-align': 'center'}
        ),
        html.Br(),
        html.Button(['Generate'], id='btn')  #])

    ])

    # ------------------------------------------------------------------------------
    # Connect the Plotly graphs with Dash Components
    @app.callback([Output("table", "data"),
                   Output('table', 'columns')
                   ],
                  [Input(component_id='btn', component_property='n_clicks')]
                  # [Output(component_id='output_container', component_property='children'),
                  #  Output(component_id='my_bee_map', component_property='figure')],
                  # [Input(component_id='slct_year', component_property='value')]
                  )
    def updateTable(clicked):

        columns = columns_generate(df)
        columns = [{"name": i, "id": i} for i in df.columns]
        if clicked is None:
            df_temp1 = generate_random_table(df)
            return df_temp1.to_dict('records'), columns
        df_temp1 = generate_random_table(df)
        data=df_temp1#.values[0]
        return data.to_dict('records') , columns
    # df.to_dict('records')

    app.run_server(debug=True)


# if __name__ == '__main__':
main()

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

app = dash.Dash(__name__)

#renta = pd.read_csv("C:\Users\j0rge\OneDrive\Escritorio\Office_Rentals\data\Data_renta.csv")
#venta = pd.read_csv("C:\Users\j0rge\OneDrive\Escritorio\Office_Rentals\data\Data_venta.csv")

app.layout = html.Div(children=[
    html.H1(children='Analisis General sobre las Inmobiliarias en renta y venta')
])

app.layout = html.Div(children=[
    dcc.Graph(#Grafica
        id='Grafica_Inicial',
        figure={
            'data': ['Colonia', 'M2', 'Precio'],
            'layout':#Contenido de la tabla de la grafica
            go.Layout(title='Grafica de venta', barmode='stack')
    })
])



if __name__ == '__main__':
    app.run_server(debug=True)
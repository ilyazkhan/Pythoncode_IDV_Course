import numpy as np
from matplotlib import pyplot as pl
from pandas.plotting import scatter_matrix
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
pl.style.use('classic')
from matplotlib import colors
import seaborn as sns
import mplcursors


with open('DataWeierstrass.csv') as data:
    data_reader = pd.read_csv(data, delimiter=';', usecols=['professor', 'lecture', 'participants', 'professional expertise', 'motivation', 'clear presentation', 'overall impression'])
    print(data_reader)

    professor_number = data_reader.iloc[:, 0].values
    lecture_number = data_reader.iloc[:, 1].values

    #converting to float because professor and lecture are nominal data
    for rows in range(len(professor_number)):
        professor_number[rows] = float(professor_number[rows].replace('prof', ''))

    for i in range(len(lecture_number)):
        lecture_number[i] = float(lecture_number[i].replace('lecture', ''))


    combined = np.vstack((professor_number, lecture_number)).T

    data_reader['professor'] = combined[:, 0]
    data_reader['lecture'] = combined[:, 1]

    # A. Scattermatrix
    #reference: https://stackoverflow.com/questions/7908636/possible-to-make-labels-appear-when-hovering-over-a-point-in-matplotlib
    #https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
    sns.set()
    g = sns.PairGrid(data_reader, vars=['professor','lecture', 'participants', 'professional expertise', 'motivation', 'clear presentation', 'overall impression'],
    hue='professor', palette='hls', dropna=True, diag_sharey='hist')
    g.fig.tight_layout()

    g.map(pl.scatter)
    g.add_legend()
    pl.subplots_adjust(top=0.95)
    g.fig.suptitle('Scattermatrix for lecture evaluation', fontsize=20)
    mplcursors.cursor(hover=True)
    pl.show()


    # B. Parallel coordinates
    #Reference: https://plotly.com/python/parallel-coordinates-plot/
    data = [go.Parcoords(
        line=dict(color=data_reader['professor'],
                  colorscale=[[0,'gold'],[0.5,'lightseagreen'],[1,'violet']],
                  showscale=True,
                  cmin=0,
                  cmax=55),
        dimensions=list([
            dict(range=[0, 50], label="Professor Id", values=data_reader['professor']),
            dict(range=[0, 105], label='Lecture Id', values=data_reader['lecture']),
            dict(tickvals=[0, 50, 100, 150, 200, 250, 300, 330],
                 ticktext=['0', '50', '100', '150', '200', '250', '300', 330], visible=True,
                 label='Participants', values=data_reader['participants']),
            dict(range=[0, 3], tickvals=[0, 1, 2, 3], ticktext=['0', '1', '2', '3'], visible=True,
                 label='Professional Expertise', values=data_reader['professional expertise']),
            dict(range=[1, 5], tickvals=[1, 2, 3, 4, 5],
                 ticktext=['1', '2', '3', '4', '5'],
                 visible=True,
                 label='Motivation', values=data_reader['motivation']),
            dict(range=[1, 5],
                 tickvals=[1, 2, 3, 4, 5],
                 ticktext=['1', '2', '3', '4', '5'],
                 visible=True,
                 label='Clear Presentation(1:best and 6:worst)', values=data_reader['clear presentation']),
            dict(range=[1, 5],
                 tickvals=[1, 2, 3, 4, 5],
                 ticktext=['1', '2', '3', '4', '5'],
                 visible=True,
                 label='Overall Impression(1:best and 6:worst)', values=data_reader['overall impression'])])
        )
    ]

    fig = go.Figure(data=data)
    fig.update_layout(hovermode='x unified', title="Parallel coordinate for Lecture Evaluatiation")
    fig.show()











import plotly.express as px
import matplotlib.pyplot as plt
from fpdf import FPDF
import pandas as pd
import plotly.graph_objects as go

def makeReport(df_res, pars, article_df, table):

    plt.plot(df_res['Days_since_publication'], df_res['Probability_Top_Article'])
    df_aux = df_res[df_res['Actual_day']==1]
    plt.scatter(df_aux['Days_since_publication'], df_aux['Probability_Top_Article'], color='red')
    plt.title('Article Evolution')
    plt.xlabel('Days since publication')
    plt.ylabel('Probability Top Article')
    plt.savefig('./reports/figures/clapsEvolution.png')

    #Initial conditions page
    pdf=FPDF("L", "mm", "A4")

    #Page 0
    pdf.add_page()
    pdf.image('./reports/figures/portada.png', x = -10, y = 15, w =330, h =180)

    #Page 1
    pdf.add_page()
    pdf.set_font('Times','', 10.0) 
    pdf.cell(20, 10, 'Article', 1, 0, 'C', 0)
    pdf.cell(180, 10, pars.args.url, 1, 1, 'C', 0)
    pdf.cell(20, 10, 'Title', 1, 0, 'C', 0)
    pdf.cell(180, 10, article_df['Title'][0], 1, 0, 'C', 0)
    pdf.image('./reports/figures/clapsEvolution.png', x = 30, y = 35, w =0, h =0)
    pdf.text(200, 170, f"Class 1: Claps > 90")
    pdf.text(200, 175, f"Class 0: Claps < 90")

    #table
    layout = go.Layout(
    autosize=False,
    width=1000,
    height=900)

    fig = go.Figure(data=[go.Table(
        columnorder = [1,2,3,4,5,6,7,8],
        columnwidth = [15,70,40,40,20,20,20,32],
        header=dict(values=['Claps', 'Title', 'Publication', 'Reading_Time', 'Links', 'Bolded', 'Images', 'Distance'],
                    align='center'),
        cells=dict(values=[table.Claps, table.Title, table.Publication, table.Reading_Time, table.Links, table.Bolded, table.Images, table.Distance],
                    align='center')),
        ], layout=layout)
    fig.write_image('./reports/figures/table.png')

    pdf.add_page()
    pdf.set_font('Times','B', 20.0) 
    pdf.image('./reports/figures/table.png', x = -28, y = 20, w =0, h =0)
    pdf.text(127, 50, f'Recommendations')

    #Save Report
    print('\n') 
    pdf.output("./reports/clapsEvolution.pdf", "F")
    print('A report has been generated in <reports> folder\n')
    

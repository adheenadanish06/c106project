import plotly.express as px
import csv
import numpy as np 

def getdatasuorce(datapath):
    icreamsales =[]
    temperature = []
    with open(datapath)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            temperature.append(float(row["Cold-drink-sales"]))
            icreamsales.append(float(row["Temperature"]))

    return {"x": temperature,"y":icreamsales}
    
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation: ",correlation[0,1])

def plotfigure():
    with open ("iceCream.csv")as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Temperature",y="Ice-cream-Sales")
        fig.show()

def setup():
    datapath = "c106\iceCream.csv"
    datasource = getdatasuorce(datapath)
    findcorrelation(datasource)

plotfigure()
setup()
from joblib import load
import numpy as np
from keras.models import load_model

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
import plotly

MPSModel = load_model("../savedStates/meanParticleSize_model.savedstate")
MPSSc = load("../savedStates/meanParticleSize_scaler.savedstate")

EEModel = load_model("../savedStates/entrapmentEfficiency_model.savedstate")
EESc = load("../savedStates/entrapmentEfficiency_scaler.savedstate")

RRPercentageModel = load_model("../savedStates/releaseRatePercentage_model.savedstate")
RRPercentageSc = load("../savedStates/releaseRatePercentage_scaler.savedstate")

RRHoursModel = load_model("../savedStates/releaseRateHours_model.savedstate")
RRHoursSc = load("../savedStates/releaseRateHours_scaler.savedstate")


MW = 751
XLOGP = 3.6
TPSA = 196
CX = 1440

# MPS
def MPSData(pdr, lg):
    return MPSModel.predict(np.array(MPSSc.transform([np.array([pdr, lg, MW, XLOGP, TPSA, CX])])).reshape(-1, 6))[0][0]

# EE
def EEData(pdr, lg):
    return EEModel.predict(np.array(EESc.transform([np.array([MW, CX, lg, TPSA, pdr, XLOGP])])).reshape(-1, 6))[0][0]

def RRPercentageData(ee, lg, mps):
    return RRPercentageModel.predict(np.array(RRPercentageSc.transform([np.array([XLOGP, ee, TPSA, MW, lg, CX, mps])])).reshape(-1, 7))[0][0]

def RRHoursData(ee, lg, mps):
    return RRHoursModel.predict(np.array(RRHoursSc.transform([np.array([XLOGP, ee, TPSA, MW, CX, lg, mps])])).reshape(-1, 7))[0][0]

# Generate graph for MPS
def MPSGraph():
    fig = go.Figure()

    for i in np.arange(1, 4, 1):
        pdrPlotData = []
        for j in np.arange(0, 50, 1):
            pdrPlotData.append(MPSData(j, i))

        fig.add_trace(go.Scatter(x=np.arange(0, 50, 1), y=pdrPlotData, name="L:G = " + str(i)))

    fig.update_layout(
        title="Effect of PLGA:Drug ratio and lactide:glycolide ratio on mean particle size",
        xaxis_title="PLGA:Drug ratio",
        yaxis_title="Mean Particle Size",
    )

    return fig

# Generate graph for EE
def EEGraph():
    fig = go.Figure()

    for i in np.arange(1, 4, 1):
        pdrPlotData = []
        for j in np.arange(0, 50, 1):
            pdrPlotData.append(EEData(j, i)*100)

        fig.add_trace(go.Scatter(x=np.arange(0, 50, 1), y=pdrPlotData, name="L:G = " + str(i)))

    fig.update_layout(
        title="Effect of PLGA:Drug ratio and lactide:glycolide ratio on entrapment efficiency",
        xaxis_title="PLGA:Drug ratio",
        yaxis_title="Entrapment Efficiency (%)",
    )

    return fig

def RRHours():
    fig = make_subplots(rows=2, cols=3)

    for i in range(1, 4):
        for k in np.arange(0, 101, 10):
            pdrPlotData = []
            for j in np.arange(100, 200, 1):
                pdrPlotData.append(RRHoursData(k, i, j))
            if i == 1 or i == 2 or i == 3:
                r = 1
            else:
                r=2
            if i == 1 or i == 4:
                c = 1
            elif i == 2 or i == 5:
                c=2
            else:
                c=3

            fig.add_trace(go.Scatter(x=np.arange(100, 200, 1), y=pdrPlotData, name="EE = " + str(k)), row=r, col=c)
        print(i)
        # fig.update_layout(
        #     title="Effect of entrapment efficiency and mean particle size on release rate hours (l:g) = " + str(i),
        #     xaxis_title="Entrapment Efficiency (%)",
        #     yaxis_title="Release Rate Hours",
        #
        # )

    return fig

def RRPercentage():
    fig = make_subplots(rows=2, cols=3)

    for i in range(1, 4):
        for k in np.arange(0, 101, 10):
            pdrPlotData = []
            for j in np.arange(100, 200, 1):
                pdrPlotData.append(RRPercentageData(k, i, j)*100)

            if i == 1 or i == 2 or i == 3:
                r = 1
            else:
                r=2
            if i == 1 or i == 4:
                c = 1
            elif i == 2 or i == 5:
                c=2
            else:
                c=3
            fig.add_trace(go.Scatter(x=np.arange(100, 200, 1), y=pdrPlotData, name="EE = " + str(k)), row=r, col=c)
        print(i)
        # fig.update_layout(
        #     title="Effect of entrapment efficiency and mean particle size on release rate hours (l:g) = " + str(i),
        #     xaxis_title="Entrapment Efficiency (%)",
        #     yaxis_title="Release Rate Hours",
        #
        # )

    return fig

def RRRate():
    fig = make_subplots(rows=2, cols=3)

    for i in range(1, 4):
        for k in np.arange(0, 101, 10):
            pdrPlotData = []
            for j in np.arange(100, 200, 1):
                pdrPlotData.append(RRPercentageData(k, i, j)*100/RRHoursData(k, i, j))
            if i == 1 or i == 2 or i == 3:
                r = 1
            else:
                r=2
            if i == 1 or i == 4:
                c = 1
            elif i == 2 or i == 5:
                c=2
            else:
                c=3

            fig.add_trace(go.Scatter(x=np.arange(100, 200, 1), y=pdrPlotData, name="EE = " + str(k)), row=r, col=c)
        print(i)
        # fig.update_layout(
        #     title="Effect of entrapment efficiency and mean particle size on release rate hours (l:g) = " + str(i),
        #     xaxis_title="Entrapment Efficiency (%)",
        #     yaxis_title="Release Rate Hours",
        #
        # )

    return fig


MPSGraph().show()
EEGraph().show()
RRPercentage().show()
RRHours().show()
RRRate().show()




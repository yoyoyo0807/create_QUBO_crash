import plotly.express as px
import pandas as pd

def plot_mesh_map(df, color="risk_score"):
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        size="n_cases",
        color=color,
        color_continuous_scale="RdYlGn_r",
        mapbox_style="carto-positron",
        zoom=11,
        height=600
    )
    return fig


def plot_hospital_map(df):
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        size="stress_score",
        color="stress_score",
        hover_name="hospital_name",
        color_continuous_scale="Reds",
        mapbox_style="carto-positron",
        zoom=11,
        height=600
    )
    return fig

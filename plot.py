import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output

# Load CSV 
file_path = "EEG and ECG data_02_raw.csv"
df = pd.read_csv(file_path, comment="#")

# Channels
eeg_channels = [
    "Fz", "Cz", "P3", "C3", "F3", "F4", "C4", "P4",
    "Fp1", "Fp2", "T3", "T4", "T5", "T6", "O1", "O2",
    "F7", "F8", "A1", "A2", "Pz"
]

ecg_channels = ["X1:LEOG", "X2:REOG"]
ref_channel = "CM"

all_channels = eeg_channels + ecg_channels + [ref_channel]

# Dash App
app = Dash(__name__)

app.layout = html.Div([
    html.H2("EEG & ECG Data Explorer"),

    html.Label("Select Channels:"),
    dcc.Dropdown(
        options=[{"label": ch, "value": ch} for ch in all_channels],
        value=eeg_channels[:5] + ecg_channels,  
        multi=True,
        id="channel-select"
    ),

    html.Label("Normalization:"),
    dcc.RadioItems(
        options=[
            {"label": "Raw Values", "value": "raw"},
            {"label": "Normalized (z-score)", "value": "norm"},
        ],
        value="raw",
        id="normalize-toggle",
        inline=True
    ),

    dcc.Graph(id="eeg-ecg-plot", style={"height": "80vh"})
])

# Callbacks
@app.callback(
    Output("eeg-ecg-plot", "figure"),
    Input("channel-select", "value"),
    Input("normalize-toggle", "value")
)
def update_plot(selected_channels, normalize):
    fig = go.Figure()

    # Apply normalization if selected
    plot_df = df.copy()
    if normalize == "norm":
        plot_df[selected_channels] = (plot_df[selected_channels] - plot_df[selected_channels].mean()) / plot_df[selected_channels].std()

    for ch in selected_channels:
        if ch in eeg_channels or ch == ref_channel:
            fig.add_trace(go.Scatter(
                x=plot_df["Time"], y=plot_df[ch],
                mode="lines", name=ch, yaxis="y1"
            ))
        elif ch in ecg_channels:
            fig.add_trace(go.Scatter(
                x=plot_df["Time"], y=plot_df[ch],
                mode="lines", name=ch, yaxis="y2"
            ))

    fig.update_layout(
        title="EEG & ECG Data Explorer",
        xaxis=dict(title="Time (s)", rangeslider=dict(visible=True)),
        yaxis=dict(title="EEG (µV)", side="left"),
        yaxis2=dict(title="ECG (mV)", overlaying="y", side="right"),
        legend=dict(orientation="h", y=-0.25),
    )
    return fig


# Run
if __name__ == "__main__":
    app.run(debug=True)

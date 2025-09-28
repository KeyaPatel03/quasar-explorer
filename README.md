# EEG + ECG Interactive Explorer
This project is part of the QUASAR Coding Screener.
It loads raw EEG + ECG data from CSV and creates an interactive, scrollable/zoomable explorer using Plotly + Dash.

# Features
Scrollable/Zoomable plot (via Plotly range slider & zoom tools).
Multi-channel selection dropdown (choose EEG/ECG/CM channels).
Normalization toggle (compare signals on same scale with z-score).
Dual y-axes scaling:
EEG channels plotted in µV (left axis).
ECG channels plotted in mV (right axis).
CM reference channel plotted separately (dashed).
Legend toggling → click channel names to show/hide traces.

# Dataset Notes
Lines starting with # are metadata (ignored).
Time column = x-axis (seconds).
EEG channels: Fz, Cz, P3, C3, F3, F4, C4, P4, Fp1, Fp2, T3, T4, T5, T6, O1, O2, F7, F8, A1, A2, Pz
ECG channels: X1:LEOG (Left ECG), X2:REOG (Right ECG)
Reference channel: CM (not ECG, but included as dashed line)
Ignore X3: and other unused columns.

# Installation
1. Clone this repo:
git clone https://github.com/your-username/quasar-explorer.git
cd quasar-explorer

2. Install dependencies:
pip install pandas plotly dash

# Run
python plot.py

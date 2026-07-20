import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.data_loader import load_unified_dataset, get_observations

st.set_page_config(page_title="Ethiopia Financial Inclusion Dashboard", layout="wide")

# ---------- Data loading (cached so it only runs once per session) ----------
@st.cache_data
def load_data():
    data_df, impact_df = load_unified_dataset(
        Path(__file__).resolve().parent.parent / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"
    )
    obs_df = get_observations(data_df)
    events_df = data_df[data_df["record_type"] == "event"].copy()
    events_df["observation_date"] = pd.to_datetime(events_df["observation_date"], errors="coerce")
    return data_df, impact_df, obs_df, events_df

try:
    data_df, impact_df, obs_df, events_df = load_data()
except FileNotFoundError as e:
    st.error(f"Could not load dataset: {e}")
    st.stop()

# ---------- Sidebar navigation ----------
page = st.sidebar.radio("Navigate", ["Overview", "Trends", "Forecasts", "Inclusion Projections"])

st.sidebar.markdown("---")
st.sidebar.caption("Ethiopia Financial Inclusion Forecasting System — Selam Analytics")
# ---------- Overview Page ----------
if page == "Overview":
    st.title("Ethiopia Financial Inclusion: Overview")
    st.markdown("Key metrics tracking Ethiopia's progress toward the NFIS-II financial inclusion targets.")

    acc = obs_df[(obs_df["indicator_code"] == "ACC_OWNERSHIP") & (obs_df["gender"] == "all")].sort_values("observation_date")
    mm = obs_df[obs_df["indicator_code"] == "ACC_MM_ACCOUNT"].sort_values("observation_date")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Account Ownership (Access)", f"{acc['value_numeric'].iloc[-1]:.0f}%",
                   f"+{acc['value_numeric'].iloc[-1] - acc['value_numeric'].iloc[-2]:.0f}pp since {acc['observation_date'].iloc[-2].year}")
    with col2:
        st.metric("Mobile Money Ownership", f"{mm['value_numeric'].iloc[-1]:.1f}%",
                   f"+{mm['value_numeric'].iloc[-1] - mm['value_numeric'].iloc[-2]:.1f}pp since {mm['observation_date'].iloc[-2].year}")
    with col3:
        st.metric("Gender Gap (Access)", "20pp", "unchanged 2021\u21922024")
    with col4:
        st.metric("P2P vs ATM Crossover", "Oct 2024", "P2P volume overtook ATM")

    st.markdown("---")
    st.subheader("Data Coverage Summary")
    col1, col2 = st.columns(2)
    with col1:
        record_counts = data_df["record_type"].value_counts()
        fig = go.Figure(data=[go.Pie(labels=record_counts.index, values=record_counts.values, hole=0.4)])
        fig.update_layout(title="Records by Type", height=350)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        pillar_counts = data_df[data_df["pillar"].notna()]["pillar"].value_counts()
        fig = go.Figure(data=[go.Bar(x=pillar_counts.index, y=pillar_counts.values)])
        fig.update_layout(title="Records by Pillar", height=350)
        st.plotly_chart(fig, use_container_width=True)
# ---------- Trends Page ----------
elif page == "Trends":
    st.title("Trends")
    st.markdown("Explore indicator trends over time. Use the date range selector to zoom into a specific period.")

    indicator_options = sorted(obs_df["indicator_code"].dropna().unique())
    selected_indicators = st.multiselect(
        "Select indicators to compare", indicator_options,
        default=["ACC_OWNERSHIP", "ACC_MM_ACCOUNT"]
    )

    min_date = obs_df["observation_date"].min().date()
    max_date = obs_df["observation_date"].max().date()
    date_range = st.slider("Date range", min_value=min_date, max_value=max_date,
                            value=(min_date, max_date))

    filtered = obs_df[
        (obs_df["indicator_code"].isin(selected_indicators)) &
        (obs_df["observation_date"].dt.date >= date_range[0]) &
        (obs_df["observation_date"].dt.date <= date_range[1]) &
        (obs_df["gender"].isin(["all", np.nan]) | obs_df["gender"].isna())
    ]

    if filtered.empty:
        st.info("No data for this selection.")
    else:
        fig = go.Figure()
        for code in selected_indicators:
            series = filtered[filtered["indicator_code"] == code].sort_values("observation_date")
            if not series.empty:
                fig.add_trace(go.Scatter(
                    x=series["observation_date"], y=series["value_numeric"],
                    mode="lines+markers", name=code
                ))
        fig.update_layout(title="Indicator Trends", height=500, xaxis_title="Date", yaxis_title="Value")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Underlying data")
        st.dataframe(filtered[["observation_date", "indicator_code", "value_numeric", "unit", "source_name"]]
                     .sort_values("observation_date"), use_container_width=True)

        csv = filtered.to_csv(index=False).encode("utf-8")
        st.download_button("Download this data as CSV", csv, "trend_data.csv", "text/csv")
# ---------- Forecasts Page ----------
elif page == "Forecasts":
    st.title("Forecasts")
    st.markdown("Access and Usage projections for 2025-2027, based on trend regression and event-augmented modeling (see Task 3-4 methodology).")

    forecast_table_path = Path(__file__).resolve().parent.parent / "reports" / "final_forecast_table.csv"
    if not forecast_table_path.exists():
        st.warning("Forecast table not found. Run notebooks/04_forecasting.ipynb first.")
    else:
        forecast_df = pd.read_csv(forecast_table_path, parse_dates=["date"])

        model_choice = st.selectbox(
            "Access forecast model",
            ["Base case", "Event-augmented", "Full range (optimistic/pessimistic)"]
        )

        acc_hist = obs_df[(obs_df["indicator_code"] == "ACC_OWNERSHIP") & (obs_df["gender"] == "all")].sort_values("observation_date")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=acc_hist["observation_date"], y=acc_hist["value_numeric"],
                                  mode="lines+markers", name="Observed", line=dict(color="black", width=3)))

        if model_choice == "Base case":
            fig.add_trace(go.Scatter(x=forecast_df["date"], y=forecast_df["access_base"],
                                      mode="lines+markers", name="Base case forecast", line=dict(dash="dash")))
        elif model_choice == "Event-augmented":
            fig.add_trace(go.Scatter(x=forecast_df["date"], y=forecast_df["access_event_augmented"],
                                      mode="lines+markers", name="Event-augmented forecast", line=dict(dash="dash")))
        else:
            fig.add_trace(go.Scatter(x=forecast_df["date"], y=forecast_df["access_optimistic"],
                                      mode="lines", name="Optimistic", line=dict(dash="dot", color="green")))
            fig.add_trace(go.Scatter(x=forecast_df["date"], y=forecast_df["access_pessimistic"],
                                      mode="lines", name="Pessimistic", line=dict(dash="dot", color="firebrick"),
                                      fill="tonexty", fillcolor="rgba(150,150,150,0.15)"))
            fig.add_trace(go.Scatter(x=forecast_df["date"], y=forecast_df["access_base"],
                                      mode="lines+markers", name="Base case", line=dict(color="steelblue")))

        fig.update_layout(title="Access: Account Ownership Forecast", height=450, xaxis_title="Date", yaxis_title="% of adults")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Usage: Mobile Money Account Ownership Forecast")
        mm_hist = obs_df[obs_df["indicator_code"] == "ACC_MM_ACCOUNT"].sort_values("observation_date")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=mm_hist["observation_date"], y=mm_hist["value_numeric"],
                                   mode="lines+markers", name="Observed", line=dict(color="black", width=3)))
        fig2.add_trace(go.Scatter(x=forecast_df["date"], y=forecast_df["usage_mm_account_forecast"],
                                   mode="lines+markers", name="Log-linear forecast", line=dict(dash="dash", color="darkorange")))
        fig2.update_layout(height=400, xaxis_title="Date", yaxis_title="% of adults")
        st.plotly_chart(fig2, use_container_width=True)

        st.caption("Note: the Usage forecast is a proxy (Mobile Money Account Ownership) since no indicator "
                   "natively tagged 'Usage' has enough historical points for a reliable trend fit.")

        st.subheader("Forecast Table")
        st.dataframe(forecast_df, use_container_width=True)
# ---------- Inclusion Projections Page ----------
else:
    st.title("Inclusion Projections")
    st.markdown("Progress toward Ethiopia's National Financial Inclusion Strategy (NFIS-II) targets.")

    forecast_table_path = Path(__file__).resolve().parent.parent / "reports" / "final_forecast_table.csv"
    forecast_df = pd.read_csv(forecast_table_path, parse_dates=["date"])

    nfis_target = 70  # NFIS-II target, % account ownership -- adjust if your target record differs
    target_rows = data_df[data_df["record_type"] == "target"]
    if not target_rows.empty:
        st.caption(f"{len(target_rows)} official target record(s) found in dataset — cross-check the {nfis_target}% figure below against these.")
        st.dataframe(target_rows[["indicator", "value_numeric", "observation_date", "notes"]], use_container_width=True)

    scenario = st.select_slider(
        "Scenario", options=["Pessimistic", "Base case", "Event-augmented", "Optimistic"], value="Base case"
    )
    scenario_col_map = {
        "Pessimistic": "access_pessimistic", "Base case": "access_base",
        "Event-augmented": "access_event_augmented", "Optimistic": "access_optimistic"
    }
    chosen_col = scenario_col_map[scenario]

    acc_hist = obs_df[(obs_df["indicator_code"] == "ACC_OWNERSHIP") & (obs_df["gender"] == "all")].sort_values("observation_date")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=acc_hist["observation_date"], y=acc_hist["value_numeric"],
                              mode="lines+markers", name="Observed", line=dict(color="black", width=3)))
    fig.add_trace(go.Scatter(x=forecast_df["date"], y=forecast_df[chosen_col],
                              mode="lines+markers", name=f"{scenario} forecast", line=dict(dash="dash", color="steelblue")))
    fig.add_hline(y=nfis_target, line_dash="dot", line_color="red",
                  annotation_text=f"NFIS-II Target ({nfis_target}%)", annotation_position="top left")
    fig.update_layout(title=f"Access Progress Toward NFIS-II Target — {scenario} Scenario", height=450,
                       xaxis_title="Date", yaxis_title="% of adults")
    st.plotly_chart(fig, use_container_width=True)

    projected_2027 = forecast_df[chosen_col].iloc[-1]
    gap = nfis_target - projected_2027
    st.metric(f"Projected 2027 Access ({scenario})", f"{projected_2027:.1f}%", f"{gap:.1f}pp short of {nfis_target}% target")

    st.markdown("---")
    st.subheader("Answers to the Consortium's Key Questions")
    st.markdown(f"""
    **What drives financial inclusion in Ethiopia?**
    Infrastructure and mobile money product launches drive Usage strongly, but Access growth
    has decoupled from Usage growth since 2021 — see Trends page and Task 2 insights.

    **How do events affect inclusion outcomes?**
    See the Forecasts page's event-augmented model — EVT_0004 (infrastructure, 2024) is the only
    cataloged event whose modeled effect lands within 2025-2027.

    **How will inclusion look in 2026-2027?**
    Under the {scenario} scenario, Access is projected to reach **{projected_2027:.1f}%** by 2027,
    which is **{gap:.1f} percentage points short** of the {nfis_target}% NFIS-II target.
    """)
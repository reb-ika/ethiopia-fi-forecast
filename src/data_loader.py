"""Data loading utilities for the Ethiopia financial inclusion dataset.

Primary entrypoint is CSV, per the assignment's Project Structure specification:
- data/raw/ethiopia_fi_unified_data.csv
- data/raw/ethiopia_fi_unified_data_impact.csv
- data/raw/reference_codes.csv
"""

from pathlib import Path
import pandas as pd


def load_unified_dataset(data_dir):
    """Load the unified data, impact, and reference code CSVs.

    Parameters
    ----------
    data_dir : str or Path
        Directory containing ethiopia_fi_unified_data.csv,
        ethiopia_fi_unified_data_impact.csv, and reference_codes.csv.

    Returns
    -------
    tuple of (pd.DataFrame, pd.DataFrame, pd.DataFrame)
        (data_df, impact_df, reference_df)

    Raises
    ------
    FileNotFoundError
        If any required CSV is missing from data_dir.
    """
    data_dir = Path(data_dir)
    required_files = {
        "data": "ethiopia_fi_unified_data.csv",
        "impact": "ethiopia_fi_unified_data_impact.csv",
        "reference": "reference_codes.csv",
    }

    missing = [f for f in required_files.values() if not (data_dir / f).exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing required file(s) in {data_dir}: {missing}. "
            f"Place all three CSVs in data/raw/ before running this notebook."
        )

    data_df = pd.read_csv(data_dir / required_files["data"])
    impact_df = pd.read_csv(data_dir / required_files["impact"])
    reference_df = pd.read_csv(data_dir / required_files["reference"])
    return data_df, impact_df, reference_df


def get_observations(data_df):
    """Return only observation-type records, with observation_date parsed
    as datetime (handles mixed string/datetime values from enrichment)."""
    if "record_type" not in data_df.columns:
        raise ValueError("data_df is missing the required 'record_type' column.")

    obs_df = data_df[data_df["record_type"] == "observation"].copy()
    obs_df["observation_date"] = pd.to_datetime(
        obs_df["observation_date"], errors="coerce"
    )
    return obs_df
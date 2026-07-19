"""Data loading utilities for the Ethiopia financial inclusion dataset."""

from pathlib import Path
import pandas as pd


def load_unified_dataset(file_path):
    """Load the unified data and impact sheets from the Ethiopia FI dataset.

    Parameters
    ----------
    file_path : str or Path
        Path to the .xlsx file containing 'ethiopia_fi_unified_data' and
        'Impact_sheet' sheets.

    Returns
    -------
    tuple of (pd.DataFrame, pd.DataFrame)
        (data_df, impact_df)

    Raises
    ------
    FileNotFoundError
        If file_path does not exist.
    ValueError
        If the expected sheets are missing from the file.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {file_path}. "
            f"Place the starter file in data/raw/ before running this notebook."
        )

    try:
        xls = pd.ExcelFile(file_path)
    except Exception as e:
        raise ValueError(f"Could not open {file_path} as an Excel file: {e}")

    required_sheets = {"ethiopia_fi_unified_data", "Impact_sheet"}
    missing = required_sheets - set(xls.sheet_names)
    if missing:
        raise ValueError(
            f"Expected sheet(s) {missing} not found in {file_path}. "
            f"Found sheets: {xls.sheet_names}"
        )

    data_df = pd.read_excel(file_path, sheet_name="ethiopia_fi_unified_data")
    impact_df = pd.read_excel(file_path, sheet_name="Impact_sheet")
    return data_df, impact_df


def get_observations(data_df):
    """Return only the observation-type records, with observation_date parsed
    as datetime (handles mixed string/datetime values from enrichment)."""
    if "record_type" not in data_df.columns:
        raise ValueError("data_df is missing the required 'record_type' column.")

    obs_df = data_df[data_df["record_type"] == "observation"].copy()
    obs_df["observation_date"] = pd.to_datetime(
        obs_df["observation_date"], errors="coerce"
    )
    return obs_df
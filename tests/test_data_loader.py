import sys
from pathlib import Path
import pytest
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.data_loader import load_unified_dataset, get_observations


def test_load_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_unified_dataset("data/raw/does_not_exist.xlsx")


def test_get_observations_missing_column_raises():
    df = pd.DataFrame({"not_record_type": [1, 2, 3]})
    with pytest.raises(ValueError):
        get_observations(df)


def test_get_observations_filters_correctly():
    df = pd.DataFrame({
        "record_type": ["observation", "event", "observation"],
        "observation_date": ["2024-01-01", "2024-02-01", pd.Timestamp("2024-03-01")],
    })
    result = get_observations(df)
    assert len(result) == 2
    assert pd.api.types.is_datetime64_any_dtype(result["observation_date"])
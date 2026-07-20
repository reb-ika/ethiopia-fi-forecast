# Forecasting Financial Inclusion in Ethiopia

Week 11 capstone — 10 Academy Kifiya AI Mastery Program. Client: Selam Analytics,
building a forecasting system for Ethiopia's Access (Account Ownership) and Usage
(Digital Payment Adoption) indicators through 2027.

## Project Structure

| Folder | Contents |
|---|---|
| `data/raw/` | Original starter files (gitignored — not tracked, see below) |
| `data/processed/` | Enriched/cleaned datasets produced by notebooks |
| `notebooks/` | Analysis notebooks, one per task |
| `src/` | Reusable, tested functions (data loading, transforms) |
| `tests/` | Unit tests for `src/` |
| `dashboard/` | Streamlit app (Task 5) |
| `reports/` | Generated charts (`reports/figures/`) and written reports |
| `models/` | Saved forecasting models (Task 4) |

**Note on `data/`:** raw data files are excluded from version control via `.gitignore`
since they contain client-provided data. To reproduce this analysis, place
`ethiopia_fi_unified_data.xlsx`, `reference_codes.xlsx`, and
`Additional Data Points Guide.xlsx` into `data/raw/` before running the notebooks.

## Deliverables

| Task | Notebook | Key Outputs |
|---|---|---|
| Task 1: Enrichment | [`notebooks/01_data_exploration.ipynb`](notebooks/01_data_exploration.ipynb) | `data/processed/ethiopia_fi_unified_data_enriched.xlsx`, [`data_enrichment_log.md`](data_enrichment_log.md) |
| Task 2: EDA | [`notebooks/02_eda.ipynb`](notebooks/02_eda.ipynb) | [`reports/figures/`](reports/figures/), [`reports/key_insights.md`](reports/key_insights.md) |
| Interim Report | — | [`reports/interim_report.docx`](reports/interim_report.docx) |

## Setup
```**Required raw data files** (place in `data/raw/` before running notebooks):
- `ethiopia_fi_unified_data.csv`
- `ethiopia_fi_unified_data_impact.csv`
- `reference_codes.csv`
```
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

```
## Running the Dashboard

```powershell
.\venv\Scripts\Activate.ps1
streamlit run dashboard\app.py
```

Then open http://localhost:8501 in your browser. Requires `data/processed/ethiopia_fi_unified_data_enriched.xlsx` to exist (produced by `notebooks/01_data_exploration.ipynb`).
## Author

Rebika Woldeyesus 

## Task 4: Forecast Interpretation

**Access (Account Ownership) forecast, 2025-2027:**
- Base case: 52.3% (2025) -> 54.2% (2026) -> 56.0% (2027)
- Event-augmented (adds EVT_0004 infrastructure effect landing Jan 2026): 53.8% -> 55.7% -> 57.5%
- Range: pessimistic 50.1-52.2%, optimistic 54.4-59.9%

Access growth is forecast to continue decelerating relative to 2014-2021 rates. The
scenario band (2.2-7.7pp spread by 2027) reflects genuine uncertainty from only 4
historical data points spanning two different growth regimes (fast 2014-21, slow
2021-24). The event-augmented estimate adds a modest +1.5pp from EVT_0004's
infrastructure investment, the only cataloged event whose lagged effect lands within
the forecast window for this indicator.

**Usage (Mobile Money Account Ownership, proxy) forecast, 2025-2027:**
- Log-linear trend: 16.7% (2025) -> 23.2% (2026) -> 32.3% (2027), ~39%/year growth

This series is growing far faster than Access, consistent with the Task 2 finding that
usage is outpacing access. However, this forecast should be treated as an upper-bound
scenario: it is fit on only 3 points, the fitted 2025 value (16.7%) undershoots the
actual observed 2025 value (19.4%) by ~3pp, and sustained 39%/year growth is unlikely
to continue indefinitely as the market matures and early-adopter effects fade.

**Which events matter most:** EVT_0001 (Telebirr) remains the most consequential event
in the dataset by breadth of effect (3 indicators), though its Access effect was
revised down in Task 3 validation. EVT_0004 (infrastructure, Jan 2024) is the only event
whose modeled effect on Access lands within the 2025-2027 forecast window, making it the
single most relevant upcoming driver in this model -- though this also reflects a
limitation: only one event's lag places it in-window, so the event-augmented model may
understate real-world event effects that this dataset simply hasn't captured.

**Key uncertainties:**
- Only 4 (Access) and 3 (Usage proxy) real data points underlie these forecasts --
  standard for Findex-based work given its 3-year survey cycle, but it means every
  forecast here should be read as directional, not precise.
- No Usage-pillar indicator has 3+ clean points; ACC_MM_ACCOUNT (technically an Access
  sub-indicator) was used as the best available Usage proxy. A true "digital payment
  adoption" forecast would need additional Findex disaggregation data not present in
  this dataset.
- The event-augmented model relies on the categorical-to-numeric magnitude conversion
  from Task 3, an explicit simplification rather than a fitted relationship.

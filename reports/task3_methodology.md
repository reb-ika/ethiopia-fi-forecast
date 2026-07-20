
## Task 3: Event Impact Modeling - Methodology

**Approach:** Impact links (event -> indicator relationships) were encoded as a signed
numeric score: magnitude (low=1, medium=2, high=3) multiplied by direction (+1 increase,
-1 decrease). This produces a single comparable score per event-indicator pair, visualized
as a heatmap association matrix (rows=events, columns=indicators).

**Effect timing:** Effects are modeled as taking hold after `lag_months` from the event
date, per the lag_months field already present in the impact_link schema. This project
does not model gradual ramp-up within the lag window (e.g. a smooth curve) -- effects are
treated as a step change at lag_months, which is a simplification given how sparse the
underlying observation data is (most indicators have 1-3 points total, insufficient to
fit a more complex functional form).

**Combining multiple events:** Where multiple events affect the same indicator (e.g. 4
separate events all target USG_P2P_COUNT), this analysis treats their signed scores as
additive rather than modeling interaction effects, since there is no evidence in the
dataset to support a more complex combination rule.

**Validation:** The Telebirr launch (EVT_0001) impact estimate was tested against observed
Access and mobile-money-account trends (see task3_validation.md). The USG_TELEBIRR_USERS
and USG_P2P_COUNT estimates were supported by the data; the ACC_OWNERSHIP estimate was not
and was revised from "high" to "low" magnitude accordingly.

**Key assumptions and limitations:**
- Impact magnitudes (low/medium/high) are ordinal estimates based on literature, empirical
  Ethiopian data where available, or theoretical reasoning where not -- they are not derived
  from a fitted statistical model, given data sparsity.
- EVT_0009 (Sep 2021 policy) has no impact_link -- no quantified effect was found in
  available sources, and none was estimated to avoid introducing unsupported guesses.
- Only one event (EVT_0001/Telebirr) could be validated against real before/after data
  with reasonable confidence; the remaining 9 events' estimates rely more heavily on
  comparable-country evidence and are correspondingly lower-confidence.

# Data Enrichment Log

Generated 2026-07-19 by Rebika

## New Observations (10)
- **REC_0034** | ACC_OWNERSHIP = 36 percentage (2024-12-31) | confidence: high | source: Global Findex 2025 (via Shega)
  - Notes: Women's account ownership 2024 Findex; gender gap component
  - URL: https://shega.co/news/findex-2025-and-ethiopias-digital-financial-leap-momentum-without-maturity
- **REC_0035** | ACC_OWNERSHIP = 56 percentage (2024-12-31) | confidence: high | source: Global Findex 2025 (via Shega)
  - Notes: Men's account ownership 2024 Findex; gender gap component
  - URL: https://shega.co/news/findex-2025-and-ethiopias-digital-financial-leap-momentum-without-maturity
- **REC_0036** | ACC_MM_ACCOUNT = 19.4 percentage (2025-12-31) | confidence: high | source: Global Findex 2025 (via Shega)
  - Notes: Mobile money account ownership quadrupled from 4.7% (2021) to 19.4% (2025)
  - URL: https://shega.co/news/findex-2025-and-ethiopias-digital-financial-leap-momentum-without-maturity
- **REC_0037** | ACC_4G_COV = 70.8 percentage (2025-06-30) | confidence: medium | source: Ethio Telecom / GSMA
  - Notes: Single-operator (Ethio Telecom) 4G coverage, up from 33% in 2023 — not full-market figure
  - URL: https://en.wikipedia.org/wiki/Ethio_Telecom
- **REC_0038** | ACC_FAYDA = 15 millions (2025-05-31) | confidence: high | source: ID4Africa 2025 / ID Tech
  - Notes: Fayda enrollment as of May 2025
  - URL: https://idtechwire.com/ethiopia-launches-fayda-digital-id-system-to-cover-90-million-citizens-by-2027/
- **REC_0039** | ACC_FAYDA = 16.4 millions (2025-06-04) | confidence: high | source: Biometric Update
  - Notes: Fayda enrollment as of June 4, 2025
  - URL: https://www.biometricupdate.com/202607/ethiopia-partners-with-safaricom-to-run-digital-id-enrollment-in-7-regions
- **REC_0040** | ACC_FAYDA = 28 millions (2025-11-01) | confidence: high | source: EBC
  - Notes: Fayda enrollment ~Nov 2025; target 60M by mid-2026
  - URL: https://www.ebc.et/english/Home/NewsDetails?NewsId=2981
- **REC_0041** | ACC_FAYDA = 46.5 millions (2026-07-12) | confidence: high | source: Biometric Update
  - Notes: Most recent Fayda enrollment figure
  - URL: https://www.biometricupdate.com/202607/ethiopia-partners-with-safaricom-to-run-digital-id-enrollment-in-7-regions
- **REC_0042** | USG_P2P_VALUE = 577.7 billion_birr (nan) | confidence: high | source: EthSwitch Annual Report (via The Reporter Ethiopia)
  - Notes: 128.3M P2P transactions, FY2024/25
  - URL: https://www.thereporterethiopia.com/47608/
- **REC_0043** | USG_ATM_VALUE = 156 billion_birr (nan) | confidence: high | source: EthSwitch Annual Report (via The Reporter Ethiopia)
  - Notes: ~120M ATM withdrawals, FY2024/25; P2P value now exceeds this
  - URL: https://www.thereporterethiopia.com/47608/

## New Events (1)
- **REC_0044** | category: product_launch | date: 2025-12-01 | confidence: medium | source: Capital Newspaper
  - Notes: EthSwitch launched 'Ethiopay' unified national digital payment brand integrating mobile/digital payment services
  - URL: https://capitalethiopia.com/2025/12/21/ethswitch-launches-ethiopay-to-unify-national-digital-paymentsby-our-staff-reporter/

## New Impact Links (3)
- **IMP_0015** | EVT_0006 → USG_CROSSOVER (increase, high, lag 0mo) | evidence: empirical | confidence: high
  - Notes: P2P interoperable transaction volume exceeded ATM withdrawal volume for first time, Oct 2024; P2P value also surpassed ATM value in FY24/25
- **IMP_0016** | REC_0044 → USG_P2P_COUNT (increase, medium, lag 6mo) | evidence: theoretical | confidence: low
  - Notes: EthioPay brand unification launched Dec 2025; too recent for empirical evidence, estimate is theoretical based on stated goal of unifying fragmented digital payment services
- **IMP_0017** | REC_0044 → ACC_MM_ACCOUNT (increase, low, lag 12mo) | evidence: theoretical | confidence: low
  - Notes: Unified branding may reduce friction/confusion across mobile money providers, modestly aiding account adoption

## Data Quality Notes
- Real observation date range (excluding target rows): 2014-12-31 to 2025-12-31
- Most indicators have only 1-2 data points; only ACC_OWNERSHIP (6) and ACC_FAYDA (now 7 with enrichment) support real trend analysis
- EVT_0006 previously had no impact_link — now filled with empirical evidence (see above)
- EVT_0009 (policy, 2021-09-01) still has no impact_link — no quantified before/after effect found; documented as a genuine data gap, not estimated
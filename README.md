# Business Development Intelligence System

**Automated Lead Identification, Enrichment, and Ranking for 3D In-Vitro Model Adoption**

---

## Project Overview

The **Business Development Intelligence System** is an end-to-end data pipeline and dashboard designed to help business development teams **identify, enrich, and prioritize high-probability leads** for **3D in-vitro models used in drug discovery and therapy design**.

The system automates what is traditionally a manual and error-prone workflow involving PubMed reviews, conference scanning, and funding research, and replaces it with a **repeatable, explainable, and configurable intelligence pipeline**.

The final output is a **ranked, searchable, and exportable dashboard** showing decision-makers most likely to engage, based on scientific intent, organizational readiness, and budget signals.

---

## Problem Statement

Business development in biotech faces three core challenges:

1. **Low signal-to-noise**: Thousands of scientists exist, but only a small subset are relevant, funded, and ready to engage.
2. **Manual research overhead**: LinkedIn searches, PubMed reviews, and funding checks are slow and inconsistent.
3. **Poor prioritization**: Teams lack a systematic way to decide *who to contact first*.

This system addresses these challenges by turning publicly available scientific, professional, and business data into a **prioritized lead list with an explainable propensity-to-buy score**.

---

## System Architecture

The system is organized into three sequential stages, followed by a presentation layer:

```
→ Stage 1: Identification
→ Stage 2: Enrichment
→ Stage 3: Ranking
→ Lead Generation Dashboard
```

Each stage is independently runnable and testable, but also orchestrated through a single pipeline runner.

---

## Stage 1: Identification (Candidate Discovery)

**Objective:**
Maximize recall by identifying all *potentially relevant* individuals before any scoring or filtering.

**Data Sources:**

* LinkedIn / Sales Navigator results provided as a pre-generated CSV export (e.g., from Clay) located in `src/data/input/`
* Scientific publication databases (PubMed)
* Biomedical conferences (SOT, AACR, ISSX, ACT)

**What is identified:**

* Scientists and decision-makers in toxicology, safety, hepatic biology, and preclinical research
* Authors of recent (last 24 months) relevant publications
* Conference speakers, poster presenters, and exhibitors

**Output:**

* `stage1_candidates.csv`
* Each candidate retains **source evidence** (LinkedIn / PubMed / Conference) without scoring

This stage intentionally allows noise and duplicates, prioritizing **coverage over precision** to avoid missing high-value leads.

---

## Stage 2: Enrichment (Data Augmentation)

**Objective:**
Convert identified candidates into **BD-ready profiles** by adding contactability, geographic clarity, and budget context.

**Enrichment Signals:**

### Person-level

* Business email and phone (Apollo, with mock fallback)
* Job title normalization
* Employment tenure (new-hire signal)
* Person location (remote vs office)

### Company-level

* Company HQ location
* Funding stage (Seed, Series A, Series B, Public, Grant-funded)
* Academic vs industry classification

### Scientific & Academic

* Active researcher flag
* Publication count
* NIH grant detection (NIH RePORTER)

**Output:**

* `stage2_enriched.csv`

At this stage, **no ranking is applied**. The goal is to gather all evidence required for scoring.

---

## Stage 3: Ranking (Propensity-to-Buy Engine)

**Objective:**
Assign an explainable **0–100 probability score** representing the likelihood that a person wants to work with 3D in-vitro models.

### Scoring Model

The model is **rule-based, deterministic, and fully explainable**, aligned exactly with the assignment rubric.

| Signal Category   | Criteria                                      | Weight |
| ----------------- | --------------------------------------------- | ------ |
| Role Fit          | Toxicology, Safety, Hepatic, 3D roles         | +30    |
| Scientific Intent | Recent publication on liver toxicity / DILI   | +40    |
| Company Intent    | Series A / B funding                          | +20    |
| Technographic     | Uses or is open to advanced models (proxy)    | +15    |
| Location          | Biotech hubs (Boston, Cambridge, Basel, etc.) | +10    |
| Tenure            | New hire (<2.5 years)                         | +5     |

All weights, keywords, and hub locations are **externalized into YAML configuration files**.

**Output:**

* `stage3_ranked_leads.csv`
* Includes score breakdown for transparency

---

## Configuration-Driven Design

All business logic is configurable without code changes:

### Config Files

* `keywords.yaml` – role and scientific keywords
* `hubs.yaml` – geographic hubs
* `scoring_weights.yaml` – scoring weights

This allows:

* Rapid tuning by Business Development teams
* Easy regional or therapeutic focus changes
* Auditability of scoring logic

---

## Pipeline Orchestration

The system provides a **single CLI entry point** that runs all stages in order.

### Modes

* **Dummy mode**: Uses mock enrichment (no paid APIs)
* **Actual mode**: Uses real APIs when keys are provided

### Command

```bash
python -m src.pipeline.run_all --mode dummy
python -m src.pipeline.run_all --mode actual
```

Each stage can also be run independently for debugging or development.

---

## Lead Generation Dashboard (Final Output)

The final output is a **Streamlit web dashboard** designed for business users.

### Features

* Ranked lead table
* Free-text search (e.g. “Boston”, “Oncology”)
* Clear split between person location and company HQ
* Action column for outreach prioritization
* CSV and Excel export (strict schema)

### Display Columns

* Rank
* Probability
* Name
* Title
* Company
* Location
* HQ
* Email
* LinkedIn
* Action

### Run Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

## Project Structure

```
src/
├── config/
│   ├── keywords.yaml
│   ├── hubs.yaml
│   └── scoring_weights.yaml
│
├── ingestion/              # Stage 1
├── enrichment/             # Stage 2
├── scoring/                # Stage 3
├── pipeline_run_all.py     # Orchestration
├── dashboard/              # Streamlit UI
├── data/                   # CSV outputs
```

---

## Legal and Ethical Considerations

* No direct LinkedIn scraping
* Professional data accessed via compliant tools (Clay, Apollo)
* Scientific data sourced from public APIs (PubMed, NIH RePORTER)
* Dummy mode enables safe demos without API keys

---

## Future Enhancements

* Machine-learning based scoring layer
* CRM integrations (HubSpot / Salesforce)
* Conference site scrapers
* Multi-region hub configuration
* Lead status tracking

---

# Twitter Analytics Pet Project

This repository demonstrates a full analytics pipeline on social media data  
using a **Twitter dataset from Kaggle** ([link](https://www.kaggle.com/sudishbasnet/truthseekertwitterdataset2023)).

---

## 📁 Project Structure

```
data/           Raw CSV files downloaded from Kaggle  
notebooks/      Jupyter Notebook (eda.ipynb) with exploratory data analysis  
scripts/        ETL scripts:  
                - create_tables.py: defines and creates PostgreSQL tables  
                - etl.py: loads, cleans, and populates tables from CSV  
docs/           Generated HTML report (EDA_report.html)  
venv/           Python virtual environment  
requirements.txt Python dependencies  
README.md       This file  
```

---

## 🔎 Quick View

The HTML report of the analysis is already available. To review results  
without running any code, simply open:

```bash
open docs/EDA_report.html
```

---

## 🛠️ Reproduce Locally

_If you want to run the pipeline yourself:_

1. **Clone the repository**

   ```bash
   git clone https://github.com/USERNAME/twitter_analytics.git
   cd twitter_analytics
   ```

2. **Set up Python environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Create PostgreSQL tables**

   ```bash
   python3 scripts/create_tables.py
   ```

4. **Load & clean the data**

   ```bash
   python3 scripts/etl.py
   ```

5. **Launch the notebook**

   ```bash
   jupyter lab notebooks/eda.ipynb
   ```

---

## 📊 Key Insights

1. **Balanced labels** — `majority_target` and `binary_num_target` are roughly equal, enabling unbiased modeling.  
2. **Heavy-tailed user metrics** — follower/friend counts and tweet volumes have long tails; most users are small, a few are mega-influencers.  
3. **Uneven engagement** — most tweets get minimal reactions; a few go viral with thousands of retweets/likes.  
4. **Likes ↔ Retweets correlation** — nearly perfect correlation (r ≈ 0.95), while user reach correlates weakly (r ≈ 0.07).  
5. **Stable text stats** — tweets average ~40 words and ~5–6 characters per word, simplifying NLP feature engineering.  

---
## 📊 Hashtag A/B Test

We perform a retrospective A/B-style analysis to measure the impact of hashtags:

### 🔬 Option 1: Run the Notebook

```bash
jupyter lab notebooks/ab_test_hashtags.ipynb
```

> Execute all cells in order.

---

### ⚙️ Option 2: Run the Script

```bash
./scripts/analyze_ab_test.py
```

This script will:

- Load data from your Postgres database.
- Define two groups:
  - **Group A** — tweets without hashtags.
  - **Group B** — tweets with hashtags.
- Stratify `followers_count` into 10 quantile bins.
- Compute average values for:
  - retweets,
  - favourites,
  - engagement rate.
- Perform:
  - Welch’s t-test,
  - Mann–Whitney U test.
- Print a summary table and p-values.

---

Enjoy exploring and extending this analysis!
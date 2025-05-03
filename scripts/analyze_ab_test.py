#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu
from sqlalchemy import create_engine

def main():
    engine = create_engine("postgresql://localhost/postgres")
    tweets         = pd.read_sql_table("tweets", engine, index_col="tweet_idx")
    tweet_metrics  = pd.read_sql_table("tweet_metrics", engine, index_col="tweet_idx")
    author_metrics = pd.read_sql_table("author_metrics", engine, index_col="tweet_idx")
    df = tweets.join(tweet_metrics).join(author_metrics)

    df["group"] = np.where(df["hashtags"] > 0, "B", "A")
    print("Initial group sizes:\n", df.group.value_counts(), "\n")

    df["foll_bin"] = pd.qcut(df["followers_count"], q=10, duplicates="drop")
    balanced = []
    for _, sub in df.groupby("foll_bin"):
        b_sub = sub[sub.group=="B"]
        a_sub = sub[sub.group=="A"]
        n_b = len(b_sub)
        if n_b == 0:
            continue
        a_sample = a_sub.sample(n=n_b, random_state=42)
        balanced.append(pd.concat([b_sub, a_sample]))
    df_bal = pd.concat(balanced).reset_index(drop=True)
    print("Balanced group sizes:\n", df_bal.group.value_counts(), "\n")

    summary = df_bal.groupby("group").agg(
        mean_rt   = ("retweets",  "mean"),
        std_rt    = ("retweets",  "std"),
        n_tweets  = ("retweets",  "count"),
        mean_fav  = ("favourites","mean"),
    )
    tot_rt     = df_bal.groupby("group")["retweets"].sum()
    tot_fav    = df_bal.groupby("group")["favourites"].sum()
    tot_follow = df_bal.groupby("group")["followers_count"].sum()
    summary["eng_rate"] = (tot_rt + tot_fav) / tot_follow
    print("=== Aggregated metrics (balanced) ===")
    print(summary.round(3), "\n")

    a = df_bal[df_bal.group=="A"]["retweets"]
    b = df_bal[df_bal.group=="B"]["retweets"]
    t_stat, p_t = ttest_ind(b, a, equal_var=False)
    u_stat, p_u = mannwhitneyu(b, a, alternative="two-sided")
    print(f"Welch t-test:       t = {t_stat:.3f}, p = {p_t:.3f}")
    print(f"Mann–Whitney U-test: U = {u_stat:.3f}, p = {p_u:.3f}")

if __name__ == "__main__":
    main()
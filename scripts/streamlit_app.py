import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

DB_URL = "postgresql://localhost/postgres"

@st.cache_resource
def get_engine():
    return create_engine(DB_URL)

@st.cache_data
def load_data():
    engine = get_engine()
    tweets = pd.read_sql_table("tweets", engine)
    author_metrics = pd.read_sql_table("author_metrics", engine)
    tweet_metrics = pd.read_sql_table("tweet_metrics", engine)
    return tweets, author_metrics, tweet_metrics

tweets, author_metrics, tweet_metrics = load_data()

st.sidebar.header("Filters & Metrics")
label_opt = st.sidebar.selectbox("majority_target:", ["All", True, False])
if label_opt != "All":
    mask = tweets["majority_target"] == label_opt
    ftweets = tweets[mask].copy()
    ft_metrics = tweet_metrics.loc[mask.values].copy()
else:
    ftweets = tweets.copy()
    ft_metrics = tweet_metrics.copy()

metric = st.sidebar.selectbox(
    "Select metric:",
    ["Tweet count", "Unique authors", "Avg retweets", "Avg favourites"]
)

if metric == "Tweet count":
    metric_value = len(ftweets)
elif metric == "Unique authors":
    metric_value = ftweets["tweet_idx"].nunique()
elif metric == "Avg retweets":
    metric_value = ft_metrics["retweets"].mean().round(2)
else:
    metric_value = ft_metrics["favourites"].mean().round(2)

st.title("Twitter Analytics Dashboard")
st.subheader("Current Metric")
st.metric(metric, metric_value)

# Top 10 Authors by Followers
top_auth = author_metrics.nlargest(10, "followers_count")
fig1 = px.bar(
    top_auth,
    x="followers_count",
    y=top_auth.index.astype(str),
    orientation="h",
    title="Top 10 Authors by Followers",
)
st.plotly_chart(fig1, use_container_width=True)

# Retweet Distribution
fig2 = px.histogram(ft_metrics, x="retweets", nbins=50, title="Retweet Distribution")
st.plotly_chart(fig2, use_container_width=True)

# Retweets vs Likes
sample = ft_metrics.sample(min(1000, len(ft_metrics)), random_state=1)
fig3 = px.scatter(sample, x="retweets", y="favourites", title="Retweets vs Likes (sample)")
st.plotly_chart(fig3, use_container_width=True)

# Top 5 Tweets by Engagement
st.write("### Top 5 Tweets by Retweets")
top_rt = ft_metrics.nlargest(5, "retweets").copy()
# присоединяем текст из ftweets по индексу
top_rt = top_rt.join(ftweets.set_index("tweet_idx")["tweet_text"])
st.dataframe(top_rt[["tweet_text", "retweets", "favourites"]])

st.write("### Top 5 Tweets by Favourites")
top_fav = ft_metrics.nlargest(5, "favourites").copy()
top_fav = top_fav.join(ftweets.set_index("tweet_idx")["tweet_text"])
st.dataframe(top_fav[["tweet_text", "retweets", "favourites"]])
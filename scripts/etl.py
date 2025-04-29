import pandas as pd
from sqlalchemy import create_engine

CSV_PATH = '../data/truthseeker_twitter/Twitter Analysis.csv'
ENGINE_URL = "postgresql://localhost/postgres"

engine = create_engine(ENGINE_URL)

df = pd.read_csv(CSV_PATH)

df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(' ', '_', regex=False)
      .str.replace('%', '_pct', regex=False)
      .str.replace('-', '_', regex=False)
)

df.rename(columns={
    'tweet': 'tweet_text',
    'binarynumtarget': 'binary_num_target',
    'botscore': 'bot_score',
    'botscorebinary': 'bot_binary',
    'average_word_length': 'avg_word_length'
}, inplace=True)

df.drop_duplicates(subset=['tweet_text'], inplace=True)

df.reset_index(drop=True, inplace=True)


tweets_df = df[[
    'majority_target',
    'statement',
    'binary_num_target',
    'tweet_text'
]].copy()

tweets_df.to_sql(
    'tweets',
    engine,
    if_exists='replace',
    index=True,
    index_label='tweet_idx'
)

def load_table(name, cols):
    tbl = df[cols].copy()
    tbl.to_sql(
        name,
        engine,
        if_exists='replace',
        index=True,
        index_label='tweet_idx'
    )

load_table('author_metrics', [
    'followers_count','friends_count','favourites_count','statuses_count',
    'listed_count','following','bot_score','bot_binary','cred','normalize_influence'
])

load_table('tweet_metrics', [
    'mentions','quotes','replies','retweets','favourites',
    'hashtags','urls','unique_count','total_count'
])

entity_cols = [c for c in df.columns if c.endswith('_pct')]
load_table('entity_features', entity_cols)

load_table('text_features', [
    'word_count','max_word_length','min_word_length','avg_word_length',
    'present_verbs','past_verbs','adjectives','adverbs','adpositions',
    'pronouns','tos','determiners','conjunctions','dots',
    'exclamation','questions','ampersand','capitals','digits',
    'long_word_freq','short_word_freq'
])

load_table('embeddings', ['embeddings'])

print("ETL завершён успешно.")
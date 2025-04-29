## Таблица tweets
- tweet_idx         SERIAL PRIMARY KEY
- majority_target   VARCHAR
- statement         TEXT
- binary_num_target INTEGER
- tweet_text        TEXT

## Таблица author_metrics
- tweet_idx           INTEGER PRIMARY KEY
- followers_count     INTEGER
- friends_count       INTEGER
- favourites_count    INTEGER
- statuses_count      INTEGER
- listed_count        INTEGER
- following           INTEGER
- bot_score           FLOAT
- bot_binary          INTEGER
- cred                FLOAT
- normalize_influence FLOAT

## Таблица tweet_metrics
- tweet_idx     INTEGER PRIMARY KEY
- mentions      INTEGER
- quotes        INTEGER
- replies       INTEGER
- retweets      INTEGER
- favourites    INTEGER
- hashtags      INTEGER
- urls          INTEGER
- unique_count  INTEGER
- total_count   INTEGER

## Таблица entity_features
- tweet_idx     INTEGER PRIMARY KEY
- org_pct       FLOAT
- norp_pct      FLOAT
- gpe_pct       FLOAT
- person_pct    FLOAT
- money_pct     FLOAT
- date_pct      FLOAT
- cardinal_pct  FLOAT
- percent_pct   FLOAT
- ordinal_pct   FLOAT
- fac_pct       FLOAT
- law_pct       FLOAT
- product_pct   FLOAT
- event_pct     FLOAT
- time_pct      FLOAT
- loc_pct       FLOAT
- work_of_art_pct FLOAT
- quantity_pct  FLOAT
- language_pct  FLOAT

## Таблица text_features
- tweet_idx         INTEGER PRIMARY KEY
- word_count        INTEGER
- max_word_length   INTEGER
- min_word_length   INTEGER
- avg_word_length   FLOAT
- present_verbs     INTEGER
- past_verbs        INTEGER
- adjectives        INTEGER
- adverbs           INTEGER
- adpositions       INTEGER
- pronouns          INTEGER
- tos               INTEGER
- determiners       INTEGER
- conjunctions      INTEGER
- dots              INTEGER
- exclamation       INTEGER
- questions         INTEGER
- ampersand         INTEGER
- capitals          INTEGER
- digits            INTEGER
- long_word_freq    FLOAT
- short_word_freq   FLOAT

## Таблица embeddings
- tweet_idx   INTEGER PRIMARY KEY
- embeddings  TEXT

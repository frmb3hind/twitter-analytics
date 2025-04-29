from sqlalchemy import (
    Column, Integer, String, Text, Float,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ENGINE_URL = "postgresql://localhost/postgres"
engine = create_engine(ENGINE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Tweets(Base):
    __tablename__ = "tweets"
    tweet_idx         = Column(Integer, primary_key=True)
    majority_target   = Column(String)
    statement         = Column(Text)
    binary_num_target = Column(Integer)
    tweet_text        = Column(Text)

class AuthorMetrics(Base):
    __tablename__ = "author_metrics"
    tweet_idx           = Column(Integer, primary_key=True)
    followers_count     = Column(Integer)
    friends_count       = Column(Integer)
    favourites_count    = Column(Integer)
    statuses_count      = Column(Integer)
    listed_count        = Column(Integer)
    following           = Column(Integer)
    bot_score           = Column(Float)
    bot_binary          = Column(Integer)
    cred                = Column(Float)
    normalize_influence = Column(Float)

class TweetMetrics(Base):
    __tablename__ = "tweet_metrics"
    tweet_idx    = Column(Integer, primary_key=True)
    mentions     = Column(Integer)
    quotes       = Column(Integer)
    replies      = Column(Integer)
    retweets     = Column(Integer)
    favourites   = Column(Integer)
    hashtags     = Column(Integer)
    urls         = Column(Integer)
    unique_count = Column(Integer)
    total_count  = Column(Integer)

class EntityFeatures(Base):
    __tablename__ = "entity_features"
    tweet_idx        = Column(Integer, primary_key=True)
    org_pct          = Column(Float)
    norp_pct         = Column(Float)
    gpe_pct          = Column(Float)
    person_pct       = Column(Float)
    money_pct        = Column(Float)
    date_pct         = Column(Float)
    cardinal_pct     = Column(Float)
    percent_pct      = Column(Float)
    ordinal_pct      = Column(Float)
    fac_pct          = Column(Float)
    law_pct          = Column(Float)
    product_pct      = Column(Float)
    event_pct        = Column(Float)
    time_pct         = Column(Float)
    loc_pct          = Column(Float)
    work_of_art_pct  = Column(Float)
    quantity_pct     = Column(Float)
    language_pct     = Column(Float)

class TextFeatures(Base):
    __tablename__ = "text_features"
    tweet_idx         = Column(Integer, primary_key=True)
    word_count        = Column(Integer)
    max_word_length   = Column(Integer)
    min_word_length   = Column(Integer)
    avg_word_length   = Column(Float)
    present_verbs     = Column(Integer)
    past_verbs        = Column(Integer)
    adjectives        = Column(Integer)
    adverbs           = Column(Integer)
    adpositions       = Column(Integer)
    pronouns          = Column(Integer)
    tos               = Column(Integer)
    determiners       = Column(Integer)
    conjunctions      = Column(Integer)
    dots              = Column(Integer)
    exclamation       = Column(Integer)
    questions         = Column(Integer)
    ampersand         = Column(Integer)
    capitals          = Column(Integer)
    digits            = Column(Integer)
    long_word_freq    = Column(Float)
    short_word_freq   = Column(Float)

class Embeddings(Base):
    __tablename__ = "embeddings"
    tweet_idx  = Column(Integer, primary_key=True)
    embeddings = Column(Text)

if __name__ == "__main__":
    print("Creating all tables…")
    Base.metadata.create_all(engine)
    print("Done.")
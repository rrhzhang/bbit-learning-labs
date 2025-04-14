"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
import json
import app.utils.redis as redis

@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str

def _format_as_article(data: dict) -> Article:
    return Article(
        author=data["author"],
        title=data["title"],
        body=data["text"],
        publish_date=datetime.fromisoformat(data["published"]),
        image_url=data["thread"]["main_image"],
        url=data["url"],
    )


def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 
    all_articles = redis.REDIS_CLIENT.get_entry("all_articles")
    
    if all_articles is None:
        return []
        
    return [_format_as_article(article) for article in all_articles]


def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    # 2. Return as a list of articles sorted by most recent date
    articles = get_all_news()
    return sorted(articles, key=lambda article: article.publish_date)[-1]
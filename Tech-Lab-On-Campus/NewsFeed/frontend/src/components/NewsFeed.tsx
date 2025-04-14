import React from 'react';
import { Article } from '../utils/types';
import NewsCard from './NewsCard';

interface NewsFeedProps {
    articles: Article[];
}

// The NewsFeed component receives an array of Article objects and renders them in a grid.
function NewsFeed({ articles }: NewsFeedProps ) {
    return (
        <div className="stories-container">
            <div className="stories-grid">
                {articles.map((article, i) => (
                    <NewsCard
                        key={`${article}_${i}`}
                        article={article}
                    />
                ))}
            </div>
        </div>
    );
};
export default NewsFeed;

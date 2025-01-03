
# Google Daily Trends - Reddit Posts Sentiment Analyzer

Analyze the sentiments of Reddit posts related to the top daily Google Trends using Python, the Reddit API, and Google Cloud SQL.

## Overview

This project retrieves the top 10 daily Google Trends and analyzes posts on Reddit related to these trends. It uses sentiment analysis to classify the posts into positive, negative, or neutral categories, providing insights into public opinion on trending topics.

## Features

- Fetches daily top 10 Google Trends automatically.
- Collects Reddit posts related to each trend using the Reddit API.
- Performs sentiment analysis on the collected posts, categorizing them as:
  - Positive
  - Negative
  - Neutral
- Stores and retrieves data using Google Cloud SQL for efficient data handling.

## Tech Stack

- **Programming Language:** Python
- **APIs:**
  - Google Trends API
  - Reddit API
- **Database:** Google Cloud SQL
- requests` for web scraping and API calls

## Installation

Clone this repository:
   ```bash
   git clone https://github.com/your-username/Google-Trends-Reddit-Sentiment-Analyzer.git

Set up your API keys:
    Google Trends API Key
    Reddit API Credentials (Client ID, Client Secret, and User Agent)
    Configure your Google Cloud SQL database connection.

Usage

    Run the main script to fetch trends and analyze sentiments:

python main.py

View the sentiment analysis results:

    Results are stored in the Google Cloud SQL database.
    Use the View.py script or integrate a visualization tool to display the data.

# Future Enhancements

    Add support for more APIs like Twitter or Facebook for broader analysis.
    Integrate advanced sentiment analysis tools like Vader or machine learning models.
    Provide a real-time dashboard for visualizing sentiment trends.

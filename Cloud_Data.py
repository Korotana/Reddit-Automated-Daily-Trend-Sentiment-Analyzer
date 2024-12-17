import logging

import mysql.connector

import CloudConnection




def get_all_trends():
    try:
        connection = CloudConnection.get_cloud_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        # SQL query to fetch all trends
        query = "SELECT name FROM Trends;"

        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all rows of results

        connection.close()
        return result

    except mysql.connector.Error as err:
        logging.error(f"Error fetching all trends: {err}")
        return None




def get_sentiment_by_trend():
    try:
        connection = CloudConnection.get_cloud_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        # SQL query to fetch sentiment data by trend
        query = """
        SELECT t.name AS trend,
       SUM(CASE WHEN m.sentiment = 'positive' THEN 1 ELSE 0 END) AS positive_count,
       SUM(CASE WHEN m.sentiment = 'neutral' THEN 1 ELSE 0 END) AS neutral_count,
       SUM(CASE WHEN m.sentiment = 'negative' THEN 1 ELSE 0 END) AS negative_count
        FROM Trends t
        JOIN Mentions m ON t.id = m.trend_id
        GROUP BY t.name
        ORDER BY trend;
        """

        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all rows of results

        connection.close()
        return result

    except mysql.connector.Error as err:
        logging.error(f"Error fetching sentiment by trend: {err}")
        return None



def get_sentiment_by_date():
    try:
        connection = CloudConnection.get_cloud_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        # SQL query to fetch sentiment data by date
        query = """
        SELECT DATE(m.timestamp) AS date,
       SUM(CASE WHEN m.sentiment = 'positive' THEN 1 ELSE 0 END) AS positive_count,
       SUM(CASE WHEN m.sentiment = 'neutral' THEN 1 ELSE 0 END) AS neutral_count,
       SUM(CASE WHEN m.sentiment = 'negative' THEN 1 ELSE 0 END) AS negative_count
        FROM Mentions m
        GROUP BY DATE(m.timestamp)
        ORDER BY date DESC;
        """

        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all rows of results

        connection.close()
        return result

    except mysql.connector.Error as err:
        logging.error(f"Error fetching sentiment by date: {err}")
        return None



def get_mentions_by_date_range(start_date, end_date):
    try:
        connection = CloudConnection.get_cloud_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        # SQL query to fetch mentions within a date range
        query = """
        SELECT p.post_url, p.post_text, p.sentiment, p.timestamp
        FROM Mentions p
        WHERE p.timestamp BETWEEN %s AND %s;
        """

        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchall()  # Fetch all rows of results

        connection.close()
        return result

    except mysql.connector.Error as err:
        logging.error(f"Error fetching mentions for date range {start_date} to {end_date}: {err}")
        return None




def get_sentiment_for_post(post_url):
    try:
        connection = CloudConnection.get_cloud_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        # SQL query to fetch sentiment score for a specific post
        query = """
        SELECT sentiment
        FROM Mentions
        WHERE post_url = %s;
        """

        cursor.execute(query, (post_url,))
        result = cursor.fetchone()  # Fetch the first result (there should only be one)

        connection.close()
        return result

    except mysql.connector.Error as err:
        logging.error(f"Error fetching sentiment for post {post_url}: {err}")
        return None




def get_posts_by_trend(trend_name):
    try:
        connection = CloudConnection.get_cloud_connection()
        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries

        # SQL query to fetch posts for a specific trend
        query = """
        SELECT p.post_url, p.post_text, p.sentiment, p.timestamp
        FROM Mentions p
        JOIN Trends t ON p.trend_id = t.id
        WHERE t.name = %s;
        """

        cursor.execute(query, (trend_name,))
        result = cursor.fetchall()  # Fetch all rows of results

        connection.close()
        return result

    except mysql.connector.Error as err:
        logging.error(f"Error fetching posts for trend {trend_name}: {err}")
        return None

#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""

import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.

    This function sends a GET request to the JSONPlaceholder API to
    retrieve a list of posts.
    It prints the status code of the response and, if the request was
    successful, iterates
    through the posts and prints the title of each post.
    """

    # Send a GET request to fetch posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response into a Python list
        posts = response.json()
        # Iterate through each post in the list
        for post in posts:
            # Print the title of the current post
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.

    This function sends a GET request to the JSONPlaceholder
    API to retrieve a list of posts.
    If the request is successful, it processes the JSON data to
    extract the id, title, and body
    of each post, and writes this data into a CSV file named 'posts.csv'
    with appropriate headers.
    """

    # Send a GET request to fetch posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response into a Python list
        posts = response.json()
        # Extract relevant data from each post
        posts_list = [{"id": post["id"], "title": post["title"],
                       "body": post["body"]} for post in posts]
        # Open a new CSV file to write the data
        with open('posts.csv', 'w', newline='') as csvfile:
            # Define the header fieldnames for the CSV file
            fieldnames = ["id", "title", "body"]
            # Create a DictWriter object with the specified fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write the header row to the CSV file
            writer.writeheader()
            # Iterate through each post in the list
            for post in posts_list:
                # Write the post data to the CSV file
                writer.writerow(post)

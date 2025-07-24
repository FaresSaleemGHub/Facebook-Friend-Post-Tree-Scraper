# Facebook Friend-Post Tree Scraper

A Python automation tool that logs into Facebook, collects a user’s posts and their friends’ profiles recursively (multi-level tree structure), and stores the data into a text file.

## Features
- Logs in using email and password.
- Scrapes user posts and friend links.
- Recursively dives into friends’ profiles to scrape their posts.
- Customizable depth and post limits.

## Technologies Used
- Python
- Selenium
- BeautifulSoup
- Regular Expressions

## How It Works
1. Prompts the user for login credentials and scraping depth.
2. Scrapes a user’s posts and friends.
3. Navigates to each friend and repeats the process up to the given depth.
4. Saves all data in `collection.txt`.


# Facebook Friend-Post Tree Scraper
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) <br>
A Python automation tool that logs into Facebook, collects a user’s posts and their friends’ profiles recursively (multi-level tree structure), and stores the data into a text file.

---

## 📌 Overview
This tool uses Selenium and BeautifulSoup to simulate browser behavior, log into a Facebook account, and recursively navigate through friends' profiles to scrape posts and links. It's designed for educational, research, or personal data analysis purposes.

You can customize:
- The number of posts and friends per profile.
- The depth of recursion through the friend network.

---

## ✨ Features
- Automated login to Facebook with session handling.
- Dynamic content handling via Selenium.
- Multi-level scraping (tree-style recursion).
- Extracts posts and friend profile links.
- Adjustable scraping depth and number of records.
- Saves data to a human-readable `.txt` file.

---

## 🔧 Technologies Used
- Python
- Selenium
- BeautifulSoup
- Regular Expressions

---

## 🚀 How It Works
1. Prompts the user for login credentials and scraping depth.
2. Scrapes a user’s posts and friends.
3. Navigates to each friend and repeats the process up to the given depth.
4. Saves all data in `collection.txt`.

---

## ⚠️ Disclaimer
This tool is for educational purposes only. Scraping social media content may violate Facebook’s Terms of Service. Use responsibly.

---

## 👤 Author
Written with passion by – @FaresSaleemGHub

---

## 📜 License
This project is open-source and available under the MIT License.

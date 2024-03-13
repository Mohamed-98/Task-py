<h1 align="center">Task-py</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---
<h4 align="center">Geek Labs Backend technical task 
</h4>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Requirements](#Requirements)
- [Installing](#Installing)
- [Run the Project](#Run_the_Project)
- [Usage](#Usage)
- [Input Format](#Input_Format)
- [Output Format](#Output_Format)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Task-py is a Python script that scrapes Twitter accounts for mentions of stock symbols and provides relevant statistics.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine.

### Requirements <a name = "Requirements"></a>

- Python 3.x
- Selenium
- BeautifulSoup

### Installing <a name = "Installing"></a>

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/Task-py.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

## 🔧 Run the Project <a name = "Run_the_Project"></a>

```
python twitter_scraper.py
```

## 🎈 Usage <a name="usage"></a>

1. Follow the prompts to input the Twitter accounts, stock symbol (ticker), and time interval for scraping sessions.
2. The script will continuously scrape the Twitter accounts for mentions of the provided stock symbol and display the results.

## ❗ Input Format <a name="Input_Format"></a>

- **Twitter Accounts:** Enter the Twitter usernames for the accounts you want to scrape. You can enter up to 10 accounts.
- **Stock Symbol (Ticker):** Enter the stock symbol (e.g., \$TSLA, \$SOFI, \$AAPL) you want to search for mentions of.
- **Time Interval:** Enter the time interval (in minutes) for scraping sessions.

## ❗ Output Format <a name="Output_Format"></a>

The script will output the following for each scraping session:
- The number of times the stock symbol was mentioned for each Twitter account.
- The time interval used for the scraping session.

## Example Output:
```
$TSLA was mentioned 5 times in @Mr_Derivative's tweets.
$TSLA was mentioned 3 times in @ChartingProdigy's tweets.
Waiting for 15 minutes for next scraping session...
```

## Notes
- Ensure you have a stable internet connection.

## ✍️ Authors <a name = "authors"></a>

- [@Mohamed-98](https://github.com/Mohamed-98) - Initial work


from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

def scrape_twitter_accounts(accounts, ticker):
    driver = webdriver.Chrome()  
    
    for account in accounts:
        url = f"https://twitter.com/{account}"
        driver.get(url)
        
        time.sleep(5)
        
        #You can check BeautifulSoup Documentation for how to use it 
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tweet_divs = soup.find_all('div', {'class': 'css-175oi2r'})
        tweets = [tweet.text for tweet in tweet_divs]
        mentions = sum(1 for tweet in tweets if f'${ticker}' in tweet)
        print(f"{ticker} was mentioned {mentions} times in {account}'s tweets.")
    
    driver.quit()


# Input/Enter Twitter accounts
twitter_accounts = [] 
for i in range(10):
    string = input("Enter Twitter account {}: ".format(i + 1))
    twitter_accounts.append(string)

# Input/Enter ticker
ticker = input("Enter stock symbol (e.g., $TSLA, $SOFI, $AAPL): ")

# Input/Enter time interval
interval_minutes = int(input("Enter time interval for scraping session (in minutes): "))

while True:
    scrape_twitter_accounts(twitter_accounts, ticker)
    print(f"Waiting for {interval_minutes} minutes for next scraping session...")
    time.sleep(interval_minutes * 60)  # Convert minutes to seconds

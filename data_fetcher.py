import yfinance as yf
from config import DATA_FOLDER
from loguru import logger
import os


def fetch_stock_data(ticker, period="1mo"):
    logger.info(f"Fetching data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df


def save_to_csv(df, ticker):
    filename = f"{DATA_FOLDER}/{ticker.replace('.', '_')}.csv"
    df.to_csv(filename)
    logger.info(f"Saved: {filename}")


def fetch_current_price(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1d")
    if df.empty:
        logger.warning(f"No data returned for {ticker}")
        return None
    price = df["Close"].iloc[-1]
    logger.info(f"{ticker} price fetched: {round(price, 2)}")
    return round(price, 2)

def save_results_to_csv(results, filename="data/risk_report.csv"):
    import pandas as pd
    df = pd.DataFrame(results)
    df["date"] = pd.Timestamp.today().strftime("%Y-%m-%d")
    df.to_csv(filename, index=False)
    logger.info(f"Results saved to {filename}")
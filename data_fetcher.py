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
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1d")

        if df.empty:
            logger.warning(f"No data returned for {ticker}")
            return None

        price = df["Close"].iloc[-1]
        logger.info(f"{ticker} price fetched: {round(price, 2)}")
        return round(price, 2)

    except Exception as e:
        logger.error(f"Failed to fetch price for {ticker}: {e}")
        return None

def save_results_to_csv(results, filename="data/risk_report.csv"):
    try:
        import pandas as pd
        df = pd.DataFrame(results)
        df["date"] = pd.Timestamp.today().strftime("%Y-%m-%d")
        df.to_csv(filename, index=False)
        logger.info(f"Results saved to {filename}")
    except Exception as e:
        logger.error(f"Failed to save results: {e}")

def fetch_and_save_historical(ticker, period="1mo"):
    try:
        logger.info(f"Fetching historical data for {ticker}...")
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)

        if df.empty:
            logger.warning(f"No historical data for {ticker}")
            return None

        df = df[["Open", "High", "Low", "Close", "Volume"]]
        df.index = df.index.tz_localize(None)

        filename = f"{DATA_FOLDER}/{ticker.replace('.', '_')}_history.csv"
        df.to_csv(filename)
        logger.info(f"Historical data saved: {filename} ({len(df)} rows)")
        return df

    except Exception as e:
        logger.error(f"Failed to fetch historical data for {ticker}: {e}")
        return None
    
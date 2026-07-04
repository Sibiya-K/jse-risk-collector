from config import TICKERS, CONFIDENCE_LEVEL
from data_fetcher import fetch_current_price, fetch_stock_data, save_results_to_csv
from risk_calculator import analyse_stock
from loguru import logger

logger.info("JSE Risk Collector Starting:")
print(f"Analysing {len(TICKERS)} stocks at {CONFIDENCE_LEVEL*100}% confidence\n")

all_results = []

for ticker in TICKERS:
    price = fetch_current_price(ticker)

    if price is None:
        print(f"Skipping {ticker} - no price data\n")
        continue

    result = analyse_stock(ticker, price, 100, CONFIDENCE_LEVEL)
    all_results.append(result)

    print(f"Ticker:            {result['ticker']}")
    print(f"Current Price:     R{price}")
    print(f"Portfolio Value:   R{result['portfolio_value']}")
    print(f"95% VaR:           R{result['var_95']}")
    print("-" * 35)

save_results_to_csv(all_results)
logger.info("JSE Risk Collector Complete")

def calculate_portfolio_value(price, shares):
    return price * shares


def calculate_var(portfolio_value, confidence_level):
    return portfolio_value * (1 - confidence_level)


def calculate_daily_pnl(portfolio_value, daily_return):
    return portfolio_value * daily_return


def analyse_stock(ticker, price, shares, confidence_level=0.95):
    portfolio_value = calculate_portfolio_value(price, shares)
    var = calculate_var(portfolio_value, confidence_level)

    return {
        "ticker": ticker,
        "portfolio_value": round(portfolio_value, 2),
        "var_95": round(var, 2),
    }
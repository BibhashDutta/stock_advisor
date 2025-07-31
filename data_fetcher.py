import yfinance as yf
import pandas as pd

def fetch_market_data():
    symbols = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS"]
    data = {
        "Stock": [],
        "Opening Price": [],
        "Current Price": [],
        "Volume": []
    }

    for symbol in symbols:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d", interval="1m")

        if not hist.empty:
            data["Stock"].append(symbol.replace(".NS", ""))
            data["Opening Price"].append(round(hist['Open'].iloc[0], 2))
            data["Current Price"].append(round(hist['Close'].iloc[-1], 2))
            data["Volume"].append(int(hist['Volume'].sum()))
        else:
            data["Stock"].append(symbol.replace(".NS", ""))
            data["Opening Price"].append(None)
            data["Current Price"].append(None)
            data["Volume"].append(None)

    return pd.DataFrame(data)

def format_data_as_text(df):
    df_formatted = df.copy()
    df_formatted["Opening Price"] = df_formatted["Opening Price"].map(lambda x: f"{x:.2f}" if pd.notnull(x) else "N/A")
    df_formatted["Current Price"] = df_formatted["Current Price"].map(lambda x: f"{x:.2f}" if pd.notnull(x) else "N/A")
    df_formatted["Volume"] = df_formatted["Volume"].map(lambda x: f"{x:,}" if pd.notnull(x) else "N/A")
    return df_formatted.to_string(index=False)

# Example
if __name__ == "__main__":
    df = fetch_market_data()
    print(format_data_as_text(df))

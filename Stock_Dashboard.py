import streamlit as st
import yfinance as yf
import plotly.express as px

# Title
st.title("Stock Dashboard")
st.markdown("*Real-Time Market Data at Your Fingertips* 📱")

# Sidebar Layout
st.sidebar.title("Enter Stock Details:")
ticker_symbol = st.sidebar.text_input("Ticker", "AAPL")
start_date = st.sidebar.date_input("Start Date",value=None)
end_date = st.sidebar.date_input("End Date",value=None)


ticker = yf.Ticker(ticker_symbol)
historical_data = ticker.history(start= start_date,end= end_date)
# st.write(historical_data)

if start_date is not None and end_date is not None:
    # st.write(historical_data)
    st.subheader(f'{ticker_symbol} Stock Overview')
    stockData = yf.download(ticker_symbol, start=start_date, end=end_date)
    price_tab, hist_tab, chart_tab= st.tabs(["Price Summary", "Historical Data", "Charts"])

    with price_tab:
        st.write("Price Summary")
        st.write(stockData)
    with hist_tab:
        st.write("Historical Data")
        st.write(historical_data)
    with chart_tab:
        st.write("Charts")
        st.line_chart(stockData['Adj Close'])
        # line_charts = px.line(stockData,stockData.index,  y= stockData['Adj Close'], title=ticker_symbol)
        # st.plotly_chart(line_charts)

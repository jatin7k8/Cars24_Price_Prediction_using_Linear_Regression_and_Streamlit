import yfinance as yf
import streamlit as st

# mstf = yf.Ticker("MSFT")
#
# # Fetch historical data with daily frequency
# hist = mstf.history(period="1d", start="2019-01-01", end="2023-01-01")
#
# # Display the historical data in Streamlit
# st.write(hist)
#
#
#
st.write(

    """
    # This is my Heading

    Learn Stock Market using streamlit

    """
)
#
# import datetime
#
# start_date = st.date_input("Please enter starting date", datetime.date(2019, 1, 1))
# end_date = st.date_input("Please enter ending date", datetime.date(2022, 12, 31))


### creating for apple

import datetime

# col1 , col2 = st.columns(2)
#
# with col1:
#     start_date = st.date_input("Please enter starting date", datetime.date(2019, 1, 1))
#
# with col2:
#     end_date = st.date_input("Please enter ending date", datetime.date(2022, 12, 31))
#
# ticker_symbol = 'AAPL'
# ticker_data = yf.Ticker(ticker_symbol)
#
#
# ticker_df = ticker_data.history(period="1d",start=start_date, end=end_date)
# st.dataframe(ticker_df)

#
# st.write(
#
#     """
#     ## Daily Closing Price Chart
#     """
# )
#
# st.line_chart(ticker_df.Close)
#
#
# st.write(
#
#     """
#     ## Volume of shares Traded Each Day
#     """
# )
# st.line_chart(ticker_df.Volume)


col1 , col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter starting date", datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input("Please enter ending date", datetime.date(2022, 12, 31))

ticker_symbol = st.text_input("Enter Stock Symbol",
                              "AAPL",
                              key = "placeholder")

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period = '1d', start = start_date, end = end_date)
st.dataframe(ticker_df)


st.write(

    """
    ## Daily Closing Price Chart
    """
)

st.line_chart(ticker_df.Close)


st.write(

    """
    ## Volume of shares Traded Each Day 
    """
)
st.line_chart(ticker_df.Volume)
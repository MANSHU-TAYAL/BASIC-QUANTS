# WELCOME TO MY PROJECT

import pandas as pd


def READ_NSE_EQUITY_BHAVCOPY():
    print("Example: Read NSE EQUITY BHAVCOPY")

    file_name = "BhavCopy_NSE_CM_0_0_0_20250923_F_0000"
    file_path = rf"C:\Users\MANNC\PycharmProjects\PythonProject\{file_name}.csv"

    df_nse_bhavcopy = pd.read_csv(file_path)
    print(df_nse_bhavcopy)


# call the function
#READ_NSE_EQUITY_BHAVCOPY()

def READ_NSE_EQUITY_BHAVCOPY2():
    file_path = r"C:\Users\MANNC\PycharmProjects\PythonProject\20250915_NSE.csv"
    df_data_ohlc = pd.read_csv(file_path)
    print(df_data_ohlc)

# function call
#READ_NSE_EQUITY_BHAVCOPY2()

def READ_STOCKS_OHLC_BHAV_COPY():
    """SYMBOL	SERIES	OPEN	HIGH	LOW	CLOSE	LAST	PREVCLOSE	TOTTRDQTY	TOTTRDVAL	TIMESTAMP	TOTALTRADES	ISIN"""
    print("Example 6")
    file_path = r"C:\Users\MANNC\PycharmProjects\PythonProject\20250915_NSE.csv"
    df_data_ohlc = pd.read_csv(file_path)

    for index, row in df_data_ohlc.iterrows():
        if row['SERIES'] == "EQ":  # filter only EQ series
            open_price = row['OPEN']
            high_price = row['HIGH']
            close_price = row['CLOSE']
            low_price = row['LOW']


            print(f"OHLC DATA FOR stock {row['SYMBOL']}, open:{open_price} high:{high_price} low:{low_price} close:{close_price}")

# Call the function
#READ_STOCKS_OHLC_BHAV_COPY()

def READ_NSE_BHAV_COPY_WICK_2_WICK():
    """SYMBOL	SERIES	OPEN	HIGH	LOW	CLOSE	LAST	PREVCLOSE	TOTTRDQTY	TOTTRDVAL	TIMESTAMP	TOTALTRADES	ISIN"""
    print("Example 6")
    file_path = r"C:\Users\MANNC\PycharmProjects\PythonProject\20250915_NSE.csv"
    df_data_ohlc = pd.read_csv(file_path)

    for index, row in df_data_ohlc.iterrows():
        if row['SERIES'] == "EQ":
            open_price = row['OPEN']
            high_price = row['HIGH']
            low_price = row['LOW']
            close_price = row['CLOSE']

            # Calculate wick-to-wick range
            WICK_2_WICK_RANGE = round(high_price - low_price,2)

            print(f"OHLC DATA FOR stock {row['SYMBOL']}, WICK_2_WICK_RANGE: {WICK_2_WICK_RANGE}")

# Call the function
#READ_NSE_BHAV_COPY_WICK_2_WICK


def Write_message_textfile():
    message = "Write data to file"
    message2 = "learn quants trading"
    columnname = "Message"

    write_message = {columnname: [message, message2]}
    df = pd.DataFrame(write_message)

    destinationpath = r"C:\Users\MANNC\PycharmProjects\PythonProject\dataWrite.txt"
    df.to_csv(destinationpath, index=False)


# Call the function
Write_message_textfile()


def WRITE_READ_STOCKS_OHLC_BHAV_COPY():
    """SYMBOL	SERIES	OPEN	HIGH	LOW	CLOSE	LAST	PREVCLOSE	TOTTRDQTY	TOTTRDVAL	TIMESTAMP	TOTALTRADES	ISIN"""
    print("Example 8")
    file_path = r"C:\Users\MANNC\PycharmProjects\PythonProject\20250915_NSE.csv"

    # Read file
    df_data_ohlc = pd.read_csv(file_path)

    # Save file
    destinationpath = r"C:\Users\MANNC\PycharmProjects\PythonProject\filterfile.csv"
    df_data_ohlc.to_csv(destinationpath, index=False)


# Call the function
WRITE_READ_STOCKS_OHLC_BHAV_COPY()


def Filter_df_and_write_to_csv():
    print("Example 9")

    file_path = r"C:\Users\MANNC\PycharmProjects\PythonProject\20250915_NSE.csv"

    # Read file
    df_dataohlc = pd.read_csv(file_path)

    """FILTER"""
    filter_condition = df_dataohlc["SERIES"] == "EQ"

    # Apply filter with where (keeps NaN where condition is False)
    df_dataohlc.where(filter_condition, inplace=True)

    """REMOVE NaN values"""
    df_new = df_dataohlc.dropna(subset=["SERIES"])  # corrected variable name

    """Write this to file"""
    destination_path = r"C:\Users\MANNC\PycharmProjects\PythonProject\20250915_NSE_updated.csv"
    df_new.to_csv(destination_path, index=False)

    # Print dataframe
    print(df_new)


# Function call
#Filter_df_and_write_to_csv()






import pandas as pd

def Read_Feed_as_BhavCopy():
    print("Example 10 : BUY STOCKS")

    # Corrected file path
    filepath = r"C:\Users\MANNC\PycharmProjects\PythonProject\20250915_NSE.csv"
    df_dataohlc = pd.read_csv(filepath)

    """  BUY STOCKS  """
    for idx, row in df_dataohlc.iterrows():
        Open = row["OPEN"]
        High = row["HIGH"]
        Low = row["LOW"]
        Close = row["CLOSE"]

        stockname = row["SYMBOL"]

        # Condition 1 - Buy
        if Open == Low and row["SERIES"] == "EQ":
            print(f"BUY STOCKS : {stockname}")

# Start Trading
Read_Feed_as_BhavCopy()

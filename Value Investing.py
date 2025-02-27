import pandas as pd

# Load the data
data = pd.read_csv('d:\\Value_Investing.csv')

# Select relevant columns
columns_of_interest = ['Name', 'ISIN', 'P/E Ratio (TTM) (Long)', 'P/B Ratio (TTM) (Long)', 'Dividend Yield (Long)']
data = data[columns_of_interest]

# Drop rows with missing data in the columns of interest
data.dropna(subset=columns_of_interest, inplace=True)

# Calculate average values for the thresholds
average_pe_ratio = data['P/E Ratio (TTM) (Long)'].mean()
average_pb_ratio = data['P/B Ratio (TTM) (Long)'].mean()
average_dividend_yield = data['Dividend Yield (Long)'].mean()

# Define thresholds for value investing criteria based on averages
pe_ratio_threshold = average_pe_ratio  # Select stocks with a P/E ratio less than the average
pb_ratio_threshold = average_pb_ratio  # Select stocks with a P/B ratio less than the average
dividend_yield_threshold = average_dividend_yield  # Select stocks with a dividend yield greater than the average

# Shortlist Value Funds - Liberal Approach (Approach#02)
value_funds_01 = data[
    (data['P/E Ratio (TTM) (Long)'] < pe_ratio_threshold) &
    (data['P/B Ratio (TTM) (Long)'] < pb_ratio_threshold) &
    (data['Dividend Yield (Long)'] > dividend_yield_threshold)
]

# Shortlist Value Funds - Liberal Approach (Approach#02)
value_funds_02 = data[
    (data['P/E Ratio (TTM) (Long)'] > pe_ratio_threshold) |
    (data['P/B Ratio (TTM) (Long)'] > pb_ratio_threshold) |
    (data['Dividend Yield (Long)'] > dividend_yield_threshold)
]

# Export the selected funds to an Excel file
value_funds_01.to_excel('d:\\value_funds_01.xlsx', index=False, sheet_name='Filtered Funds')
value_funds_02.to_excel('d:\\value_funds_02.xlsx', index=False, sheet_name='Filtered Funds')
import pandas as pd

# Load the data
data = pd.read_excel('d:\\Growth_Investing.xlsx')

# Assuming 'NAV Growth' is a column in your CSV, add it to your columns of interest
columns_of_interest = ['Name', 'ISIN', 'P/E Ratio (TTM) (Long)', 'P/B Ratio (TTM) (Long)', 'NAV Growth']
data = data[columns_of_interest]

# Drop rows with missing data in the columns of interest
data.dropna(subset=columns_of_interest, inplace=True)

# Calculate average values for the thresholds
average_pe_ratio = data['P/E Ratio (TTM) (Long)'].mean()
average_pb_ratio = data['P/B Ratio (TTM) (Long)'].mean()
average_nav_growth = data['NAV Growth'].mean()

# Define thresholds for growth investing criteria
# Select funds with higher than average P/E and P/B ratios which indicate expected growth
pe_ratio_threshold = average_pe_ratio  # Select stocks with a P/E ratio greater than the average
pb_ratio_threshold = average_pb_ratio  # Select stocks with a P/B ratio greater than the average
nav_growth_threshold = average_nav_growth  # Select stocks with NAV growth greater than the average

# Shortlist growth fund - Conservative approach (Approach#01)
growth_funds_01 = data[
    (data['P/E Ratio (TTM) (Long)'] > pe_ratio_threshold) &
    (data['P/B Ratio (TTM) (Long)'] > pb_ratio_threshold) &
    (data['NAV Growth'] > nav_growth_threshold)
]

# Shortlist growth fund - Liberal Approach (Approach#02)
growth_funds_02 = data[
    (data['P/E Ratio (TTM) (Long)'] > pe_ratio_threshold) |
    (data['P/B Ratio (TTM) (Long)'] > pb_ratio_threshold) |
    (data['NAV Growth'] > nav_growth_threshold)
]

# Export the selected funds to an Excel file
growth_funds_01.to_excel('d:\\growth_funds_01.xlsx', index=False, sheet_name='Filtered Funds')
growth_funds_02.to_excel('d:\\growth_funds_02.xlsx', index=False, sheet_name='Filtered Funds')
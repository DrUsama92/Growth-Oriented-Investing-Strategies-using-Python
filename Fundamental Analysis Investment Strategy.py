import pandas as pd

# Load the data
data = pd.read_excel('Fundemental Analysis Investment Strategy.xlsx')
data

# Drop rows with missing data
data.dropna(inplace=True)
data

#Removing leading and trailing spaces
data.columns = data.columns.str.strip()

#Calculate average value of NAV, Net Expense Ratio, P/B Ratio, P/E Ratio and ROE

average_NAV = data['Net Asset Value(NAV)'].mean()
average_Net_Expense=data['Net Expense Ratio'].mean()
average_PB_ratio=data['P/B Ratio (TTM) (Long)'].mean()
average_PE_ratio=data['P/E Ratio (TTM) (Long)'].mean()
averag_ROE_ratio=data['ROE % (TTM) (Long)'].mean()

#Defining Fundemental Analysis investment criteria
#Select funds with a P/B Ratio, P/E Ratio, and Expense Ratio below their average values, and a ROE and NAV above the average value.
#Short list funds
fundamental_funds_01 = data[
    (data['Net Asset Value(NAV)'] > average_NAV ) &
    (data['P/B Ratio (TTM) (Long)'] < average_PB_ratio ) |
    (data['P/E Ratio (TTM) (Long)'] < average_PE_ratio ) &
    (data['ROE % (TTM) (Long)'] > averag_ROE_ratio  ) &
    (data['Net Expense Ratio'] < average_Net_Expense )]
fundamental_funds_01

# Export the selected funds to an Excel file

fundamental_funds_01.to_excel('fundemental_funds_01.xlsx', index=False, sheet_name='Filtered Funds')





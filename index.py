python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'adx_data.csv' with your dataset file)
data = pd.read_csv('adx_data.csv')

# Sample preprocessing: Convert date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Filter data for a specific company
company_name = "Abu Dhabi Commercial Bank"
company_data = data[data['Company Name'] == company_name]

# Plot market capitalization over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=company_data, x='Date', y='Market Capitalization', label='Market Capitalization')
plt.title(f'Market Capitalization Over Time for {company_name}')
plt.xlabel('Date')
plt.ylabel('Market Capitalization (in AED)')
plt.legend()
plt.grid(True)
plt.show()

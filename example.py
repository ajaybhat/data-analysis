from data_analysis_sdk import DataAnalysisSDK

# Instantiate the SDK with the data file
sdk = DataAnalysisSDK('data.csv')

# Load and explore the data
sdk.load_data()
sdk.explore_data()

# Clean the data
sdk.clean_data()

# Perform analysis and visualize data
sdk.perform_analysis()
sdk.visualize_data()

# Save analysis results
sdk.save_analysis_results('output.csv')

import os
import kaggle

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Set the path for kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()

# Now you can use the Kaggle API to download datasets
kaggle.api.dataset_download_files('deepcontractor/squid-game-netflix-twitter-data', path=os.getcwd(), unzip=True)
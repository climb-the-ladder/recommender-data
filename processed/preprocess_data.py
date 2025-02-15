import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(script_dir, "../raw/dataset.csv")
dataset_path = os.path.normpath(dataset_path)

df = pd.read_csv(dataset_path)

if "Field" in df.columns:
    df = df.drop(columns=["Field"])
    print("Column 'Field' removed successfully.")

processed_folder = os.path.join(script_dir, "../processed")
os.makedirs(processed_folder, exist_ok=True)

processed_dataset_path = os.path.join(processed_folder, "processed_dataset.csv")

df.to_csv(processed_dataset_path, index=False)

print(f"Data preprocessing complete! Processed dataset saved at: {processed_dataset_path}")

import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

dataset1_path = os.path.join(script_dir, "../raw/dataset1.csv")
dataset2_path = os.path.join(script_dir, "../raw/dataset2.csv")

dataset1_path = os.path.normpath(dataset1_path)
dataset2_path = os.path.normpath(dataset2_path)

df1 = pd.read_csv(dataset1_path)
df2 = pd.read_csv(dataset2_path)

print("Files loaded successfully from:", dataset1_path, "and", dataset2_path)

# Drop unnecessary personal fields from df1
df1_cleaned = df1.drop(columns=['id', 'first_name', 'last_name', 'email', 'gender'])

# Compute GPA from subject scores in df1
subject_columns = ['math_score', 'history_score', 'physics_score', 
                   'chemistry_score', 'biology_score', 'english_score', 'geography_score']
df1_cleaned['GPA'] = df1_cleaned[subject_columns].mean(axis=1)

# Rename 'career_aspiration' to 'Career' to match df2
df1_cleaned = df1_cleaned.rename(columns={'career_aspiration': 'Career'})

# Standardize extracurricular activities naming
df1_cleaned = df1_cleaned.rename(columns={'extracurricular_activities': 'Extracurricular_Activities'})

# Drop individual subject scores since they are now included in GPA
df1_cleaned = df1_cleaned.drop(columns=subject_columns)

# Ensure column order and missing fields alignment
missing_cols_df2 = set(df2.columns) - set(df1_cleaned.columns)
missing_cols_df1 = set(df1_cleaned.columns) - set(df2.columns)

# Add missing fields in df1 (filling with 0 as default value for skills-based columns)
for col in missing_cols_df2:
    df1_cleaned[col] = 0

# Add missing fields in df2 (filling with 0 where necessary)
for col in missing_cols_df1:
    df2[col] = 0

# Ensure same column order in both datasets
df1_cleaned = df1_cleaned[df2.columns]

# Define paths for saving processed datasets
processed_folder = os.path.join(script_dir, "../processed")
os.makedirs(processed_folder, exist_ok=True)

processed_dataset1_path = os.path.join(processed_folder, "processed_dataset1.csv")
processed_dataset2_path = os.path.join(processed_folder, "processed_dataset2.csv")

df1_cleaned.to_csv(processed_dataset1_path, index=False)
df2.to_csv(processed_dataset2_path, index=False)

print("Data preprocessing complete!")
print(f"Processed Dataset 1 saved at: {processed_dataset1_path}")
print(f"Processed Dataset 2 saved at: {processed_dataset2_path}")

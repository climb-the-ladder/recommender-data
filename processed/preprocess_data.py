import pandas as pd
import os

def preprocess_student_data():
    # Use absolute paths for Docker reliability
    input_file = '/app/raw/student-scores.csv'
    output_file = '/app/processed/output/processed_dataset.csv'
    
    print(f"Attempting to read input file from: {input_file}")
    
    # Check if file exists
    if not os.path.exists(input_file):
        print("ERROR: Input file not found!")
        print("Current directory:", os.getcwd())
        print("Directory contents:")
        for root, dirs, files in os.walk('/app'):
            print(f"Directory: {root}")
            for file in files:
                print(f"  - {file}")
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Read the data
    df = pd.read_csv(input_file)
    
    # we drop unnecessary columns including personal info and boolean flags.
    df = df.drop(columns=[
        'id', 'first_name', 'last_name', 'email', 'gender',
        'part_time_job', 'extracurricular_activities',
        'weekly_self_study_hours', 'absence_days'
    ])
    
    # we also remove rows where career_aspiration is unknown
    df = df[df['career_aspiration'] != 'Unknown']
    df = df[df['career_aspiration'] != 'Business Owner']
    
    df = df.dropna(subset=['career_aspiration'])
    
    # Final dataset preview
    print("Processed Data Sample:")
    print(df.head())
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Save to the output location
    df.to_csv(output_file, index=False)
    print(f"✅ Preprocessed dataset saved at {output_file}")

if __name__ == "__main__":
    preprocess_student_data()

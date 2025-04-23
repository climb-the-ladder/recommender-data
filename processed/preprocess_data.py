import pandas as pd

def preprocess_student_data():
    df = pd.read_csv('../raw/student-scores.csv')
    
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
    
    df.to_csv('processed_dataset.csv', index=False)
    print("✅ Preprocessed dataset saved at recommender-data/processed/processed_dataset.csv")

if __name__ == "__main__":
    preprocess_student_data()

# Career Recommender Data Repository

This repository contains the datasets and data processing scripts used by the Career Recommendation System.

## Repository Structure

## Datasets

### Raw Data

1. **student-scores.csv**
   - Contains student academic performance data across various subjects
   - Includes career aspirations for each student
   - Used for training the career recommendation model

2. **career_university_dataset.csv**
   - Maps careers to recommended universities based on GPA requirements
   - Includes university ranking information
   - Used by the chatbot to recommend universities

3. **similar_careers_dataset.csv**
   - Contains mappings between careers and similar alternative careers
   - Used to provide career alternatives in the recommendation system

### Processed Data

1. **processed_dataset.csv**
   - Cleaned version of the student data
   - Removes unnecessary columns and handles missing values
   - Filters out ambiguous career aspirations
   - Ready for model training and analysis

## Data Processing

The `preprocess_data.py` script performs the following operations:
- Removes personally identifiable information (names, emails, etc.)
- Drops unnecessary columns - the categorical data columns (part_time_job, extracurricular_activities, etc.)
- Filters out records with unknown or ambiguous career aspirations
- Handles missing values
- Saves the processed dataset for model training

To run the preprocessing script:

First, install the dependencies:

```bash:recommender-data/README.md
pip install -r requirements.txt
```

Then, run the preprocessing script:

```bash:recommender-data/README.md
cd recommender-data/processed
python preprocess_data.py
```

## Usage

This data is used by multiple components of the Career Recommendation System:

1. **AI Model Training**: The processed data is used to train the XGBoost model that predicts career recommendations based on academic scores.

2. **Chatbot Recommendations**: The university and similar careers datasets are used by the chatbot to provide university recommendations and career alternatives.

3. **Data Analysis**: The processed data is used for generating insights and visualizations about career trends and subject correlations.


## Dependencies

- pandas: For data manipulation and processing
- numpy: For numerical operations
- matplotlib & seaborn: For data visualization (only needed for insights generation)


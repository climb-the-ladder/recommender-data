Dataset 1 (dataset_1.csv - Student Academic & Career Aspirations)
Column	Description
id, first_name, last_name, email, gender	Personal details (not needed for ML)
part_time_job, absence_days, extracurricular_activities	Student activities
weekly_self_study_hours	Time spent on studying
career_aspiration	The career they want
math_score, history_score, ..., geography_score	Subject scores
🔹 Type: Student data, career aspirations, and academic performance.
🔹 Key column: career_aspiration (Target career interest).

Dataset 2 (dataset_2.csv - Career & Skills Matching)
Column	Description
Field	Broad career category (e.g., Engineering, Law)
Career	Specific job title (e.g., Urban Planner, Chemist)
GPA	Academic performance
Extracurricular_Activities, Internships, Projects, Leadership_Positions	Activities
Coding_Skills, Communication_Skills, Problem_Solving_Skills	Soft & technical skills
Industry_Certifications	Professional qualifications
🔹 Type: Career data with skills, academic performance, and experience.
🔹 Key column: Career (Target job role).

 Plan for Cleaning & Processing
Remove irrelevant fields (e.g., first_name, email, etc.).
Standardize career names between datasets.
Map student academic performance to skill scores.
Create a unified dataset for ML.

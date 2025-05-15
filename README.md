# Clinical Insights: Complete Practice of Data Analysis with Python, Power BI, MySQL and Machine Learning

This project was developed with the goal of practicing and integrating knowledge of data analysis, manipulation, and visualization, good practices for organization, and the application of unsupervised machine learning. The database is fictional, created with the Faker and Random libraries, and simulates a clinic with patients, doctors, and appointments.

The central idea is to allow a complete analysis, from data generation to extracting insights using tools like Power BI and Clustering. The project structure was carefully designed to represent a realistic, organized, and professional scenario, similar to those found in data-related work environments.

## Project Goals

- Create a realistic and well-structured database using Python;
- Practice good organization practices in data analysis projects;
- Simulate a complete clinical environment, with related tables;
- Upload the data to MySQL to reinforce relational SQL knowledge;
- Export the processed data for exploratory analysis in Power BI;
- Apply unsupervised machine learning techniques, such as KMeans and PCA;
- Document the entire process clearly, showing challenges and learnings.

## Technologies and Libraries Used

pandas - manipulation, cleaning, and analysis of tabular data.

seaborn and matplotlib - creation of statistical and graphical visualizations.

faker and random - generation of realistic and random synthetic data.

sklearn - application of Machine Learning algorithms (such as KMeans and PCA) and standardization of variables.

os - interaction with the operating system, such as managing paths and environment variables.

pathlib - robust, object-oriented manipulation of directory and file paths.

dotenv - secure loading of environment variables from .env files.

sqlalchemy - interface for connecting to, manipulating, and exporting data to relational databases (such as MySQL).

MySQL - relational data storage and execution of SQL queries.

Power BI - interactive data visualization and dashboard creation.

## Project Structure

clinical_insights/
src/
  data_preparation/    # Scripts for data generation
  database/            # Script for MySQL integration
  ml/                  # Cluster analysis
data/                  # Exported CSV files
figures/               # Plots (ML)
powerbi_reports/       # Power BI dashboard file
cluster_insights.md    # Supplementary document with cluster analysis insights
requirements.txt       # List of dependencies
README.md              # Project documentation


## Insights Generated

This project provided a series of technical and conceptual learnings through all stages.

During the creation of the relational database in MySQL, it was necessary to carefully plan the logical and physical model of the tables, prioritizing referential integrity, normalization, and consistency across records. This step solidified knowledge in data modeling and SQL language.

Exploratory data analysis, conducted with the Pandas, Seaborn, and Matplotlib libraries in Python and Power BI, allowed for the identification of relevant patterns, such as:

- Distribution of doctors by specialty;
- Total clinic revenue over the months;
- Number of appointments per professional;
- Percentage of patients by health plan type;
- Monthly revenue progression by plan.

In the machine learning module, the clustering technique with KMeans was applied, aiming to segment patients based on characteristics like age, sex, and health plan type. The analysis of the clusters helped identify profiles with similar behaviors, which could serve as a basis for strategies such as service personalization, targeted campaigns, or restructuring health plans.

To simplify the visualization of clusters, the dimensionality reduction technique with PCA was used, allowing the distribution of groups to be seen in a two-dimensional space, while maintaining the highest possible variance from the original data.

Moreover, the integration between Python, MySQL, and Power BI emphasized the importance of efficient ETL practices and communication between different tools in the data stack. The created dashboard summarizes the key indicators in a visual form, making it easy and quick to interpret the clinic's data.

## Notes

This project practically and structurally simulates the entire workflow of a data team in the healthcare sector. From modeling and implementing the database to creating an interactive dashboard, through exploratory analysis and the application of machine learning algorithms (unsupervised), each step was designed to reflect real-world scenarios.

More than just a technical exercise, this project represents a practical consolidation of skills in SQL, Python, Power BI, and data pipeline structuring, with special attention to code clarity, reproducibility (use of seeds), and documentation to make it easier for recruiters, colleagues, and others to understand.

It is important to mention that some of the data in the database contain logical inconsistencies, such as patients being registered before their birth date. These anomalies were intentionally kept untouched, as the main objective of this project was to practice data manipulation and analysis, not data validation. Fixing these issues would be trivial, but was not necessary for the Power BI and Machine Learning pipelines to function correctly.

Additionally, older scripts such as those for database creation make use of the traditional os.path module for file path handling, while the upload script uses pathlib, a more modern and object-oriented alternative that improves code readability, portability across operating systems, and robustness in managing complex paths. This also allowed for testing different approaches and ensuring adaptability for future projects.

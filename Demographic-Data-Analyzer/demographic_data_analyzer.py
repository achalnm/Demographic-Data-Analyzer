import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def race_count(df):
    return df['race'].value_counts()

def average_age_men(df):
    return df[df['sex'] == 'Male']['age'].mean()

def percentage_bachelors(df):
    total = df.shape[0]
    bachelors = df[df['education'] == 'Bachelors'].shape[0]
    return round((bachelors / total) * 100, 1)

def percentage_more_than_50k(df):
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    total_advanced = advanced_education.shape[0]
    high_earners_advanced = advanced_education[advanced_education['salary'] == '>50K'].shape[0]
    return round((high_earners_advanced / total_advanced) * 100, 1)

def percentage_no_advanced_education_more_than_50k(df):
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    total_no_advanced = no_advanced_education.shape[0]
    high_earners_no_advanced = no_advanced_education[no_advanced_education['salary'] == '>50K'].shape[0]
    return round((high_earners_no_advanced / total_no_advanced) * 100, 1)

def min_hours_per_week(df):
    return df['hours-per-week'].min()

def percentage_min_hours_more_than_50k(df):
    min_hours = min_hours_per_week(df)
    min_hours_df = df[df['hours-per-week'] == min_hours]
    total_min_hours = min_hours_df.shape[0]
    high_earners_min_hours = min_hours_df[min_hours_df['salary'] == '>50K'].shape[0]
    return round((high_earners_min_hours / total_min_hours) * 100, 1)

def highest_percentage_country(df):
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    country_salary['percentage'] = country_salary['>50K'] * 100
    max_country = country_salary['percentage'].idxmax()
    max_percentage = country_salary.loc[max_country, 'percentage']
    return max_country, round(max_percentage, 1)

def most_popular_occupation_in_india(df):
    india_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular = india_df['occupation'].value_counts().idxmax()
    return most_popular

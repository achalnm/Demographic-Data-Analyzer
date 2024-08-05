import demographic_data_analyzer as dda

df = dda.load_data('data.csv')

print("Race Count:\n", dda.race_count(df))
print("Average Age of Men:", dda.average_age_men(df))
print("Percentage with Bachelor's Degree:", dda.percentage_bachelors(df))
print("Percentage of Advanced Education Earning >50K:", dda.percentage_more_than_50k(df))
print("Percentage of No Advanced Education Earning >50K:", dda.percentage_no_advanced_education_more_than_50k(df))
print("Minimum Hours per Week:", dda.min_hours_per_week(df))
print("Percentage of Minimum Hours Earning >50K:", dda.percentage_min_hours_more_than_50k(df))
print("Country with Highest Percentage Earning >50K:", dda.highest_percentage_country(df))
print("Most Popular Occupation in India Earning >50K:", dda.most_popular_occupation_in_india(df))

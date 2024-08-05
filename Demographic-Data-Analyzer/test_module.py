import unittest
import pandas as pd
import demographic_data_analyzer as dda

class TestDemographicDataAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv('data.csv')

    def test_race_count(self):
        result = dda.race_count(self.df)
        self.assertEqual(result['White'], 27816)
        self.assertEqual(result['Black'], 3124)

    def test_average_age_men(self):
        result = dda.average_age_men(self.df)
        self.assertAlmostEqual(result, 39.4, places=1)

    def test_percentage_bachelors(self):
        result = dda.percentage_bachelors(self.df)
        self.assertAlmostEqual(result, 16.3, places=1)

    def test_percentage_more_than_50k(self):
        result = dda.percentage_more_than_50k(self.df)
        self.assertAlmostEqual(result, 24.0, places=1)

    def test_percentage_no_advanced_education_more_than_50k(self):
        result = dda.percentage_no_advanced_education_more_than_50k(self.df)
        self.assertAlmostEqual(result, 10.4, places=1)

    def test_min_hours_per_week(self):
        result = dda.min_hours_per_week(self.df)
        self.assertEqual(result, 1)

    def test_percentage_min_hours_more_than_50k(self):
        result = dda.percentage_min_hours_more_than_50k(self.df)
        self.assertAlmostEqual(result, 100.0, places=1)

    def test_highest_percentage_country(self):
        result = dda.highest_percentage_country(self.df)
        self.assertEqual(result[0], 'United-States')
        self.assertAlmostEqual(result[1], 29.0, places=1)

    def test_most_popular_occupation_in_india(self):
        result = dda.most_popular_occupation_in_india(self.df)
        self.assertEqual(result, 'Prof-specialty')

if __name__ == '__main__':
    unittest.main()

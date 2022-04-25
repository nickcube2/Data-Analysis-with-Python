import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"] == "Male"]["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    num__bachelors = len(df[df["education"] == "Bachelors"])
    total_num = len(df)

    percentage_bachelors = round(num__bachelors / total_num * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]    


    # percentage with salary >50K

    non_percentage_higher = len(higher_education[higher_education.salary == ">50K"])

    higher_education_rich = round(n

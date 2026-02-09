import pandas as pd

def calculate_demographic_data(print_data=True):
    """
    Analyze demographic data from the Adult Census dataset.

    The function calculates statistics related to race distribution, age,
    education level, working hours, salary, and occupation using pandas.

    Parameters:
        print_data (bool): Whether to print the calculated results to console.

    Returns:
        dict: A dictionary containing all computed demographic statistics.
    """

    # Load dataset from CSV file into a pandas DataFrame
    df = pd.read_csv("adult.data.csv")

    # ----------------------------------------------------
    # Race distribution
    # ----------------------------------------------------
    # Count the number of people belonging to each race
    races = df["race"].value_counts()
    race_count = pd.Series(data=races.values, index=races.index)

    # ----------------------------------------------------
    # Average age of men
    # ----------------------------------------------------
    # Filter dataset to include only male records
    men_chart = df[df.ne("Female").all(axis=1)]
    average_age_men = round(men_chart["age"].mean(), 1)

    # ----------------------------------------------------
    # Percentage of people with a Bachelor's degree
    # ----------------------------------------------------
    bachelor_counts = (df["education"] == "Bachelors").sum()
    education_total = df["education"].count()
    percentage_bachelors = round((bachelor_counts / education_total) * 100, 1)

    # ----------------------------------------------------
    # Income comparison based on education level
    # ----------------------------------------------------
    # People with advanced education (Bachelors, Masters, Doctorate)
    advance_education = df.loc[
        df["education"].str.contains("Bachelors|Masters|Doctorate")
    ]
    adv_high_salary = advance_education.loc[
        advance_education["salary"].str.contains(">50K")
    ]
    higher_education_count = adv_high_salary["salary"].count()

    # People without advanced education
    low_education = df.loc[
        ~df["education"].str.contains("Bachelors|Masters|Doctorate")
    ]
    low_high_salary = low_education.loc[
        low_education["salary"].str.contains(">50K")
    ]
    low_high_salary_count = low_high_salary["salary"].count()

    # Calculate percentage of high earners in each group
    all_high_salary = advance_education["salary"].count()
    all_low_salary = low_education["salary"].count()
    higher_education_rich = round(higher_education_count / all_high_salary * 100, 1)
    lower_education_rich = round(low_high_salary_count / all_low_salary * 100, 1)

    # ----------------------------------------------------
    # Minimum working hours
    # ----------------------------------------------------
    # Identify the minimum number of working hours per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of people earning >50K among those who work minimum hours
    min_hours_rich = df.loc[
        (df["hours-per-week"] == 1) & (df["salary"] == ">50K")
    ]
    all_min_hours = df.loc[df["hours-per-week"] == 1]
    num_min_workers_rich = len(min_hours_rich.index)
    rich_percentage = round(
        (num_min_workers_rich / len(all_min_hours.index)) * 100, 1
    )

    # ----------------------------------------------------
    # Country with highest percentage of high earners
    # ----------------------------------------------------
    all_salary = df.loc[df["salary"] == ">50K"]
    high_country_count = all_salary["native-country"].value_counts()
    country_count = df["native-country"].value_counts()

    highest_earning_country = (high_country_count / country_count).idxmax()
    highest_earning_country_percentage = round(
        (high_country_count / country_count).max() * 100, 1
    )

    # ----------------------------------------------------
    # Most popular occupation for high earners in India
    # ----------------------------------------------------
    high_salary_indians = df.loc[
        (df["native-country"] == "India") & (df["salary"] == ">50K")
    ]
    occupation_count = high_salary_indians["occupation"].value_counts()
    top_IN_occupation = occupation_count.idxmax()

    # ----------------------------------------------------
    # Output results
    # ----------------------------------------------------
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: "
            f"{highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }

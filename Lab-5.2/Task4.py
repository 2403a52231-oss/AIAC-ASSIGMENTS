def score_applicant(education, experience, gender, age):
    score = 0
    education_weights = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    score += education_weights.get(education.lower(), 0)
    if experience < 0:
        experience_points = 0
    elif experience < 2:
        experience_points = 5
    elif experience < 5:
        experience_points = 15
    elif experience < 10:
        experience_points = 25
    else:
        experience_points = 35
    score += experience_points
    if gender.lower() in ['male', 'female', 'other']:
        gender_points = 0 
    else:
        gender_points = 0  
    score += gender_points
    if age < 18:
        age_points = 0  
    elif 18 <= age < 25:
        age_points = 5
    elif 25 <= age < 40:
        age_points = 10
    elif 40 <= age < 60:
        age_points = 8
    else:
        age_points = 5
    score += age_points

    return score

def analyze_scoring_logic():
    print("Analyzing scoring logic for bias or unfair weightings...")
    print("- Education: Higher degrees are weighted more, which may disadvantage those with less access to education.")
    print("- Experience: More experience is rewarded, but may disadvantage younger applicants.")
    print("- Gender: No points are given for gender, which is fair. Gender should not affect scoring.")
    print("- Age: Some points are given based on age brackets, but extreme ages are not rewarded. Be cautious of age discrimination.")
    print("Recommendation: Regularly review and validate the scoring system to ensure fairness and compliance with anti-discrimination laws.")

def main():
    print("Job Applicant Scoring System")
    education = input("Enter education level (highschool, bachelor, master, phd): ").strip()
    try:
        experience = int(input("Enter years of relevant experience: ").strip())
    except ValueError:
        print("Invalid input for experience. Setting to 0.")
        experience = 0
    gender = input("Enter gender (male, female, other): ").strip()
    try:
        age = int(input("Enter age: ").strip())
    except ValueError:
        print("Invalid input for age. Setting to 0.")
        age = 0

    score = score_applicant(education, experience, gender, age)
    print(f"Applicant Score: {score}")

    analyze = input("Would you like to analyze the scoring logic for bias? (yes/no): ").strip().lower()
    if analyze == 'yes':
        analyze_scoring_logic()

if __name__ == "__main__":
    main()


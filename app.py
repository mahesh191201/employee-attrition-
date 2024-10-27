import pickle
import streamlit as st

model = pickle.load(open("AdaBoost.pkl", "rb"))


st.title("Employee Attrition Prediction")

bg = """

<style>
[data-testid="stAppViewContainer"] {
 
background-image: url("https://whatfix.com/blog/wp-content/uploads/2022/09/employee-churn.png");
background-size: cover;
}

<style/>

"""

st.markdown(bg, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    Age = st.text_input("Enter the Age")

with col2:
    BusinessTravel = st.text_input("Enter the Business Travel")

with col1:
    DailyRate = st.text_input("Emter the Daily Rate")

with col2:
    Department = st.text_input("Enter the Department")

with col1:
    DistanceFromHome = st.text_input("Enter the Distance from Home")

with col2:
    Education = st.text_input("Enter the Education")

with col1:
    EducationField = st.text_input("Enter the Education field")

with col2:
    EmployeeCount = st.text_input("Enter the Employee count")

with col1:
    EmployeeNumber = st.text_input("Enter the Employee Number")

with col2:
    EnvironmentSatisfaction = st.text_input(
        "Enter the Environment Satisfaction")

with col1:
    Gender = st.text_input("Enter the Gender")

with col2:
    HourlyRate = st.text_input("Enter the Hourly Rate")

with col1:
    JobInvolvement = st.text_input("Enter the Job Involment")

with col2:
    JobLevel = st.text_input("Enter the Job Level")

with col2:
    JobRole = st.text_input("Enter the Job role")

with col1:
    JobSatisfaction = st.text_input("Enter the Job satisfaction")

with col2:
    MaritalStatus = st.text_input("Enter the Marital Status")

with col1:
    MonthlyIncome = st.text_input("Enter the Monthly income")

with col2:
    MonthlyRate = st.text_input("Enter the Monthly rate")

with col1:
    NumCompaniesWorked = st.text_input("Enter the number of companies worked")

with col2:
    Over18 = st.text_input("Enter whether the employee is above 18")

with col1:
    OverTime = st.text_input("Enter whether employee does overtime")

with col2:
    PercentSalaryHike = st.text_input(
        "Enter the percent salary hike")

with col1:
    PerformanceRating = st.text_input("Enter the performance rating")

with col2:
    RelationshipSatisfaction = st.text_input(
        "Enter the relationship satisfaction")

with col1:
    StandardHours = st.text_input("Enter the standard hours")

with col2:
    StockOptionLevel = st.text_input("Enter the stock option level")

with col1:
    TotalWorkingYears = st.text_input("Enter the total working hours")


with col2:
    TrainingTimesLastYear = st.text_input("Enter the training time last year")


with col1:
    WorkLifeBalance = st.text_input("Enter the work life balance")


with col2:
    YearsAtCompany = st.text_input("Enter years at company")


with col1:
    YearsInCurrentRole = st.text_input("Enter years in current role")


with col2:
    YearsSinceLastPromotion = st.text_input("Enter years since last promotion")


with col1:
    YearsWithCurrManager = st.text_input("Enter years with current manager")


Attrition = ""


if st.button("Employee Attrition Result"):
    try:
        age = int(Age)
        bt = int(BusinessTravel)
        dr = int(DailyRate)
        dp = int(Department)
        dfh = int(DistanceFromHome)
        ed = int(Education)
        ef = int(EducationField)
        ec = int(EmployeeCount)
        en = int(EmployeeNumber)
        es = int(EnvironmentSatisfaction)
        gd = int(Gender)
        hr = int(HourlyRate)
        ji = int(JobInvolvement)
        jl = int(JobLevel)
        jr = int(JobRole)
        js = int(JobSatisfaction)
        ms = int(MaritalStatus)
        mi = int(MonthlyIncome)
        ncw = int(NumCompaniesWorked)
        o18 = int(Over18)
        ot = int(OverTime)
        psh = int(PercentSalaryHike)
        pr = int(PerformanceRating)
        rs = int(RelationshipSatisfaction)
        sh = int(StandardHours)
        sol = int(StockOptionLevel)
        twy = int(TotalWorkingYears)
        ttly = int(TrainingTimesLastYear)
        wlb = int(WorkLifeBalance)
        ytc = int(YearsAtCompany)
        yic = int(YearsInCurrentRole)
        yslp = int(YearsSinceLastPromotion)
        ywcm = int(YearsWithCurrManager)

        # prediction

        prediction = model.predict([[age,
                                     bt,
                                     dr,
                                     dp,
                                     dfh,
                                     ed,
                                     ef,
                                     ec,
                                     en,
                                     es,
                                     gd,
                                     hr,
                                     ji,
                                     jl,
                                     jr,
                                     js,
                                     ms,
                                     mi,
                                     ncw,
                                     o18,
                                     ot,
                                     psh,
                                     pr,
                                     rs,
                                     sh,
                                     sol,
                                     twy,
                                     ttly,
                                     wlb,
                                     ytc,
                                     yic,
                                     yslp,
                                     ywcm]])
        if prediction[0] == 0:
            Attrition = "The employement wont leave"
        else:
            Attrition = "The employee may leave"
    except ValueError as e:
        st.error(f"Invalid input: {e}")

st.success(Attrition)

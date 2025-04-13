Use Python 3.10.8 and install the necessary libraries from requirements.txt file.

Prediction results are accurate when you provide valid medical input values for example:

Example 1:
Patient Name: John Doe
Age: 45
Sex: Male
Waist Circumference: 102
BMI: 28.4
Albuminuria: Yes
Urine Albumin-to-Creatinine Ratio: 35
Uric Acid: 6.5
Blood Glucose: 155
HDL Cholesterol: 38
Triglycerides: 180
Selected Model: Random Forest

Output: At Risk of Metabolic Syndrome  
(A detailed report will be generated and can be downloaded.)

---

Example 2:
Patient Name: Jane Smith  
Age: 34  
Sex: Female  
Waist Circumference: 85  
BMI: 22.7  
Albuminuria: No  
Urine Albumin-to-Creatinine Ratio: 18  
Uric Acid: 4.8  
Blood Glucose: 95  
HDL Cholesterol: 60  
Triglycerides: 120  
Selected Model: SVM

Output: Not at Risk of Metabolic Syndrome

---

📝 Notes:
- Always ensure that all input fields are filled to get accurate predictions.
- Select the model that best suits your testing criteria (SVM, Random Forest, XGBoost).
- The system supports generating a printable report after prediction.
- For best performance, deploy using Django's runserver or host on a cloud server.

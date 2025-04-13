import os
import joblib
import numpy as np
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('input')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')

@login_required
def input_view(request):
    if request.method == 'POST':
        try:
            # ✅ Collect Patient Name
            name = request.POST.get('name')

            # Collect other input data
            age = float(request.POST.get('age'))
            sex_text = request.POST.get('sex')
            sex = 1 if sex_text == 'Male' else 0
            waist = float(request.POST.get('waist'))
            bmi = float(request.POST.get('bmi'))
            albuminuria = float(request.POST.get('albuminuria'))
            urine_ratio = float(request.POST.get('urine_ratio'))
            uric_acid = float(request.POST.get('uric_acid'))
            glucose = float(request.POST.get('glucose'))
            hdl = float(request.POST.get('hdl'))
            triglycerides = float(request.POST.get('triglycerides'))
            selected_model = request.POST.get('model')

            # Map model names from form to actual filenames
            model_map = {
                'SVM': 'svm_model',
                'RandomForest': 'rf_model',
                'XGBoost': 'xgb_model'
            }

            model_file = model_map.get(selected_model)
            if not model_file:
                return render(request, 'accounts/input.html', {'error': 'Invalid model selected'})

            # Prepare input array
            input_data = np.array([[age, sex, waist, bmi, albuminuria, urine_ratio,
                                    uric_acid, glucose, hdl, triglycerides]])

            # Load scaler and scale the input
            scaler_path = os.path.join(settings.BASE_DIR, 'models', 'scaler.pkl')
            scaler = joblib.load(scaler_path)
            scaled_data = scaler.transform(input_data)

            # Load model
            model_path = os.path.join(settings.BASE_DIR, 'models', f'{model_file}.pkl')
            model = joblib.load(model_path)

            # Predict
            result = model.predict(scaled_data)[0]
            prediction_text = "Metabolic Syndrome Detected" if result == 1 else "No Metabolic Syndrome"

            # ✅ Store report data in session, including name
            request.session['report_data'] = {
                'Patient Name': name,
                'Age': age,
                'Sex': sex_text,
                'Waist': waist,
                'BMI': bmi,
                'Albuminuria': albuminuria,
                'Urine Ratio': urine_ratio,
                'Uric Acid': uric_acid,
                'Glucose': glucose,
                'HDL': hdl,
                'Triglycerides': triglycerides,
                'Selected Model': selected_model,
                'Prediction': prediction_text
            }

            return render(request, 'accounts/output.html', {'prediction': prediction_text})
        except Exception as e:
            return render(request, 'accounts/input.html', {'error': f'Error: {str(e)}'})

    return render(request, 'accounts/input.html')

@login_required
def output_view(request):
    return render(request, 'accounts/output.html')

@login_required
def report_view(request):
    report_data = request.session.get('report_data', {})
    return render(request, 'accounts/report.html', {'report_data': report_data})

def logout_view(request):
    logout(request)
    return redirect('login')

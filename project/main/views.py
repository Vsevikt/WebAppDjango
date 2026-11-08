from datetime import date, timedelta

from django.shortcuts import render

def home(request):
    active_task = 'login'

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if username == 'admin' and password == 'admin123':
            login_success = True
            login_result = 'Welcome, Administrator! Access level: Administrator.'
        elif username == 'user' and password == 'user123':
            login_success = True
            login_result = 'Welcome, User! Access level: User.'
        else:
            login_success = False
            login_result = 'Incorrect username or password.'

    return render(request, 'main/index.html', locals())


def calculator(request):
    active_task = 'calculator'

    if request.method == 'POST':
        try:
            number1 = float(request.POST['number1'])
            number2 = float(request.POST['number2'])
            number3 = float(request.POST['number3'])

            operation = request.POST.get('operation')

            if operation == 'min':
                result = min(number1, number2, number3)
            elif operation == 'max':
                result = max(number1, number2, number3)
            else:
                result = (number1 + number2 + number3) / 3

            calculator_result = f'{result:g}'

        except (KeyError, ValueError):
            calculator_error = 'Please enter three valid numbers.'

    return render(request, 'main/index.html', locals())


def registration(request):
    active_task = 'registration'

    if request.method == 'POST':
        data = request.POST

        newsletter = 'Yes' if data.get('newsletter') else 'No'

        registration_result = (
            f"Name: {data.get('first_name', '').strip()} {data.get('last_name', '').strip()}\n"
            f"Age: {data.get('age', '')}\n"
            f"Email: {data.get('email', '').strip()}\n"
            f"Gender: {data.get('gender', '')}\n"
            f"Delivery address: {data.get('address', '').strip()}\n"
            f"Newsletter subscription: {newsletter}"
        )

    return render(request, 'main/index.html', locals())


def programmer_day(request):
    active_task = 'programmer_day'

    if request.method == 'POST':
        try:
            year = int(request.POST['year'])

            if year < 1960 or year > 2100:
                raise ValueError

            day = date(year, 1, 1) + timedelta(days=255)

            programmer_day_result = day.strftime('%B %d (%A)')
            programmer_year = year

        except (KeyError, ValueError, OverflowError):
            programmer_day_error = 'Enter a year between 1960 and 2100.'

    return render(request, 'main/index.html', locals())

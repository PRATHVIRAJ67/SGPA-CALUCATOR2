from flask import Flask, request, render_template
app = Flask(__name__, template_folder=r'C:\Users\prathviraj\Desktop\sgpa')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    subjects = {
        'Math': (0, 3),
        'Design and Analysis of Algorithms': (0, 4),
        'Microcontrollers': (0, 4),
        'OS': (0, 3),
        'Biology': (0, 2),
        'Kannada': (0, 1),
        'UHV': (0, 1),
        'IIP': (0, 1),
        'Python Lab': (0, 1),
        'Shell Programming': (0, 1),
    }

    grade_system = {
        range(91, 101): 10,
        range(81, 91): 9,
        range(71, 81): 8,
        range(61, 71): 7,
    }

    total_weighted_grade_points = 0
    total_credits = 0

    for subject, (marks, credits) in subjects.items():
        marks = int(request.form[subject])
        for grade_range, grade_point in grade_system.items():
            if marks in grade_range:
                weighted_grade_points = grade_point * credits
                total_weighted_grade_points += weighted_grade_points
                total_credits += credits
                break

    sgpa = total_weighted_grade_points / total_credits
    return "Your SGPA is {:.2f}".format(sgpa)

if __name__ == '__main__':
    app.run(debug=True)
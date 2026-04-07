from flask import Flask, render_template, request, redirect, url_for, flash
from backend import SchoolManagement
import os

app = Flask(__name__)
app.secret_key = 'school_management_secret_key'

# Initialize the school management system
sm = SchoolManagement()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/students')
def students():
    students_list = sm.get_all_students()
    return render_template('students.html', students=students_list)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = request.form
        result = sm.add_student(
            data['admin_no'], data['name'], data['gender'],
            data['class'], data['father_name'], data['mother_name'],
            data['contact_no'], data['dob']
        )
        if "successfully" in result:
            flash(result, 'success')
            return redirect(url_for('students'))
        else:
            flash(result, 'error')
    return render_template('add_student.html')

@app.route('/search_student', methods=['GET', 'POST'])
def search_student():
    student = None
    if request.method == 'POST':
        admin_no = request.form['admin_no']
        student = sm.search_student(admin_no)
        if not student:
            flash('Student not found', 'error')
    return render_template('search_student.html', student=student)

@app.route('/update_student/<admin_no>', methods=['GET', 'POST'])
def update_student(admin_no):
    if request.method == 'POST':
        field = request.form['field']
        value = request.form['value']
        result = sm.update_student(admin_no, field, value)
        flash(result, 'info')
        return redirect(url_for('search_student'))
    return render_template('update_student.html', admin_no=admin_no)

@app.route('/add_exam', methods=['GET', 'POST'])
def add_exam():
    if request.method == 'POST':
        data = request.form
        result = sm.add_exam_marks(
            data['admin_no'], int(data['physics']), int(data['chemistry']),
            int(data['biology']), int(data['maths']), int(data['cs']),
            int(data['hindi']), int(data['english'])
        )
        flash(result, 'info')
    return render_template('add_exam.html')

@app.route('/results')
def results():
    results_list = sm.get_exam_result()
    return render_template('results.html', results=results_list)

@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        admin_no = request.form['admin_no']
        result = sm.delete_student(admin_no)
        flash(result, 'info')
        return redirect(url_for('students'))
    return render_template('delete_student.html')

if __name__ == '__main__':
    app.run(debug=True)
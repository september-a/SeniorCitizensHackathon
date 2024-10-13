from flask import *
from extensions import db
from models.courses import Course
from models.Colleges import Colleges
from models.department import Department
from models.courseListings import CourseListings
from models.majors import Majors
from models.faculty import Faculty
import os

app = Flask(__name__)
cwd = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + cwd + '/database.db'
db.init_app(app)

@app.route('/html/courses')
def getAllCourses():
    courses = Course.query.all()  # Query all courses from the database
    # Convert courses to a list of dictionaries for JSON serialization
    courses_data = [{'name': course.name, 'department': course.department_name} for course in courses]
    # return jsonify(courses_data)
    return render_template('courses.html', data=courses_data)


@app.route('/html/colleges')
def getAllColleges():
    colleges = Colleges.query.all() #Query all colleges from the database
    #convert the colleges to a list of dictionaries for JSON serialization
    college_data = [{'name': colleges.name} for colleges in colleges]
    # return jsonify(college_data)
    return render_template('colleges.html', data=college_data)


@app.route('/html/majors')
def getAllMajors():
    majors = Majors.query.all()
    major_data = [{'name': major.name,
                   'program type': major.degreeType,
                   'college': major.college} for major in majors]
    # return jsonify(major_data)
    return render_template('majors.html', data=major_data)
    

@app.route('/html/department')
#    "Department": {
#       "Name": "String",
#       "abbreviation": "String",
#       "college": "String",
def getAllDepartments():
    departments = Department.query.all()
    #Convert the departments to a list of dictionaries for JSON serialization
    department_data = [{'name':departments.name} for departments in departments]

    # return jsonify(department_data)
    return render_template('departments.html', data=department_data)

@app.route('/html/faculty')
def getAllFaculty():
    faculty = Faculty.query.all()
    faculty_data = [{'name':fac.name,  
                     'Position':fac.positions, 
                     'Phone Number':fac.phoneNumber, 
                     'email':fac.emailAddress,} 
                     for fac in faculty]
    # return jsonify(faculty_data)
    return render_template('faculty.html', data=faculty_data)

@app.route('/html/courselistings')
def getAllCourseListings():
    course_listings = CourseListings.query.all()
    course_data = [{'CRN':course_listing.CRN,
                    'course':course_listing.course, 
                    'title':course_listing.title,
                    'max_enrollment':course_listing.max_enrollment,
                    'start':course_listing.start,
                    'end':course_listing.end,
                    'days':course_listing.days,}
                    for course_listing in course_listings]
    #return jsonify(course_data)
    return render_template('courseListings.html', data=course_data)


@app.route('/')
def list_endpoints():
    # Define a list of endpoint URLs
    endpoints = [
        '/html/department',
        '/html/courses',
        '/html/colleges',
        '/html/courselistings',
        '/html/faculty',
        '/html/majors'
        # Add more endpoints as needed
    ]
    return render_template('endpoints.html', endpoints=endpoints)

@app.route('/courses')
def getAllCoursesJSON():
    courses = Course.query.all()  # Query all courses from the database
    # Convert courses to a list of dictionaries for JSON serialization
    courses_data = [{'name': course.name, 'department': course.department_name} for course in courses]
    return jsonify(courses_data)


@app.route('/colleges')
def getAllCollegesJSON():
    colleges = Colleges.query.all() #Query all colleges from the database
    #convert the colleges to a list of dictionaries for JSON serialization
    college_data = [{'name': colleges.name} for colleges in colleges]
    return jsonify(college_data)


@app.route('/majors')
def getAllMajorsJSON():
    majors = Majors.query.all()
    major_data = [{'name': major.name,
                   'program type': major.degreeType,
                   'college': major.college} for major in majors]
    return jsonify(major_data)
    

@app.route('/department')
#    "Department": {
#       "Name": "String",
#       "abbreviation": "String",
#       "college": "String",
def getAllDepartmentsJSON():
    departments = Department.query.all()
    #Convert the departments to a list of dictionaries for JSON serialization
    department_data = [{'name':departments.name} for departments in departments]

    return jsonify(department_data)

@app.route('/faculty')
def getAllFacultyJSON():
    faculty = Faculty.query.all()
    faculty_data = [{'name':fac.name,  
                     'Position':fac.positions, 
                     'Phone Number':fac.phoneNumber, 
                     'email':fac.emailAddress,} 
                     for fac in faculty]
    return jsonify(faculty_data)

@app.route('/courselistings')
def getAllCourseListingsJSON():
    course_listings = CourseListings.query.all()
    course_data = [{'CRN':course_listing.CRN,
                    'course':course_listing.course, 
                    'title':course_listing.title,
                    'max_enrollment':course_listing.max_enrollment,
                    'start':course_listing.start,
                    'end':course_listing.end,
                    'days':course_listing.days,}
                    for course_listing in course_listings]
    return jsonify(course_data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port = 5001)

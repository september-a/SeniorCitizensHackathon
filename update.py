from extensions import db
from app_db import app
import _grabbers.DeptGrabber as DeptGrabber
import _grabbers.ProgramGrabber as ProgramGrabber
import _grabbers.FacultyGrabber as FacultyGrabber
from _grabbers.CourseGrabber import scrape_schedule_information

with app.app_context():
    # Drop existing tables, create new ones, and populate data
    db.drop_all()
    db.create_all()
    DeptGrabber.getCourses()
    ProgramGrabber.getPrograms()
    scrape_schedule_information()
    FacultyGrabber.populateFaculty()

#Collection of handlers to process route request from main.py

import webapp2
import cgi
import jinja2
import os

from datetime import datetime
from logics import Employee
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        emp = Employee() 
        template_values = {'employees': emp.list_employee()}
        template = jinja_environment.get_template('template/index.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.POST.get('delete'): #if user click "Delete" button
                employee_ids = self.request.get('employee_id',allow_multiple=True) #allow_multiple=True so that it reads multiple keys into list.
                emp = Employee()
                emp.delete_employee(employee_ids)
                self.redirect('/')
        else:
            self.redirect(users.create_login_url(self.request.uri))


class CreateHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = jinja_environment.get_template('template/create.html')
            self.response.out.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        #get input values
        input_name = self.request.get('name').strip()
        input_gender = self.request.get('gender').strip()
        input_dob = self.request.get('dob').strip()
        
        emp = Employee()
        emp.save_employee(input_name,input_gender,input_dob,0)
        self.redirect('/')


class EditHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            #get entity
            emp = Employee()
            emp = emp.get_employee(long(self.request.get('id')))
            
            template_values = {'employee': emp}
            template = jinja_environment.get_template('template/edit.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        #get all input values
        input_id = self.request.get('id')
        input_name = self.request.get('name').strip()
        input_gender = self.request.get('gender').strip()
        input_dob = self.request.get('dob').strip()

        emp = Employee()
        emp.save_employee(input_name,input_gender,input_dob,long(input_id))
        self.redirect('/')
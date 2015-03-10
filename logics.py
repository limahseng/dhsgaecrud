#Business logic

from models import EmployeeModel
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

class Employee(object):
	def save_employee(self,name,gender,dob,id):
		#id will be greater than zero when EDIT action is triggered.
		if id > 0:
			emp = EmployeeModel.get_by_id(id)
		else:
			emp = EmployeeModel()

		emp.name = name
		emp.gender = gender
		emp.dob = datetime.date(year=int(dob[:4]), month=int(dob[5:7]), day=int(dob[8:]))
		emp.email = users.get_current_user().email()
		emp.put()

	def delete_employee(self, employee_ids):
		if len(employee_ids) > 0:
			for employee_id in employee_ids:
				emp = EmployeeModel.get_by_id(long(employee_id))
				emp.key.delete()

	def list_employee(self):
		employee_query = EmployeeModel.query()
		return employee_query

	def get_employee(self, employee_id):
		emp = EmployeeModel.get_by_id(employee_id)
		return emp
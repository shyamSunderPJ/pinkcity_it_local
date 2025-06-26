# Copyright (c) 2025, pinkcity and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ApiTest(Document):
	pass

    # In my_app/my_app/my_module.py
    
@frappe.whitelist()
def send_data_to_python():
	data = frappe.new_doc('Api Test')
	data.primary_name = frappe.form_dict.get('full_name')
	data.current_age = frappe.form_dict.get('age')
	data.date_of_birth = frappe.form_dict.get('Birth')
	
	data.append("more_details", {
		"gender": frappe.form_dict.get('Gender'),
		"phone_no": frappe.form_dict.get('phone_no'),
		"city": frappe.form_dict.get('city'),
		"age": frappe.form_dict.get('Age'),
	})
	data.insert()
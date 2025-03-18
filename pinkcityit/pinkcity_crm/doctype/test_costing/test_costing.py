# Copyright (c) 2025, Pink city IT team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TestCosting(Document):
	# pass

	def autoname(self):

		temp_name = 'TCost'

		if self.clients_code : 
			temp_name = temp_name + "-" +self.clients_code

		last_doc_name = frappe.db.get_list('Test Costing',
                filters={
                    "name": ["like", "%"+temp_name+"%"]
                },
                fields=['name'],
                order_by='name desc',
                # start=10,
                page_length=1,
                # as_list=True
            )

		####### this only gave name for new entry
		new_name = temp_name + "-00001"
		if last_doc_name :
			for last_doc in last_doc_name:
				# frappe.msgprint(last_doc.get("name", "00-0"));
				last_doc_arr_name = last_doc.get("name", "00-0")
				last_name_digit_array = last_doc_arr_name.split("-")

				last_name_digit = last_name_digit_array[-1]
				last_no = 1
				if self.clients_code : 
					if(len(last_name_digit_array) >= 4) :
						last_name_digit = last_name_digit_array[-2]
					else :
						last_name_digit = last_name_digit_array[-1]
					# last_no = int( int(last_name_digit or 0) + 1 or 1 ) 
				else :
					if(len(last_name_digit_array) >= 3) :
						last_name_digit = last_name_digit_array[-2]
					else :
						last_name_digit = last_name_digit_array[-1]
					# last_no = int( int(last_name_digit or 0) + 1 or 1 ) 
				try :
					last_no = int(last_name_digit) + 1
				except :
					last_no = 1
					
				new_name =  temp_name + "-"+ str(last_no).zfill(4)
        
		self.name = new_name
	

	
	def before_insert(self) :
		temp_name = 'TCost'

		if self.clients_code : 
			temp_name = temp_name + "-" +self.clients_code

		last_doc_name = frappe.db.get_list('Test Costing',
                filters={
                    "name": ["like", "%"+temp_name+"%"]
                },
                fields=['name'],
                order_by='name desc',
                # start=10,
                page_length=1,
                # as_list=True
            )

		####### this only gave name for new entry
		new_name = temp_name + "-00001"
		if last_doc_name :
			for last_doc in last_doc_name:
				# frappe.msgprint(last_doc.get("name", "00-0"));
				last_doc_arr_name = last_doc.get("name", "00-0")
				last_name_digit_array = last_doc_arr_name.split("-")

				last_name_digit = last_name_digit_array[-1]
				last_no = 1
				if self.clients_code : 
					if(len(last_name_digit_array) >= 4) :
						last_name_digit = last_name_digit_array[-2]
					else :
						last_name_digit = last_name_digit_array[-1]
					# last_no = int( int(last_name_digit or 0) + 1 or 1 ) 
				else :
					if(len(last_name_digit_array) >= 3) :
						last_name_digit = last_name_digit_array[-2]
					else :
						last_name_digit = last_name_digit_array[-1]
					# last_no = int( int(last_name_digit or 0) + 1 or 1 ) 
				try :
					last_no = int(last_name_digit) + 1
				except :
					last_no = 1
					
				new_name =  temp_name + "-"+ str(last_no).zfill(4)
        
		self.name = new_name

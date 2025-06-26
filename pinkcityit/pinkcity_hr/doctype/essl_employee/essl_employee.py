# Copyright (c) 2025, Pink city IT team and contributors
# For license information, please see license.txt

import frappe, pymssql
from frappe.model.document import Document


class ESSLEmployee(Document):
	
	def db_insert(self, *args, **kwargs):
		pass

	def load_from_db(self):
		server = '192.168.5.110'
		user = 'esslNew'
		password = 'admin@122'
		database = 'etimetracklite1'

		conn = pymssql.connect(server=server, user=user, password=password, database=database, port=5555,  tds_version=r'7.0')
		cursor = conn.cursor(as_dict=True)

		query = f"""SELECT 
						e.EmployeeCode name,
						e.EmployeeName employee_name,
						d.DepartmentFName department,
						e.SubDepartment sub_department,
						e.Grade grade,
						e.Location location,
						ct.CategoryFName category,
						e.DOJ doj,
						e.Status status,
						e.Gender gender,
						e.EmployeeCode employee_code,
						c.CompanyFName company,	
						e.Designation designation,
						e.Team team,
						e.EmployementType employment_type,
						e.DOC doc,
						e.AadhaarNumber aadhar_card,
						e.EmployeeId employee_id,
						e.EnrolledDate creation,
						e.EnrolledDate modified
					FROM Employees e
					LEFT JOIN Companies c on c.CompanyId = e.CompanyId 
					LEFT JOIN Departments d on d.DepartmentId = e.DepartmentId
					LEFT JOIN Categories ct on ct.CategoryId = e.CategoryId
					WHERE e.EmployeeCode = '{self.name}'
					"""
		
		cursor.execute(query)
		row = cursor.fetchone()
		super(Document, self).__init__(row)


	def db_update(self, *args, **kwargs):
		pass

	@staticmethod
	def get_list(args):
		server = '192.168.5.110'
		user = 'esslNew'
		password = 'admin@122'
		database = 'etimetracklite1'

		conn = pymssql.connect(server=server, user=user, password=password, database=database, port=5555,  tds_version=r'7.0')
		cursor = conn.cursor(as_dict=True)

		start = int(args.get("start") or 0)
		page_length = int(args.get("page_length") or 0) 

		order_by = args.get("order_by", 'name desc')
		order_by = order_by.replace('`tabESSL Employee`.', '')
		order_by = order_by.replace('`', '')

		filters = args.get("filters", [])
		where_query = ""
		i = 0
		for filter in filters :
			if i > 0 :
				where_query = where_query + " AND "
			if filter[1]=='employee_name':
				where_query = where_query + " e.EmployeeName " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			if filter[1]=='employee_code':
				where_query = where_query + " e.EmployeeCode " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			if filter[1]=='location':
				where_query = where_query + " e.Location " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			if filter[1]=='status':
				where_query = where_query + " e.Status " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			

		query = f"""SELECT 
						e.EmployeeCode name,
						e.EmployeeName employee_name,
						e.EmployeeCode employee_code,
						e.Designation designation,
						e.EmployementType employment_type,	
						e.Status status,
						e.Location location,
						e.EnrolledDate creation,
						e.EnrolledDate modified
					FROM Employees e
					"""
		if where_query :
			query = query + " WHERE  " + where_query

		query = query + f""" 
					ORDER BY {order_by}
					OFFSET {start} ROWS
					FETCH NEXT {page_length} ROWS ONLY """
		
		cursor.execute(query)
		all_row = cursor.fetchall()
		return all_row

	@staticmethod
	def get_count(args):
		server = '192.168.5.110'
		user = 'esslNew'
		password = 'admin@122'
		database = 'etimetracklite1'

		total_no = 0 
		conn = pymssql.connect(server=server, user=user, password=password, database=database, port=5555,  tds_version=r'7.0')
		cursor = conn.cursor(as_dict=True)

		filters = args.get("filters", [])
		where_query = ""
		i = 0
		for filter in filters :
			if i > 0 :
				where_query = where_query + " AND "
			if filter[1]=='employee_name':
				where_query = where_query + " e.EmployeeName " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			if filter[1]=='employee_code':
				where_query = where_query + " e.EmployeeCode " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			if filter[1]=='location':
				where_query = where_query + " e.Location " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			if filter[1]=='status':
				where_query = where_query + " e.Status " + filter[2] + " '" + filter[3] + "'"
				i = i + 1
			# if filters.get("company"):
			# 	if filters.get("company") == "Pinkcity Jewelhouse Private Ltd-Mahapura":
			# 		conditions += " e.location = 'PC-M' "
			# 	if filters.get("company") == "Pinkcity Jewelhouse Private Limited- Unit 1":
			# 		conditions += " e.location = 'PC-I' "
			# 	if filters.get("company") == "Pinkcity Jewelhouse Private Limited-Unit 2":
			# 		conditions += " e.location = 'PC-II' "
			# 	if filters.get("company") == "PINKCITY COLORSTONES PVT. LTD.":
			# 		conditions += " e.location = 'SILVER' "
			# 	if filters.get("company") == "ATELIER PINKCITY PRIVATE LIMITED":
			# 		conditions += " e.location = 'Atelier' "

		query = f"""SELECT 
					COUNT (e.EmployeeId) total_no
					FROM Employees e
					"""
		
		if where_query :
			query = query + " WHERE " + where_query

		cursor.execute(query)
		row = cursor.fetchone()
		total_no = row.get("total_no", 0) 
		return  total_no


	@staticmethod
	def get_stats(args):
		pass

# Copyright (c) 2025, pinkcity and contributors
# For license information, please see license.txt

import frappe, pymssql , datetime
from frappe.model.document import Document
# from hrms.hr.doctype.shift_type.shift_type import process_auto_attendance

class ESSLCompany(Document):
	
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
						CompanyId name,
						CompanyFName company_name,
						CompanySName short_name,
						CompanyEmail email,
						CompanyWebsite website,	
						CompanyAddress address,
						CompanyIsVisible visible_to_all,
						GETDATE() creation,
						GETDATE() modified
					FROM Companies
					WHERE CompanyId = '{self.name}'
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
		order_by = order_by.replace('`tabESSL Company`.', '')
		order_by = order_by.replace('`', '')

		# filters = args.get("filters", [])
		# where_query = ""
		# i = 0
		# for filter in filters :
		# 	if i > 0 :
		# 		where_query = where_query + " AND "
		# 	if filter[1]=='employee_name':
		# 		where_query = where_query + " e.EmployeeName " + filter[2] + " '" + filter[3] + "'"
		# 		i = i + 1
		# 	if filter[1]=='employee_code':
		# 		where_query = where_query + " e.EmployeeCode " + filter[2] + " '" + filter[3] + "'"
		# 		i = i + 1
		# 	if filter[1]=='location':
		# 		where_query = where_query + " e.Location " + filter[2] + " '" + filter[3] + "'"
		# 		i = i + 1
		# 	if filter[1]=='status':
		# 		where_query = where_query + " e.Status " + filter[2] + " '" + filter[3] + "'"
		# 		i = i + 1


		query = f"""SELECT 
						CompanyId name,
						CompanyFName company_name,
						CompanySName short_name,
						CompanyEmail email,
						CompanyWebsite website,	
						CompanyAddress address,
						GETDATE() creation,
						GETDATE() modified
					FROM Companies
					"""
		# if where_query :
		# 	query = query + " WHERE  " + where_query

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

		query = f"""SELECT 
					COUNT (CompanyId) total_no
					FROM Companies 
					"""
		
		# if where_query :
		# 	query = query + " WHERE " + where_query

		cursor.execute(query)
		row = cursor.fetchone()
		total_no = row.get("total_no", 0) 
		return  total_no


	@staticmethod
	def get_stats(args):
		return {}
		# pass

@frappe.whitelist()
def employee_checkin():

	company_id = int(frappe.form_dict.get("company_id", 0) or 0)
	date = frappe.form_dict.get("date" , '')

	company_name = ""
	
	if company_id == 4:
		company_name = "Pinkcity Jewelhouse Private Ltd-Mahapura"
	if company_id == 2:
		company_name = "Pinkcity Jewelhouse Private Limited- Unit 1"
	if company_id == 3:
		company_name = "Pinkcity Jewelhouse Private Limited-Unit 2"
	if company_id == 8:
		company_name = "PINKCITY COLORSTONES PVT. LTD."
	if company_id == 9:
		company_name = "ATELIER PINKCITY PRIVATE LIMITED"
	
	getEmployeeCheck(company_name, date)

	frappe.response["status"] = True
	frappe.response["msg"] = "All Employee Checkin."


def getEmployeeCheck(company, date) :
	server = '192.168.5.110'
	user = 'esslNew'
	password = 'admin@122'
	database = 'etimetracklite1'

	conn = pymssql.connect(server=server, user=user, password=password, database=database, port=5555,  tds_version=r'7.0')
	cursor = conn.cursor(as_dict=True)

	all_employee = frappe.db.get_all('Employee',
										filters={
											'status': 'Active',
											'company': company,
										},
										fields=['employee', 'employee_name', 'attendance_device_id'],
										# order_by='date desc',
										# as_dict=True
									)
	
	# frappe.response["all_employee"] = all_employee
	# frappe.response["company_name"] = company_name
	# frappe.response["company_id"] = company_id


	conditions = ""

	current_date = datetime.datetime.strptime(str(date) , '%Y-%m-%d')
	next_date = current_date + datetime.timedelta(days=1)
	month = current_date.month
	year = current_date.year
	next_month = next_date.month
	next_year = next_date.year


	conditions += f" AND LogDate >= '{current_date.strftime('%Y-%m-%d')} 08:00:00'"
	conditions += f" AND LogDate <= '{next_date.strftime('%Y-%m-%d')} 07:59:59'"

	for employee in all_employee:
		frappe.response["hello"] = "hi22"
		if employee.get("attendance_device_id", False) :
			frappe.response["hello2"] = "hi33"
			frappe.response["attendance_device_id"] = employee.get("attendance_device_id", False)
			if month == next_month:
				query = f"""    SELECT 
								dl.UserId,
								MIN(dl.LogDate) in_time,
								MAX(dl.LogDate) out_time,
								MIN(dl.DeviceLogId) in_time_log_id,
								MAX(dl.DeviceLogId) out_time_log_id
							FROM DeviceLogs_{month}_{year} dl 
							WHERE 
								dl.UserId = '{employee.get("attendance_device_id", False)}'
								{conditions}
							GROUP BY dl.UserId
						"""
			else :
				query = f"""    SELECT 
								dl.UserId,
								MIN(dl.LogDate) in_time,
								MAX(dl.LogDate) out_time,
								MIN(dl.DeviceLogId) in_time_log_id,
								MAX(dl.DeviceLogId) out_time_log_id
							FROM DeviceLogs_{month}_{year} dl 
							WHERE 
								dl.UserId = '{employee.get("attendance_device_id", False)}'
								{conditions}
							GROUP BY dl.UserId
						UNION 
							SELECT 
								dl2.UserId,
								MIN(dl2.LogDate) in_time,
								MAX(dl2.LogDate) out_time,
								MIN(dl2.DeviceLogId) in_time_log_id,
								MAX(dl2.DeviceLogId) out_time_log_id
							FROM DeviceLogs_{next_month}_{next_year} dl2 
							WHERE 
								dl2.UserId = '{employee.get("attendance_device_id", False)}'
								{conditions}
							GROUP BY dl2.UserId
						"""
				
			cursor.execute(query)
			checkInData = cursor.fetchone()
			# frappe.response["checkInData"] = checkInData

			if checkInData :
				if checkInData.get('in_time', False) :
					if checkInData.get('out_time', False) :
						if checkInData.get('out_time') == checkInData.get('in_time') :
							addEmployeeCheckIn(employee.get("employee", ""), checkInData.get('in_time'), "IN", checkInData.get('in_time_log_id'))
						else :
							addEmployeeCheckIn(employee.get("employee", ""), checkInData.get('in_time'), "IN", checkInData.get('in_time_log_id'))
							addEmployeeCheckIn(employee.get("employee", ""), checkInData.get('out_time'), "OUT", checkInData.get('out_time_log_id'))


def addEmployeeCheckIn(employee, time, log_type, device_id):
	if frappe.db.exists("Employee Checkin", {"employee": employee, 
											 "time": time,
											 "log_type":log_type}) :
		pass
	else :
		checkInDoc = frappe.new_doc('Employee Checkin') 
		checkInDoc.employee = employee
		checkInDoc.time = time
		checkInDoc.log_type = log_type
		checkInDoc.device_id = device_id
		checkInDoc.save()

def CheckinMahapura():
	date = datetime.date.today()
	previous_date = date - datetime.timedelta(days=1)
	getEmployeeCheck("Pinkcity Jewelhouse Private Ltd-Mahapura", previous_date)

def CheckinUnit1():
	date = datetime.date.today()
	previous_date = date - datetime.timedelta(days=1)
	getEmployeeCheck("Pinkcity Jewelhouse Private Limited- Unit 1", previous_date)

def CheckinUnit2():
	date = datetime.date.today()
	previous_date = date - datetime.timedelta(days=1)
	getEmployeeCheck("Pinkcity Jewelhouse Private Limited-Unit 2", previous_date)

def CheckinColorstone():
	date = datetime.date.today()
	previous_date = date - datetime.timedelta(days=1)
	getEmployeeCheck("PINKCITY COLORSTONES PVT. LTD.", previous_date)



def applyAttendance():
	date = datetime.date.today()
	markAttendance("ColorStones Unit Shift", date)
	markAttendance("Mahapura Unit Shift", date)
	markAttendance("Unit 1 Shift Sitapura", date)
	markAttendance("Unit 2 Shift Sitapura", date)


def markAttendance(shift_name, date):
	shift_doc = frappe.get_cached_doc('Shift Type', shift_name)
	old_last_sync_of_checkin = datetime.datetime.strptime(str(shift_doc.last_sync_of_checkin), "%Y-%m-%d %H:%M:%S")
	shift_doc.last_sync_of_checkin = str(date.today()) + " " + str(old_last_sync_of_checkin.time())

	previous_date = date - datetime.timedelta(days=1)
	previous_date = datetime.datetime.strptime(str(previous_date), "%Y-%m-%d")
	shift_doc.process_attendance_after = str(previous_date.date())
	# shift_doc.save()

	shift_doc.process_auto_attendance()

# def updateEmployeeLeave() :
# 	frappe.enqueue(
# 		updateEmployeeLeavesByCompany(), # python function or a module path as string
# 		# queue="default", # one of short, default, long
# 		queue="default", # one of short, default, long
# 		timeout= (60 * 30), # pass timeout manually -- 30 minute
# 		is_async=True, # if this is True, method is run in worker
# 		now=False, # if this is True, method is run directly (not in a worker) 
# 		job_name=None, # specify a job name
# 		enqueue_after_commit=False, # enqueue the job after the database commit is done at the end of the request
# 		at_front=False, # put the job at the front of the queue
# 		track_job=True, # tracks some metadata in `Background Task` doctype
# 		# **kwargs, # kwargs are passed to the method as arguments
# 	)

# def updateEmployeeLeavesByCompany() :
def updateEmployeeLeave() :
	date = datetime.date.today()
	year = date.year
	# print(year)
	# updateLeave("PINKCITY COLORSTONES PVT. LTD.", year)
	# updateLeave("Pinkcity Jewelhouse Private Ltd-Mahapura", year)
	# updateLeave("Pinkcity Jewelhouse Private Limited- Unit 1", year)
	updateLeave("Pinkcity Jewelhouse Private Limited-Unit 2", year)
	frappe.enqueue(
		updateLeave("PINKCITY COLORSTONES PVT. LTD.", year), # python function or a module path as string
		# queue="default", # one of short, default, long
		queue="default", # one of short, default, long
		timeout= (60 * 15), # pass timeout manually -- 30 minute
		is_async=True, # if this is True, method is run in worker
		now=False, # if this is True, method is run directly (not in a worker) 
		job_name=None, # specify a job name
		enqueue_after_commit=False, # enqueue the job after the database commit is done at the end of the request
		at_front=False, # put the job at the front of the queue
		track_job=True, # tracks some metadata in `Background Task` doctype
		# **kwargs, # kwargs are passed to the method as arguments
	)
	# frappe.enqueue(
	# 	updateLeave("Pinkcity Jewelhouse Private Ltd-Mahapura", year), # python function or a module path as string
	# 	# queue="default", # one of short, default, long
	# 	queue="default", # one of short, default, long
	# 	timeout= (60 * 15), # pass timeout manually -- 30 minute
	# 	is_async=True, # if this is True, method is run in worker
	# 	now=False, # if this is True, method is run directly (not in a worker) 
	# 	job_name=None, # specify a job name
	# 	enqueue_after_commit=False, # enqueue the job after the database commit is done at the end of the request
	# 	at_front=False, # put the job at the front of the queue
	# 	track_job=True, # tracks some metadata in `Background Task` doctype
	# 	# **kwargs, # kwargs are passed to the method as arguments
	# )
	# frappe.enqueue(
	# 	updateLeave("Pinkcity Jewelhouse Private Limited- Unit 1", year), # python function or a module path as string
	# 	# queue="default", # one of short, default, long
	# 	queue="default", # one of short, default, long
	# 	timeout= (60 * 15), # pass timeout manually -- 30 minute
	# 	is_async=True, # if this is True, method is run in worker
	# 	now=False, # if this is True, method is run directly (not in a worker) 
	# 	job_name=None, # specify a job name
	# 	enqueue_after_commit=False, # enqueue the job after the database commit is done at the end of the request
	# 	at_front=False, # put the job at the front of the queue
	# 	track_job=True, # tracks some metadata in `Background Task` doctype
	# 	# **kwargs, # kwargs are passed to the method as arguments
	# )
	# frappe.enqueue(
	# 	updateLeave("Pinkcity Jewelhouse Private Limited-Unit 2", year), # python function or a module path as string
	# 	# queue="default", # one of short, default, long
	# 	queue="default", # one of short, default, long
	# 	timeout= (60 * 15), # pass timeout manually -- 30 minute
	# 	is_async=True, # if this is True, method is run in worker
	# 	now=False, # if this is True, method is run directly (not in a worker) 
	# 	job_name=None, # specify a job name
	# 	enqueue_after_commit=False, # enqueue the job after the database commit is done at the end of the request
	# 	at_front=False, # put the job at the front of the queue
	# 	track_job=True, # tracks some metadata in `Background Task` doctype
	# 	# **kwargs, # kwargs are passed to the method as arguments
	# )
	




def updateLeave(company, year) :
	# For EL-PL
	query = f"""SELECT 
					SUM(CASE
							WHEN status = 'Present' then 1
							WHEN status = 'Half Day' then 0.5
							ELSE 0
						END) total_present, 
					employee, employee_name, company
				FROM tabAttendance 
				WHERE 
					YEAR(attendance_date) = {year} 
					AND company = '{company}'
					AND docstatus = 1
				GROUP BY employee """
	emp_data = frappe.db.sql(query, as_dict=1)
	# AND employee = 'HR-EMP-PJH1-0521'
	print(emp_data)
	# return 0

	for emp in emp_data :
		total_present = float(emp.get("total_present", 0) or 0)
		total_el_pl = total_present / 20
		if total_el_pl >= 15 :
			total_el_pl = 15
		
		print(total_el_pl)


		if frappe.db.exists({
							'doctype': 'Leave Allocation',
							'employee': emp.get("employee"),
							'docstatus': 1,
							'to_date': str(year) + "-12-31",
							'leave_type' : 'EL/PL'
							}) :
			leave_allocation_doc =  frappe.get_last_doc('Leave Allocation', filters={
									'employee': emp.get("employee"),
									'docstatus': 1,
									'to_date': str(year) + "-12-31",
									'leave_type' : 'EL/PL'
								})
			leaves =  float(leave_allocation_doc.get("unused_leaves", 0) or 0)
			total_el_pl = leaves + total_el_pl
			leave_allocation_doc.db_set('total_leaves_allocated', total_el_pl)
			# leave_allocation_doc.save()
			# print(leave_allocation_doc.get("name"))
			# print(emp.get("employee"))
			# print(str(year) + "-12-31")
			# frappe.db.set_value('Leave Allocation', leave_allocation_doc.get("name"), 'total_leaves_allocated', total_el_pl)
			# print(leave_allocation_doc.get("unused_leaves", 0))
			# print(leave_allocation_doc)

			if frappe.db.exists({
								'doctype': 'Leave Ledger Entry',
								'transaction_name': leave_allocation_doc.get("name"),
								'is_carry_forward': 0,
								'leave_type' : 'EL/PL'
								}) :
				leave_ledger_doc = frappe.get_last_doc('Leave Ledger Entry', filters={
										'transaction_name': leave_allocation_doc.get("name"),
										'is_carry_forward': 0,
										'leave_type' : 'EL/PL'
									})
				print(leave_ledger_doc.get("name"))
				leave_ledger_doc.db_set('leaves', total_el_pl)
				# frappe.db.set_value('Leave Ledger Entry', leave_ledger_doc.get("name"), 'leaves', total_el_pl)




	# For CL
	all_employee = frappe.db.get_all('Employee',
									filters={
										# 'status': 'Active',
										'company': company,
										# 'employee': 'HR-EMP-PJH1-0521'
									},
									fields=['employee', 'employee_name', 'attendance_device_id'],
									# order_by='date desc',
								)
	
	# print(all_employee)
	if all_employee :
		for employee in all_employee :
			query = f"""SELECT 
							SUM(CASE
									WHEN status = 'Present' then 1
									WHEN status = 'Half Day' then 0.5
									ELSE 0
								END) total_present, 
								MONTH(attendance_date) attend_month,
							employee, employee_name, company
						FROM tabAttendance 
						WHERE 
							YEAR(attendance_date) = {year} 
							AND company = '{company}'
							AND employee = '{employee.get("employee")}'
							AND docstatus = 1
						GROUP BY employee, attend_month """
			emp_data = frappe.db.sql(query, as_dict=1)

			total_cl = 0
			for emp in emp_data :
				total_present = float(emp.get("total_present", 0) or 0)
				if total_present >= 10 :
					total_cl += 0.59
			# print(total_cl)

			if frappe.db.exists({
								'doctype': 'Leave Allocation',
								'employee': employee.get("employee"),
								'docstatus': 1,
								'to_date': str(year) + "-12-31",
								'leave_type' : 'CL'
								}) :
				leave_allocation_doc =  frappe.get_last_doc('Leave Allocation', filters={
										'employee': employee.get("employee"),
										'docstatus': 1,
										'to_date': str(year) + "-12-31",
										'leave_type' : 'CL'
									})
				leave_allocation_doc.db_set('total_leaves_allocated', total_cl)
				# print(leave_allocation_doc.get("name"))

				if frappe.db.exists({
									'doctype': 'Leave Ledger Entry',
									'transaction_name': leave_allocation_doc.get("name"),
									'is_carry_forward': 0,
									'leave_type' : 'CL'
									}) :
					leave_ledger_doc = frappe.get_last_doc('Leave Ledger Entry', filters={
											'transaction_name': leave_allocation_doc.get("name"),
											'is_carry_forward': 0,
											'leave_type' : 'CL'
										})
					print(leave_ledger_doc.get("name"))
					leave_ledger_doc.db_set('leaves', total_cl)


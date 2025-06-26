# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)


	report_summary = get_report_summary(data)

	total_employee_contribution = sum(row.get("esi_contribution", 0) for row in data)
	total_payment_days = sum(row.get("payment_days", 0) for row in data)
	employer_contribution = sum(row.get("esi_earnings", 0) for row in data)
	total_employer_contribution = employer_contribution * 3.25 / 100
	data.append({
		"employee_name": "<p style='font-weight: bold;'>Employee Contribution</p>",
		"esi_earnings": round(total_employee_contribution, 2)
	})
	data.append({
		"employee_name": "<p style='font-weight: bold;'>Employer Contribution</p>",
		"esi_earnings": round(total_employer_contribution, 2)
	})
	data.append({
		"employee_name": "<p style='font-weight: bold;'>Total Contribution</p>",
		"esi_earnings": round(total_employee_contribution + total_employer_contribution, 2)
	})
	data.append({
		"employee_name": "<p style='font-weight: bold;'>Total </p>",
		"payment_days": round(total_payment_days),
		"esi_earnings": round(employer_contribution),
		"esi_contribution": round(total_employee_contribution)
	})

	return columns, data, None, None, report_summary


def get_columns():
	return [
		{"fieldname":"esic_no", "fieldtype":"Data", "label":"ESI NO.", "width":150},
		{"fieldname":"employee_name", "fieldtype":"Data", "label":"Name of Member", "width":250},
		{"fieldname":"payment_days", "fieldtype":"Data", "label":"Days Worked", "width":150},
		{"fieldname":"esi_earnings", "fieldtype":"Currency", "label":"ESI Earnings", "width":180},
		{"fieldname":"esi_contribution", "fieldtype":"Currency", "label":"ESI Contribution", "width":220},
		
	]

def get_data(filters):
	conditions = get_conditions(filters)

	query = f"""SELECT 
					ss.esic_no,
					ss.employee_name,
					ROUND(ss.payment_days) AS payment_days,
					ROUND(ss.gross_pay - IFNULL((
												SELECT td.amount 
												FROM `tabSalary Detail` td 
												WHERE td.parent = sd.parent AND td.abbr = 'WA'
										), 0)) AS esi_earnings,
					ROUND(sd.amount) AS esi_contribution
				FROM `tabSalary Slip` ss
				LEFT JOIN `tabSalary Detail` sd ON ss.name = sd.parent AND sd.abbr = 'ESI'
				WHERE (
						SELECT amount 
						FROM `tabSalary Detail` tsd 
						WHERE tsd.parent = ss.name AND tsd.abbr = 'ESI'
					) > 0
					AND ss.esic_exit_date IS NULL
					AND ss.esic_no IS NOT NULL
					{conditions}
				"""
	data = frappe.db.sql(query, as_dict=1,)
	# total_employee_contribution = sum(row.get("esi_contribution", 0) for row in data)
	# employer_contribution = sum(row.get("esi_earnings", 0) for row in data)
	# total_employer_contribution = employer_contribution * 3.25 / 100
	# data.append({
	# 	"employee_name": "Employee Contribution",
	# 	"esi_earnings": round(total_employee_contribution, 2)
	# })
	# data.append({
	# 	"employee_name": "Employer Contribution",
	# 	"esi_earnings": round(total_employer_contribution, 2)
	# })
	# data.append({
	# 	"employee_name": "Total Contribution",
	# 	"esi_earnings": round(total_employee_contribution + total_employer_contribution, 2)
	# })
	return data

	# return frappe.db.sql(query, as_dict=1,)

def get_conditions(filters):
	conditions = ""
	
	if filters.get("company"):
		conditions += " AND ss.company = '" + filters.get("company") +"' " 

	if filters.get("month"):
		month = [
			"Jan",
			"Feb",
			"Mar",
			"Apr",
			"May",
			"Jun",
			"Jul",
			"Aug",
			"Sep",
			"Oct",
			"Nov",
			"Dec",
		].index(filters["month"]) + 1
		conditions += f" AND MONTH(ss.start_date) = {month} "
	
	if filters.get("year"):
		conditions += f" AND YEAR(ss.start_date) =  " + filters.get("year") +" " 
	
	if filters.get("employee"):
		conditions += f" AND ss.employee =  '" + filters.get("employee") +"' " 
	

	return conditions


def get_report_summary(data):
	if not data:
		return None

	employee_contribution = 0
	employer_contribution = 0
	total_esi_earnings = 0
	total = 0

	for row in data :
		employee_contribution += float(row.get("esi_contribution", 0) or 0)
		total_esi_earnings += float(row.get("esi_earnings", 0) or 0)
	employer_contribution = round(total_esi_earnings * 3.25 / 100 )
	total = employee_contribution + employer_contribution

	return [
		{
			"value": employee_contribution,
			"indicator": "Blue" if employee_contribution > 50 else "Red",
			"label": _("Employee Contribution"),
			"datatype": "Currency",
		},
		{
			"value": employer_contribution,
			"indicator": "Blue",
			"label": _("Employer Contribution"),
			"datatype": "Currency",
		},
		{
			"value": total,
			"indicator": "Green",
			"label": _("Total"),
			"datatype": "Currency",
		},
	]

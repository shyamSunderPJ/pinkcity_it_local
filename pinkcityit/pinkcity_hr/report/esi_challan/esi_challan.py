# Copyright (c) 2025, pinkcity and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data




def get_data(filters):
	conditions = get_conditions(filters)

	query = f"""
				SELECT 
					tss.esic_no,
					tss.employee_name,
					ROUND(tss.payment_days) AS payment_days,
					ROUND(
						tss.gross_pay - IFNULL(
							(SELECT td.amount 
							FROM `tabSalary Detail` td 
						WHERE td.parent = `tabSalary Detail`.parent 
						AND td.abbr = 'WA'), 
							0)
					) AS esi_earnings,
					(IF(payment_days > 0, 0, 1)) AS workings_day1,
					tss.esic_exit_date AS last_working_day
				FROM `tabSalary Slip` tss
				LEFT JOIN `tabSalary Detail` 
				ON tss.name = `tabSalary Detail`.parent
				AND `tabSalary Detail`.abbr = 'B'
				WHERE tss.esic_exit_date IS NULL
				AND tss.esic_no IS NOT NULL
				AND (SELECT tsd.amount 
					FROM `tabSalary Detail` tsd 
				WHERE tsd.parent = tss.name 
					AND tsd.abbr = 'ESI') > 0
				AND payment_days IS NOT NULL
				{conditions}
				"""


	return frappe.db.sql(query, as_dict=1,)



def get_columns():
	return [
		{"fieldname":"esic_no", "fieldtype":"Data", "label":"IP Number (10 Digits)", "width":250},
		{"fieldname":"employee_name", "fieldtype":"Data", "label":"IP Name (Only alphabets and space)", "width":250},
		{"fieldname":"payment_days", "fieldtype":"Data", "label":"No of Days for which wages paid payable during the month", "width":250},
		{"fieldname":"esi_earnings", "fieldtype":"Data", "label":"Total Monthly Wages", "width":250},
		{"fieldname":"workings_day1", "fieldtype":"Data", "label":"Reason Code for Zero workings days(numeric only;provide 0 for\n all other reasons- Click on the link for referencel)", "width":250},
		{"fieldname":"last_working_day", "fieldtype":"Data", "label":"Last Working DayFormat DD/MM/YYYY or DD-MM-YYYY)", "width":250},

	]



def get_conditions(filters):
	conditions = ""
	
	if filters.get("company"):
		conditions += " AND tss.company = '" + filters.get("company") +"' " 

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
		conditions += f" AND MONTH(tss.start_date) = {month} "
	
	if filters.get("year"):
		conditions += f" AND YEAR(tss.start_date) =  " + filters.get("year") +" " 
	
	if filters.get("employee"):
		conditions += f" AND tss.employee =  '" + filters.get("employee") +"' " 
	

	return conditions

      
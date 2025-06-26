# Copyright (c) 2025, pinkcity and contributors
# For license information, please see license.txt
import json

import frappe
from frappe import _

def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	return [
		{"fieldname":"uan_number", "fieldtype":"Data", "label":"UAN", "width":130},
		{"fieldname":"employee_name", "fieldtype":"Data", "label":"Member Name", "width":150},
		{"fieldname":"gross_pay", "fieldtype":"Int", "label":"Gross Wages", "width":120},
		{"fieldname":"amount1", "fieldtype":"Float", "label":"EPF Wages", "width":120},
		{"fieldname":"amount2", "fieldtype":"Float", "label":"EPS Wages", "width":120},
		{"fieldname":"amount3", "fieldtype":"Float", "label":"EDLI Wages", "width":120},
		{"fieldname":"pf", "fieldtype":"Float", "label":"EPF Contribution remitted", "width":200},
		{"fieldname":"eps", "fieldtype":"Float", "label":"EPS Contribution remitted", "width":200},
		{"fieldname":"epsepf", "fieldtype":"Float", "label":"EPF and EPS Diff remitted", "width":200},
		{"fieldname":"leave_without_pay", "fieldtype":"Float", "label":"NCP Days", "width":120},
		{"fieldname":"eps_scheme_not_applicable", "fieldtype":"Float", "label":"Refund of Advances", "width":150},
		
	]

def get_data(filters):
	conditions = get_conditions(filters)

	query = f"""	SELECT 
						tss.uan_number,
						tss.employee_name,
						ROUND(tss.gross_pay) AS gross_pay,
						IF(tsd.amount < 15000, ROUND(tsd.amount), ROUND(15000)) AS amount1,
						IF(tsd.amount < 15000, ROUND(tsd.amount), ROUND(15000)) AS amount2,
						IF(tsd.amount < 15000, ROUND(tsd.amount), ROUND(15000)) AS amount3,
						IF(tsd.amount < 15000, ROUND((tsd.amount * 12) / 100), ROUND((15000 * 12) / 100)) AS pf,
						IF(tsd.amount < 15000, ROUND((tsd.amount * 8.33) / 100), ROUND((15000 * 8.33) / 100)) AS eps,
						IF(tsd.amount < 15000, 
							(ROUND((tsd.amount * 12) / 100) - ROUND((tsd.amount * 8.33) / 100)),
							(ROUND((15000 * 12) / 100) - ROUND((15000 * 8.33) / 100))
						) AS epsepf,
						ROUND(tss.leave_without_pay) AS leave_without_pay,
						tss.eps_scheme_not_applicable
					FROM `tabSalary Slip` tss
					LEFT JOIN `tabSalary Detail` tsd  ON tss.name = tsd.parent AND tsd.abbr = 'B'
					WHERE tss.eps_scheme_not_applicable = 0
						AND tss.uan_number != ''
						{conditions}
				UNION 
					SELECT 
						tss.uan_number,
						tss.employee_name,
						ROUND(tss.gross_pay) AS gross_pay,
						IF(amount<15000, round(amount),  round(15000)  ) amount1,
						0 amount2,
						IF(amount<15000, round(amount),  round(15000)  ) amount3,
                        IF(amount<15000, round(((amount*12)/100)),  round(((15000*12)/100))  ) pf,
                        0 eps,
						IF(amount<15000, round(((amount*12)/100)),  round(((15000*12)/100))  ) epsepf,
						round(leave_without_pay) leave_without_pay,
						tss.eps_scheme_not_applicable
					FROM `tabSalary Slip` tss
					LEFT JOIN `tabSalary Detail` tsd  ON tss.name = tsd.parent AND tsd.abbr = 'B'
					WHERE tss.eps_scheme_not_applicable = 1
						AND tss.uan_number != ''
						{conditions}
			"""


	return frappe.db.sql(query, as_dict=1)


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

@frappe.whitelist()
def get_txt(filters, report_name, data):
	filters = json.loads(filters)
	report_data = json.loads(data)
	company = ""
	if filters.get("company"):
		company = filters.get("company") 
	data = ""
	for row in report_data :
		data += str(row.get("uan_number")) + "#~#" 
		data += row.get("employee_name") + "#~#" 
		data += str(row.get("gross_pay")) + "#~#" 
		data += str(row.get("amount1")) + "#~#" 
		data += str(row.get("amount2")) + "#~#" 
		data += str(row.get("amount3")) + "#~#" 
		data += str(row.get("pf")) + "#~#" 
		data += str(row.get("eps")) + "#~#" 
		data += str(row.get("epsepf")) + "#~#" 
		data += str(row.get("leave_without_pay")) + "#~#" 
		data += str(row.get("eps_scheme_not_applicable")) + "#~#" 
		data += str(row.get("leave_without_pay")) + "\n" 
	return {
        "report_name": report_name,
        "company": company,  
        "data": data
    }


@frappe.whitelist()
def download_txt_file():
    data = frappe._dict(frappe.local.form_dict)
    frappe.response["filename"] = (
        frappe.scrub(f"{data['report_name']} {data['company']}") + ".txt"
    )
    frappe.response["filecontent"] = data["data"]
    frappe.response["content_type"] = "application/txt"
    frappe.response["type"] = "download"

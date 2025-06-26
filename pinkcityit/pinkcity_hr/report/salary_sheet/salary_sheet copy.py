# Copyright (c) 2025, Pink city IT team and contributors
# For license information, please see license.txt


import frappe
from frappe import _

from frappe.utils import flt

def get_group_header_row():
    return {
        "occupation": "",
        "gross_pay": "",
        "employee": "",
        "basic": "<b>Earnings</b>",
        "city_compensatory_allowance": "",
        "washing_allowance": "",
        "house_rent_allowance": "",
        "overtime": "",
        "arrear": "",
        "incentive_pay": "",
        "leave_encashment": "",
        "travelling_allowance": "",
        "abry_scheme": "",
        "earned_gross": "",
        "net_gross": "",
        "employee_contribution_pf": "<b>Deductions</b>",
        "employee_contribution_esi": "",
        "late_hours_deduction": "",
        "advance_deduction": "",
        "tax_deducted_at_source": "",
        "professional_tax": "",
        "income_tax": "",
        "gmi": "",
        "total": ""
    }

def get_spacer_row():
    # Optional: visually separate the header row
    return {k: "" for k in [col["fieldname"] for col in get_columns()]}


# def get_columns():
#     row_1 = [
#         {"fieldname": "occupation", "fieldtype": "Data", "label": "Occupation", "width": 120},
#         {"fieldname": "gross_pay", "fieldtype": "Data", "label": "Gross Pay", "width": 120},
#         {"fieldname": "employee", "fieldtype": "Data", "label": "Employee", "options": "Employee", "width": 120},
#     ]
#     row_2 = [
#         {"fieldname": "occupation", "fieldtype": "Data", "label": "Occupation", "width": 120},
#         {"fieldname": "gross_pay", "fieldtype": "Data", "label": "Gross Pay", "width": 120},
#         {"fieldname": "employee", "fieldtype": "Data", "label": "Employee", "options": "Employee", "width": 120},
#         {"fieldname": "basic", "fieldtype": "Data", "label": "Basic", "width": 120, "group": "Earnings"},
#         {"fieldname": "city_compensatory_allowance", "fieldtype": "Data", "label": "City Compensatory Allowance", "width": 150, "group": "Earnings"},
#         {"fieldname": "washing_allowance", "fieldtype": "Data", "label": "Washing Allowance", "width": 120, "group": "Earnings"},
#         {"fieldname": "house_rent_allowance", "fieldtype": "Data", "label": "House Rent Allowance", "width": 150, "group": "Earnings"},
#         {"fieldname": "overtime", "fieldtype": "Data", "label": "Overtime", "width": 120, "group": "Earnings"},
#         {"fieldname": "arrear", "fieldtype": "Data", "label": "Arrear", "width": 120, "group": "Earnings"},
#         {"fieldname": "incentive_pay", "fieldtype": "Data", "label": "Incentive Pay", "width": 120, "group": "Earnings"},
#         {"fieldname": "leave_encashment", "fieldtype": "Data", "label": "Leave Encashment", "width": 140, "group": "Earnings"},
#         {"fieldname": "travelling_allowance", "fieldtype": "Data", "label": "Travelling Allowance", "width": 140, "group": "Earnings"},
#         {"fieldname": "abry_scheme", "fieldtype": "Data", "label": "Abry Scheme", "width": 120, "group": "Earnings"},
#         {"fieldname": "earned_gross", "fieldtype": "Data", "label": "Earned Gross", "width": 120, "group": "Earnings"},
#         {"fieldname": "net_gross", "fieldtype": "Data", "label": "Net Gross", "width": 120, "group": "Earnings"},
#         {"fieldname": "employee_contribution_pf", "fieldtype": "Data", "label": "Employee Contribution Pf", "width": 160, "group": "Deductions"},
#         {"fieldname": "employee_contribution_esi", "fieldtype": "Data", "label": "Employee Contribution Esi", "width": 160, "group": "Deductions"},
#         {"fieldname": "late_hours_deduction", "fieldtype": "Data", "label": "Late Hours Deduction", "width": 140, "group": "Deductions"},
#         {"fieldname": "advance_deduction", "fieldtype": "Data", "label": "Advance Deduction", "width": 140, "group": "Deductions"},
#         {"fieldname": "tax_deducted_at_source", "fieldtype": "Data", "label": "Tax Deducted At Source", "width": 160, "group": "Deductions"},
#         {"fieldname": "professional_tax", "fieldtype": "Data", "label": "Professional Tax", "width": 140, "group": "Deductions"},
#         {"fieldname": "income_tax", "fieldtype": "Data", "label": "Income Tax", "width": 120, "group": "Deductions"},
#         {"fieldname": "gmi", "fieldtype": "Data", "label": "Gmi", "width": 100, "group": "Deductions"},
#         {"fieldname": "total", "fieldtype": "Data", "label": "Total", "width": 120, "group": "Deductions"}
#     ]
#     return [row_1, row_2]
 
def get_columns():
   
    return [
        {"fieldname": "basic", "fieldtype": "Data", "label": "Basic", "width": 120, "group": "Earnings"},
        {"fieldname": "city_compensatory_allowance", "fieldtype": "Data", "label": "City Compensatory Allowance", "width": 150, "group": "Earnings"},
        {"fieldname": "washing_allowance", "fieldtype": "Data", "label": "Washing Allowance", "width": 120, "group": "Earnings"},
        {"fieldname": "house_rent_allowance", "fieldtype": "Data", "label": "House Rent Allowance", "width": 150, "group": "Earnings"},
        {"fieldname": "overtime", "fieldtype": "Data", "label": "Overtime", "width": 120, "group": "Earnings"},
        {"fieldname": "arrear", "fieldtype": "Data", "label": "Arrear", "width": 120, "group": "Earnings"},
        {"fieldname": "incentive_pay", "fieldtype": "Data", "label": "Incentive Pay", "width": 120, "group": "Earnings"},
        {"fieldname": "leave_encashment", "fieldtype": "Data", "label": "Leave Encashment", "width": 140, "group": "Earnings"},
        {"fieldname": "travelling_allowance", "fieldtype": "Data", "label": "Travelling Allowance", "width": 140, "group": "Earnings"},
        {"fieldname": "abry_scheme", "fieldtype": "Data", "label": "Abry Scheme", "width": 120, "group": "Earnings"},
        {"fieldname": "earned_gross", "fieldtype": "Data", "label": "Earned Gross", "width": 120, "group": "Earnings"},
        {"fieldname": "net_gross", "fieldtype": "Data", "label": "Net Gross", "width": 120, "group": "Earnings"},
        {"fieldname": "employee_contribution_pf", "fieldtype": "Data", "label": "Employee Contribution Pf", "width": 160, "group": "Deductions"},
        {"fieldname": "employee_contribution_esi", "fieldtype": "Data", "label": "Employee Contribution Esi", "width": 160, "group": "Deductions"},
        {"fieldname": "late_hours_deduction", "fieldtype": "Data", "label": "Late Hours Deduction", "width": 140, "group": "Deductions"},
        {"fieldname": "advance_deduction", "fieldtype": "Data", "label": "Advance Deduction", "width": 140, "group": "Deductions"},
        {"fieldname": "tax_deducted_at_source", "fieldtype": "Data", "label": "Tax Deducted At Source", "width": 160, "group": "Deductions"},
        {"fieldname": "professional_tax", "fieldtype": "Data", "label": "Professional Tax", "width": 140, "group": "Deductions"},
        {"fieldname": "income_tax", "fieldtype": "Data", "label": "Income Tax", "width": 120, "group": "Deductions"},
        {"fieldname": "gmi", "fieldtype": "Data", "label": "Gmi", "width": 100, "group": "Deductions"},
        {"fieldname": "total", "fieldtype": "Data", "label": "Total", "width": 120, "group": "Deductions"}
    ]


def get_data(filters):
    conditions = get_conditions(filters)

    query = f"""SELECT
                    CASE 
                        WHEN occupation = 'staff' THEN 'Staff'
                        WHEN occupation = 'worker' THEN 'Worker'
                        ELSE 'Other'
                    END AS occupation_type,
                    SUM(gross_pay) AS total_salary
                FROM
                    `tabSalary Slip` tss
                GROUP BY
                    occupation;
                """
    return frappe.db.sql(query, as_dict=1,)



def get_conditions(filters):
    conditions = ""

    if filters.get("occupation"):
        conditions += f" AND tss.occupation = '"+filters.get("occupation")+"'" 

    return conditions

from frappe.utils import flt

def execute(filters):
    # headings = get_heading()
    columns = get_columns()
    data = get_dynamic_data(filters)
   
    hdfc_total = sum(flt(d.get("net_gross", 0)) for d in data if d.get("bank_name") == "HDFC")
    other_total = sum(flt(d.get("net_gross", 0)) for d in data if d.get("bank_name") != "HDFC")
    grand_total = hdfc_total + other_total
    
    data.append({
		"basic": "<p style='font-weight: bold;'>HDFC BANK</p>",
		"washing_allowance": round(hdfc_total, 2)
	})
    data.append({
        "basic": "<p style='font-weight: bold;'>OTHER BANK</p>",
        "washing_allowance": round(other_total, 2)
    })
    data.append({
        "basic": "<p style='font-weight: bold;'>GRAND TOTAL</p>",
        "washing_allowance": round(grand_total, 2)
    })
    return columns, data

# def execute(filters):
#     columns = get_columns()
#     data = get_dynamic_data(filters)

#     # Render the headers
#     header_html = render_heading_row()

#     # Insert the custom header row (optional)
#     data.insert(0, get_custom_header_row())  # Insert at the beginning if necessary

#     # Do any calculations or processing for your data...

#     return columns, data, header_html  # You can return the header HTML with the data


def get_dynamic_data(filters):
    data = [
        {
            
        }
    ]

    return data



def get_custom_header_row():
    # Create the first row with the general column names
    row_1 = [
        "",  # Empty cell for "Occupation"
        "",  # Empty cell for "Gross Pay"
        "",  # Empty cell for "Employee"
        "<b style='text-align:center;'>Earnings</b>",  # Title for Earnings
        "",  # Empty space
        "",  # Empty space
        "<b style='text-align:center;'>Deductions</b>",  # Title for Deductions
        "",  # Empty space
        "",  # Empty space
    ]

    # Create the second row where each column header belongs under the Earnings/Deductions sections
    row_2 = [
        "", "", "",  # Empty spaces for Occupation, Gross Pay, Employee
        "Basic", "City Comp Allowance", "Washing Allowance", "House Rent Allowance", "Overtime", 
        "Arrear", "Incentive Pay", "Leave Encashment", "Travelling Allowance", "Abry Scheme", 
        "Earned Gross", "Net Gross",  # Earnings section
        "Employee Contribution Pf", "Employee Contribution Esi", "Late Hours Deduction", 
        "Advance Deduction", "Tax Deducted At Source", "Professional Tax", "Income Tax", 
        "Gmi", "Total"  # Deductions section
    ]

    return [row_1, row_2]


def get_header_html():
    return """
    <div style="font-size:16px; font-weight:bold; text-align:center; margin-bottom:10px;">
        Salary Report Breakdown
    </div>
    <div style="display: flex; justify-content: space-between; font-weight: bold;">
        <div style="width: 45%; text-align:center; padding: 10px;">Earnings</div>
        <div style="width: 45%; text-align:center; padding: 10px;">Deductions</div>
    </div>
    <div style="font-weight: bold; text-align:center;">
        <div style="display: inline-block; width: 20%;">Basic</div>
        <div style="display: inline-block; width: 20%;">HRA</div>
        <div style="display: inline-block; width: 20%;">Incentive</div>
        <div style="display: inline-block; width: 20%;">PF</div>
        <div style="display: inline-block; width: 20%;">ESI</div>
        <div style="display: inline-block; width: 20%;">Tax</div>
        <div style="display: inline-block; width: 20%;">Total</div>
    </div>
    """

def render_heading_row():
    # Get columns and header rows
    columns = get_columns()
    custom_row = get_custom_header_row()

    html = "<table style='width:100%; font-weight:bold; font-size:14px; margin-bottom:5px;'>"

    # Render the custom header row (first row)
    html += "<tr>"
    for col in custom_row[0]:  # First custom row with 'Earnings' and 'Deductions'
        html += f"<td style='text-align:center; padding:5px;'>{col}</td>"
    html += "</tr>"

    # Render the second custom row (detailed headers)
    html += "<tr>"
    for col in custom_row[1]:  # Second row with detailed headers for Earnings and Deductions
        html += f"<td style='text-align:center; padding:5px;'>{col}</td>"
    html += "</tr>"

    html += "</table>"
    return html

// Copyright (c) 2025, pinkcity and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["ESI Challan"] = {
	"filters": [
		{
			"fieldname": "company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"reqd": 1,
			"default": frappe.defaults.get_user_default("Company")
		},
		{
			"fieldname": "month",
			"label": __("Month"),
			"fieldtype": "Select",
			"options": ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			"reqd": 1
		},

		{
			"fieldname": "year",
			"label": __("Year"),
			"options": ["", 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028,],
			"fieldtype": "Select",
			"reqd": 1
		},

		{
			"fieldname": "employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
		},
	]
};

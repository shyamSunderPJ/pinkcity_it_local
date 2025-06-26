// Copyright (c) 2025, pinkcity and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Tree Investment"] = {
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
			"fieldname": "date_from",
			"label": __("Tree Date From"),
			"fieldtype": "Date",
			"reqd": 1,
		},
		{
			"fieldname": "date_to",
			"label": __("Tree Date To"),
			"fieldtype": "Date",
			"reqd": 1,
		},
		{
			"fieldname": "design_code",
			"label": __("Design Code"),
			"fieldtype": "Data",
		},
		{
			"fieldname": "order_no",
			"label": __("Order No"),
			"fieldtype": "Data",
		},
		{
			"fieldname": "bag_no",
			"label": __("Bag No"),
			"fieldtype": "Data",
		},
	]
};

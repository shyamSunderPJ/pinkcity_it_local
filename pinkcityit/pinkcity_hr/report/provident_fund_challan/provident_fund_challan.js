// Copyright (c) 2025, pinkcity and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Provident Fund Challan"] = {
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



	],
	onload: function (report) {

		report.page.add_inner_button(__("Download as Txt"), function () {
			let filters = report.get_values();

			frappe.call({
				method: 'pinkcityit.pinkcity_hr.report.provident_fund_challan.provident_fund_challan.get_txt',
				args: {
					data: JSON.stringify(report.data),
					report_name: report.report_name,
					filters: JSON.stringify(filters)
				},
				callback: function (r) {
					if (r.message) {
						const args = {
							cmd: 'pinkcityit.pinkcity_hr.report.provident_fund_challan.provident_fund_challan.download_txt_file',
							data: r.message.data,
							report_name: r.message.report_name,
							company: r.message.company
						};
						open_url_post(frappe.request.url, args);
					}
				}
			});
		});
	}


};



		// {
		// 	"fieldname": "month",
		// 	"label": __("Month"),
		// 	"fieldtype": "Select",
		// 	"options": "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec",
		// 	"default": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
		// 		"Dec"][frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth()],
		// },
		// {
		// 	"fieldname": "year",
		// 	"label": __("Year"),
		// 	"options": "2020\n2021\n2022\n2023\n2024\n2025\n2026\n2027\n2028\n2029\n2030",
		// 	"fieldtype": "Select",
		// 	"reqd": 1
		// },
		// {
		// 	"fieldname": "employee_name",
		// 	"label": __("Employee"),
		// 	"fieldtype": "Link",
		// 	"options": "Employee",
		// },
		// {
		// 	"fieldname": "company",
		// 	"label": __("Company"),
		// 	"fieldtype": "Link",
		// 	"options": "Company",
		// 	"default": frappe.defaults.get_user_default("Company")
		// },

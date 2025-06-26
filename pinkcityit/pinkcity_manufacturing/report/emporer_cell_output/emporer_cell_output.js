// Copyright (c) 2025, pinkcity and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Emporer Cell Output"] = {
	"filters": [
		{
			fieldname: "company",
			label: __("Company"),
			fieldtype: "Select",
			options: "PC\nPJ\nPJ2",
			default: 'PJ2',
			reqd: 1,
		},
		{
			fieldname: "from_location",
			label: __("From Location"),
			fieldtype: "Data",
		},
		{
			fieldname: "voucher_date_from",
			label: __("Voucher Date - From"),
			fieldtype: "Date",
			reqd: 1,
		},
		{
			fieldname: "voucher_date_to",
			label: __("Voucher Date - From"),
			fieldtype: "Date",
			reqd: 1,
		},
	]
};

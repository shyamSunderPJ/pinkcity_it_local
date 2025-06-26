// Copyright (c) 2025, pinkcity and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bag Details', {
	// refresh: function(frm) {

	// }

	bag_quantity: function (frm) {
		calculate_total_qty(frm)
		if (frm.doc.bag_quantity > frm.doc.total_order_quantity) {
			frm.set_value('bag_quantity', 0);
			frappe.throw("In Bag Quantity should be less than Total Quantity");
		}
		else if (frm.doc.total_order_quantity > frm.doc.bag_quantity) {
			frm.set_value('bag_quantity', frm.doc.bag_quantity);
		}
	},
	total_order_quantity: function (frm) {
		calculate_total_qty(frm)
	}
});


function calculate_total_qty(frm) {
	var bag_quantity = frm.doc.bag_quantity;
	var total_order_quantity = frm.doc.total_order_quantity;

	if (frm.doc.work_order) {
		if (bag_quantity > total_order_quantity) {
			frm.set_value('bag_quantity', 0);
			frappe.throw("In Bag Quantity should be less than Total Quantity");
		}


	}
}
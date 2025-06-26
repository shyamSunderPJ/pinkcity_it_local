// Copyright (c) 2025, pinkcity and contributors
// For license information, please see license.txt

frappe.ui.form.on('Stone Manufacturing Process', {
	refresh: function (frm) {
		frm.set_query('uom', 'mfg_process', (frm, cdt, cdn) => {
			return {
				filters: {
					name: ['in', ['Pcs', 'Cts']]
				}
			}

		});
		frm.set_query('worker_name', 'mfg_process', (frm, cdt, cdn) => {
			return {
				filters: {
					occupation: 'Worker',
					status: 'Active'
				}
			};
		})
	},
	

});

frappe.ui.form.on('SMP MFG Process', {
	receive_wt: function (frm, cdt, cdn) {
		update_data(frm, cdt, cdn);
	},
	receive_qty: function (frm, cdt, cdn) {
		update_data(frm, cdt, cdn);
	},

	low_wt: function (frm, cdt, cdn) {
		update_data(frm, cdt, cdn);
	},
	loss_qty: function (frm, cdt, cdn) {
		update_data(frm, cdt, cdn);
	},

	broken_wt: function (frm, cdt, cdn) {
		update_data(frm, cdt, cdn);
	},
	broken_qty: function (frm, cdt, cdn) {
		update_data(frm, cdt, cdn);
	},

	mfg_process_add: function (frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		var weight = parseFloat(frm.doc.weight) || '';
		var pieces = parseFloat(frm.doc.pieces) || '';

		console.log(child)
		if (child.idx == 1) {
			frappe.model.set_value(cdt, cdn, 'operations', "Inventory");
			frappe.model.set_value(cdt, cdn, 'receive_wt', weight);
			frappe.model.set_value(cdt, cdn, 'receive_qty', pieces);
			frappe.model.set_value(cdt, cdn, 'uom', 'Cts');
		}

		if (child.idx >= 2) {
			console.log("hi22")
			for (let i = 0; i < frm.doc.mfg_process.length; i++) {
				console.log("hi33")
				if (i == (child.idx - 1)) {
					console.log("hi44")
					frappe.model.set_value(cdt, cdn, 'uom', frm.doc.mfg_process[i - 1].uom);
					frappe.model.set_value(cdt, cdn, 'receive_wt', frm.doc.mfg_process[i - 1].balance_in_wt);
					frappe.model.set_value(cdt, cdn, 'receive_qty', frm.doc.mfg_process[i - 1].balance_in_qty);
				}
			}
		}

	},
	mfg_process_remove: function (frm, cdt, cdn) {
        update_total_qty(frm);
    },




});
function update_data(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	var low_wt = parseFloat(child.low_wt) || '';
	var broken_wt = parseFloat(child.broken_wt) || '';
	var loss_qty = parseFloat(child.loss_qty) || '';
	var broken_qty = parseFloat(child.broken_qty) || '';
	var receive_qty = parseFloat(child.receive_qty) || '';
	var receive_wt = parseFloat(child.receive_wt) || '';


	console.log("Setting values for child:", child);
	console.log("low_wt:", checkDigit(low_wt));
	console.log("broken_wt:", checkDigit(broken_wt));
	console.log("loss_qty:", checkDigit(loss_qty));
	console.log("broken_qty:", checkDigit(broken_qty));

	// Then set the values
	frappe.model.set_value(cdt, cdn, 'balance_in_wt', (parseFloat(checkDigit(receive_wt)) - (parseFloat(checkDigit(low_wt)) + parseFloat(checkDigit(broken_wt)))));
	frappe.model.set_value(cdt, cdn, 'balance_in_qty', (parseFloat(checkDigit(receive_qty)) - (parseFloat(checkDigit(loss_qty)) + parseFloat(checkDigit(broken_qty)))));
	update_total_qty(frm);
}



function update_total_qty(frm) {
	var total_loss_wt = 0;
	var total_loss_qty = 0;
	var total_broken_wt = 0;
	var total_broken_qty = 0;
	var fg_goods_wt = 0;
	var fg_goods_qty = 0;
	var total_receive_wt = 0;
	var total_receive_qty = 0;
	if (frm.doc.mfg_process) {
		frm.doc.mfg_process.forEach(child => {

			// for (let i = 0; i < child.length; i++) {
			// 	if (i == 0) {
			// 	}
				total_receive_wt = parseFloat(checkDigit(child.receive_wt));
				total_receive_qty = parseFloat(checkDigit(child.receive_qty));
				total_loss_wt += parseFloat(checkDigit(child.low_wt));
				total_loss_qty += parseFloat(checkDigit(child.loss_qty));
				total_broken_wt += parseFloat(checkDigit(child.broken_wt));
				total_broken_qty += parseFloat(checkDigit(child.broken_qty));
				fg_goods_wt = parseFloat(checkDigit(child.balance_in_wt));
				fg_goods_qty = parseFloat(checkDigit(child.balance_in_qty));
			// }
		});
	}

	frm.set_value('total_receive_wt', parseFloat(checkDigit(total_receive_wt)));
	frm.set_value('total_receive_qty', parseFloat(checkDigit(total_receive_qty)));
	frm.set_value('total_loss_wt', parseFloat(checkDigit(total_loss_wt)));
	frm.set_value('total_loss_qty', parseFloat(checkDigit(total_loss_qty)));
	frm.set_value('total_broken_wt', parseFloat(checkDigit(total_broken_wt)));
	frm.set_value('total_broken_qty', parseFloat(checkDigit(total_broken_qty)));
	frm.set_value('fg_goods_wt', parseFloat(checkDigit(fg_goods_wt)));
	frm.set_value('fg_goods_qty', parseFloat(checkDigit(fg_goods_qty)));
	
	var rough_yields = 0;
	rough_yields = (fg_goods_qty / total_receive_qty) * 100
	frm.set_value('rough_yields', parseFloat(checkDigit(rough_yields)));

	// frm.refresh_field("mfg_process");
}


function checkDigit(value) {
	if (value > 0 || value < 0) {
		return value;
	} else {
		return 0;
	}
}
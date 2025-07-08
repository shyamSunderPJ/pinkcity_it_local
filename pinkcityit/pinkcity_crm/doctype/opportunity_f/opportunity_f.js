frappe.ui.form.on('Opportunity F', {
	refresh(frm) {
		frm.set_query('assigned_to', 'development_details', (frm, cdt, cdn) => {
			var child = locals[cdt][cdn];
			if (child.req_quotation == "CUST2D-Costing-3D" ||
				child.req_quotation == "CUST3D-Costing-PD") {
				return { filters: { designer_type: '2D Designer' } }
			}
			else if (
				child.req_quotation == "PC-2D-3D-Costing" ||
				child.req_quotation == "CUST-2D-3D-Costing" ||
				child.req_quotation == "CUST-2D-Costing-3D") {
				return { filters: { designer_type: '2D Designer' } }
			}
			else if (
				child.req_quotation == "CUS-3D-NPD-Costing" ||
				child.req_quotation == "CUS-3D-Costing-NPD" ||
				child.req_quotation == "CUST2D-3D-Costing") {
				return { filters: { designer_type: '3D Designer' } }
			}
		});
		frm.set_query('source', () => {
			return {
				filters: {
					name: ['in', ['Existing Customer', 'Email', 'Website']]
				}
			}
		})
		fetch_npd_costing_status(frm);

	},

	onload: function (frm) {
	},

	onload_post_render(frm) {
		fetch_npd_costing_status(frm);
	},

});

// First table ---------------------------------------------
frappe.ui.form.on('Opp NPD CT F', {
	// Process Section -------------------------
	req_quotation: function (frm, cdt, cdn) {
		update_costing_opp(frm, cdt, cdn);
	},

	attachment_detail: function (frm, cdt, cdn) {
		update_costing_opp(frm, cdt, cdn);
	},

	attachment: function (frm, cdt, cdn) {
		update_costing_opp(frm, cdt, cdn);
	},

	assigned_to: function (frm, cdt, cdn) {
		update_costing_opp(frm, cdt, cdn)
	},

	// NPD Section -------------------------
	create_pd: function (frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		if (frm.is_new()) {
			frappe.msgprint("Please Save the form first");

		} else {
			createNPDOpp(frm, cdt, cdn);
		}
		// fetch_npd_status(frm, cdt, cdn)
	},

	// Costing Section -------------------------
	create_cost: function (frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		if (frm.is_new()) {
			frappe.msgprint("Please Save the form first");
		} else {
			createCostingOpp(frm, cdt, cdn);
		}
	},

	cost_client_status: function (frm, cdt, cdn) {
		// update_costing_id_in_npd(frm, cdt, cdn);
		var child = locals[cdt][cdn];
		if (child.cost_client_status == "Accepted") {
			frappe.model.set_value(cdt, cdn, 'npd_costing_id', child.costing);
		}
	},
	npd_client_status: function (frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		if (child.npd_client_status == "Accepted") {
			frappe.model.set_value(cdt, cdn, 'costing_npd_id', child.product_development);
		}
	}
});

function createNPDOpp(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	frappe.dom.freeze();
	frappe.call({
		method: "pinkcityit.pinkcity_crm.doctype.product_development.product_development.create_product_development_from_opp",
		type: "POST",
		args: {
			'customer_name': frm.doc.party_name,
			'opportunity_owner': frm.doc.custom_opportunity_owner,
			'product_specification': frm.doc.custom_product_specification,
			'opportunity_no': frm.doc.name,
			'designer': child.npd_assigned,
			'attachment': child.npd_attachment,
			'assigner_name': frm.doc.owner,
			'product_development': child.product_development,
			'costing': child.costing,
			'primary_assigner': child.primary_assigner
		},
		error: function (obj) {
			console.log("hi227");
			console.log(obj);
		},
		always: function (obj) {
			frappe.dom.unfreeze();
			if (obj.data) {
				if (obj.data.status) {
					console.log("#125")
					frappe.model.set_value(cdt, cdn, 'product_development', obj.data.data.name);
					fetch_npd_status(frm, cdt, cdn)
					frm.save();
				}
				else {
					frappe.msgprint(obj.data.msg);
				}
			} else {
				console.log("#126")
				frappe.msgprint("Something went wrong");
			}
		}
	});
}

function createCostingOpp(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	frappe.dom.freeze();
	frappe.call({
		method: "pinkcityit.pinkcity_crm.doctype.costing.costing.send_opportunity_details",
		type: "POST",
		args: {
			'costing': child.costing,
			'customer': frm.doc.party_name,
			'opportunity__id': frm.doc.name,
			'assigned_to': child.assigned_to,
			'attachment': child.attachment,
			'product_development': child.npd
		},
		error: function (obj) {
			console.log("hi22");
			console.log(obj);
		},
		always: function (obj) {
			frappe.dom.unfreeze();
			if (obj.data) {
				if (obj.data.status) {
					frappe.model.set_value(cdt, cdn, 'costing', obj.data.data.name);
					fetch_costing_status(frm, cdt, cdn);
					frm.save();
				}
				else {
					frappe.msgprint(obj.data.msg);
				}
			} else {
				frappe.msgprint("Something went wrong");
			}
		}
	});

}

function fetch_npd_costing_status(frm) {
	if (frm.doc.development_details) {
		for (var i = 0; i < frm.doc.development_details.length; i++) {
			console.log("hi81#")
			fetch_costing_status(frm, frm.doc.development_details[i].doctype, frm.doc.development_details[i].name);
			fetch_npd_status(frm, frm.doc.development_details[i].doctype, frm.doc.development_details[i].name);
		}
	}
}

function fetch_npd_status(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	if (child.npd) {
		frappe.db.get_list("Product Development", {
			fields: ["*"],
			filters: { name: child.npd },
		}).then((obj) => {
			for (var i = 0; i < obj.length; i++) {
				frappe.model.set_value(cdt, cdn, 'npd_sheet_status', obj[i].workflow_state);
			}
		});
	}
}


function fetch_costing_status(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	if (child.costing) {
		frappe.db.get_list("Costing", {
			fields: ["*"],
			filters: { name: child.costing },
		}).then((obj) => {
			for (var i = 0; i < obj.length; i++) {
				frappe.model.set_value(cdt, cdn, 'cost_status', obj[i].workflow_state);
			}
		});
	}
}

function checkString(value) {
	if (value) { return value; }
	else { return ''; }
}

function update_costing_opp(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	frappe.model.set_value(cdt, cdn, 'npd_description', child.attachment_detail);
	frappe.model.set_value(cdt, cdn, 'cost_description', child.attachment_detail);
	frappe.model.set_value(cdt, cdn, 'npd_attachment', child.attachment);
	frappe.model.set_value(cdt, cdn, 'cost_attachment', child.attachment);
	frappe.model.set_value(cdt, cdn, 'npd_assigned', child.assigned_to);
	frappe.model.set_value(cdt, cdn, 'cost_assigned', child.assigned_to);
}

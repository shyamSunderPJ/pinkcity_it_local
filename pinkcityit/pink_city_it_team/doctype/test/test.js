// Copyright (c) 2025, pinkcity and contributors
// For license information, please see license.txt

frappe.ui.form.on('Test', {
	refresh: function(frm) {

		// if(frm.doc.first_name){
		// 	frm.set_value('full_name', complete_name(frm.doc.first_name) + " "  + complete_name(frm.doc.middle_name) + " "  + complete_name(frm.doc.last_name) )
		// }
 
		var birth = new Date(frm.doc.dob);
 	 	var now = new Date();
 		var age_now = now.getFullYear() - birth.getFullYear();
		frm.set_value('age', age_now)

	},

	first_name : function(frm){
		frm.set_value('full_name', complete_name(frm.doc.first_name) + " "  + complete_name(frm.doc.middle_name) + " "  + complete_name(frm.doc.last_name) )
	},
	
	middle_name : function(frm){
		frm.set_value('full_name', complete_name(frm.doc.first_name) + " "  + complete_name(frm.doc.middle_name) + " "  + complete_name(frm.doc.last_name) )
	},
	
	last_name : function(frm){
		frm.set_value('full_name', complete_name(frm.doc.first_name) + " "  + complete_name(frm.doc.middle_name) + " "  + complete_name(frm.doc.last_name) )
	},

	// send_details: function(frm){	
	// 	// send_data(frm)
	// 	send_child_data(frm,cdt,cdn)
	// 	frappe.msgprint("Details have been send")
	// },


});


	function complete_name(value){
		if(value) { return value}
		else { return ''}
	}



function send_data(frm){
	if(frm.doc.full_name && frm.doc.age != "null"){
		frm.call({
			method:'pinkcityit.pink_city_it_team.doctype.api_test.api_test.send_data_to_python',
			args:{
				age: frm.doc.age,
				full_name : frm.doc.full_name,
				Birth : frm.doc.dob,
			},
			callback: function(r) {
				if (r.message) {
					frappe.msgprint(r.message);
				}
			}
		});
	}
	
}


function send_child_data(frm,cdt,cdn){
	var child = locals[cdt][cdn]; 
		frappe.call({
			method:'pinkcityit.pink_city_it_team.doctype.api_test.api_test.send_data_to_python',
			args:{
				more_details : frm.doc.more_details,
				phone_no : child.phone_no,
				city : child.city,
				age: frm.doc.age,
				full_name : frm.doc.full_name,
				Birth : frm.doc.dob,
				
			},
			callback: function(r) {
				if (r.message) {
					frappe.msgprint(r.message);
				}
			}
		});
	}
	
	frappe.ui.form.on('Test CT', {
		send_more_details: function(frm,cdt,cdn){
			send_child_data(frm,cdt,cdn)
			frappe.msgprint("Your Details had been send")
		},
		age : function(frm,cdt,cdn){
			var locals = [cdt][cdn]
			frappe.model.set_value ('age',age)
		}
	})
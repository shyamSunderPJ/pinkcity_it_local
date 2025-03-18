frappe.ui.form.on('NPD', {
    refresh:function(frm){
        frm.set_query('metal_type', () => {
          return {
              filters: {
                  name: ['in', [
                      'Silver 925',
											'Silver 999',
											'Re Cycle Silver 925',
											'Re Cycle Silver 999',
											'Bronze',
                      'Brass',
											'Zinc',
											'G24kt',
											'09 Kt Yellow Gold',
											'09 Kt Rose Gold',
											'09 Kt White Gold',
                      '10 Kt Yellow Gold',
											'10 Kt Rose Gold',
											'10 Kt White Gold',
											'14 Kt Yellow Gold',
                      '14 Kt Rose Gold',
											'14 Kt White Gold',
											'18 Kt Yellow Gold',
											'18 Kt Rose Gold',
                      '18 Kt White Gold',
											'22 Kt Yellow Gold',
											'22 Kt Rose Gold',
											'22 Kt White Gold',
											'Mix Metal',
                      'G14kt',
											'G18kt',
											'G22kt',
											'G9kt',
											'Gold / 9kt']]
              }
          }
      });

			frm.set_query('cost', () => {
					return {
							filters: {
									design_code_2d: frm.doc.design_code,
									design__type: '2D Design',

							}
					}
			})



// 			frm.set_query('designer_name', (frm) => {
// 			 return {
// 				 filters: {
// 						 parent_department: ['in', ['Product Development (NPD)',]],
// 						 status : 'Active',
// 						 custom_sub_department : 'CAD Designer'
// 						 }
// 					 }
// 		 });


    },


    // naming:function(frm){
    //     // var opportunity_no = frm.doc.opportunity_no;
    //     // var naming = frm.doc.opportunity_no;
    //     // frm.set_value('naming',naming);




    //     var opportunity_no = frm.doc.opportunity_no;
    //     var naming = frm.doc.opportunity_no;
    //     cur_frm.set_value('naming',naming);
    // },


	stone_details: function(frm) {
			console.log("hi22")
	},
});


// 		frappe.ui.form.on('NPD Test 2D Image', {
//     status: function(frm, cdt, cdn) {
//         let child_doc = locals[cdt][cdn];
//         if (child_doc.status == "Assign to Sales Person") {
//             frm.fields_dict['child_name'].grid.grid_rows_by_docname[cdn].toggle_editable('crm_status', false);
//         } else {
//             frm.fields_dict['child_name'].grid.grid_rows_by_docname[cdn].toggle_editable('crm_status', true);
//         }
//     }
// });
	frappe.ui.form.on('NPD Plating CT', {
        plating_type: function(frm, cdt, cdn) {
            generate_code(frm,cdt,cdn);
        },
        micron: function(frm, cdt, cdn) {
            generate_code(frm,cdt,cdn);
        },
        gold_kt: function(frm, cdt, cdn) {
            generate_code(frm,cdt,cdn);
        },
        color: function(frm, cdt, cdn) {
            generate_code(frm,cdt,cdn);
        },
        gold: function(frm, cdt, cdn) {
            generate_code(frm,cdt,cdn);
        },
        anti_tarnish: function(frm, cdt, cdn) {
            generate_code(frm,cdt,cdn);
        },

	});



frappe.ui.form.on('Opportunity Stone CT', {


		item_group_new :function(frm,cdt,cdn){
		    let child = locals[cdt][cdn];
		    if(child.item_group_new) {
	    	    frappe.db.get_doc("Item Group New", child.item_group_new).then((doc) => {
	    	        console.log(doc);
	    	        var check = 0;
	    	        if(doc.abbreviation) {
	    	            if(doc.abbreviation.length == 3){
	    	                check = 1;
	    	            }
	    	        }
	    	        if(check == 1) {
	    	            frappe.model.set_value(cdt,cdn,'item_group_s_name', doc.abbreviation);
	    	            generate_stone_code(frm,cdt,cdn);
	    	        }
	    	        else {
	    	            frappe.model.set_value(cdt,cdn,'item_group_new', "");
	    	            frappe.msgprint("Please update the stone short name.");
	    	        }
	    	    });
		    }
	    },
      item_sub_group :function(frm,cdt,cdn){
				let child = locals[cdt][cdn];
				if(child.item_sub_group) {
						frappe.db.get_doc("Item Sub Group", child.item_sub_group).then((doc) => {
								console.log(doc);
								var check = 0;
								if(doc.short_name) {
										if(doc.short_name.length == 3){
												check = 1;
										}
								}
								if(check == 1) {
										frappe.model.set_value(cdt,cdn,'subgroup_sname', doc.short_name);
										generate_stone_code(frm,cdt,cdn);
								}
								else {
										frappe.model.set_value(cdt,cdn,'item_sub_group', "");
										frappe.msgprint("Please update the short name.");
								}
						});
				}
			},

      stone_name :function(frm,cdt,cdn){
        let child = locals[cdt][cdn];
        if(child.stone_name) {
          frappe.db.get_doc("Item Category", child.stone_name).then((doc) => {
            console.log(doc);
            var check = 0;
            if(doc.short_name) {
              if(doc.short_name.length == 3){
                check = 1;
              }
            }
            if(check == 1) {
              frappe.model.set_value(cdt,cdn,'stone_short_name', doc.short_name);
              generate_stone_code(frm,cdt,cdn);
            }
            else {
              frappe.model.set_value(cdt,cdn,'stone_name', "");
              frappe.msgprint("Please update the stone short name.");
            }
          });
        }
      },

		shape :function(frm,cdt,cdn){
		    let child = locals[cdt][cdn];
		    if(child.shape) {
	    	    frappe.db.get_doc("Item Shape", child.shape).then((doc) => {
	    	        console.log(doc);
	    	        var check = 0;
	    	        if(doc.shape_aliases) {
	    	            if(doc.shape_aliases.length == 2){
	    	                check = 1;
	    	            }
	    	        }
	    	        if(check == 1) {
	    	            frappe.model.set_value(cdt,cdn,'stone_short_shape', doc.shape_aliases);
	    	            generate_stone_code(frm,cdt,cdn);
	    	        }
	    	        else {
	    	            frappe.model.set_value(cdt,cdn,'shape', "");
	    	            frappe.msgprint("Please update the shape short name.");
	    	        }
	    	    });
		    }
	    },


		cut :function(frm,cdt,cdn){
		    let child = locals[cdt][cdn];
		    if(child.cut) {
	    	    frappe.db.get_doc("Item Cut", child.cut).then((doc) => {
	    	        console.log(doc);
	    	        var check = 0;
	    	        if(doc.cut_aliases) {
	    	            if(doc.cut_aliases.length == 2){
	    	                check = 1;
	    	            }
	    	        }
	    	        if(check == 1) {
	    	            frappe.model.set_value(cdt,cdn,'stone_short_cut', doc.cut_aliases);
	    	            generate_stone_code(frm,cdt,cdn);
	    	        }
	    	        else {
	    	            frappe.model.set_value(cdt,cdn,'cut', "");
	    	            frappe.msgprint("Please update the cut short name.");
	    	        }
	    	    });
		    }
	    },


            quality :function(frm,cdt,cdn){
          let child = locals[cdt][cdn];
          if(child.quality) {
            if(child.quality.length == 2) {
              generate_stone_code(frm,cdt,cdn);
            }
            else {
                frappe.model.set_value(cdt,cdn,'quality', "");
                // frappe.msgprint("Length should be between 0 to 9");
            }
          }
        },

				length :function(frm,cdt,cdn){
					let child = locals[cdt][cdn];
			    if(child['length']) {
						if(child['length'] > 0 && child['length'] <= 99) {
							generate_stone_code(frm,cdt,cdn);
						}
						else {
								frappe.model.set_value(cdt,cdn,'length', "");
								frappe.msgprint("Length should be between 0 to 99");
						}
					}
				},

				width :function(frm,cdt,cdn){
					let child = locals[cdt][cdn];
			    if(child.width) {
						if(child.width > 0 && child.width <= 99) {
							generate_stone_code(frm,cdt,cdn);
						}
						else {
								frappe.model.set_value(cdt,cdn,'width', "");
								frappe.msgprint("Width should be between 0 to 99");
						}
			       }
				},

				    mine :function(frm,cdt,cdn){
                    let child = locals[cdt][cdn];
                    if(child.mine) {
                    if(child.mine.length == 3) {
                          generate_stone_code(frm,cdt,cdn);
                        }
                        else {
                            frappe.model.set_value(cdt,cdn,'mine', "");
                        }
                      }
                    },

                })


function generate_stone_code(frm,cdt,cdn) {
  	var child = locals[cdt][cdn];
  	var stone_code = "";
    if(checkString(child.item_group_s_name)) { stone_code += checkString(child.item_group_s_name) + '-';} else { stone_code += 'XXX'}
    if(checkString(child.subgroup_sname)) { stone_code += checkString(child.subgroup_sname) + '-';} else { stone_code += 'XXX'}
    if(checkString(child.stone_short_name)) { stone_code += checkString(child.stone_short_name) + '-';} else { stone_code += 'XXX'}
    if(checkString(child.stone_short_cut)) { stone_code += checkString(child.stone_short_cut) + '-';} else { stone_code += 'XXX'}
    if(checkString(child.stone_short_shape)) { stone_code += checkString(child.stone_short_shape) + '-';} else { stone_code += 'XXX'}
    stone_code += generate_stone_code_for_digit(child['length']) + 'x';
    stone_code += generate_stone_code_for_digit(child.width) + '-';
    if(checkString(child.quality)) { stone_code += checkString(child.quality) + '-';} else { stone_code += 'XX'}
    if(checkString(child.mine)) { stone_code += checkString(child.mine);} else { stone_code += 'XXX'}

  	frappe.model.set_value(cdt,cdn,'stone_code', stone_code);
  	cur_frm.refresh_field("stone_code");
}



frappe.ui.form.on('Opportunity Diamond CT',{
	item_group :function(frm,cdt,cdn){
			let child = locals[cdt][cdn];
			if(child.item_group) {
					frappe.db.get_doc("Item Group New", child.item_group).then((doc) => {
							console.log(doc);
							var check = 0;
							if(doc.abbreviation) {
									if(doc.abbreviation.length == 3){
											check = 1;
									}
							}
							if(check == 1) {
									frappe.model.set_value(cdt,cdn,'item_group_sname', doc.abbreviation);
									generate_diamond_code(frm,cdt,cdn);
							}
							else {
									frappe.model.set_value(cdt,cdn,'item_group', "");
									frappe.msgprint("Please update the short name.");
							}
					});
			}
		},

	item_sub :function(frm,cdt,cdn){
			let child = locals[cdt][cdn];
			if(child.item_sub) {
					frappe.db.get_doc("Item Sub Group", child.item_sub).then((doc) => {
							console.log(doc);
							var check = 0;
							if(doc.short_name) {
									if(doc.short_name.length == 3){
											check = 1;
									}
							}
							if(check == 1) {
									frappe.model.set_value(cdt,cdn,'diamond_short_name', doc.short_name);
									generate_diamond_code(frm,cdt,cdn);
							}
							else {
									frappe.model.set_value(cdt,cdn,'item_sub', "");
									frappe.msgprint("Please update the short name.");
							}
					});
			}
		},

	item_shape :function(frm,cdt,cdn){
			let child = locals[cdt][cdn];
			if(child.item_shape) {
					frappe.db.get_doc("Item Shape", child.item_shape).then((doc) => {
							console.log(doc);
							var check = 0;
							if(doc.shape_aliases) {
									if(doc.shape_aliases.length == 2){
											check = 1;
									}
							}
							if(check == 1) {
									frappe.model.set_value(cdt,cdn,'diamond_short_shape', doc.shape_aliases);
									generate_diamond_code(frm,cdt,cdn);
							}
							else {
									frappe.model.set_value(cdt,cdn,'item_shape', "");
									frappe.msgprint("Please update the Diamond shape short name.");
							}
					});
			}
		},


	item_cut :function(frm,cdt,cdn){
			let child = locals[cdt][cdn];
			if(child.item_cut) {
					frappe.db.get_doc("Item Cut", child.item_cut).then((doc) => {
							console.log(doc);
							var check = 0;
							if(doc.cut_aliases) {
									if(doc.cut_aliases.length == 2){
											check = 1;
									}
							}
							if(check == 1) {
									frappe.model.set_value(cdt,cdn,'diamond_short_cut', doc.cut_aliases);
									generate_diamond_code(frm,cdt,cdn);
							}
							else {
									frappe.model.set_value(cdt,cdn,'item_cut', "");
									frappe.msgprint("Please update the Diamond cut short name.");
							}
					});
			}
		},

	item_quality :function(frm,cdt,cdn){
			let child = locals[cdt][cdn];
			if(child.item_quality) {
					frappe.db.get_doc("Item Quality", child.item_quality).then((doc) => {
							console.log(doc);
							var check = 0;
							if(doc.id) {
									if(doc.id.length > 0){
											check = 1;
									}
							}
							if(check == 1) {
									frappe.model.set_value(cdt,cdn,'diamond_short_quality', doc.id);
									generate_diamond_code(frm,cdt,cdn);
							}
							else {
									frappe.model.set_value(cdt,cdn,'item_quality', "");
									frappe.msgprint("Please update the quality short name.");
							}
					});
			}
		},

	item_length :function(frm,cdt,cdn){
		let child = locals[cdt][cdn];
		if(child['item_length']) {
			if(child['item_length'] > 0 && child['item_length'] <= 99) {
				generate_diamond_code(frm,cdt,cdn);
			}
			else {
					frappe.model.set_value(cdt,cdn,'item_length', "");
					frappe.msgprint("Length should be between 0 to 99");
			}
		}
	},

	item_widht :function(frm,cdt,cdn){
		let child = locals[cdt][cdn];
		if(child.item_widht) {
			if(child.item_widht > 0 && child.item_widht <= 99) {
				generate_diamond_code(frm,cdt,cdn);
			}
			else {
					frappe.model.set_value(cdt,cdn,'item_widht', "");
					frappe.msgprint("Width should be between 0 to 99");
			}
		}
	},


	color :function(frm,cdt,cdn){
			let child = locals[cdt][cdn];
			if(child.color) {
					frappe.db.get_doc("Item Color", child.color).then((doc) => {
							console.log(doc);
							var check = 0;
							if(doc.id) {
									if(doc.id.length > 0){
											check = 1;
									}
							}
							if(check == 1) {
									frappe.model.set_value(cdt,cdn,'diamond_short_color', doc.id);
									generate_diamond_code(frm,cdt,cdn);
							}
							else {
									frappe.model.set_value(cdt,cdn,'color', "");
									frappe.msgprint("Please update the Diamond Color Short Name.");
							}
					});
			}
		},

	// size :function(frm,cdt,cdn){
	// 	generate_stone_code(frm,cdt,cdn);
	// },
})

function generate_diamond_code(frm,cdt,cdn) {
	var child = locals[cdt][cdn];
	var diamond_code = "";
		if(checkString(child.item_group_sname)) { diamond_code += checkString(child.item_group_sname) + '-';} else { diamond_code += 'XXX'}
	if(checkString(child.diamond_short_name)) { diamond_code += checkString(child.diamond_short_name) + '-';} else { diamond_code += 'XXX'}
	if(checkString(child.diamond_short_cut)) { diamond_code += checkString(child.diamond_short_cut) + '-';} else { diamond_code += 'X'}
	if(checkString(child.diamond_short_shape)) { diamond_code += checkString(child.diamond_short_shape) + '-';} else { diamond_code += 'X'}

	diamond_code += generate_diamond_code_for_digit(child['item_length']) + 'x';
	diamond_code += generate_diamond_code_for_digit(child.item_widht) + '-';
	if(checkString(child.diamond_short_quality)) { diamond_code += checkString(child.diamond_short_quality) + '-';} else { diamond_code += 'XX'}

	if(checkString(child.diamond_short_color)) { diamond_code += checkString(child.diamond_short_color);} else { diamond_code += 'XX'}

	// if(checkString(child.size)) { diamond_code += checkString(child.size);} else { diamond_code += 'X'}

	frappe.model.set_value(cdt,cdn,'diamond_code', diamond_code);
}

function generate_diamond_code_for_digit(value) {
	var digit_code = '00';
	if(checkDigit(value)) {
		if(value < 10) {
			if(value % 1) { digit_code = value;}
			else { digit_code = '0'+value;}
		}
		else {
			digit_code = value;
		}
	}
	return digit_code;

}



function generate_stone_code_for_digit(value) {
	var digit_code = '00';
	if(checkDigit(value)) {
		if(value < 10) {
			if(value % 1) { digit_code = value;}
			else { digit_code = '0'+value;}
		}
		else {
			digit_code = value;
		}
	}
	return digit_code;

}


function generate_code(frm,cdt,cdn) {
    var child = locals[cdt][cdn];
    var plating_value = child.plating_type;
    var micron_value = child.micron;
    var gold_kt_value = child.gold_kt;
    var color_value = child.color;
    var gold_value = child.gold;
    var anti_tarnish_value = child.anti_tarnish;

    var plating_codes = {
        "Flash Gold Plating": "PLT-FLSH",
        "Flash Rhodium": "PLT-FLSH",
        "Micron Plating": "PLT-MIC",
    };

    var plating_code = plating_codes[plating_value] || "";


    // Handle plating thickness based on selected plating value
    if (plating_value === "Micron Plating") {
				frm.set_df_property(child.parentfield, 'read_only', 0, frm.docname, 'micron', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 0, frm.docname, 'gold_kt', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 0, frm.docname, 'color', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 0, frm.docname, 'gold', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 0, frm.docname, 'anti_tarnish', child.name);
				frm.set_df_property(child.parentfield, 'options', [ "0.25 Micron",
																								            "0.50 Micron",
																								            "1.00 Micron",
																								            "1.50 Micron",
																								            "2.00 Micron",
																								            "2.50 Micron",
																								            "3.00 Micron",
																								            "N/A"
																								        ].join('\n'), frm.docname, 'micron', child.name);

        if (!micron_value || micron_value === "N/A") {
            frappe.model.set_value(cdt,cdn,'micron', "0.25 Micron");
        }

				if(micron_value == "0.25 Micron" || micron_value == "0.50 Micron" || micron_value == "1.00 Micron" || micron_value == "1.50 Micron" ||
			     micron_value == "2.00 Micron" || micron_value == "2.50 Micron" || micron_value == "3.00 Micron") {
						 plating_code += '-' + micron_value.split(' ')[0];
				}

				if(gold_kt_value == "18KT" || gold_kt_value == "24KT") {
					plating_code += '-' + gold_kt_value.split(' ')[0];
				}

				if(color_value == "9 kt" || color_value == "10 kt" || color_value == "12 kt" || color_value == "14 kt" || color_value == "18 kt" ||
			     color_value == "22 kt" || color_value == "24 kt") {
					plating_code += '-' + color_value.split(' ')[0] + 'C';
				}

				if(color_value == "Vintage" || color_value == "Hamilton") {
					plating_code += '-' + color_value.split(' ')[0] + 'C';
				}

				if(gold_value == "Yellow Gold") { plating_code += 'YG' ;}
				if(gold_value == "Rose Gold") { plating_code += 'RG' ;}

				if(anti_tarnish_value == "AT") { plating_code += '-AT' ;}

    } else if (plating_value === "Flash Gold Plating") {
        frappe.model.set_value(cdt,cdn,'micron', '3 to 5 miles');
        frappe.model.set_value(cdt,cdn,'gold_kt', "N/A");
        frappe.model.set_value(cdt,cdn,'anti_tarnish', "N/A");
				frm.set_df_property(child.parentfield, 'read_only', 1, frm.docname, 'micron', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 1, frm.docname, 'gold_kt', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 1, frm.docname, 'anti_tarnish', child.name);

				if(color_value == "9 kt" || color_value == "10 kt" || color_value == "12 kt" || color_value == "14 kt" || color_value == "18 kt" ||
			     color_value == "22 kt" || color_value == "24 kt") {
					plating_code += '-' + color_value.split(' ')[0] + 'C';
				}

				if(color_value == "Vintage" || color_value == "Hamilton") {
					plating_code += '-' + color_value.split(' ')[0] + 'C';
				}

				if(gold_value == "Yellow Gold") { plating_code += 'YG' ;}
				if(gold_value == "Rose Gold") { plating_code += 'RG' ;}

    } else if (plating_value === "Flash Rhodium") {
        frappe.model.set_value(cdt,cdn,'micron', 'Flash Rhodium');
        frappe.model.set_value(cdt,cdn,'gold_kt', "N/A");
        frappe.model.set_value(cdt,cdn,'anti_tarnish', "N/A");
				frm.set_df_property(child.parentfield, 'read_only', 1, frm.docname, 'micron', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 1, frm.docname, 'gold_kt', child.name);
				frm.set_df_property(child.parentfield, 'read_only', 1, frm.docname, 'anti_tarnish', child.name);

				if(color_value == "9 kt" || color_value == "10 kt" || color_value == "12 kt" || color_value == "14 kt" || color_value == "18 kt" ||
			     color_value == "22 kt" || color_value == "24 kt") {
					plating_code += '-' + color_value.split(' ')[0] + 'C';
				}

				if(color_value == "Vintage" || color_value == "Hamilton") {
					plating_code += '-' + color_value.split(' ')[0] + 'C';
				}

				if(gold_value == "Yellow Gold") { plating_code += 'YG' ;}
				if(gold_value == "Rose Gold") { plating_code += 'RG' ;}

    }

		frappe.model.set_value(cdt,cdn,'plating_code', plating_code);
		frm.refresh_field(child.parentfield);
}



$("#npd-pd_sheet_tab-tab").on('click', function() {
    console.log("hi33");

    if(cur_frm.doc.stone_details.length > 0) {
        cur_frm.doc.pd_stoned = [];
        for(let i =0; i<cur_frm.doc.stone_details.length; i++) {
            var childTable = cur_frm.add_child("pd_stoned");
            var old_table = cur_frm.doc.stone_details[i];
            childTable.stone_name = old_table.stone_name;
            childTable.cut = old_table.cut;
            childTable.shape = old_table.shape;
            childTable['length'] = old_table['length'];
            childTable.width = old_table.width;
            childTable.size = old_table.size;
            childTable.stone_code = old_table.stone_code;
            childTable.wght = old_table.wght;
            childTable.qty = old_table.qty;
            childTable.set_type = old_table.set_type;
            childTable.mine = old_table.mine;
            childTable.quality = old_table.quality;
            childTable.description = old_table.description;
            childTable.item_sub_group = old_table.item_sub_group;
        }
        cur_frm.refresh_field("pd_stoned");
    }



    if(cur_frm.doc.diamond_details.length > 0) {
        cur_frm.doc.pd_diamondd = []
        for(let i =0; i<cur_frm.doc.diamond_details.length; i++) {
            var childTable = cur_frm.add_child("pd_diamondd");
            var old_table = cur_frm.doc.diamond_details[i];
            childTable.diamond_code = old_table.diamond_code;
            childTable.diamond_type = old_table.diamond_type;
            childTable.item_quality = old_table.item_quality;
            childTable.item_cut = old_table.item_cut;
            childTable.item_shape = old_table.item_shape;
            childTable.item_length = old_table.item_length;
            childTable.item_widht = old_table.item_widht;
            childTable.color = old_table.color;
            childTable.qty = old_table.qty;
            childTable.item_sub = old_table.item_sub;


        }
        cur_frm.refresh_field("pd_diamondd");
    }


     if(cur_frm.doc.finding_details.length > 0) {
        cur_frm.doc.finding_details_pd = []
        for(let i =0; i<cur_frm.doc.finding_details.length; i++) {
            var childTable = cur_frm.add_child("finding_details_pd");
            var old_table = cur_frm.doc.finding_details[i];
            childTable.finding_details = old_table.finding_details;
            childTable.metal_type = old_table.metal_type;
            childTable.karat = old_table.karat;
            childTable.item_category = old_table.item_category;
            childTable.item_cut = old_table.item_cut;
            childTable.item_shape = old_table.item_shape;
        }
        cur_frm.refresh_field("finding_details_pd");
    }


// 		cur_frm.doc.pd_stoned = cur_frm.doc.stone_details;
// 		cur_frm.refresh_field('pd_stoned');

// 		cur_frm.doc.pd_diamondd = cur_frm.doc.diamond_details;
// 		cur_frm.refresh_field('pd_diamondd');
		//
		// cur_frm.doc.finding_details_pd = cur_frm.doc.finding_details;
		// cur_frm.refresh_field('finding_details_pd');
		//
		cur_frm.doc['2d_design_no'] = cur_frm.doc.design_code;
		cur_frm.refresh_field('2d_design_no');

		cur_frm.doc['metal_type1'] = cur_frm.doc.metal_type;
		cur_frm.refresh_field('metal_type1');
});



$("#npd-costing_tab-tab").on('click', function() {

	cur_frm.doc.design_code_cos = cur_frm.doc.design_code;

	frappe.db.get_list('Test Costing', {
		filters: {
			design_code_2d: cur_frm.doc.design_code,
		},
		fields: ['*'],
		limit: 1,
	}).then(res => {
		if(res.length) {
			for (var i = 0; i < res.length; i++) {
				cur_frm.set_value('cost', res[i].name);
				cur_frm.set_value('costing_sale_price', res[i].total_cost_for_ss);
				cur_frm.set_df_property('create_costing', 'hidden', 1)
			}
		}
		else {
			cur_frm.set_value('cost', '');
			cur_frm.set_value('costing_sale_price', '');
			cur_frm.set_df_property('create_costing', 'hidden', 0)
		}
	});

	cur_frm.refresh_field('design_code_cos');

});




frappe.ui.form.on('NPD',{
	create_costing:function(frm){
	    if(frm.is_new()) {
	        frappe.msgprint("Please Save the form first");
	    }
	    else {
	        addNPDCosting(frm);
	    }

	}
});

function addNPDCosting(frm) {
				frappe.call({
					method: "npd_costing",
					type: "POST",
					args: {
						'name': frm.doc.cost,
						'customer_name': frm.doc.customer_name,
						'customer_code': frm.doc.customer_code,
						'metal_type': frm.doc.metal_type,
						// 'stone_child': frm.doc.stone_details,
						// 'diamond_costing': frm.doc.diamond_details,
						// 'findings_list': frm.doc.findings_list,
						'design_code':frm.doc.design_code_cos,
					},

				// 	success: function(obj) {
				// 		console.log("hi11");
				// 		if (obj.data.status) {
				// 			console.log("hi22");
				// 			frappe.model.set_value(cdt,cdn,'npd_sheet',obj.data.data.name);
				// 			frm.save();
				// 			window.location.href= window.locaton.origin + '/app/npd/' + obj.data.data.name
				// 			console.log(window.locaton.origin + '/app/npd/' + obj.data.data.name);
				// 		} else {
				// 			console.log("hi33");
				// 			frappe.msgprint(obj.data.msg);
				// 		}
				// 	},
					error: function(obj) {
						console.log("hi22"); console.log(obj);
					},
					always: function(obj) {
					    console.log("hi44");
						if (obj.data.status) {
							console.log("hi55");
							frm.set_value('cost',obj.data.data.name);
							frm.save();
				// 			sessionStorage.redirect_to_id = obj.data.data.name
						} else {
							console.log("hi66");
							frappe.msgprint(obj.data.msg);
						}
					},
					// btn: opts.btn, freeze: false, freeze_message: "",
					async: true,
					// url: "" || frappe.request.url,
				});
			}



function checkDigit(value) {
    if (value > 0 || value < 0) { return value; }
    else { return 0; }
}


function checkString(value) {
	if(value) { return value; }
	else { return '';}
}


frappe.ui.form.on('Opportunity Stone CT',{
  item_group_new :function(frm,cdt,cdn){
      get_description(frm, cdt, cdn);
   },
   item_sub_group :function(frm,cdt,cdn){
       get_description(frm, cdt, cdn);
   },
  stone_name :function(frm,cdt,cdn){
        get_description(frm, cdt, cdn);
    },
    cut_fname :function(frm,cdt,cdn){
        get_description(frm, cdt, cdn);
    },
    shape_fname :function(frm,cdt,cdn){
        get_description(frm, cdt, cdn);
    },
    length :function(frm,cdt,cdn){
        get_description(frm, cdt, cdn);
    },
    width :function(frm,cdt,cdn){
        get_description(frm, cdt, cdn);
    },
    quality :function(frm,cdt,cdn){
        get_description(frm, cdt, cdn);
    },
    mine :function(frm,cdt,cdn){
        get_description(frm, cdt, cdn);
    },


});
function get_description(frm, cdt, cdn){
    let child = locals[cdt][cdn];
    var item_group_new = child.item_group_new|| '';
    var item_sub_group = child.item_sub_group|| '';
    var stone_name = child.stone_name|| '';
    var cut_fname = child.cut_fname || '';
    var shape_fname = child.shape_fname || '';
    var length = child['length'] || '';
    var width = child.width || '';
    var quality = child.quality || '';
    var mine = child.mine || '';

    var description = item_group_new+' '+item_sub_group +' '+stone_name + ' ' + cut_fname+' '+ shape_fname+ ' '+length+'x'+width+' '+quality + ' '+mine
    frappe.model.set_value(cdt, cdn, "description", description);
}

frappe.ui.form.on('Opportunity Diamond CT',{
    item_group :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },
    item_sub :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },
    c_dfname :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },
    s_dfname :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },
    item_length :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },
    item_widht :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },
    q_fname :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },
    cl_fname :function(frm,cdt,cdn){
        get_description_diamond(frm, cdt, cdn);
    },

});
function get_description_diamond(frm, cdt, cdn){
    let child = locals[cdt][cdn];
    var item_group = child.item_group|| '';
    var item_sub = child.item_sub|| '';
    var c_dfname = child.c_dfname || '';
    var s_dfname = child.s_dfname || '';
    var item_length = child['item_length'] || '';
    var item_widht = child.item_widht || '';
    var q_fname = child.q_fname || '';
    var cl_fname = child.cl_fname || '';

    var description = item_group+ ' ' +item_sub + ' ' + c_dfname+' '+ s_dfname+ ' '+item_length+'x'+item_widht+' '+q_fname+ ' '+cl_fname
    frappe.model.set_value(cdt, cdn, "description", description);
}

# Copyright (c) 2025, Pink city IT team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StonePriceRequest(Document):
	pass
    
	
@frappe.whitelist()
def send_stone_details() :
	stone = frappe.form_dict.get("stone_name", False)
	cut = frappe.form_dict.get("cut_name", "")
	shape = frappe.form_dict.get("shape_name", "")
	quality = frappe.form_dict.get("quality", "")
	length = frappe.form_dict.get("length", "")
	width = frappe.form_dict.get("width", "")
	height = frappe.form_dict.get("height", "")
	medium = frappe.form_dict.get("medium", "")
	qty = frappe.form_dict.get("qty", "")
	# weight_per_pcs_cts = frappe.form_dict.get("weight_per_pcs_cts", "")
	# total_weight = frappe.form_dict.get("total_weight", "")
	size = frappe.form_dict.get("size", "")
	uom = frappe.form_dict.get("uom", "")
	costing_id = frappe.form_dict.get("costing_id", "")
	design_id = frappe.form_dict.get("design_id", "")
	image_link = frappe.form_dict.get("image", "")
	client = frappe.form_dict.get("client", "")
	sales_person = frappe.form_dict.get("sales_person", "")
	metal_type = frappe.form_dict.get("metal_type", "")
	stone_code = frappe.form_dict.get("stone_code", "")
	btn_price = frappe.form_dict.get("btn_price", "Demanding Price")


	stone_generated_val = frappe.form_dict.get("stone_generated_val", "")

	data = {}

	if stone_generated_val:
		existing_stone = frappe.get_doc("Stone Price Request", stone_generated_val)
		data["status"] = False
		data["data"] = existing_stone
		data["msg"] = "Stone Quotation already exists."
		frappe.response["data"] = data
	else:
		
		doc = frappe.new_doc("Stone Price Request")
		doc.stone = stone
		doc.cut = cut
		doc.shape = shape
		doc.quality = quality
		doc.length = length
		doc.width = width
		doc.height = height
		doc.medium = medium
		doc.qty = qty
		# doc.total_weight = total_weight
		doc.uom = uom
		doc.costing = costing_id
		doc.design = design_id
		doc.image_link = image_link
		doc.workflow_state = 'Price Pending'
		doc.metal_type = metal_type
		doc.stone_code = stone_code
		doc.sales_person = sales_person
		doc.client = client
		doc.weight_per_pcs_cts = 0 
		doc.price = 0
		doc.btn_price = btn_price
		doc.save()

		data["status"] = True
		data["data"] = doc
		data["msg"] = "Stone Price detail added. Please add the price for the stone."
		frappe.response["data"] = data


@frappe.whitelist()
def update_stone_details() :
	stone_generated_val = frappe.form_dict.get("stone_generated_val", "")
	btn_price_status = frappe.form_dict.get("status", "")

	data = {}

	if stone_generated_val:
		existing_stone = frappe.get_doc("Stone Price Request", stone_generated_val)
		if existing_stone.get("price_history", False):
			for price_table in existing_stone.price_history :
				if existing_stone.price == price_table.price :
					# existing_stone[i].btn_price = btn_price_status
					price_table.btn_price = btn_price_status
		existing_stone.btn_price = btn_price_status
		existing_stone.save()
		data["status"] = True
		data["data"] = existing_stone
		data["msg"] = "Stone Price updated."
		frappe.response["data"] = data
	else:
		data["status"] = False
		data["data"] = []
		data["msg"] = "Stone Price not found."
		frappe.response["data"] = data
			

 

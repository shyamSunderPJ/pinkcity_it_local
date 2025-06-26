# Copyright (c) 2025, pinkcity and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class StoneManufacturingProcess(Document):
	pass


@frappe.whitelist()
def create_smprocess_from_jobworkreturn():
	company = frappe.form_dict.get("company", "")
	job_worker_name = frappe.form_dict.get("job_worker_name", "")
	gst_no = frappe.form_dict.get("gst_no", "")
	job_work_type = frappe.form_dict.get("job_work_type", "")
	stone_manufacturing_process = frappe.form_dict.get("stone_manufacturing_process", "")
	
	# New: get required fields
	item_code = frappe.form_dict.get("item_code", "")
	item_name = frappe.form_dict.get("item_name", "")
	type_of_goods = frappe.form_dict.get("type_of_goods", "")
	pieces = frappe.form_dict.get("pieces", 0)
	qunatity = frappe.form_dict.get("qunatity", 0)
	rate = frappe.form_dict.get("rate", 0)
	amount = frappe.form_dict.get("amount", 0)

	data = {}
	if stone_manufacturing_process:
		bag_doc = frappe.get_doc('Stone Manufacturing Process', stone_manufacturing_process)
		data['status'] = False
		data['data'] = bag_doc
		data['msg'] = "Stone Manufacturing Process already exists."
	else:
		doc = frappe.new_doc('Stone Manufacturing Process')
		doc.item_code = item_code
		doc.item_name = item_name
		doc.type_of_goods = type_of_goods
		doc.job_work_type = job_work_type
		doc.pieces = pieces
		doc.qunatity = qunatity
		doc.rate = rate
		doc.amount = amount

		doc.save()
		data['status'] = True
		data['data'] = doc
		data['msg'] = "Stone Manufacturing Process added."
	
	frappe.response["data"] = data


@frappe.whitelist()
def send_stone_details() :
	job_work_issue_details = frappe.form_dict.get("job_work_issue_details", False)
	frappe.response["hi1"] = "dhf"
	a = json.loads(job_work_issue_details)
	# for item in my_list:
	# 	a = item.split(',')
	frappe.response["job_work_issue_details"] = a
	if a: 
		frappe.response["hi2"] = "dhd23f"
		for job_work in a:
			issue_date = job_work.get("issue_date", '') ,
			challan = job_work.get("challan_no", ''),
			item_code = job_work.get("item_code", ''),
			uom = job_work.get("unique_qunatity_code", ''),
			pieces = job_work.get("pieces", ''),
			weight = job_work.get("qunatity", ''),
			rate = job_work.get("rate", ''),
			total_amount = job_work.get("total_amount", ''),
			job_work_name = job_work.get("description_of_goods", '')
			type_of_goods = job_work.get("type_of_goods", '')
			job_work_type = job_work.get("job_work_type", '')
			frappe.response["job_work"] = job_work
			frappe.response["issue_date"] = issue_date[0]
			frappe.response["item_code"] = item_code[0]
			frappe.response["challan"] = challan[0]
			frappe.response["uom"] = uom[0]
			frappe.response["pieces"] = pieces[0]
			frappe.response["weight"] = weight[0]
			frappe.response["rate"] = rate[0]
			frappe.response["total_amount"] = total_amount[0]
			frappe.response["job_work_name"] = job_work_name


			check_doc = frappe.db.exists( {
								"doctype": "Stone Manufactring Process",
								"issue_date":issue_date[0], 
								"item_code": item_code[0], 
								"challan":challan[0], 
								"uom": uom[0],
								"pieces": pieces[0],
								"weight": weight[0],
								"rate":rate[0],
								"total_amount": total_amount[0],
								"job_work_name": job_work_name,
								"type_of_goods":type_of_goods,
								"job_work_type":job_work_type
								})
			if check_doc:
			# if frappe.db.exists("Stone Manufactring Process", {
			# 													"issue_date":issue_date, 
			# 													"item_code": item_code, 
			# 													"challan":challan, 
			# 													"uom": uom,
			# 													"pieces": pieces,
			# 													"weight": weight,
			# 													"rate":rate,
			# 													"total_amount": total_amount,
			# 													"job_work_name": job_work_name
			# 													}):

				frappe.response["exists"] = item_code
			# 	frappe.response["data"] = []
			# 	frappe.response["msg"] = "Stone Manufacturing Process already exists."
				pass
			else:
				doc = frappe.new_doc("Stone Manufacturing Process")
				doc.issue_date = issue_date[0]
				doc.challan = challan[0]
				doc.item_code = item_code[0]
				doc.uom = uom[0]
				doc.pieces = pieces[0]
				doc.weight = weight[0]
				doc.rate = rate[0]
				doc.total_amount = total_amount[0]
				doc.job_work_name = job_work_name
				doc.type_of_goods = type_of_goods
				doc.job_work_type = job_work_type
				doc.save()
		frappe.response["status"] = True
		frappe.response["data"] = doc
		frappe.response["msg"] = "Stone manufacturing detail added. Please add the manufacturing for the stone."
		# frappe.response["data"] = data

	
		# if new_stone:
		# 	for doc in new_stone:
		# 		# doc = frappe.get_doc("Stone Manufacturing Process")
		# 		issue_date = doc.get("issue_date", ''),
		# 		challan = doc.get("challan", ''),
		# 		item_code = doc.get("item_code", ''),
		# 		uom = doc.get("uom", ''),
		# 		pieces = doc.get("pieces", ''),
		# 		weight = doc.get("weight", ''),
		# 		width = doc.get("width", ''),
		# 		rate = doc.get("rate", ''),
		# 		total_amount = doc.get("total_amount", ''),
		# 		job_work_name = doc.get("job_work_name", '')
		# doc.save()
			

	# issue_date = frappe.form_dict.get("issue_date", False)
	# challan = frappe.form_dict.get("challan", "")
	# item_code = frappe.form_dict.get("item_code", "")
	# uom = frappe.form_dict.get("uom", "")
	# pieces = frappe.form_dict.get("pieces", "")
	# weight = frappe.form_dict.get("weight", "")
	# rate = frappe.form_dict.get("rate", "")
	# total_amount = frappe.form_dict.get("total_amount", "")
	# job_work_name = frappe.form_dict.get("job_work_name", "")
	
	# data = {}

	# if job_work_name:
	# 	existing_stone = frappe.get_doc("Stone Manufacturing Process", job_work_name)
	# 	data["status"] = False
	# 	data["data"] = existing_stone
	# 	data["msg"] = "Stone Manufacturing Process exist."
	# 	frappe.response["data"] = data
	# else:
		
	# 	doc = frappe.new_doc("Stone Manufacturing Process")
	# 	doc.issue_date = issue_date
	# 	doc.challan = challan
	# 	doc.item_code = item_code
	# 	doc.uom = uom
	# 	doc.pieces = pieces
	# 	doc.weight = weight
	# 	doc.width = width
	# 	doc.rate = rate
	# 	doc.total_amount = total_amount
	# 	doc.job_work_name = job_work_name
	# 	doc.save()





# @frappe.whitelist()
# def create_smprocess_from_jobworkreturn() :
# 	company = frappe.form_dict.get("company", "")
# 	job_worker_name = frappe.form_dict.get("job_worker_name", "")
# 	gst_no = frappe.form_dict.get("gst_no", "")
# 	job_work_type = frappe.form_dict.get("job_work_type", "")
# 	stone_manufacturing_process = frappe.form_dict.get("stone_manufacturing_process", "")
	

# 	data = {}
# 	if stone_manufacturing_process:
# 		bag_doc = frappe.get_doc('Stone Manufacturing Process', stone_manufacturing_process)
# 		data['status'] = False
# 		data['data'] = bag_doc
# 		data['msg'] = "Stone Manufacturing Process already exists."
# 		frappe.response["data"] = data
# 	else :
# 		doc = frappe.new_doc('Stone Manufacturing Process')
# 		doc.item_code = item_code
# 		doc.item_name = item_name
# 		doc.type_of_goods = type_of_goods
# 		doc.job_work_type = job_work_type
# 		doc.pieces = pieces
# 		doc.qunatity = qunatity
# 		doc.rate = rate
# 		doc.amount = amount

# 		doc.save()
# 		data['status'] = True
# 		data['data'] = doc
# 		data['msg'] = "Stone Manufacturing Process added."
# 		frappe.response["data"] = data

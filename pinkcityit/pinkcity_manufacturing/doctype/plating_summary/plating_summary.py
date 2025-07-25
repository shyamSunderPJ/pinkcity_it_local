# Copyright (c) 2025, Pink city IT team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PlatingSummary(Document):
	pass


@frappe.whitelist()
def fetch_plating_transaction():
    company = frappe.form_dict.get("company", False)
    query = f"""SELECT 
    				tpt.company, 
                    tpmbd.design_code,
                    (
					CASE 
						WHEN tpmbd.plating_code LIKE '%0.5%' THEN '0.5'
						WHEN tpmbd.plating_code LIKE '%1.0%' THEN '1.0'
						WHEN tpmbd.plating_code LIKE '%1.5%' THEN '1.5'
						WHEN tpmbd.plating_code LIKE '%2.0%' THEN '2.0'
						WHEN tpmbd.plating_code LIKE '%2.5%' THEN '2.5'
						WHEN tpmbd.plating_code LIKE '%3.0%' THEN '3.0'
						WHEN tpmbd.plating_code LIKE '%3.5%' THEN '3.5'
						ELSE tpmbd.plating_code
					END
				) micron
				FROM `tabPlating Matler Bag Detail` tpmbd 
				JOIN `tabPlating Transaction` tpt on tpt.name = tpmbd.parent
				WHERE tpmbd.design_code NOT IN 
					( SELECT tppc.design_code 
					  FROM `tabPlating Price CT` tppc  
					  JOIN `tabPlating Summary` tps ON tps.name = tppc.parent
					  AND tps.company = '{company}'
					)
					AND tpt.company = '{company}'
				GROUP BY tpmbd.design_code, tpt.company
		"""
    data = frappe.db.sql(query ,as_dict=1,)
    frappe.response['status'] = True
    frappe.response['data'] = data
    frappe.response['msg'] = "Plating details found"
	
	
	# frappe.response['msg'] = "Plating details found"
    
            

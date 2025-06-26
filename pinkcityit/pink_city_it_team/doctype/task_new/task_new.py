# Copyright (c) 2025, Pink city IT team and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet

class TaskNew(NestedSet):
	pass
    # def after_save(self):
    #     frappe.msgprint("hello")



@frappe.whitelist()
def add_child_in_task(doc, event):
	if doc.parent_task_new:
		try:
			parent_name = doc.parent_task_new
			parent_doc = frappe.get_doc("PinkCity Task", parent_name)
			already_exists = False
			for row in parent_doc.sub_task:
				if row.name1 == doc.name:
					row.status = doc.status
					row.description = doc.description
					parent_doc.save()
					already_exists = True
					break
		
			if not already_exists:
				child = parent_doc.append("sub_task", {})
				child.name1 = doc.name
				child.status = doc.status
				child.description = doc.description
				parent_doc.save()

				# frappe.msgprint(f"Appended '{doc.name}' to parent '{parent_name}' sub_task table.")

		except Exception as e:
			frappe.throw(f"Failed to update parent task: {e}")
		# add_child_in_task()
# Copyright (c) 2025, pinkcity and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class EODesignDetails(Document):
	
	def db_insert(self, *args, **kwargs):
		pass

	def load_from_db(self):
		pass

	def db_update(self, *args, **kwargs):
		pass

	@staticmethod
	def get_list(args):
		pass

	@staticmethod
	def get_count(args):
		pass

	@staticmethod
	def get_stats(args):
		pass

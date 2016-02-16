# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies pvt. ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import throw, msgprint, _

class Sitemaster(Document):
	# pass

	def validate(self):
		if self.get("__islocal") :
			domain = str(self.domain)
			if domain[-13:] != "vlinkuerp.com" :
				frappe.throw(_("Damain name should be 'vlinkuerp.com', Please enter correct domain..!! "))

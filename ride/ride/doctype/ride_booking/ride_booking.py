# Copyright (c) 2024, Sahil and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self,method=None):
		price = self.price_per_km*self.estimated_km
		total_amount=0
		for item in self.services:
			total_amount+=item.amount
   
		self.total_amount=price+total_amount

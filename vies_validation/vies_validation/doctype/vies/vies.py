# Copyright (c) 2023, KAINOTOMO PH LTD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import requests
from xml.etree import ElementTree as ET

class Vies(Document):

	def validate(self):
		if self.vies:
			vat_number = self.vies
			# Create the SOAP envelope
			envelope = f"""<?xml version="1.0" encoding="UTF-8"?>
			<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
				<soapenv:Header/>
				<soapenv:Body>
					<urn:checkVat>
						<urn:countryCode>{vat_number[:2]}</urn:countryCode>
						<urn:vatNumber>{vat_number[2:]}</urn:vatNumber>
					</urn:checkVat>
				</soapenv:Body>
			</soapenv:Envelope>"""

			# Set the headers and body for the POST request
			headers = {'Content-Type': 'text/xml'}
			url = 'http://ec.europa.eu/taxation_customs/vies/services/checkVatService'

			# Make the SOAP request using frappe.request
			try:
				response = requests.post(url, headers=headers, data=envelope)
				# Check the response and parse the result
				if response.status_code == 200:
					# Extract the valid attribute from the SOAP response
					root = ET.fromstring(response.content)
					valid = root.find(".//{urn:ec.europa.eu:taxud:vies:services:checkVat:types}valid").text == "true"
					if not valid:
						# VAT number is invalid
						frappe.throw('Invalid VAT number')
				else:
					# Error occurred while validating VAT number
					frappe.throw('Error occurred while validating VAT number')
			except Exception as e:
				frappe.throw('Please try again with a valid VAT number')		

		# Save customer
		frappe.flags.ignore_permissions = True
		frappe.db.set_value("Customer", self.customer, "tax_id", self.vies)

	pass

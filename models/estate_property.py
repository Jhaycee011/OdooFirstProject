from odoo import  models, fields

class EstateProperty (models.Model):
    _name = "estate.property"
    _description = " Estate Properties"

    name = fields.Char(string='Name',required=True,align='left')
    description = fields.Text(string='Description',align='left')
    postcode = fields.Char(string='Postcode',align='left')
    date_availability = fields.Date(string='Date Availability',align='left')
    expected_price = fields.Float(string='Expected Price', required=True,align='left')
    selling_price = fields.Float(string='Selling Price',align='left')
    bedrooms = fields.Integer(string='Bedrooms',align='left')
    living_area = fields.Integer(string='Living Area',align='left')
    facades = fields.Integer(string='Facades',align='left')
    garage = fields.Boolean(string='Garage',align='left')
    garden = fields.Boolean(string='Garden',align='left')
    garden_area = fields.Integer(string='Garden Area',align='left')
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation'
    )
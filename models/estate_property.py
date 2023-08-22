from odoo import  models, fields
import datetime

class EstateProperty (models.Model):
    _name = "estate.property"
    _description = " Estate Properties"

    name = fields.Char(string='Name',required=True,align='left')
    description = fields.Text(string='Description',align='left')
    postcode = fields.Char(string='Postcode',align='left')
    date_availability = fields.Date(string='Date Availability',align='left',no_copy=True, default=lambda self: (datetime.datetime.now() + datetime.timedelta(days=90)).strftime('%Y-%m-%d'))
    expected_price = fields.Float(string='Expected Price', required=True,align='left')
    selling_price = fields.Float(string='Selling Price',align='left',readonly=True,no_copy=True)
    bedrooms = fields.Integer(string='Bedrooms',align='left',default=2)
    living_area = fields.Integer(string='Living Area',align='left')
    facades = fields.Integer(string='Facades',align='left')
    garage = fields.Boolean(string='Garage',align='left')
    garden = fields.Boolean(string='Garden',align='left')
    garden_area = fields.Integer(string='Garden Area',align='left')
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation'
    )

    active = fields.Boolean(string='Active', default=True)
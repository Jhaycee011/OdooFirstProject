from odoo import models, fields
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
    living_area = fields.Integer(string='Living Area (sqm)',align='left')
    facades = fields.Integer(string='Facades',align='left')
    garage = fields.Boolean(string='Garage',align='left')
    garden = fields.Boolean(string='Garden',align='left')
    garden_area = fields.Integer(string='Garden Area',align='left')
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string='Garden Orientation'
    )

    active = fields.Boolean(string='Active', default=True)
    active = fields.Boolean(string='Active', default=True)
    x_pool = fields.Boolean(string='Pool')
    x_sauna = fields.Boolean(string='Sauna')
    x_gym = fields.Boolean(string='Gym')
    x_laundry = fields.Boolean(string='Laundry services')

# The default in expected_price was the on that didn't update on the database.
# The variables that starts with "x_" are defined in Odoo localhost since it can't be modified/updated through this python code.
# Will get an error about those variables not existing in estate.property model but it was inputted there already

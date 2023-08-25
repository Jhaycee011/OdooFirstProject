from odoo import models, fields, api
import datetime


class EstateProperty (models.Model):
    _name = "estate.property"
    _description = " Estate Properties"

    name = fields.Char(string='Name',required=True,align='left')
    description = fields.Text(string='Description',align='left')
    postcode = fields.Char(string='Postcode',align='left')
    date_availability = fields.Date(string='Date Availability',align='left',no_copy=True, default=lambda self: (datetime.datetime.now() + datetime.timedelta(days=90)).strftime('%Y-%m-%d'))
    expected_price = fields.Float(string='Expected Price', required=True,align='left',default=2000000)
    selling_price = fields.Float(string='Selling Price',align='left',readonly=True, compute='_compute_selling_price', store=True)
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
    x_pool = fields.Boolean(string='Pool')
    x_sauna = fields.Boolean(string='Sauna')
    x_gym = fields.Boolean(string='Gym')
    x_laundry = fields.Boolean(string='Laundry services')
    restaurants = fields.Boolean(string='Restaurants')

    @api.depends('expected_price', 'living_area', 'bedrooms', 'garden', 'facades')
    def _compute_selling_price(self):
        for estate in self:
            estate.selling_price = estate.expected_price * (estate.living_area + estate.bedrooms + estate.garden + estate.facades)

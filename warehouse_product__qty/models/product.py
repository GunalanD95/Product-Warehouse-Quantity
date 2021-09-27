# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProductMasterInherit(models.Model):
    _inherit = ['product.template']


    check_qty = fields.Text("On hand: ",compute='compute_war_qty')


    def compute_war_qty(self):
        for war in self:
            string = ''
            product_id = self.env['product.product'].search([('product_tmpl_id', '=', war.id)])
            product_stock_location = self.env['stock.quant'].search([('product_id', '=', product_id[0].id),('location_id.usage','=','internal')])
            warehouse_names = []
            if product_stock_location:
                for n in product_stock_location:
                    vals = {
                    "warehouse_quantity" : n.quantity,
                    "warehouse_name" : n.location_id.location_id.name
                    }
                    warehouse_names.append(vals)               
                for s,k in enumerate(warehouse_names):
                    temp_string = ' in '.join([f'{value}' for key, value in k.items()])
                    string = string + '\n' + temp_string
            war.check_qty = string





# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Test(models.Model):
    _name = 'test.test'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()


class TestSession(models.Model):
    _name = 'test.testsession'

    name = fields.Char(required=True)
    start_date = fields.Date()
    end_date = fileds.Date()
    duration = fields.Float(digits=(((end_date - start_date), 2), help="Duration in days")
    

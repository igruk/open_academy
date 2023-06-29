import requests

from odoo import models
from odoo.exceptions import ValidationError
from odoo.fields import Date


class Currency(models.Model):
    _inherit = 'res.currency'

    def update_currency_rate(self):
        data = self._get_currency_data()
        currency_name = self.name
        currency = next((item for item in data if item['cc'] == currency_name), None)

        if currency:
            current_rate = currency['rate']
            current_date = Date.today()

            self.env['res.currency.rate'].create({
                'name': current_date,
                'currency_id': self.id,
                'inverse_company_rate': current_rate,
            })
        else:
            raise ValidationError('Currency not found.')

    @staticmethod
    def _get_currency_data():
        api_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        response = requests.get(api_url)
        return response.json()

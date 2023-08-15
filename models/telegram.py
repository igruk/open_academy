import os

import requests

from odoo import fields, models, api


class TelegramUser(models.Model):
    _name = 'open_academy.telegram_user'
    _description = 'Telegram User'

    name = fields.Char()
    chat_id = fields.Char()
    send_message = fields.Boolean()

    def get_updates(self):
        bot_token = os.environ.get('BOT_TOKEN')
        api_endpoint = f'https://api.telegram.org/bot{bot_token}/getUpdates'
        response = requests.get(api_endpoint)

        if response.status_code == 200:
            data = response.json()
            users = self.extract_user_data(data)
            self.create_telegram_users(users)
        else:
            print(f'Request failed with status code: {response.status_code}')

    @staticmethod
    def extract_user_data(data):
        users = {}
        for result in data['result']:
            chat = result['message']['chat']
            chat_id = chat['id']
            username = chat.get('username') or chat.get('first_name')
            users[chat_id] = username
        return users

    def create_telegram_users(self, users):
        user = self.env['open_academy.telegram_user']
        for chat_id, username in users.items():
            if chat_id and not user.search([('chat_id', '=', chat_id)], limit=1):
                user.create({
                    'name': username,
                    'chat_id': chat_id,
                    'send_message': True,
                })

    @api.model
    def get_chat_ids(self):
        users = self.search([])
        chat_ids = users.mapped('chat_id')
        return chat_ids

    def send_telegram_message(self, chat_id, text):
        bot_token = os.environ.get('BOT_TOKEN')
        api_endpoint = f'https://api.telegram.org/bot{bot_token}/sendMessage'

        data = {
            'chat_id': chat_id,
            'text': text
        }

        requests.post(api_endpoint, data)


# class CrmLead(models.Model):
#     _inherit = 'crm.lead'
#
#     @api.model
#     def create(self, vals):
#         lead_name = vals.get('name', '')
#         telegram_users = self.env['open_academy.telegram_user']
#         chat_ids = telegram_users.get_chat_ids()
#         text = f'New Lead Created: {lead_name}'
#
#         for user in chat_ids:
#             telegram_users.send_telegram_message(user, text)
#
#         return super(CrmLead, self).create(vals)

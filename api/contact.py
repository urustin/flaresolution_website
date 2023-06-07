from http.server import BaseHTTPRequestHandler
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_error(400, 'Invalid JSON')
            return

        if 'email' not in data:
            self.send_error(400, 'Missing "email" field')
            return

        email = data['email']

        message = Mail(
            from_email='admin@flaresolution.com',
            to_emails='admin@flaresolution.com',
            subject='Website Request',
            plain_text_content='')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            self.send_error(500, 'Error sending email')
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("success".encode())
        return

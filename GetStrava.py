#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------
# Professional Cycling - Data to Text
# ---------------------------------------
#
# GetStrava.py
# ----------------------------------------
#
from stravalib.client import Client

class GetStrava():
    def authorize(self):
        client = Client()
        authorize_url = client.authorization_url(client_id=9531,redirect_uri='http://127.0.0.1:5000/authorization')
        # Have the user click the authorization URL, a 'code' param will be added to the redirect_uri
        # .....

        # Extract the code from your webapp response
        # code = request.args.get('code') # or whatever your framework does
        # access_token = client.exchange_code_for_token(client_id=9531, client_secret='111b5017534c4bd4049f8ff941790b0762b63701', code=code)
        
        access_token = "990aa3bd5897c731ee759794edeecd7c058939de"
        # Now store that access token somewhere (a database?)
        client.access_token = access_token
        athlete = client.get_athlete()
        print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))
        athlete = client.get_athlete(227615)
        print("Hello, {}".format(athlete.firstname))
 
def main():
    f = GetStrava()
    f.authorize()

main()
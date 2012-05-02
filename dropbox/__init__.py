#!/usr/bin/env python
# encoding: utf-8
"""
dropbox/__init__.py

Created by Maximillian Dornseif on 2011-02-06.
Copyright (c) 2011 HUDORA. All rights reserved.
BSD-licensed
"""


def get_dropbox_client(consumer_key, consumer_secret, access_token):
    """Gibt ein vorkonfiguriertes Dropbox Client Object zurück.

        db_client = dropbox.get_dropbox_client(consumer_key='wj123',
                                               consumer_secret='ph123',
                                               access_token='oauth_token_secret=xe123&oauth_token=1w123')
    """
    # Lazy Import
    from dropbox import auth
    from dropbox import client
    from dropbox.libs.oauth import oauth

    dbconfig = dict(server='api.dropbox.com',
                    port=80,
                    request_token_url='https://api.dropbox.com/0/oauth/request_token',
                    access_token_url='https://api.dropbox.com/0/oauth/access_token',
                    authorization_url='https://www.dropbox.com/0/oauth/authorize',
                    trusted_access_token_url='https://api.dropbox.com/0/token',
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret)

    dba = auth.Authenticator(dbconfig)
    access_token = oauth.OAuthToken.from_string(access_token)

    # and finally make a dropbox client to work with
    db_client = client.DropboxClient('api.dropbox.com',
                 'api-content.dropbox.com', 80, dba, access_token)
    return db_client

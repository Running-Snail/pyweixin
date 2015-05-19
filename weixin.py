import binascii
import requests
import message
import hashlib
import urllib
import helper
import time
import json
import urls
import os


class Weixin(object):
    """\
        Weixin api class
    """
    SNSAPI_BASE = 'snsapi_base'
    SNSAPI_USERINFO = 'snsapi_userinfo'
    AUTH_URL = ('https://open.weixin.qq.com/connect/oauth2/authorize?'
                'appid={appid}&redirect_uri={redirect_uri}&response_type=code&'
                'scope={scope}&state={state}#wechat_redirect')

    def __init__(self, app_id='', app_secret=''):
        super(Weixin, self).__init__()
        self.appid = app_id
        self.appsecret = app_secret

    def handle_response(self, response):
        return response.json()

    @staticmethod
    def check_sign(token, data):
        """\
            when set the weixin backend url,
            weixin need to check signature
            data should be dict
            {
                'signature': '',
                'timestamp': '', (string!)
                'nonce': ''
            }
        """
        try:
            sign_list = [token, data['timestamp'], data['nonce']]
            sign_list.sort()
            print(sign_list)
            plain = ''.join(sign_list)
            sha1 = hashlib.sha1()
            sha1.update(plain)
            sign = sha1.hexdigest()
            print('encrypted {}'.format(sign))
            if sign == data['signature']:
                return True
        except KeyError:
            pass
        return False

    def retrive_access_token(self):
        """\
            retrive the access token from weixin api(not cached)
            should "NOT" use this on your own
        """
        params = {
            'grant_type': 'client_credential',
            'appid': self.appid,
            'secret': self.appsecret
        }
        r = requests.get(urls.ACCESS_TOKEN, params=params)
        return self.handle_response(r)

    def __access_token_get(self, url, access_token, params=None):
        """\
            helper to preform get request with access token
        """
        if params is None:
            params = {}
        params['access_token'] = access_token
        return requests.get(url, params=params)

    def __access_token_post(self, url, access_token, data):
        """\
            helper to preform post request with access token
        """
        params = {
            'access_token': access_token
        }
        return requests.post(url, params=params, data=data)

    def get_server_ip(self, access_token):
        """\
            get weixin servers' ip
        """
        return self.handle_response(
            self.__access_token_get(urls.SERVER_IPS, access_token)
        )

    def get_media_count(self, access_token):
        """\
            get weixin media count
        """
        return self.handle_response(
            self.__access_token_get(urls.MEDIA_COUNT, access_token)
        )

    def get_media_list(self, access_token, type, offset, count):
        """\
            get weixin media list
        """
        data = {
            'type': type,
            'offset': offset,
            'count': count
        }
        return self.handle_response(
            self.__access_token_post(
                urls.MEDIA_LIST,
                access_token,
                json.dumps(data)
            )
        )

    def get_user_info(self, access_token, open_id):
        """\
            get user info
        """
        return self.handle_response(
            self.__access_token_get(
                urls.USER_INFO,
                access_token,
                {
                    'openid': open_id
                }
            )
        )

    def create_menu(self, access_token, json_config):
        """\
            create menu
        """
        return self.handle_response(
            self.__access_token_post(
                urls.CREATE_MENU,
                access_token,
                json_config
            )
        )

    def upload_temporary_media(self, access_token, filepath, media_type):
        """\
            upload temporary media
        """
        files = {'media': open(filepath, 'rb')}
        params = {
            'access_token': access_token,
            'type': media_type
        }
        return self.handle_response(
            requests.post(
                urls.UPLOAD_TEMPORARY_MEDIA,
                params=params,
                files=files
            )
        )

    def get_temporary_media(self, access_token, media_id):
        """\
            get temporary media
        """
        params = {
            'access_token': access_token,
            'media_id': media_id
        }
        return self.handle_response(
            requests.get(
                urls.GET_TEMPORARY_MEDIA,
                params=params
            )
        )

    def parse_message(self, xml_string):
        return message.Message(helper.xml2dict(xml_string))

    @staticmethod
    def auth_page(appid, redirect_uri,
                  scope='snsapi_userinfo', state=''):
        return Weixin.AUTH_URL.format(
            appid=appid,
            redirect_uri=urllib.quote_plus(redirect_uri),
            scope=scope,
            state=state
        )

    def get_web_access_token(self, code):
        params = {
            'code': code,
            'appid': self.appid,
            'secret': self.appsecret,
            'grant_type': 'authorization_code'
        }
        return self.handle_response(
            requests.get(
                urls.GET_WEB_ACCESS_TOKEN,
                params=params
            )
        )

    def refresh_web_access_token(self, refresh_token):
        params = {
            'appid': self.appid,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
        return self.handle_response(
            requests.get(
                urls.REFRESH_WEB_ACCESS_TOKEN,
                params=params
            )
        )

    def web_get_user_info(self, access_token, openid, lang='zh_CN'):
        params = {
            'access_token': access_token,
            'openid': openid,
            'lang': lang
        }
        return self.handle_response(
            requests.get(
                urls.WEB_GET_USER_INFO,
                params=params
            )
        )

    def check_web_access_token(self, access_token, openid):
        params = {
            'access_token': access_token,
            'openid': openid
        }
        return self.handle_response(
            requests.get(
                urls.CHECK_WEB_ACCESS_TOKEN,
                params=params
            )
        )

    @staticmethod
    def is_ok(response_json):
        if response_json.get('errcode', 0) == 0:
            return True
        return False

    @staticmethod
    def genearate_jssdk_signature(url, ticket):
        info = {
            'jsapi_ticket': ticket,
            'noncestr': binascii.b2a_hex(os.urandom(16)),
            'timestamp': int(time.time()),
            'url': url
        }
        pat = ('jsapi_ticket={jsapi_ticket}&'
               'noncestr={noncestr}&'
               'timestamp={timestamp}&'
               'url={url}')
        string1 = pat.format(**info)
        print(string1)
        sha1 = hashlib.sha1()
        sha1.update(string1)
        signature = sha1.hexdigest()
        return signature, info

    def get_jssdk_ticket(self, access_token):
        params = {
            'access_token': access_token,
            'type': 'jsapi'
        }
        return self.handle_response(
            requests.get(
                urls.GET_WEIXIN_JSSDK_TICEKT,
                params=params
            )
        )

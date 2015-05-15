import requests
import message
import hashlib
import urllib
import helper
import json
import urls


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
        return r.json()

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
        return self.__access_token_get(urls.SERVER_IPS, access_token).json()

    def get_media_count(self, access_token):
        """\
            get weixin media count
        """
        return self.__access_token_get(urls.MEDIA_COUNT, access_token).json()

    def get_media_list(self, access_token, type, offset, count):
        """\
            get weixin media list
        """
        data = {
            'type': type,
            'offset': offset,
            'count': count
        }
        return self.__access_token_post(
            urls.MEDIA_LIST,
            access_token,
            json.dumps(data)
        ).json()

    def get_user_info(self, access_token, open_id):
        """\
            get user info
        """
        return self.__access_token_get(
            urls.USER_INFO,
            access_token,
            {
                'openid': open_id
            }
        ).json()

    def create_menu(self, access_token, json_config):
        """\
            create menu
        """
        return self.__access_token_post(
            urls.CREATE_MENU,
            access_token,
            json_config
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
        return requests.post(
            urls.UPLOAD_TEMPORARY_MEDIA,
            params=params,
            files=files
        ).json()

    def get_temporary_media(self, access_token, media_id):
        """\
            get temporary media
        """
        params = {
            'access_token': access_token,
            'media_id': media_id
        }
        return requests.get(
            urls.GET_TEMPORARY_MEDIA,
            params=params
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

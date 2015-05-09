import time
import xml.etree.ElementTree as ET
import helper


class Text(object):
    XML_TEMPLATE = (
        u'<xml>'
        u'<ToUserName><![CDATA[{to_user_name}]]></ToUserName>'
        u'<FromUserName><![CDATA[{from_user_name}]]></FromUserName>'
        u'<CreateTime>{create_time}</CreateTime>'
        u'<MsgType><![CDATA[text]]></MsgType>'
        u'<Content><![CDATA[{content}]]></Content>'
        u'</xml>'
    )

    @staticmethod
    def to_xml(data):
        return Text.XML_TEMPLATE.format(
            to_user_name=data['to_user_name'],
            from_user_name=data['from_user_name'],
            create_time=str(data.get('create_time', int(time.time()))),
            content=data['content']
        )


class Image(object):
    XML_TEMPLATE = (
        u'<xml>'
        u'<ToUserName><![CDATA[{to_user_name}]]></ToUserName>'
        u'<FromUserName><![CDATA[{from_user_name}]]></FromUserName>'
        u'<CreateTime>{create_time}</CreateTime>'
        u'<MsgType><![CDATA[image]]></MsgType>'
        u'<Image>'
        u'<MediaId><![CDATA[{media_id}]]></MediaId>'
        u'</Image>'
        u'</xml>'
    )

    @staticmethod
    def to_xml(data):
        return Image.XML_TEMPLATE.format(
            to_user_name=data['to_user_name'],
            from_user_name=data['from_user_name'],
            create_time=str(data.get('create_time', int(time.time()))),
            media_id=data['media_id']
        )


class Voice(object):
    XML_TEMPLATE = (
        u'<xml>'
        u'<ToUserName><![CDATA[{to_user_name}]]></ToUserName>'
        u'<FromUserName><![CDATA[{from_user_name}]]></FromUserName>'
        u'<CreateTime>{create_time}</CreateTime>'
        u'<MsgType><![CDATA[voice]]></MsgType>'
        u'<Voice>'
        u'<MediaId><![CDATA[{media_id}]]></MediaId>'
        u'</Voice>'
        u'</xml>'
    )

    @staticmethod
    def to_xml(data):
        return Voice.XML_TEMPLATE.format(
            to_user_name=data['to_user_name'],
            from_user_name=data['from_user_name'],
            create_time=str(data.get('create_time', int(time.time()))),
            media_id=data['media_id']
        )


class Video(object):
    XML_TEMPLATE = (
        u'<xml>'
        u'<ToUserName><![CDATA[{to_user_name}]]></ToUserName>'
        u'<FromUserName><![CDATA[{from_user_name}]]></FromUserName>'
        u'<CreateTime>{create_time}</CreateTime>'
        u'<MsgType><![CDATA[video]]></MsgType>'
        u'<Video>'
        u'<MediaId><![CDATA[media_id]]></MediaId>'
        u'<Title><![CDATA[{title}]]></Title>'
        u'<Description><![CDATA[{description}]]></Description>'
        u'</Video> '
        u'</xml>'
    )

    @staticmethod
    def to_xml(data):
        return Video.XML_TEMPLATE.format(
            to_user_name=data['to_user_name'],
            from_user_name=data['from_user_name'],
            create_time=str(data.get('create_time', int(time.time()))),
            media_id=data['media_id'],
            title=data['title'],
            description=data['description']
        )


class Music(object):
    XML_TEMPLATE = (
        u'<xml>'
        u'<ToUserName><![CDATA[{to_user_name}]]></ToUserName>'
        u'<FromUserName><![CDATA[{from_user_name}]]></FromUserName>'
        u'<CreateTime>{create_time}</CreateTime>'
        u'<MsgType><![CDATA[music]]></MsgType>'
        u'<Music>'
        u'<Title><![CDATA[{title}]]></Title>'
        u'<Description><![CDATA[{description}]]></Description>'
        u'<MusicUrl><![CDATA[{music_url}]]></MusicUrl>'
        u'<HQMusicUrl><![CDATA[{hq_music_url}]]></HQMusicUrl>'
        u'<ThumbMediaId><![CDATA[{media_id}]]></ThumbMediaId>'
        u'</Music>'
        u'</xml>'
    )

    @staticmethod
    def to_xml(data):
        return Music.XML_TEMPLATE.format(
            to_user_name=data['to_user_name'],
            from_user_name=data['from_user_name'],
            create_time=str(data.get('create_time', int(time.time()))),
            media_id=data['media_id'],
            title=data['title'],
            description=data['description'],
            music_url=data['music_url'],
            hq_music_url=data['hq_music_url']
        )


class News(object):
    XML_TEMPLATE = (
        u'<xml>'
        u'<ToUserName><![CDATA[{to_user_name}]]></ToUserName>'
        u'<FromUserName><![CDATA[{from_user_name}]]></FromUserName>'
        u'<CreateTime>{create_time}</CreateTime>'
        u'<MsgType><![CDATA[news]]></MsgType>'
        u'<ArticleCount>{article_count}</ArticleCount>'
        u'<Articles>'
        u'{articles}'
        u'</Articles>'
        u'</xml>'
    )

    ARTICLE_ITEM_XML_TEMPLATE = (
        u'<item>'
        u'<Title><![CDATA[{title}]]></Title>'
        u'<Description><![CDATA[{description}]]></Description>'
        u'<PicUrl><![CDATA[{picurl}]]></PicUrl>'
        u'<Url><![CDATA[{url}]]></Url>'
        u'</item>'
    )

    @staticmethod
    def to_xml(data):
        articles = ''
        for a in data['articles']:
            articles += News.ARTICLE_ITEM_XML_TEMPLATE.format(
                title=a['title'],
                description=a['description'],
                picurl=a['picurl'],
                url=a['url']
            )
        article_count = len(data['articles'])
        return News.XML_TEMPLATE.format(
            to_user_name=data['to_user_name'],
            from_user_name=data['from_user_name'],
            create_time=str(data.get('create_time', int(time.time()))),
            article_count=article_count,
            articles=articles
        )

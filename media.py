import time


class Media(object):
    @staticmethod
    def __str_create_time(create_time=None):
        if create_time is None:
            create_time = int(time.time())
        return str(create_time)


class Text(Media):
    XML_TEMPLATE = (
        u'<xml>'
        u'<ToUserName><![CDATA[{to_user_name}]]></ToUserName>'
        u'<FromUserName><![CDATA[{from_user_name}]]></FromUserName>'
        u'<CreateTime>{create_time}</CreateTime>'
        u'<MsgType><![CDATA[text]]></MsgType>'
        u'<Content><![CDATA[{content}]]></Content>'
        u'</xml>'
    )

    def __init__(self, content, create_time=None):
        self.content = content
        self.create_time = Media.__str_create_time(create_time)

    def to_xml(self, to_user_name, from_user_name):
        return Text.XML_TEMPLATE.format(
            to_user_name=to_user_name,
            from_user_name=from_user_name,
            create_time=self.create_time,
            content=self.content
        )


class Image(Media):
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

    def __init__(self, media_id, create_time=None):
        self.media_id = media_id
        self.create_time = Media.__str_create_time(create_time)

    def to_xml(self, to_user_name, from_user_name):
        return Image.XML_TEMPLATE.format(
            to_user_name=to_user_name,
            from_user_name=from_user_name,
            create_time=self.create_time,
            media_id=self.media_id
        )


class Voice(Media):
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

    def __init__(self, media_id, create_time=None):
        self.media_id = media_id
        self.create_time = Media.__str_create_time(create_time)

    def to_xml(self, to_user_name, from_user_name):
        return Voice.XML_TEMPLATE.format(
            to_user_name=to_user_name,
            from_user_name=from_user_name,
            create_time=self.create_time,
            media_id=self.media_id
        )


class Video(Media):
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

    def __init__(self, media_id, title, description, create_time=None):
        self.media_id = media_id
        self.title = title
        self.description = description
        self.create_time = Media.__str_create_time(create_time)

    def to_xml(self, to_user_name, from_user_name):
        return Video.XML_TEMPLATE.format(
            to_user_name=to_user_name,
            from_user_name=from_user_name,
            create_time=self.create_time,
            media_id=self.media_id,
            title=self.title,
            description=self.description
        )


class Music(Media):
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

    def __init__(self, media_id, title, description,
                 music_url, hq_music_url, create_time=None):
        self.media_id = media_id
        self.title = title
        self.description = description
        self.music_url = music_url
        self.hq_music_url = hq_music_url
        self.create_time = Media.__str_create_time(create_time)

    def to_xml(self, to_user_name, from_user_name):
        return Music.XML_TEMPLATE.format(
            to_user_name=to_user_name,
            from_user_name=from_user_name,
            create_time=self.create_time,
            media_id=self.media_id,
            title=self.title,
            description=self.description,
            music_url=self.music_url,
            hq_music_url=self.hq_music_url
        )


class News(Media):
    XML_TEMPLATE = (
        u'<item>'
        u'<Title><![CDATA[{title}]]></Title>'
        u'<Description><![CDATA[{description}]]></Description>'
        u'<PicUrl><![CDATA[{picurl}]]></PicUrl>'
        u'<Url><![CDATA[{url}]]></Url>'
        u'</item>'
    )

    def __init__(self, title, description, picurl, url):
        self.title = title
        self.description = description
        self.picurl = picurl
        self.url = url

    def to_xml(self):
        return News.XML_TEMPLATE.format(
            title=self.title,
            description=self.description,
            picurl=self.picurl,
            url=self.url
        )


class NewsSet(Media):
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

    def __init__(self, articles, create_time=None):
        self.articles = articles
        self.create_time = Media.__str_create_time(create_time)

    def to_xml(self, to_user_name, from_user_name):
        articles = ''
        for a in self.articles:
            articles += a.to_xml()
        article_count = len(self.articles)
        return News.XML_TEMPLATE.format(
            to_user_name=to_user_name,
            from_user_name=from_user_name,
            create_time=self.create_time,
            article_count=article_count,
            articles=articles
        )

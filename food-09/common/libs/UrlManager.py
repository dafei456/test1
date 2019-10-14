import time


class UrlManager(object):

    @staticmethod
    def build_url(path):
        return path

    @staticmethod
    def build_static_url(path):
        version = "%s" % (int(time.time()))
        path = "/static" + path + "?v=" + version
        return UrlManager.build_url(path)

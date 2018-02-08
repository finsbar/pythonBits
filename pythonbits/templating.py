# -*- coding: utf-8 -*-
from functools import partial


def tag(tag_name):
    def func(value=None):
        if value:
            return "[" + tag_name + "=" + unicode(value) + "]"
        return "[" + tag_name + "]"
    return func


def tag_enc(tag_name):
    return lambda ev, tv=None: (tag(tag_name)(tv) + unicode(ev) +
                                tag('/' + tag_name)())


img = tag('img')
b = tag_enc('b')
link = tag_enc('url')
size = tag_enc('size')
quote = tag_enc('quote')
spoiler = tag_enc('spoiler')
mi = tag_enc('mediainfo')
s1 = partial(size, tv=1)
s2 = partial(size, tv=2)  # default
s3 = partial(size, tv=3)
s4 = partial(size, tv=4)
s7 = partial(size, tv=7)
align = tag_enc('align')
center = partial(align, tv='center')
_list = tag_enc('list')


def list(x, style=None):
    v = "".join("[*]"+x for x in x)
    return _list(v, style)


def h(x):
    s = ""
    for c in x:
        if c.isupper():
            s += s3(c)
        else:
            s += c.upper()
    return b(s)


def section(name, content):
    return center(h(name)) + quote(content)

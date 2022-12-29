# -*- coding:utf-8 -*-
# AUTHOR: SUN
from function import replace, sequence, subtitle, suffix

functions = {
    '增删': replace.main,
    '按序': sequence.main,
    '后缀': suffix.main,
    '字幕': subtitle.main
}

config_init = {
    'replace': {
        'replace': {
            'key': '',
            'to': '',
            're': ''
        },

        'delete': {
            'key': '',
            're': ''
        }
    },

    'sequence': {
        'range': 0,
        'sequence': 0,
        'type': 0,
        'words': ''
    },

    'suffix': {
        'key': '',
        'to': ''
    },

    'subtitle': {
        'video': '.mp4|.mkv|.avi|.webm',
        'subtitle': '.ass|.srt|.smi|.ssa|.sub|.idx',
        'way': 0
    }
}

if __name__ == '__main__':
    pass

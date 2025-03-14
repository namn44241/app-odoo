# -*- coding: utf-8 -*-

# Created on 2023-10-06
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# Copyright (C) 2009~2024 odooAi.cn

# Odoo16在线用户手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/index.html

# Odoo16在线开发者手册（长期更新）
# https://www.odooai.cn/documentation/16.0/zh_CN/developer.html

# 行业应用说明，应该是带 Industry 的就会放入

##############################################################################
#    Copyright (C) 2009-TODAY odooAi.cn Ltd. https://www.odooai.cn
#    Author: Ivan Deng，300883@qq.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': 'odooapp.cn SaaS Client.Odoo中文应用商店SaaS云服务客户端',
    'version': '16.24.11.08',
    'author': 'odooai.cn',
    'category': 'Base',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'OPL-1',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'summary': '''
    Odoo中文云服务客户端，模块持续更新中。
    支持Odoo中文版在线更新及 www.odooapp.cn 的信息推送等。
    安装即代表同意我司云服务用户协议及隐私政策。 https://www.odooapp.cn/conditions
    ''',
    'description': '''
    1. 快速访问Odoo中文应用商店并获取独享Odoo中文通行码
    2. 一键获取最新应用信息，最新行业服务包
    3. 一键获取Odoo中文翻译更新
    4. 快速获取Odoo服务，Odoo升级评估
    11.多语言支持，多公司支持
    12.仅从Odoo18企业版，社区版版本开始支持
    13.代码完全开源
    ''',
    'depends': [
        'app_common',
        # 'website',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'app_/static/src/scss/style.scss',
        ],
        'web.assets_backend': [
            # 'app_/static/src/js/*.js',
        ],
    },
    'demo': [
        # 'data/model_new_demo.xml',
        # 'views/website_templates.xml',
    ],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}

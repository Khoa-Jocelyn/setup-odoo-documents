{
    'name': "Libarary Management",
    'name_vi_VN': "Quản lý thư viện",
    'summary': """Libarary Management Software""",
    'summary_vi_VN': """Phần mềm quản lý thư viện""",
    'sequence': -100,
    'description': """Libarary Management Software""",
    'description_vi_VN': """Phần mềm quản lý thư viện""",
    'author': "Viindoo",
    'website': "https://viindoo.com",
    'support': "apps.support@viindoo.com",
    'category': 'Productivity',
    'version': '1.0',
    'depends': [
        'base'
    ],
    'data': [
        "security/library_management_security.xml",
        "security/ir.model.access.csv",
        "views/book_views.xml",
        "views/author_views.xml",
        "views/category_views.xml",
        "views/producer_views.xml",
    ],
    'demo' : [],
    'images' : [
        'static/description/icon.png'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'LGPL-3',
}

{
    "name": "Web Company Color",
    "category": "web",
    "version": "13.0.0.0.1",
    "author": "IDT",
    'website': 'http://www.infinitedt.com',
    "depends": ["web", "base_sparse_field"],
    "data": [
        "view/assets.xml",
        "view/res_company.xml",
        "view/theme.xml",
    ],
    "uninstall_hook": "uninstall_hook",
    "post_init_hook": "post_init_hook",
    "license": "AGPL-3",
    "auto_install": False,
    "installable": True,
}

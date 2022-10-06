{
    'name': 'OdooCMS Academic',
    'version': '13.0.1.0.6',
    'summary': """Academic Module for UMS""",
    'description': 'Academic Module of Educational Institutes (University Level)',
    'category': 'OdooCMS',
    'sequence': 2,
    'author': 'GlobalXS',
    'company': 'GlobalXS Technology Solutions',
    'website': "https://www.globalxs.co",
    'depends': ['odoocms_registration','odoocms'],
    'data': [
        'security/odoocms_academic_security.xml',
        'security/ir.model.access.csv',

        'data/data.xml',
        'data/sequence.xml',

        'views/odoocms_academic_menu.xml',
        'views/res_config_setting_view.xml',
        'views/view_assessment.xml',
        'views/class_view.xml',
        'views/grades_view.xml',
        'views/inherited_views.xml',
        'views/disposal_charge_view.xml',

        'views/dbs_view.xml',
        'views/fbs_view.xml',

        'wizard/assessment_export_view.xml',
        'wizard/assessment_import_view.xml',
        'wizard/assign_grades_view.xml',
        'wizard/confirm_classes_wiz_view.xml',
        'wizard/approve_dbs_view.xml',
        'wizard/student_curriculum_batches_wizard.xml',

        'reports/reports.xml',
        'reports/student_curriculum_batches_report.xml',

    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}

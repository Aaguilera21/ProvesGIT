{
        "name" : "school_category",
        "version" : "5.T13",
        "author" : "Isidre Guixà",
        "category" : "Unknown",
        "description": """
          Curs 15-16 - DAM2 - M10 - UF2 - T13
        """,
        "depends" : ['base','school'],
        "init_xml" : [ ],
        "demo_xml" : [],
        "update_xml" : ['school_category_view.xml','security/school_category_security.xml','security/ir.model.access.csv',
						'report/school_category_reports.xml','school_category_dashboard_view.xml'],
        "installable": True
}
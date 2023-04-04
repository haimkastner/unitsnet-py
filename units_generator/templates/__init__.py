

# Load jinja template for the python unit class
unit_class_template = ""
with open("units_generator/templates/unit_template.jinja2", "r", encoding="utf-8") as f:
    unit_class_template = f.read()
    
    
export_classes_template = ""
with open("units_generator/templates/export_template.jinja2", "r", encoding="utf-8") as f:
    export_classes_template = f.read()
    

readme_template = ""
with open("units_generator/templates/readme_template.jinja2", "r", encoding="utf-8") as f:
    readme_template = f.read()


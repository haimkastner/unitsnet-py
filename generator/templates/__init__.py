

# Load jinja template for the python unit class
unit_class_template = ""
with open("generator/templates/unit_template.jinja2", "r") as f:
    unit_class_template = f.read()
    
    
export_classes_template = ""
with open("generator/templates/export_template.jinja2", "r") as f:
    export_classes_template = f.read()
    

readme_template = ""
with open("generator/templates/readme_template.jinja2", "r") as f:
    readme_template = f.read()


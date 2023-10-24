import os
import shutil


jwt = "{{cookiecutter.use_jwt}}"
project_slug = "{{cookiecutter.project_slug}}"

def delete_resource(resource):
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


if jwt == "n":
    delete_resource(f"{project_slug}/authentication/")
    delete_resource(f"{project_slug}/users/")

def fix_line_endings(file_name):
    sh_file = os.path.join('docker/', file_name)

    with open(sh_file, 'r') as file:
        script_contents = file.read()

    with open(sh_file, 'w', newline='\n') as file:
        file.write(script_contents)

fix_line_endings("production_web_entrypoint.sh")
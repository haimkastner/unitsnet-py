from .utils import get_json_from_cdn, read_json_file, write_json_file
    
def get_definitions(repo_owner_and_name):
    directory_url = f"https://api.github.com/repos/{repo_owner_and_name}/contents/Common/UnitDefinitions"
    files_url = f"https://raw.githubusercontent.com/{repo_owner_and_name}/master/Common/UnitDefinitions"

    directory_files = read_json_file('files.json')
    if not directory_files:
        print("[get_definitions] Fetching units files list...")
        directory_files = get_json_from_cdn(directory_url)
        write_json_file('files.json', directory_files)

    print("[get_definitions] Fetching units definitions...")

    definitions = []
    for file in directory_files:
        name = file.get("name")
        definition = read_json_file(name)
        if not definition:
            definition = get_json_from_cdn(f"{files_url}/{name}")
            write_json_file(name, definition)

        for unit in definition["Units"]:
            mark_as_deprecated = False
            unit_name = unit.get("Name")
            plural_name = unit.get("PluralName")
            obsolete_text = unit.get("ObsoleteText")
            if obsolete_text:
                print(
                    f'[get_definitions] Unit {unit_name}.{plural_name} marked as obsolete, message: "{obsolete_text}"'
                )
                mark_as_deprecated = True

            if unit.get("SkipConversionGeneration"):
                print(
                    f"[get_definitions] Unit {unit_name}.{plural_name} marked to be ignored"
                )
                mark_as_deprecated = True

            unit["Deprecated"] = mark_as_deprecated

        definitions.append(definition)

        print(f"[get_definitions] Unit {name} successfully fetched")

    print("[get_definitions] Fetching units definitions finished successfully")

    return definitions

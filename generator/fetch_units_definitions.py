import requests
import json


def __get_json_from_cdn(cdn_url):
    try:
        response = requests.get(
            cdn_url, headers={"user-agent": "PostmanRuntime/7.20.1"}
        )
        response.raise_for_status()
        # Skip utf-8 BOM char.
        cleaned_text = response.text.lstrip('\ufeff')
        json_data = json.loads(cleaned_text)
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve JSON from cdn: {e}")


def get_definitions(repo_owner_and_name):
    directory_url = f"https://api.github.com/repos/{repo_owner_and_name}/contents/Common/UnitDefinitions"
    files_url = f"https://raw.githubusercontent.com/{repo_owner_and_name}/master/Common/UnitDefinitions"

    print("Fetching units files list...")
    # directory_files = [{ 'name': 'Volume.json'}]
                        
    directory_files = __get_json_from_cdn(directory_url)
    
    definitions = []
    for file in directory_files:
        name = file.get('name')
        definition = __get_json_from_cdn(f'{files_url}/{name}')
        
        for unit in definition['Units']:
            markAsDeprecated = False
            pluralName = unit.get('PluralName')
            obsoleteText = unit.get('ObsoleteText')
            if obsoleteText:
                print(f'[get_definitions] Unit {name}.{pluralName} marked as obsolete, message: "{obsoleteText}"')
                markAsDeprecated = True
            
            if unit.get('SkipConversionGeneration'):
                print(f'[get_definitions] Unit {name}.{pluralName} marked to be ignored')
                markAsDeprecated = True
            
            unit['Deprecated'] = markAsDeprecated
            
        definitions.append(definition)
        
        print(f'[get_definitions] Unit {name}.{pluralName} successfully fetched')
    
    return definitions
        
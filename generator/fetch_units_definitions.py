
from utils import get_json_from_cdn

def get_definitions(repo_owner_and_name):
    directory_url = f"https://api.github.com/repos/{repo_owner_and_name}/contents/Common/UnitDefinitions"
    files_url = f"https://raw.githubusercontent.com/{repo_owner_and_name}/master/Common/UnitDefinitions"

    print("Fetching units files list...")
    # directory_files = [{ 'name': 'Length.json'}]
                        
    directory_files = get_json_from_cdn(directory_url)
    
    definitions = []
    for file in directory_files:
        name = file.get('name')
        definition = get_json_from_cdn(f'{files_url}/{name}')
        
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
        
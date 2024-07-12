import sys

# Function to parse version string to major, minor, patch
def parse_version(version):
    major, minor, patch = map(int, version.split('.'))
    return {'major': major, 'minor': minor, 'patch': patch}

# Function to increment the version
def increment_version(current_version, definition_version, current_definition_version):
    current = parse_version(current_version)
    definition = parse_version(definition_version)
    current_definition = parse_version(current_definition_version)

    if current_definition['major'] > definition['major']:
        # Increment major version
        return f"{current['major'] + 1}.0.0"
    else:
        # Increment patch version
        return f"{current['major']}.{current['minor']}.{current['patch'] + 1}"

# Get the current version from command line arguments
if len(sys.argv) < 4:
    print('Please provide the current version, definition version, and current definition version as arguments.')
    sys.exit(1)

current_version, definition_version, current_definition_version = sys.argv[1:4]

new_version = increment_version(current_version, definition_version, current_definition_version)
print(new_version)

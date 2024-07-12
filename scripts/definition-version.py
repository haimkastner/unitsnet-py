import requests
import xml.etree.ElementTree as ET

url = 'https://raw.githubusercontent.com/angularsen/UnitsNet/master/UnitsNet/UnitsNet.csproj'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    xml = response.text
    root = ET.fromstring(xml)

    # Assuming the structure of the XML is consistent with the example
    version = root.find('.//PropertyGroup/Version').text
    print(version)

except requests.exceptions.RequestException as e:
    print('Error fetching the URL:', e)
except ET.ParseError as e:
    print('Error parsing XML:', e)
except Exception as e:
    print('Error:', e)

import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

package_json = os.path.join(__location__, 'version.json')

with open(package_json) as json_file:
    data = json.load(json_file)

    __version__ = data.get('version')
    __version_info__ = tuple([
        int(num) if num.isdigit() else num
        for num in __version__.replace('-', '.', 1).split('.')
    ])

    json_file.close()

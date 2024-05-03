import os
import shutil

import toml


def change_prop(name, key, value):
    print(name)

    file_path = f'{name}.toml'
    data = toml.load(file_path)
    if data['torrent_title_rule'] == data['torrent_subtitle_rule']:
        data[key] = value
    # for attr, value in data.items():
    #     data[attr] = True

    with open(file_path, 'w') as toml_file:
        toml.dump(data, toml_file)


def merge_toml(name):
    source_data = toml.load(f'{name}.toml')
    level_data = toml.load(f'./rules/{name}.toml')
    source_data.update(level_data)
    with open(f'{name}.toml', 'w') as toml_file:
        toml.dump(source_data, toml_file)
        shutil.move(f'./rules/{name}.toml', f'./rules/completed/{name}.toml')


def replace_site_url(name):
    source_data = toml.load(f'{name}.toml')
    logo = source_data.get('logo')
    urls = source_data.get('url')
    for url in urls:
        if url.startswith('http'):
            logo = logo.replace(url, '')
    source_data['logo'] = logo
    with open(f'{site}.toml', 'w') as toml_file:
        toml.dump(source_data, toml_file)


if __name__ == '__main__':
    toml_files = [file.replace('.toml', '') for file in os.listdir('.') if
                  file.endswith('.toml')]
    key = 'torrent_title_rule'
    value = ".//td/a[contains(@href,'detail')]/b/text()[last()]"
    for site in toml_files:
        change_prop(site, key, value)

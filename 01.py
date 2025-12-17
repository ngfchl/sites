import os

import toml


def h():
    for i in os.listdir():
        if i.endswith('.toml'):
            d = toml.load(i)
            # if d['logo'].startswith('http'):
            #     print(d['name'])
            # d["nation"] = "china"  # HDCity Filelist Discuz Avistaz NexusPHP UNIT3D GazellePW NYPT iPt HDSpace MTorrent
            # if '条记录' not in d['my_publish_rule']:
            #     d['my_publish_rule'] = "//div[contains(., '条记录')]/b[1]/text()"
            d['page_search'] = [d['page_search']]
            with open(i, "w") as f:
                toml.dump(d, f)


if __name__ == '__main__':
    h()

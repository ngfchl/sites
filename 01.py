import os

import toml


def h():
    for i in os.listdir():
        if i.endswith('.toml'):
            d = toml.load(i)
            # if d['logo'].startswith('http'):
            #     print(d['name'])
            # d["nation"] = "china"  # HDCity Filelist Discuz Avistaz NexusPHP UNIT3D GazellePW NYPT iPt HDSpace MTorrent
            d['my_email_rule'] = "//td[contains(text(),'邮箱')]/following-sibling::td[1]//text()"
            d[
                'my_username_rule'] = "//table[@id='info_block']//span/a[contains(@class,'_Name') and contains(@href,'userdetails.php?id=')]/b/text()"
            d['buy_page'] = "mybonus.php?action=exchange"
            d['buy_action'] = {
                "100GB上传流量": "3",
                "100GB下载流量": "5",
                "1个邀请名额": "6",
                "1个临时邀请名额": "7",
                "贵宾待遇": "9",
            }
            with open(i, "w") as f:
                toml.dump(d, f)


if __name__ == '__main__':
    h()

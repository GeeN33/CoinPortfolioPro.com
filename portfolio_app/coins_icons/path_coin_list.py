import json
import os
from core.settings import BASE_DIR
from portfolio_app.models import CoinIcon
from pathlib import Path

dir_pathT = 'portfolio_app/coins_icons/coins_icons_list.json'

dir_path = os.path.join(BASE_DIR, dir_pathT)

def loading_To_icons():
    list_symbol=[]
    with open(dir_path, 'r') as f:
        data = json.loads(f.read())
        try:
            list_symbol = data
        except Exception as e:
            print(e)

    for symbol in list_symbol:
        print(symbol)
        if '.png' in symbol:
            name = symbol.replace('.png', '')
            path = '/media/coins_icons/'+symbol
            CoinIcon.objects.filter(path=path).update(name=name)

from django.shortcuts import render
from airtable import Airtable




def index(request):
    airtable = Airtable('appdqzfZoeTcXC7VD', 'CONFIG', api_key='keyGud53GenTwK01X')
    db_items = airtable.get_all(formula="AND({LIVE}=1, NOT({ACTIONS}=''))")

    main_menus = []
    for item in db_items:
        if item["fields"]["MainMenu"] not in main_menus:
            main_menus.append(item["fields"]["MainMenu"])

    context = {'db_items': db_items, 'main_menus': main_menus}
    return render(request, 'polls/index.html', context)
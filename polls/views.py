from django.shortcuts import render
from airtable import Airtable




def index(request):
    airtable = Airtable('appdqzfZoeTcXC7VD', 'CONFIG', api_key='keyGud53GenTwK01X')
    db_data = airtable.get_all(formula="AND({LIVE}=1, NOT({ACTIONS}=''))")
    print("Hello")
    menus = {}
    for menu in db_data:
        menu_name = menu["fields"]["MainMenu"]
        if menu_name not in menus.keys():
            menus[menu_name] = {}

            for sub_menu in db_data:
                if "Sub-menu" in sub_menu["fields"]:
                    sub_menu_name = sub_menu["fields"]["Sub-menu"]
                    if sub_menu["fields"]["MainMenu"] == menu_name and sub_menu_name not in menus[menu_name].keys():
                        menus[menu_name][sub_menu_name] = {}

                        for item in db_data:
                            if item["fields"]["MainMenu"] == menu_name and item["fields"]["Sub-menu"] == sub_menu_name:
                                url = item["fields"]["URL"]
                                url_name = item["fields"]["Actions"]

                                menus[menu_name][sub_menu_name]['url'] = url
                                menus[menu_name][sub_menu_name]['url_name'] = url_name
                    else:
                        for item in db_data:
                            if item["fields"]["MainMenu"] == menu_name:
                                url = item["fields"]["URL"]
                                url_name = item["fields"]["Actions"]

                                menus[menu_name]['url'] = url
                                menus[menu_name]['url_name'] = url_name

    context = {'menus': menus}
    return render(request, 'polls/index.html', context)

    # def index(request):
    # airtable = Airtable('appdqzfZoeTcXC7VD', 'CONFIG', api_key='keyGud53GenTwK01X')
    # db_data = airtable.get_all(formula="AND({LIVE}=1, NOT({ACTIONS}=''))")
    #
    # menus = []
    # for menu in db_data:
    #     menu_name = menu["fields"]["MainMenu"]
    #     if menu_name not in menus:
    #         menus[menu_name] = []
    #
    #         for sub_menu in db_data:
    #             sub_menu_name = sub_menu["fields"]["Sub-menu"]
    #             if sub_menu_name not in menus[menu_name] and sub_menu["fields"]["MainMenu"] == menu_name:
    #                 menus[menu_name][sub_menu_name] = {}
    #
    #                 for item in db_data:
    #                     url = item["fields"]["URL"]
    #                     url_name = item["fields"]["Actions"]
    #
    #                     menus[menu_name][sub_menu_name]['url'] = url
    #                     menus[menu_name][sub_menu_name]['url_name'] = url_name
    #
    # context = {'menus': menus}
    # return render(request, 'polls/index.html', context)
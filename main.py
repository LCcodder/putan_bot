import vk_api

from cfg import token


# token must be your uploaded token
session = vk_api.VkApi(token=token)
vk = session.get_api()

my_id = 513544698



cur_id = input('potential putan id: ~ ' )




def su_us(id):

    putan_rating = 0
    selected_user = session.method('users.get', {'user_id': id})
    selected_user_groups = session.method('groups.get', {'user_id': id})
    selected_user_friends = session.method('friends.get', {'user_id': id})
    putan_groups = [190923816, 73247559, 125327221, 178062416, 91050183, 161276195, 150980704, 168313675, 87800684, 53562980, 96834311, 191645367]
    putan_groups_music = [114454317, 76136416, 163226140, 182863061, 134965725, 41734504, 94657756, 19522161, 23482802, 184730616]
    putan_status_dates = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    putan_status_key_words = ['~', '"', "'", '-', '.', ',']
    putan_name_key_words = ["'"]
    putan_last_name_variations = ['мирная', "митинская", "забивная", "холодная", ]
    putan_status = ["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]

    selected_user_main_info = session.method('account.getInfo', {'user_id': id})
    selected_user_status = session.method('status.get', {'user_id': id})
    options = 0
    girls_as = ['а', "a", "я"]

    for selected_user_info_unhashed in selected_user:

        last_name = selected_user_info_unhashed['last_name']
        first_name = selected_user_info_unhashed['first_name']
        if last_name[-1] not in girls_as:
            print("sex: Male ----- result will be irrelevant*")






        if last_name.lower() in putan_last_name_variations:
            putan_rating = putan_rating + 0.96
            options = options + 1
        for l_n_test in last_name:

            if l_n_test in putan_name_key_words:
                putan_rating = putan_rating + 0.84
                options = options + 1
 

    if selected_user_main_info['no_wall_replies'] == 1:
        putan_rating = putan_rating + 1.2
        options = options + 1



    for selected_user_status_s in selected_user_status['text']:
        selected_user_status_symbols = len(selected_user_status_s)
        if len(selected_user_status['text']) >= 5:
            putan_rating = putan_rating + 0.004
            options = options + 1
        if 15 > len(selected_user_status['text']) >= 10:
            putan_rating = putan_rating + 0.004
            options = options + 1
        if 20 > len(selected_user_status['text']) >= 15:
            putan_rating = putan_rating + 0.004
            options = options + 1
        if len(selected_user_status['text']) >= 20:
            putan_rating = putan_rating + 0.004
            options = options + 1
        if selected_user_status_s in putan_status:

            if selected_user_status_symbols == 1 or 2:
                putan_rating = putan_rating + 0.76
                options = options + 1
            if selected_user_status_symbols >= 3:
                putan_rating = putan_rating + 0.94
                options = options + 1
        if selected_user_status_s in putan_status_dates:
            if selected_user_status_symbols > 1:
                putan_rating = putan_rating + 0.78
                options = options + 1
        if selected_user_status_s in putan_status_key_words:

            if selected_user_status_symbols == 1 or 2:
                putan_rating = putan_rating + 0.32
                options = options + 1

            if 2 < selected_user_status_symbols <= 4:
                putan_rating = putan_rating + 0.56
                options = options + 1


    if 100 >= len(selected_user_friends['items']) > 50:
        putan_rating = putan_rating + 0.64
        options = options + 1

    if 150 >= len(selected_user_friends['items']) > 100:

        putan_rating = putan_rating + 1.12
        options = options + 1

    if 200 >= len(selected_user_friends['items']) > 150:

        putan_rating = putan_rating + 1.08
        options = options + 1
    if 300 >= len(selected_user_friends['items']) > 200:

        putan_rating = putan_rating + 1.45
        options = options + 1
    if 400 >= len(selected_user_friends['items']) > 300:

        putan_rating = putan_rating + 1.95
        options = options + 1
    if 500 >= len(selected_user_friends['items']) > 400:

        putan_rating = putan_rating + 2.45
        options = options + 1
    if 500 < len(selected_user_friends['items']):

        putan_rating = putan_rating + 2.85
        options = options + 1



    for unhashed_selected_user_groups in selected_user_groups['items']:


        if unhashed_selected_user_groups in putan_groups:
            if 1 < len(selected_user_groups['items']) <= 3:
                putan_rating = putan_rating + 0.65
                options = options + 1
            if 3 < len(selected_user_groups['items']) <= 6:
                putan_rating = putan_rating + 0.97
                options = options + 1
            if len(selected_user_groups['items']) > 6:
                putan_rating = putan_rating + 1.13
                options = options + 1

        if unhashed_selected_user_groups in putan_groups_music:
            if 1 < len(selected_user_groups['items']) <= 4:
                putan_rating = putan_rating + 0.7
                options = options + 1
            if len(selected_user_groups['items']) > 4:
                putan_rating = putan_rating + 1.01
                options = options + 1


    for selected_user_stats in selected_user:
        if selected_user_stats['is_closed'] == True:
            putan_rating = putan_rating + 1.09
            options = options + 1


    if putan_rating > 10:
        putan_rating = putan_rating - putan_rating / 100 * 20

    print('.\n.\n.\n' + str(round(putan_rating * 10, 1)) + '% ----- normal putan value ~ 27%-51% \nvalidated options: ' + str(options) + ' out of 25 сircuits')



su_us(cur_id)
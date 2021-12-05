import vk_api
import time
from cfg import token


# vk_session = vk_api.VkApi('+79256167868', 'robocopid12')
# vk_session.auth()
#
# vk = vk_session.get_api()
#
# print(vk.wall.post(message='Hello world!'))
session = vk_api.VkApi(token=token)
vk = session.get_api()

my_id = 513544698

# u = input('ты кто: ')
#
# selected_friend = input('айди друга: ')

# command = input('список комманд: \t поставить динамический статус(видно только на пк) - "set_dynamic_status" \t сканер друзей на наличие шлюх  - "friend_putan_scan" \t сканер пользователя на шлюховатость - "user_putan_scan" \t ')



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
    #     if last_name[-1] not in girls_as:
    #         print("sex: Male ------ putan can't be rated")
    #     else:

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
        # putan_rating = putan_rating - 0.6
        putan_rating = putan_rating + 1.12
        options = options + 1

    if 200 >= len(selected_user_friends['items']) > 150:
        # putan_rating = putan_rating - 1
        putan_rating = putan_rating + 1.08
        options = options + 1
    if 300 >= len(selected_user_friends['items']) > 200:
        # putan_rating = putan_rating - 1.2
        putan_rating = putan_rating + 1.45
        options = options + 1
    if 400 >= len(selected_user_friends['items']) > 300:
        # putan_rating = putan_rating - 1.2
        putan_rating = putan_rating + 1.95
        options = options + 1
    if 500 >= len(selected_user_friends['items']) > 400:
        # putan_rating = putan_rating - 1.2
        putan_rating = putan_rating + 2.45
        options = options + 1
    if 500 < len(selected_user_friends['items']):
        # putan_rating = putan_rating - 1.2
        putan_rating = putan_rating + 2.85
        options = options + 1



    for unhashed_selected_user_groups in selected_user_groups['items']:

        # [unhashed_selected_user_groups in selected_user_groups['items'] for unhashed_selected_user_groups in putan_groups
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
    # else:
    print('.\n.\n.\n' + str(round(putan_rating * 10, 1)) + '% ----- normal putan value ~ 27%-51% \nvalidated options: ' + str(options) + ' out of 25 сircuits')







def fr_list(user_id):



    friends = session.method('friends.get', {'user_id': user_id})
    girls_as = ['а', "a", "я"]
    # online_friends = session.method('friends.getOnline', {'user_id': user_id})
    #
    # for online_friend in online_friends:
    #     online_friend_info = session.method('friends.get', {'user_id': online_friend})
    #     for each_online_friend_info in online_friend_info['items']:
    #         online_friend_info_unhashed = session.method('users.get', {'user_ids': each_online_friend_info})
    #
    #         for each_online_friend_info_unhashed in online_friend_info_unhashed:
    #             last_name = each_online_friend_info_unhashed['last_name']
    #             first_name = each_online_friend_info_unhashed['first_name']
    #             for last_name_a in last_name[-1]:
    #                 print(each_online_friend_info_unhashed)
    #                 if each_online_friend_info_unhashed['is_closed'] == True:
    #                     if last_name_a not in girls_as:
    #                         print(last_name + ' ' + first_name + ' -пидорок')
    #
    #                     else:
    #                         print(last_name + " " + first_name + ' -шлюха')
    #
    #                 else:
    #                     print('error')

    for friend in friends['items']:

        each_friend = session.method('users.get', {'user_ids': friend})

        for each_friend_stats in each_friend:
            last_name = each_friend_stats['last_name']
            first_name = each_friend_stats['first_name']
            for last_name_a in last_name[-1]:
                putan_groups = [190923816, 73247559, 125327221, 178062416, 91050183, 161276195]
                friends_groups = session.method('groups.get', {'user_ids': friend} )
                for friend_groups in friends_groups['items']:
                    print(each_friend)
                    # if set(str(friend_groups)).issubset(str(putan_groups)):



                if each_friend_stats['is_closed'] == True:
                    if last_name_a in girls_as:
                        print(last_name + " " + first_name + ' -шлюха с закрытым профилем')

                    else:
                        print(last_name + ' ' + first_name + ' -пидорок с закрытым профилем')



    # for each in each_friend[0]['is_closed']:
    #     print(each)
    # status = session.method('status.get', {'user_id': user_id})
    # print(status['text'])




def set_dynamic_status():
    while True:

        time.sleep(2)
        vk.status.set(text='┌(ಠ_ಠ)┘')
        time.sleep(2)
        vk.status.set(text='(─‿‿─)')
        time.sleep(2)
        vk.status.set(text='(ʘᗩʘ)')
        time.sleep(2)
        vk.status.set(text='(；一_一)')
        time.sleep(2)




su_us(cur_id)


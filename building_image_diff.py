def read(file_name_left, file_name_right):

    with open(file_name_left, 'r', encoding='utf-8') as f_left, \
         open(file_name_right, 'r', encoding='utf-8') as f_right, \
         open('only_left.txt', 'w', encoding='utf-8') as f_w_left, \
         open('only_right.txt', 'w', encoding='utf-8') as f_w_right:

        file_left = f_left.readlines()
        file_right = f_right.readlines()

        # 改行を除く
        list_left = list(map(lambda x: x.replace('\n', ''), file_left))
        list_right = list(map(lambda x: x.replace('\n', ''), file_right))

        print("left数  : " + str(len(list_left)))
        print("right数 : " + str(len(list_right)))

        # list_leftのみ
        print("==leftのみ==")
        only_left_data = _diff(list_left, list_right)

        print("only left  : " + str(len(only_left_data)))
        f_w_left.writelines(only_left_data)

        # list_rightのみ
        print("==rightのみ==")
        only_right_data = _diff(list_right, list_left)

        print("only right : " + str(len(only_right_data)))
        f_w_right.writelines(only_right_data)

def _diff(list1, list2):
    only = []

    for l in list1:
        if l not in list2:
            only.append(l)

    return only

if __name__ == '__main__':

    read('image.txt', 'large_image.txt')

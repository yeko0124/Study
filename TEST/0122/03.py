
a1 = [1, 2, 3]
a2 = [2, 3, 4]
s1 = set(a1)
s2 = set(a2)


def differ(lst1, lst2):
    result: list = lst1 + lst2
    result.sort()
    # print('res:', result)
    # res: [1, 2, 2, 3, 3, 4]

    idx = 0
    box = list()

    # 비교할 숫자가, 하나만 있으면 호출, 두개가 중복되면 패스
    for idx in range(len(result)):
        if (idx+1) < len(result):
            # print(result[i], result[i+1])
            if result[idx] != result[idx+1]:
                box.append(result[idx])
                result.pop(idx)
                for idx in range(len(result)):
                    if (idx + 1) < len(result):
                        # print(result[i], result[i+1])
                        if result[idx] != result[idx + 1]:
                            box.append(result[idx])
                            # print(box)
                            result.pop(idx)
                            # print('result:', box)
                        elif result[idx] == result[idx + 1]:
                            result.pop(idx)
                            result.pop(idx)
                            for idx in range(len(result)):
                                if (idx + 1) < len(result):
                                    # print(result[i], result[i+1])
                                    if result[idx] != result[idx + 1]:
                                        box.append(result[idx])
                                        # print(box)
                                        result.pop(idx)
                                    elif result[idx] == result[idx + 1]:
                                        # print(idx)
                                        result.pop(idx)
                                        # print(result)
                                        result.pop(idx)
                                        # print(result)
                                        box.append(result[idx])
                print('result:', box)
            elif result[idx] == result[idx+1]:
                result.pop(idx)
                result.pop(idx)
                print('dd', box)
            return box
        else:
            return print(box)
            # 임시적으로 result 리스트를 두개로 분리하면, Recursive 가능하지 않나.어차피 함수 다시 시작하면 합치니까
# TODO 꼭 하고야 만다ㅏㅏ
                #..recursive.. 안돼ㅐㅐㅐㅑㅑ 리스트가 없어ㅓ 이미 합쳐졋어ㅓㅓㅓㅓㅓㅡㅓㅓ
    # 2개일 경우라 가능할듯, 중복 3개면 안될 듯


differ(a1, a2)


def differ2(lst1, lst2):
    pass
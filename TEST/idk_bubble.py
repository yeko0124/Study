
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
    # index[0]과 [1]을 비교하고, 같으면 인덱스 0, 1을 pop, 같지 않으면 인덱스 0을 저장.
    # 그래서 한계점 : 2번 반복만 가능. 3번 반복되면 망함
    for idx in range(len(result)):
        if (idx+1) < len(result):
            if result[idx] != result[idx+1]:
                box.append(result[idx])
                result.pop(idx)
                for idx in range(len(result)):
                    if (idx + 1) < len(result):
                        if result[idx] != result[idx + 1]:
                            box.append(result[idx])
                            result.pop(idx)
                        elif result[idx] == result[idx + 1]:
                            result.pop(idx)
                            result.pop(idx)
                            for idx in range(len(result)):
                                if (idx + 1) < len(result):
                                    if result[idx] != result[idx + 1]:
                                        box.append(result[idx])
                                        result.pop(idx)
                                    elif result[idx] == result[idx + 1]:
                                        result.pop(idx)
                                        result.pop(idx)
                                        # pop을 두번하는 이유는, idx = 0인데 0을 pop하면 idx[1]이 다시 0의 자리로 오니까.
                                        # you know what i am saying
                                        box.append(result[idx])
                print('result:', box)
            elif result[idx] == result[idx+1]:
                result.pop(idx)
                result.pop(idx)
                print('dd', box)
            return box
        else:
            return print(box)


differ(a1, a2)

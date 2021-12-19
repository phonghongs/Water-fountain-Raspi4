def ReadScript(_FileDir):
    _Script_Content = []
    with open(_FileDir, 'r') as f:
        contents = f.read().split('\n')
        for cnt in contents:
            _Script_Content.append(cnt.split(';'))

    return _Script_Content


def List2Dict(_list):
    dct_result = {_list[i][0]: _list[i][1] for i in range(0, len(_list))}
    return dct_result

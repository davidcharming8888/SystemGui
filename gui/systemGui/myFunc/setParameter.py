def setParameter(rawData):
    '''
    :param rawData: 包含某一设备信息的dict
    :return para_list: 包含某一设备信息的ParaTree
    '''
    para_list = list()
    for k1,v1 in rawData.items():
        cdata = list()
        para_list.append({"name": k1, "type": "group", "children": cdata})
        for k2, v2 in v1.items():
            bool = "设备描述" in k2 or "设备隐患" in k2 or "设备功能描述" in k2
            if bool:
                cdata.append({"name": k2, "type": "text", "value": v2, "readonly": True})
            else:
                cdata.append({"name": k2, "type": "str", "value": v2, "readonly": True})
    return para_list


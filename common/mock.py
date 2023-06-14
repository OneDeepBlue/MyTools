import random
import time


def mock_cname(sex: int = None) -> str:
    """
    随机生成中文姓名
    :param sex: 性别， 0是男生，1是女生
    :return: 中文姓名，2~4个字
    """
    FIRST_NAMES = ['王', '李', '张', '刘', '陈', '杨', '黄', '赵', '周', '吴', '徐', '孙', '马', '胡', '朱', '郭', '何',
                   '罗', '高', '林', '韩', '犯', '曹', '金', '史', '韦', '陶', '吕', '欧阳', '上官', '司马', '夏侯',
                   '诸葛',
                   '公孙', '慕容']
    LAST_NAMES_2 = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩' \
                   '中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦' \
                   '翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛'
    LAST_NAMES_3 = '钧慧巧美颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰娜静淑惠珠翠雅芝玉萍红娥' \
                   '玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾韵融园' \
                   '艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽秀娟英华'
    if sex == 0:
        last_names = LAST_NAMES_2
    elif sex == 1:
        last_names = LAST_NAMES_3
    else:
        last_names = random.choice([LAST_NAMES_2, LAST_NAMES_3])
    return random.choice(FIRST_NAMES) + "".join(random.choice(last_names) for i in range(random.choice([1, 2, 2, 2])))


def mock_phone():
    """
    随机生成一个国内手机号（11位）
    :return: 国内手机号
    """
    phone_prefix = ['139', '138', '137', '136', '135', '134', '133', '132', '131', '130', '159', '158', '157', '156',
                    '155', '150', '151', '152', '153', '189', '188', '187', '186', '185', '184', '183', '182', '181',
                    '180', '178', '177', '176', '175', '173']
    prefix = random.choice(phone_prefix)
    postfix = "".join(random.choices("0123456789", k=8))
    return prefix + postfix


def mock_url(agree='https'):
    """
    随机生成URL网址
    :param agree: 协议类型
    :return: URL网址
    """
    s = 'abcdefghijklmnopqrstuvwxyz'
    domains = ['.com', '.asia', '.net', '.info', '.biz', '.pro', '.mobi', '.cn', '.com.cn', '.net.cn', '.org.cn',
               '.cc', '.tv', '.co', '.gov.cn', '.art', '.beer', '.company', '.chat', '.city', '.cool', '.cloud',
               '.club', '.center', '.design', '.email', '.fund', '.fans', '.fun', '.fit', '.group', '.guru', '.gold',
               '.host', '.icu', '.shop', '.site', '.social', '.show', '.top', '.today', '.tech', '.team', '.vip',
               '.video', '.world', '.wiki', '.xyz', '.xin', '.io', '.zone']
    name = "".join(random.choice(s) for i in range(random.randint(3, 15)))
    url = "".join(random.choice(s) for i in range(random.randint(3, 15)))
    domain = random.choice(domains)
    realm = f"{agree}://{name}{domain}/{url}"
    return realm


def mock_email():
    """
    随机生成邮箱
    :return: 邮箱
    """
    s = 'abcdefghijklmnopqrstuvwxyz'
    domains = ['.com', '.asia', '.net', '.info', '.biz', '.pro', '.mobi', '.cn', '.com.cn', '.net.cn', '.org.cn',
               '.cc', '.tv', '.co', '.gov.cn', '.art', '.beer', '.company', '.chat', '.city', '.cool', '.cloud',
               '.club', '.center', '.design', '.email', '.fund', '.fans', '.fun', '.fit', '.group', '.guru', '.gold',
               '.host', '.icu', '.shop', '.site', '.social', '.show', '.top', '.today', '.tech', '.team', '.vip',
               '.video', '.world', '.wiki', '.xyz', '.xin', '.io', '.zone']
    name = "".join(random.choice(s) for i in range(random.randint(3, 15)))
    field = "".join(random.choice(s) for i in range(random.randint(3, 10)))
    domain = random.choice(domains)
    email = f"{name}@{field}{domain}"
    return email


def mock_id():
    """
    随机生成身份证号
    :return: 有效的身份证号
    """
    province = ('11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42',
                '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '66')
    region = province[random.randint(0, len(province) - 1)] + '0101'
    # 生成年，1933到今年中随机一个
    yea = random.randint(1950, int(time.strftime("%Y")))  # 生成年，1950到今年中随机一个
    # 生成月
    mon = random.randint(1, 12)
    ran_mon = '0' + str(mon) if mon < 10 else mon
    # 生成日
    day = random.randint(1, 27)
    ran_day = '0' + str(day) if day < 10 else day
    #  生成年月日后的三位数
    value = random.randint(10, 199)
    if value < 100:
        ran_value = "0" + str(value)
    else:
        ran_value = str(value)
    ran = str(region) + str(yea) + str(ran_mon) + str(ran_day) + str(ran_value)
    #  前17位每位需要乘上的系数，用字典表示，比如第一位需要乘上7，最后一位需要乘上2
    coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4,
           17: 2}
    summat = 0
    #  循环计算前17位每位乘上系数之后的和
    for i in range(17):
        summat = summat + int(ran[i:i + 1]) * coe[i + 1]
    #  前17位每位乘上系数之后的和除以11得到的余数对照表，比如余数是0，那第18位就是1
    mat = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    cid = ran + mat[summat % 11]
    return cid


def get_constellation(month: int, date: int) -> str:
    """
    计算星座
    :param month: 月
    :param date: 日
    :return: 星座
    """
    constellations = (
        (1, 20, "摩羯"), (2, 19, "水瓶"), (3, 21, "双鱼"), (4, 20, "白羊"),
        (5, 21, "金牛"), (6, 22, "双子"), (7, 23, "巨蟹"), (8, 23, "狮子"),
        (9, 23, "处女"), (10, 24, "天秤"), (11, 23, "天蝎"), (12, 22, "射手"))
    for constellation in constellations:
        if (month, date) <= constellation[:2]:
            return constellation[-1]


def mock_carno():
    """
    随机生成国内车牌号
    :return: 国内车牌号，如：粤B88889
    """
    provincial = random.choice('辽吉黑沪苏浙皖闽赣鲁豫鄂湘粤桂琼川贵云渝藏陕甘青宁新')
    market = random.choice('ABCDEFGHJKLMNPRS')
    no = ''.join(random.choices('ABCDEFGHJKLMNPRS012345678901234567890123456789', k=5))
    return f"{provincial}{market}{no}"


if __name__ == '__main__':
    # print(mock_cname(3))
    # print(get_constellation(10,8))
    # print(mock_id())
    # print(get_constellation(4, 7))
    print(mock_id())
    print(mock_carno())

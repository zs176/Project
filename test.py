# 将歌词解析封装成类，要求：提供一个方法(根据时间返回歌词)

class Song:  # 定义歌词类
    def __init__(self, song):
        self.song = song


class Song_jiexi:  # 定义歌词解析函数
    def __init__(self, song_word):
        self.song_word = song_word

    

    def chazhao_time(self, t):
        # 准备一个字典，用来保存歌曲信息
        song_dict = {}

        # 准备一个字典，用来保存歌词信息
        lrc_dict = {}

        # 按照换行进行切割
        str_list = (self.song_word.song).splitlines()

        # 遍历处理
        for string in str_list:
            # 判断是否是歌词信息
            if string[1].isdecimal():
                # [02:11.55][01:50.60][00:22.63]穿过幽暗的岁月
                # 按照']'进行切割
                lrc_list = string.split(']')
                # 提取歌词信息
                lrc_info = lrc_list[-1]
                # 提取时间信息
                time_info = lrc_list[:-1]
                # 遍历处理时间信息
                for time_str in time_info:
                    # [00:00.70
                    # 去掉左边的'['
                    time_str = time_str[1:]
                    # 00:00.70
                    # 按照':'进行切割
                    time_info_list = time_str.split(':')
                    # 提取分钟
                    time_min = float(time_info_list[0])
                    # 提取秒数
                    time_sec = float(time_info_list[1])
                    # 合并时间
                    time = time_min * 60 + time_sec
                    # 保存到歌词字典中
                    lrc_dict[time] = lrc_info
            else:
                # 去掉两边的[]
                string = string[1:-1]
                # 按照':'进行切割
                song_list = string.split(':')
                # 保存到歌曲字典中
                if song_list[0] == 'ti':
                    song_dict['标题'] = song_list[1]
                elif song_list[0] == 'ar':
                    song_dict['艺术家'] = song_list[1]
                elif song_list[0] == 'al':
                    song_dict['专辑'] = song_list[1]

        # 提取歌词字典中所有的键
        time_list = list(lrc_dict)
        # 排序
        time_list.sort(reverse=True)

        for i in time_list:
            if i <= t:
                tt = i
                break
        return lrc_dict[tt]


# 测试代码
test = Song('''[ti:蓝莲花]
[ar:许巍]
[al:留声十年绝版青春北京演唱会]
[00:-01.70]蓝莲花
[00:-00.70]演唱：许巍
[00:00.00]
[00:00.70]没有什么能够阻挡
[00:06.01]你对自由的向往
[00:11.43]天马行空的生涯
[00:16.99]你的心了无牵挂
[00:21.20]
[02:11.55][01:50.60][00:22.63]穿过幽暗的岁月
[02:16.93][01:55.60][00:27.81]也曾感到彷徨
[02:22.21][02:01.09][00:33.13]当你低头的瞬间
[02:27.62][02:06.33][00:38.32]才发觉脚下的路
[02:31.64][02:10.23][00:42.37]
[02:32.97][00:43.79]心中那自由的世界
[02:38.23][00:49.50]如此的清澈高远
[02:43.30][00:54.31]盛开着永不凋零
[02:47.70][00:58.50]蓝莲花
[02:53.95][03:00.06][01:05.41]''')

test2 = Song_jiexi(test)
# print(type(test.song))

print(test2.chazhao_time(50))
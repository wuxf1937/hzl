from collections import namedtuple as namedtuple

gua2num = {
	# 阳爻为1，阴爻为0，最高位为上爻
	# 以下乾宫八卦，俱属金
	"乾": 0b111111,		
	"姤": 0b111110,
	"遁": 0b111100,
	"否": 0b111000,
	"观": 0b110000,
	"剥": 0b100000,
	"晋": 0b101000,
	"大有": 0b101111,

	# 以下震宫八卦，具属木
	"震": 0b001001,
	"豫": 0b001000,
	"解": 0b001010,
	"恒": 0b001110,
	"升": 0b000110,
	"井": 0b010110,
	"大过": 0b011110,
	"随": 0b011001,

	# 以下坎宫八卦，具属水
	"坎": 0b010010,
	"节": 0b010011,
	"屯": 0b010001,
	"既济": 0b010101,
	"革": 0b011101,
	"丰": 0b001101,
	"明夷": 0b000101,
	"师":0b000010,

	# 以下艮宫八卦，具属土
	"艮": 0b100100,
	"贲": 0b100101,
	"大畜": 0b100111,
	"损": 0b100011,
	"睽": 0b101011,
	"履": 0b111011,
	"中孚": 0b110011,
	"渐": 0b110100,

	# 以下坤宫八卦，具属土
	"坤": 0b000000,
	"复": 0b000001,
	"临": 0b000011,
	"泰": 0b000111,
	"大壮": 0b001111,
	"夬": 0b011111,
	"需": 0b010111,
	"比": 0b010000,

	# 以下巽宫八卦，具属木
	"巽": 0b110110,
	"小畜": 0b110111,
	"家人": 0b110101,
	"益": 0b110001,
	"无妄": 0b111001,
	"噬嗑": 0b101001,
	"颐": 0b100001,
	"蛊": 0b100110,

	# 以下离宫八卦，具属火
	"离": 0b101101,
	"旅": 0b101100,
	"鼎": 0b101110,
	"未济": 0b101010,
	"蒙": 0b100010,
	"涣": 0b110010,
	"讼": 0b111010,
	"同人": 0b111101,

	# 以下兑宫八卦，具属金
	"兑": 0b011011,
	"困": 0b011010,
	"萃": 0b011000,
	"咸": 0b011100,
	"蹇": 0b010100,
	"谦": 0b000100,
	"小过": 0b001100,
	"归妹": 0b001011,
}

# 数字到六十四卦的映射
num2gua = {num:gua for gua,num in gua2num.items()}

# 八宫卦表
gong_gua = [gua for gua in gua2num if (gua2num[gua] >> 3) == (gua2num[gua] & 0b000111)]

# 宫之五行
gong2wuxing = {
	"乾": "金",
	"坎": "水",
	"艮": "土",
	"震": "木",
	"巽": "木",
	"离": "火",
	"坤": "土",
	"兑": "金",
}

# 八卦之象
gong2xiang = {
	"乾": "天",
	"坎": "水",
	"艮": "山",
	"震": "雷",
	"巽": "风",
	"离": "火",
	"坤": "地",
	"兑": "泽",
}

# 八宫納甲
gong2gan = {
	"乾内": "甲",
	"乾外": "壬",
	"坎": "戊",
	"艮": "丙",
	"震": "庚",
	"巽": "辛",
	"离": "己",
	"坤内": "乙",
	"坤外": "癸",
	"兑": "丁",	
}
gong2zhi = {
	"乾": ("子", "寅", "辰", "午", "申", "戌"),
	"坎": ("寅", "辰", "午", "申", "戌", "子"),
	"艮": ("辰", "午", "申", "戌", "子", "寅"),
	"震": ("子", "寅", "辰", "午", "申", "戌"),
	"巽": ("丑", "亥", "酉", "未", "巳", "卯"),
	"离": ("卯", "丑", "亥", "酉", "未", "巳"),
	"坤": ("未", "巳", "卯", "丑", "亥", "酉"),
	"兑": ("巳", "卯", "丑", "亥", "酉", "未"),
}

#宫、世表
num2shigong = {
	0: "上世",
	1: "一世",
	3: "二世",
	7: "三世",
	15: "四世",
	31: "五世",
	23: "游魂",
	16: "归魂",
}

shigong2shiyao = {
	"上世": 5,
	"一世": 0,
	"二世": 1,
	"三世": 2,
	"四世": 3,
	"五世": 4,
	"游魂": 3,
	"归魂": 2,
}

# 天干五行
gan2wuxing = {
	"甲": "木",
	"乙": "木",
	"丙": "火",
	"丁": "火",
	"戊": "土",
	"己": "土",
	"庚": "金",
	"辛": "金",
	"壬": "水",
	"癸": "木",
}

# 地支五行
zhi2wuxing = {
	"寅": "木",
	"卯": "木",
	"辰": "土",
	"巳": "火",
	"午": "火",
	"未": "土",
	"申": "金",
	"酉": "金",
	"戌": "土",
	"亥": "水",
	"子": "水",
	"丑": "土",
}

# 八卦之数
gong2num = {gong: num & 0b000111 for gong, num in gua2num.items() if gong in gong_gua}

num2gong = {num: gong for gong, num in gong2num.items()}

# 五行相生
wuxing_sheng = {
	"金": "水",
	"水": "木",
	"木": "火",
	"火": "土",
	"土": "金",
}

# 五行生我者
wuxing_shengwo = {sheng:xing for xing,sheng in wuxing_sheng.items()}

# 五行相克
wuxing_ke = {
	"金": "木",
	"木": "土",
	"土": "水",
	"水": "火",
	"火": "金",
}

# 五行克我者
wuxing_kewo = {ke:xing for xing,ke in wuxing_ke.items()}

# 六十甲子
jiazi = (
	"甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
	"甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
	"甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
	"甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
	"甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
	"甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥",
)

# 六兽
liushou = (
	"青龙",
	"朱雀",
	"勾陈",
	"螣蛇",
	"白虎",
	"玄武",
)

class Gua(object):
	"""某卦，及其装卦。
	.name: 卦名，如：复
	.gong: 所属何宫，如复属 坤 宫
	.yao[0-5]: list of named tuple. 0-5: 初至上爻
	.yao[?].name： 爻名，如初六、九二等
	.yao[?].gan .zhi .wuxing：爻的干支、五行
	.yao[?].liuqin：六亲，如官鬼、兄弟
	.gongshi：所属宫的几世卦，如上世、三世、游魂等
	.shi: 世爻的名字，如六三
	.ying: 应爻的名字"""

	def __init__(self, num = 0b111111):
		"""从数字确定挂名"""
		self.name = num2gua[num]
		self.num = num
		self.zhuang_gua()
		self.find_lname()

	def zhuang_gua(self):
		"""装卦"""

		# 所属何宫几世
		self.find_gongshi()
		# 装六爻
		self.zhuang_yao()
		# 定世应
		self.find_shiying()
		# 装卦辞

	def find_gongshi(self):
		"""确定某卦的宫和世"""
		for gong in gong_gua:
			num = gua2num[self.name] ^ gua2num[gong]
			if num in num2shigong:
				self.gong = gong
				self.shigong = num2shigong[num]
	
	def zhuang_yao(self):
		"""定各爻，及其属性。六爻为列表，0-5：初-上。"""
		y = namedtuple("y", "name, gan, zhi, wuxing, liuqin")

		self.yao = []

		yinyao_names = ("初六", "六二", "六三", "六四", "六五", "上六")
		yangyao_names = ("初九", "九二", "九三", "九四", "九五", "上九")
		for pos in range(6):

			if 1 << pos & self.num == 0:	# 阴爻
				name = yinyao_names[pos]
			else:							# 阳爻
				name = yangyao_names[pos]

			gan, zhi = self.najia(pos)			# 納甲
			wuxing = zhi2wuxing[zhi]
			liuqin = self.find_liuqin(wuxing)

			yc = y(name, gan, zhi, wuxing, liuqin)
			self.yao.append(yc)

	def najia(self, pos):
		"""各爻納甲"""
		if self.gong == "乾" or self.gong == "坤":
			if pos < 3:
				gongj = self.gong + "内"
			else:
				gongj = self.gong + "外"
		else:
			gongj = self.gong

		gan = gong2gan[gongj]

		if pos < 3:		#内挂某爻
			for gong in gong_gua:
				if self.num & 0b000111 == gua2num[gong] & 0b000111:
					zhi = gong2zhi[gong][pos]
					break
		else:			#外卦某爻
			for gong in gong_gua:	
				if self.num & 0b111000 == gua2num[gong] & 0b111000:
					zhi = gong2zhi[gong][pos]
					break

		return gan, zhi

	def find_liuqin(self, wuxing):
		"""定六亲"""
		if gong2wuxing[self.gong] == wuxing:
			return "兄弟"
		elif wuxing_sheng[gong2wuxing[self.gong]] == wuxing:
			return "子孙"
		elif wuxing_shengwo[gong2wuxing[self.gong]] == wuxing:
			return "父母"
		elif wuxing_ke[gong2wuxing[self.gong]] == wuxing:
			return "妻财"
		elif wuxing_kewo[gong2wuxing[self.gong]] == wuxing:
			return "官鬼"

		raise ValueError

	def find_shiying(self):
		"""定世应"""
		self.shinum = shigong2shiyao[self.shigong]
		self.shi = self.yao[self.shinum].name
		self.yingnum = (self.shinum + 3) % 6
		self.ying = self.yao[self.yingnum].name

	def find_lname(self):
		for gong in gong_gua:
			if self.num & 0b000111 == gua2num[gong] & 0b000111:
				self.neigua = gong
			if self.num & 0b111000 == gua2num[gong] & 0b111000:
				self.waigua = gong
		if self.name in gong_gua:
			self.lname = self.name + "为" + gong2xiang[self.gong]
		else:
			self.lname = gong2xiang[self.waigua] + gong2xiang[self.neigua] + self.name

	def __str__(self):
		s = self.name + ": " +self.lname + ", " + self.gong + "宫, " + self.shigong + "卦\n"
		for yao in reversed(self.yao):
			yao_s = ". ".join([yao.name, yao.gan + yao.zhi + yao.wuxing, yao.liuqin])
			if yao.name == self.shi:
				yao_s = yao_s + ", " + "世"
			elif yao.name == self.ying:
				yao_s = yao_s + ", " + "应"
			s = s + yao_s + "\n"

		return s

class ZhanGua(object):
	"""一次占卦。
	date: 起卦日期。named tuple. 如date.year .month .day = "甲子"，
	whom: 所占何人，如："同事"，
	what: 所占何事，如："婚姻"，
	gender: 问卜者性别，"男" or "女",
	yao_gua: 摇卦结果, 如("单", "坼", "重", "交", "单", "坼"),
	"""
	def __init__(self, date, whom, what, gender, yao_gua):
		d = namedtuple("d", "year, month, day")
		self.date = d(date[0], date[1], date[2])
		self.whom = whom
		self.what = what
		self.gender = gender

		bengua_num = 0b000000
		zhigua_num = 0b000000
		self.bianyao = []
		for x in range(6):
			if yao_gua[x] == "单":
				yao = 1 << x
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao
			elif yao_gua[x] == "坼":
				yao = 0 << x 				# just for clearness
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao
			elif yao_gua[x] == "重":
				yao = 1 << x
				self.bianyao.append(x)
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao ^ (1 << x)
			elif yao_gua[x] == "交":
				yao = 0 << x
				self.bianyao.append(x)				
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao ^ (1 << x)
			else:
				raise ValueError
		self.bengua = Gua(bengua_num)
		self.zhigua = Gua(zhigua_num)
		self.an_bianqin()
	#	self.an_liushou()

	def an_bianqin(self):
		"""重定变爻六亲"""
		self.bianqin = []
		for x in self.bianyao:
			if gong2wuxing[self.bengua.gong] == self.zhigua.yao[x].wuxing:
				self.bianqin.append("兄弟")
			elif wuxing_sheng[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.bianqin.append("子孙")
			elif wuxing_shengwo[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.bianqin.append("父母")
			elif wuxing_ke[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.bianqin.append("妻财")
			elif wuxing_kewo[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.bianqin.append("官鬼")
			else:
				raise ValueError
	def an_liushou(self):
		if self.date.day[0] == "甲" or self.date.day[0] == "乙":
			liushou_start = 0
		elif self.date.day[0] == "丙" or self.date.day[0] == "丁":
			liushou_start = 1
		elif self.date.day[0] == "戊":
			liushou_start = 2
		elif self.date.day[0] == "己":
			liushou_start = 3
		elif self.date.day[0] == "庚" or self.date.day[0] == "辛":
			liushou_start = 4
		elif self.date.day[0] == "壬" or self.date.day[0] == "癸":
			liushou_start = 5
		else:
			raise ValueError

		for x in range(6):
			self.bengua.yao[x].liushou = liushou[(liushou_start + x) % 6]
	def __str__(self):
		return(str(self.bengua) + str(self.zhigua) + str(self.bianyao) + str(self.bianqin))

def main():
	"""	for n in range(64):
		g = Gua(n)
		print(g)
	"""
	g = ZhanGua(("甲子", "乙丑", "丙寅"), "同事", "职业", "男", "单坼交重单坼")
	print(g)

if __name__ == '__main__':
	main()
		
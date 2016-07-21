from mysteries import LunarDate, liushou
from Gua import Gua

class ZhanGua(object):
	"""一次占卦。
	date: 起卦日期。named tuple. 如date.year .month .day = "甲子"，
	whom: 所占何人，如："同事"，
	what: 所占何事，如："婚姻"，
	gender: 问卜者性别，"男" or "女",
	qi_gua: 摇卦结果, 如("单坼重交单坼"),
	"""
	def __init__(self, date, whom, what, gender, qi_gua):
		self.date = LunarDate(date[0], date[1], date[2])
		self.whom = whom
		self.what = what
		self.gender = gender

		bengua_num = 0b000000
		zhigua_num = 0b000000
		self.bianyao = []
		for x in range(6):
			if qi_gua[x] == "单":
				yao = 1 << x
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao
			elif qi_gua[x] == "坼":
				yao = 0 << x 				# just for clearness
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao
			elif qi_gua[x] == "重":
				yao = 1 << x
				self.bianyao.append(x)
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao ^ (1 << x)
			elif qi_gua[x] == "交":
				yao = 0 << x
				self.bianyao.append(x)				
				bengua_num = bengua_num | yao
				zhigua_num = zhigua_num | yao ^ (1 << x)
			else:
				raise ValueError
		self.bengua = Gua(bengua_num)
		self.zhigua = Gua(zhigua_num)
		self.an_bianqin()
		self.an_liushou()

	def an_bianqin(self):
		"""重定变爻六亲"""
		for x in self.bianyao:
			self.zhigua.yao[x].liuqin = self.bengua.find_liuqin(self.zhigua.yao[x].wuxing)
			"""
			if gong2wuxing[self.bengua.gong] == self.zhigua.yao[x].wuxing:
				self.zhigua.yao[x].liuqin = "兄弟"
			elif wuxing_sheng[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.zhigua.yao[x].liuqin = "子孙"
			elif wuxing_shengwo[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.zhigua.yao[x].liuqin = "父母"
			elif wuxing_ke[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.zhigua.yao[x].liuqin = "妻财"
			elif wuxing_kewo[gong2wuxing[self.bengua.gong]] == self.zhigua.yao[x].wuxing:
				self.zhigua.yao[x].liuqin = "官鬼"
			else:
				raise ValueError
			"""
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
		s = "问卜人，{}，于 {}年{}月{}日 问 {} {} 事，\n".format(self.gender, self.date.year, self.date.month, self.date.day, self.whom, self.what)
		s = s + "得 {} 之 {} 卦。\n".format(self.bengua.lname, self.zhigua.lname)

		for x in reversed(range(6)):
			yao_s = ". ".join([self.bengua.yao[x].name, self.bengua.yao[x].liushou, self.bengua.yao[x].zhi + self.bengua.yao[x].wuxing, self.bengua.yao[x].liuqin])
			if x in self.bianyao:
				yao_s = yao_s + " 化为 " + ". ".join([self.zhigua.yao[x].zhi + self.zhigua.yao[x].wuxing, self.zhigua.yao[x].liuqin])
			if x == self.bengua.shi:
				yao_s = yao_s + ", " + "世"
			elif x == self.bengua.ying:
				yao_s = yao_s + ", " + "应"
			s = s + yao_s + "\n"

		return(s)

def main():
	g = ZhanGua(("甲子", "乙丑", "丙寅"), "同事", "职业", "男", "坼坼交重单坼")
	print(g)

if __name__ == '__main__':
	main()


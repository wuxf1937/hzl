from mysteries import *

class Yao(object):
	"""爻。 可能包含：
	.name: 名字，如初九，六三等;
	.yinyang: 阴，阳，老阴，单等；
	.gan: 所属天干;
	.zhi: 地支;
	.wuxing: 五行属性;
	.liuqin: 六亲;
	.liushou: 六兽;
	"""
	def __init__(self):
		super(Yao, self).__init__()


class Gua(object):
	"""某卦，及其装卦。
	.name: 卦名，如：复
	.gong: 所属何宫，如复属 坤 宫
	.yao[0-5]: list of Yao. 0-5: 初至上爻
	.yao[?].name： 爻名，如初六、九二等
	.yao[?].gan .zhi .wuxing：爻的干支、五行
	.yao[?].liuqin：六亲，如官鬼、兄弟
	.shigong：所属宫的几世卦，如上世、三世、游魂等
	.shi: 世爻的位置，0-5
	.ying: 应爻的位置
	"""

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
#		y = Yao()
		self.yao = []
		yinyao_names = ("初六", "六二", "六三", "六四", "六五", "上六")
		yangyao_names = ("初九", "九二", "九三", "九四", "九五", "上九")

		for pos in range(6):
			y = Yao()
			if 1 << pos & self.num == 0:	# 阴爻
				y.name = yinyao_names[pos]
			else:							# 阳爻
				y.name = yangyao_names[pos]

			y.gan, y.zhi = self.najia(pos)			# 納甲
			y.wuxing = zhi2wuxing[y.zhi]
			y.liuqin = self.find_liuqin(y.wuxing)

			self.yao.append(y)

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
		self.shi = shigong2shiyao[self.shigong]
		self.ying = (self.shi + 3) % 6

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
		s = self.name + ": " + self.lname + ", " + self.gong + "宫, " + self.shigong + "卦\n"
		for x in reversed(range(6)):
			yao_s = ". ".join([self.yao[x].name, self.yao[x].gan + self.yao[x].zhi + self.yao[x].wuxing, self.yao[x].liuqin])
			if x == self.shi:
				yao_s = yao_s + ", " + "世"
			elif x == self.ying:
				yao_s = yao_s + ", " + "应"
			s = s + yao_s + "\n"

		return s

def main():
	for n in range(64):
		g = Gua(n)
		print(g)
	
if __name__ == '__main__':
	main()

import os
from urllib import request
from urllib import parse
import json
import random
import time


# 翻译模块
def fanyi(danci):
	# Request URL
	Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	# 创建Form_Data字典，存储得到的Form Data
	Form_Data = {}
	Form_Data['type'] = 'AUTO'
	Form_Data['from'] = 'AUTO'  # 自动检测语言
	Form_Data['to'] = 'AUTO'
	Form_Data['smartresult'] = 'dict'
	Form_Data['doctype'] = 'json'
	Form_Data['version'] = '2.1'
	Form_Data['keyfrom'] = 'fanyi.web'
	Form_Data['action'] = 'FY_BY_REALTIME'
	# 使用urlencode方法转换标准格式
	while 1:
		Form_Data['i'] = danci
		if Form_Data['i'].lower() == 'exit':
			print('已退出')
			exit(0)
		data = parse.urlencode(Form_Data).encode('utf-8')
		# 传递Request对象和转换完格式的数据
		response = request.urlopen(Request_URL, data)
		# 读取信息并解码
		html = response.read().decode('utf-8')
		# 使用JSON
		translate_results = json.loads(html)
		# 找到翻译结果
		translate_results = translate_results['translateResult'][0][0]['tgt']
		# 打印翻译信息
		zimu = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
				'c', 'v', 'b', 'n', 'm']
		if translate_results[:1].lower() in zimu:
			return translate_results.lower()
		else:
			return translate_results


# 存入单词程序
def cundanci(danci):
	zimu = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
			'c', 'v', 'b', 'n', 'm']
	while True:
		duqu = open('./data\\word.txt', 'r').read()
		xiaoxie = duqu.lower()
		if danci[:1].lower() in zimu:
			if danci in xiaoxie:
				print("您的这个单词已经存在到数据中了")
				print("数据为({}{}{})".format(danci, '----', fanyi(danci)))
				print("请重新输入")
				print("*" * 100)
				return
		else:
			if danci in xiaoxie:
				print("您的这个中文已经存在到数据中了")
				print("数据为({}{}{})".format(fanyi(danci), '----', danci))
				print("请重新输入")
				print("*" * 100)
				return
		if danci == fanyi(danci):
			print("翻译为{}----{}".format(danci, fanyi(danci)))
			print("单词不对，请重新输入")
			print("*" * 100)
			return
		break
	chazhao = duqu.rfind('.')
	jishu = 1
	if chazhao == -1:
		pass
	else:
		zhenshijishu = chazhao - 1
		cunru_shuzi = ''
		zhenshi_cunru_shuzi = ''
		while True:
			if xiaoxie[zhenshijishu] != '\n':
				cunru_shuzi += xiaoxie[zhenshijishu]
				zhenshijishu -= 1
			else:
				zhenshi_cunru_shuzi = cunru_shuzi[::-1]
				break
		jishu = int(zhenshi_cunru_shuzi) + 1
	cunru = open('./data\\word.txt', 'a')
	if danci[:1] in zimu:
		cunru.write(str(jishu) + '.' + danci + '----' + fanyi(danci) + '\n')
		print("已将({}.{}{}{})成功保存到数据中".format(jishu, danci, '----', fanyi(danci)))
		print("*" * 100)
	else:
		cunru.write(str(jishu) + '.' + fanyi(danci) + '----' + danci + '\n')
		print("已将({}.{}{}{})成功保存到数据中".format(jishu, fanyi(danci), '----', danci))
		print("*" * 100)
	cunru.close()


# 删除单词模块
def shanchudanci(danci):
	diyi = open('./data\\word.txt', 'r')
	dier = open('./data\\word.txt', 'r')
	zongliebiao = []
	if danci in diyi.read():
		while True:
			zz = dier.readline()
			if not zz:
				break
			zongliebiao.append(zz)

		xin_liebao = []
		for i in zongliebiao:
			weizhi = i.find('.')
			quchu = i[weizhi + 1:]
			if danci in i:
				pass
			else:
				xin_liebao.append(quchu)
		print("已成功生成新的数据，正在执行下一步......")
		print("*"*100)

		cunru = open('./data\\word.txt', 'w')
		a = 1
		for ii in xin_liebao:
			cunru.write('{}.{}'.format(str(a), ii))
			a += 1
		cunru.close()
		print('已成功删除数据')
		print("*"*100)
	else:
		print('单词不存在，请重新输入')
		print("*"*100)

# 统计单词数目
def tongji():
	dakai = open('./data\\word.txt', 'r').read()
	weizhi = dakai.rfind('.')
	zhenshijishu = weizhi - 1
	cunru_shuzi = ''
	zhenshi_cunru_shuzi = ''
	while True:
		if dakai[zhenshijishu] != '\n':
			cunru_shuzi += dakai[zhenshijishu]
			zhenshijishu -= 1
		else:
			zhenshi_cunru_shuzi = cunru_shuzi[::-1]
			break
	cunru = open('./data\\number.txt', 'w')
	cunru.write(zhenshi_cunru_shuzi)
	cunru.close()


# 单词指定位置抽取
def huodezhididanci(shubiao):
	duqu = open('./data\\word.txt', 'r').read()
	while True:
		cunzai = duqu.find(str(shubiao)) + 1
		jiashu_jiance = 1
		baocun = ''
		if cunzai == -1:
			pass
		else:
			while True:
				qwe = duqu[cunzai + jiashu_jiance]
				if qwe != '\n':
					baocun += duqu[cunzai + jiashu_jiance]
					jiashu_jiance += 1
				else:
					break
		break
	return baocun


# 单词抽取
def suijichouqudanci(chouqushuling):
	duqu_shumu = open('./data\\number.txt', 'r').read()
	liebao = []
	fanhuizidian = {}
	for ii in range(1, int(duqu_shumu) + 1):
		liebao.append(ii)
	liebao_suiji = random.sample(liebao, chouqushuling)
	for i in liebao_suiji:
		hanshuhuoqu = huodezhididanci(i)
		weizhi_yi = hanshuhuoqu.find('-')
		weizhi_er = hanshuhuoqu.rfind('-') + 1
		fanhuizidian[hanshuhuoqu[weizhi_er:]] = hanshuhuoqu[:weizhi_yi]
	return fanhuizidian


# 单词转换拼写字符
def dancipinxieshengcheng(zidain):
	zhenshi_zidian = {}
	tiuchu = 0
	for yingyu in zidain:
		cunchu = ''
		hoqu = zidain[yingyu]
		for i in hoqu:
			if i == ' ':
				cunchu += i
				continue
			else:
				if tiuchu == 0:
					cunchu += i
					tiuchu = 1
				else:
					cunchu += '*'
					tiuchu = 0
		zhenshi_zidian[yingyu] = cunchu
	return zhenshi_zidian


# 检查单词是否正确
def jiancudancicuozaiweizhi(pinxiedanci, zhengqundanci):
	# pinxiedanci为用户写的pinxie单词
	# zhengqundanci为正确的
	shumu = len(pinxiedanci)
	shumu_1 = len(zhengqundanci)
	if shumu == shumu_1:
		install = []
		for i in range(shumu):
			if pinxiedanci[i] == zhengqundanci[i]:
				pass
			else:
				install.append(pinxiedanci[i])
		if install == []:
			return 1
		else:
			return "单词{}，{}不正确".format(pinxiedanci, tuple(install))
	if shumu > shumu_1:
		install_douqu = []
		install_shaoqu = []
		diyi = list(pinxiedanci)
		dier = list(zhengqundanci)
		a = 0
		for i in diyi:
			try:
				if dier[a] == i:
					a += 1
					continue
				else:
					install_douqu.append(i)
			except:
				install_douqu.append(i)
				continue
		return "单词{}，多出{}".format(pinxiedanci, tuple(install_douqu))
	else:
		install_queshao = []
		yi = list(pinxiedanci)
		er = list(zhengqundanci)
		for er_1 in er:
			if er_1 in yi:
				pass
			else:
				install_queshao.append(er_1)
		return "单词{}，缺少{}".format(pinxiedanci, tuple(install_queshao))


# 提示
def tishi(shumu, hanyi):
	if shumu == 1:
		print("*" * 100)
		return '中文意思为：{}'.format(hanyi)
	else:
		pass

#翻译记录模块
def fanyijilu(danci):
	shijian = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	zimu = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
			'c', 'v', 'b', 'n', 'm']
	cunru=open('./data\\record.txt','a')
	if danci[0] in zimu:
		cunru.write(shijian+" "+"({}----{})\n".format(danci,fanyi(danci)))
	else:
		cunru.write(shijian+" "+"({}----{})\n".format(fanyi(danci),danci))
	cunru.close()

#翻译单词检测
def jiancefanyishifouzhengqun(danci):
	if fanyi(danci)==danci:
		return 1
	else:
		return 2

#记录一次正确的
def zhengqunde_zhengque(danci):
	duqu=open('./data\\correct.txt','r').read()
	a=1
	if danci in duqu:
		zimu = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
				'c', 'v', 'b', 'n', 'm']
		danci1=danci
		while True:
			if danci1[0] in zimu:
				diyi_liebiao = []
				wert=open('./data\\correct.txt','r')
				while True:
					duqumeiyihang=wert.readline()
					if not duqumeiyihang:
						break
					diyi_liebiao.append(duqumeiyihang)

				xin_liebiao=[]
				for i in diyi_liebiao:
					if danci in i:
						quanxin=i.find('--')
						shumu = int(duqu[:quanxin])
						xin_liebiao.append(str(shumu+1)+i[quanxin:]+'\n')
					else:
						xin_liebiao.append(i)

				cunru = open('./data\\correct.txt', 'w')
				for ii in xin_liebiao:
					cunru.write(ii)
				cunru.close()
				break
			else:
				danci1=fanyi(danci)
				continue
	else:
		zimu = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
				'c', 'v', 'b', 'n', 'm']
		if danci[0] in zimu:
			cunru=open('./data\\correct.txt','a')
			cunru.write(str(a)+"--"+"({}----{})\n".format(fanyi(danci),danci))
			a+=1
			cunru.close()
		else:
			cunru=open('./data\\correct.txt','a')
			cunru.write(str(a) + "--" + "({}----{})\n".format(danci,fanyi(danci)))
			a += 1
			cunru.close()

while True:
	print("*" * 100)
	print("欢迎进入背单词程序，请选择一下服务(填括号里的数字)")
	print("(1)进入存单词模式")
	print("(2)进入删除单词模式")
	print("(3)进入拼写单词模式")
	print("(4)进入翻译模式")
	print("(5)退出程序")
	print("*" * 100)

	try:
		moshijinru = int(input("请选择你要进入的模式："))
		print("*" * 100)
	except:
		print("输入错误，请重新选择服务")
		print("*" * 100)
		continue
	if moshijinru == 1:
		while True:
			print("按数字1可以退出存入程序")
			try:
				www = input("请输入你要存入的单词：")
			except:
				continue
			if www == str(1):
				break
			cundanci(www)
			tongji()

	if moshijinru == 2:
		while True:
			print("按数字1可以退出删除程序")
			try:
				www_shanchu = input("请输入你要删除的单词：")
			except:
				continue
			if www_shanchu == str(1):
				break
			shanchudanci(www_shanchu)
			tongji()

	elif moshijinru == 3:
		shuliang = 0
		while True:
			try:
				shuliang = int(input("请输入你要练习单词的数目："))
				print("*" * 100)
				break
			except:
				print("请填写正确的数目（数字）")
				continue
		zhengquede = suijichouqudanci(shuliang)
		pinxiede = dancipinxieshengcheng(zhengquede)
		pinxiede_yi = pinxiede.values()
		liebiao = []
		for i_i_w in pinxiede_yi:
			liebiao.append(i_i_w)
		a = 0
		for hanyi, yingwen in zhengquede.items():
			pinxiede_er = liebiao[a]
			a += 1
			print("请输入完整的单词，如果单词里有空格，也要空格")
			print("单词为（{}）".format(pinxiede_er))
			print("输入数字1为中文意思（提示）")
			print("*" * 100)
			while True:
				danru = input('请输入：')
				try:
					if int(danru) == 1:
						print(tishi(int(danru), hanyi))
						continue
					else:
						break
				except:
					break
			fanhui = jiancudancicuozaiweizhi(danru, yingwen)
			if fanhui == 1:
				print("*" * 100)
				print("拼写正确")
				zhengqunde_zhengque(danru)
			else:
				print('拼写不正确将进入第二次')
				print("*" * 100)
				print("提醒一次中文翻译：{}".format(tishi(1, hanyi)))
				print("第二次输入，单词为（{}）".format(pinxiede_er))
				print("*" * 100)
				danru1 = input("请输入：")
				fanhui1 = jiancudancicuozaiweizhi(danru1, yingwen)
				if fanhui1 == 1:
					print("*" * 100)
					print("拼写正确")
				else:
					print(fanhui1)
					print("正确答案为---单词{}----中文翻译{}".format(yingwen, hanyi))
					print("进行下一个单词")
					print("*" * 100)
					continue

	elif moshijinru==4:
		while True:
			print("按下数字1可以退出程序")
			try:
				fanyi_dezifu=input('请输入你要翻译的词语：')
			except:
				continue
			if fanyi_dezifu==str(1):
				break
			else:
				if jiancefanyishifouzhengqun(fanyi_dezifu)==1:
					print("请重新输入，翻译不正确")
					print("*"*100)
					continue
				else:
					print("翻译为：{}".format(fanyi(fanyi_dezifu)))
					fanyijilu(fanyi_dezifu)
					print("*"*100)

	elif moshijinru == 5:
		print("谢谢使用，欢迎下次使用本程序，再见")
		break

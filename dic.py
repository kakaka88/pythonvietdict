
import re
import codecs
import sys
class Dictionary:
	def __init__(self,filename):
		data = self.readData(filename)
		self.dic = self.creatDictionary(data)

	def readData(self,filename):
		f = codecs.open(filename,'r','utf-8')
		data = f.read()
		return data.split('@')

	def creatDictionary(self,data):
		dictionary = {}
		for i in data:
			key_i = i.split('\n')[0]
			value_i = i[len(key_i):]
			dictionary[key_i] = value_i
		return dictionary

	def find(self,keyword):
		find_result = []
		for i in self.dic.keys():
			regex = '([/].*?[/])'
			pattern = re.compile(regex)
			r = pattern.findall(i)
			tmp = i
			for result in r:
				tmp = tmp.replace(result,'')
			if keyword.lower().strip() == tmp.lower() or keyword.lower().strip() +' ' == tmp.lower():
				find_result.append(i)
		if len(find_result):
			return find_result
		else:
			return "Not found!"



#dict1 = Dictionary('data2.dict')
#for key in r.keys():
#	sys.stdout.buffer.write(key.encode('utf-8'))
#	print('\n')
#	sys.stdout.buffer.write(r[key].encode('utf-8'))

#	print('\n**** \n')
#a = dict1.find('excUse ')
#sys.stdout.buffer.write(a.encode('utf-8'))
#sys.stdout.buffer.write(r[a].encode('utf-8'))
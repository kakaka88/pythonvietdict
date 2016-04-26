from tkinter import *
from dic import Dictionary

class DictionaryGUI:
	def __init__(self,master,dic):
		self.dictionary = dic
		frame = Frame(master,width=100, height=30, bg="")
		frame.pack()
		self.keyword = Entry(frame, bd = 2, fg = 'red')
		self.keyword.pack(side = LEFT)
		self.result = Text(master,width = 80,height = 20,bd = 2)
		self.result.pack()
		self.search_button = Button(frame, text = "Dịch", command = self.setResult)
		self.search_button.pack(side= LEFT)
		master.bind("<Return>", self.setResultEvent)
	def setResult(self):
		self.result.delete('1.0',END)
		self.text_result = self.dictionary.find(self.keyword.get())
		if type(self.text_result) ==str:
			self.result.insert(INSERT,self.text_result)
		else:
			mes = ''
			for i in self.text_result:
				mes+=i+ self.dictionary.dic[i]+'\n'
			self.result.insert(INSERT,mes)
			
	def setResultEvent(self,event):
		self.result.delete('1.0',END)
		self.text_result = self.dictionary.find(self.keyword.get())
		if type(self.text_result) ==str:
			self.result.insert(INSERT,self.text_result)
		else:
			mes = ''
			for i in self.text_result:
				mes+=i+ self.dictionary.dic[i]+'\n'
			self.result.insert(INSERT,mes)

dic = Dictionary('data2.dict')
root = Tk()
root.title("DICTIONARY EXAMPLE!")
root.iconbitmap('dic.ico')
img = PhotoImage(file='dic.png')
root.tk.call('wm', 'iconphoto', root._w, img)
dictGUi =  DictionaryGUI(root,dic)
root.mainloop()
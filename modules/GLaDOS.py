from modules.tasks import spin,spinrestore,getUsbList,askyesno,SysTrayIcon
from playsound import playsound
import threading,pyttsx3,win32file,random,time,os,webbrowser,pythoncom,sys
import PyHook3 as pyHook

class GLaDOS:
	def __init__(self):
		hover_text="GLaDOS"
		def surprise(sysTrayIcon):self.whee()
		def bye(sysTrayIcon):
			lines=["dont press that button","goodbye"]
			self.speakline(random.choice(lines))
			sys.exit()
		menu_options=(("Surprise","potatos.ico",surprise),)
		#SysTrayIcon("potatos.ico",hover_text,menu_options,on_quit=bye,default_menu_index=1)
		sysTrayThread=threading.Thread(target=SysTrayIcon,args=("potatos.ico",hover_text,menu_options),kwargs={"on_quit":bye,"default_menu_index":1})
		sysTrayThread.daemon=True
		sysTrayThread.start()
		
		usbSpyThread=threading.Thread(target=self.usbSpy)
		usbSpyThread.daemon=True
		usbSpyThread.start()

		keyboardSpyThread=threading.Thread(target=self.keyboardSpy)
		keyboardSpyThread.daemon=True
		keyboardSpyThread.start()
		
		self.speakline("fully connected")

	def usbSpy(self):
		current_list=getUsbList()
		old_list=current_list
		while True:
			current_list=getUsbList()
			if len(current_list)>len(old_list):
				lines=["dont plug it in","dont plug it in2",
					   "dont plug it in3","dont plug it in4"]
				self.speakline(random.choice(lines))
			elif len(current_list)<len(old_list):
				lines=["you broke it","file deleted","good","really ok"]
				self.speakline(random.choice(lines))
			old_list=current_list
			
	def keyboardSpy(self):
		self.logged=[]
		hm=pyHook.HookManager()
		hm.KeyDown=self.OnKeyboardEvent
		hm.HookKeyboard()
		pythoncom.PumpMessages()

	def OnKeyboardEvent(self,event):
		self.logged.append(event.Key)
		self.check_keys()
		return True

	def check_keys(self):
		fullstring=""
		for key in self.logged:
			fullstring=fullstring+key
			fullstring=fullstring.replace("Lshift","")
			fullstring=fullstring.replace("Rshift","")
			fullstring=fullstring.replace("Capital","")
			if "APERTURE" in fullstring.upper():
				self.respond("APERTURE")
				self.logged=[]
			elif "CAVE" in fullstring.upper() and "JOHNSON" in fullstring.upper():
				self.respond("CAVE JOHNSON")
				self.logged=[]
			elif "GLADOS" in fullstring.upper():
				self.respond("GLADOS")
				self.logged=[]
			elif "TWITTER" in fullstring.upper():
				self.respond("TWITTER")
				self.logged=[]
			elif "TURRET" in fullstring.upper():
				self.respond("TURRET")
				self.logged=[]
			elif "CAKE" in fullstring.upper():
				self.respond("CAKE")
				self.logged=[]
			elif "WHEATLEY" in fullstring.upper():
				self.respond("WHEATLEY")
				self.logged=[]
			elif "PORTAL" in fullstring.upper():
				self.respond("PORTAL")
				self.logged=[]
			elif "CAROLINE" in fullstring.upper():
				self.respond("CAROLINE")
				self.logged=[]
			elif len(self.logged)>100:
				self.logged=[]

	def respond(self,reason):
		if reason=="APERTURE":
			lines=["oh my facility","good people dont end up here"]
		elif reason=="CAVE JOHNSON":
			lines=["oh i like this guy","goodbye sir","burning people","yes sir"]
		elif reason=="GLADOS":
			lines=["hello","hello2",
				   "are you doing that just to aggravate me",
				   "did you do that on purpose","excellent",
				   "good job","good","i hate you so much",
				   "i hope that was a joke","just stop it already",
				   "no","oh hi","oh its you","really ok","time out",
				   "wasting my time","wow","yeah","yes","yes2",
				   "you dont need to do that"]
		elif reason=="TWITTER":
			lines=["bird1","bird2"]
		elif reason=="TURRET":
			lines=["turrets"]
		elif reason=="CAKE":
			lines==["all the cake is gone","before any cake","cake will be served",
					"cake and grief counselling","you will be baked","for your cake",
					"cut the cake","whos gonna make the cake","there really was a cake"]
		elif reason=="WHEATLEY":
			lines==["hey moron","uh oh","trouble","oh no","the part where he kills us",
					"kill wheatley"]
		elif reason=="PORTAL":
			lines==["open portal","safe","most importantly","safe testing","warning"]
		elif reason=="CAROLINE":
			lines=["caroline"]
		self.speakline(random.choice(lines))

	def speakline(self,line):
		if line=="die":
			playsound("./speech/die1.wav")
			playsound("./speech/die2.wav")
		else:
			playsound("./speech/"+line+".wav")

	def speak(self,words):
		s=pyttsx3.init()
		s.say(words)
		s.runAndWait()
		
	def hello(self):
		lines=["can you hear me","is anyone there"]
		self.speakline(random.choice(lines))

	def whee(self):
		self.speakline("i have a surprise for you")
		spin()
		lines=["whee","fling"]
		self.speakline(random.choice(lines))
		r=askyesno("Aperture AntiVirus","Do you want AAV to fix your PC?")
		if r==6:
			spinrestore()
			self.speakline("i already fixed it")
		else:
			self.speakline("trapped1")
			self.speakline("trapped2")
			spinrestore()

	def blah(self):
		self.speakline("blah1")
		self.speakline("blah2")
		self.speakline("blah3")
		self.speakline("blah4")
		self.speakline("blah5")
		self.speakline("blah6")
		self.speakline("blah7")

	def yesno(self,title,message):
		return askyesno(title,message)

	def fixpc(self):
		self.speakline("uh oh")
		result=self.yesno("Aperture AntiVirus","VIRUS DETECTED !! \n\n Would you like AAV to fix your PC?")
		if result==6:
			self.speakline("i already fixed it")
			time.sleep(1)
			self.speakline("hahaha")
			self.speakline("heheh")
		else:
			self.speakline("good")

	def motivate(self):
		self.speakline("encouragement")
		os.system("explorer")
		self.speakline("file deleted")

from modules.tasks import spin,spinrestore,getUsbList,askyesno,SysTrayIcon
from playsound import playsound
import threading,pyttsx3,win32file,random,time,os,webbrowser,pythoncom,sys
import PyHook3 as pyHook

class GLaDOS:
	def __init__(self):
		hover_text="GLaDOS"
		def surprise(sysTrayIcon):
			self.nag()
		def bye(sysTrayIcon):
			self.speakline("dont press that button","goodbye","dont come back","murder")
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
		
	def speakline(self,*args):
		if len(args)==0:
			line="can you hear me"
		else:
			line=random.choice(args)
		playsound("./speech/"+line+".wav")
		self.logged=[]

	def speak(self,words):
		s=pyttsx3.init()
		s.say(words)
		s.runAndWait()

	def usbSpy(self):
		current_list=getUsbList()
		old_list=current_list
		while True:
			current_list=getUsbList()
			if len(current_list)>len(old_list):
				self.speakline("dont plug it in","dont plug it in2",
								"dont plug it in3","dont plug it in4")
			elif len(current_list)<len(old_list):
				self.speakline("you broke it","file deleted","good","really ok","hero")
			old_list=current_list
			
	def keyboardSpy(self):
		self.logged=[]
		hm=pyHook.HookManager()
		hm.KeyDown=self.OnKeyboardEvent
		hm.HookKeyboard()
		pythoncom.PumpMessages()

	def OnKeyboardEvent(self,event):
		self.logged.append(str(event.Key))
		self.check_keys()
		return True

	def check_keys(self):
		fullstring=""
		for key in self.logged:
			lines=[]
			
			fullstring=fullstring+key
			fullstring=fullstring.replace("Lshift","")
			fullstring=fullstring.replace("Rshift","")
			fullstring=fullstring.replace("Capital","")
			if "APERTURE" in fullstring.upper():
				self.speakline("oh my facility","good people dont end up here")
			elif "CAVE" in fullstring.upper() and "JOHNSON" in fullstring.upper():
				self.speakline("oh i like this guy","goodbye sir","burning people","yes sir")
			elif "GLADOS" in fullstring.upper():
				self.speakline("hello","hello2",
				   "are you doing that just to aggravate me",
				   "did you do that on purpose","excellent",
				   "good job","good","i hate you so much",
				   "i hope that was a joke","just stop it already",
				   "no","oh hi","oh its you","really ok","time out",
				   "wasting my time","wow","yeah","yes","yes2",
				   "you dont need to do that")
			elif "TWITTER" in fullstring.upper():
				self.speakline("bird1","bird2")
			elif "TURRET" in fullstring.upper():
				self.speakline("turrets","spherical","marry")
			elif "CAKE" in fullstring.upper():
				self.speakline("all the cake is gone","before any cake","cake will be served",
					"cake and grief counselling","you will be baked","for your cake",
					"cut the cake","whos gonna make the cake","there really was a cake")
			elif "WHEATLEY" in fullstring.upper():
				self.speakline("hey moron","uh oh","trouble","oh no","the part where he kills us",
						"kill wheatley","not coming back")
			elif "PORTAL" in fullstring.upper():
				self.speakline("open portal","safe","most importantly","safe testing","warning")
			elif "CAROLINE" in fullstring.upper():
				self.speakline("caroline","being caroline")
			elif "CHELL" in fullstring.upper():
				self.speakline("dangerous mute lunatic","dangerous mute lunatic","killing you is hard",
						"you win")
			elif len(self.logged)>100:
				self.logged=[]
		
	def nag(self):
		n=random.randint(0,5) # increase upper bound when adding nags with multiple consecutive lines
		if n==0:
			# add all one-liner nags to this call
			self.speakline("can you hear me","is anyone there",
							"youre not a good person","present",
							"subject name here","why do i hate you")
		elif n==1: # just thinking about all the ways in which humans can die
			self.speakline("die1")
			self.speakline("die2")
		elif n==2: # blah blah blah blah blah (glados is a great singer)
			self.speakline("blah1")
			self.speakline("blah2")
			self.speakline("blah3")
			self.speakline("blah4")
			self.speakline("blah5")
			self.speakline("blah6")
			self.speakline("blah7")
		elif n==3: # the difference between us is that i can feel pain
			self.speakline("pain1")
			self.speakline("pain2")
		elif n==4: # gibberish
			self.speakline("gib1")
			self.speakline("gib2")
			self.speakline("gib3")
			self.speakline("gib4")
			self.speakline("gib5")
			self.speakline("gib6")

	def whee(self):
		self.speakline("i have a surprise for you")
		spin()
		self.speakline("whee","fling","turkey leg")
		r=askyesno("Aperture AntiVirus","Do you want AAV to fix your PC?")
		if r==6:
			spinrestore()
			self.speakline("i already fixed it")
		else:
			self.speakline("trapped1")
			self.speakline("trapped2")
			spinrestore()

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

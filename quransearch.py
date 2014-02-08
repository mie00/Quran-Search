#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	Copyright 2013 Mohamed Ibrahim Elawadi
	
	Email: mielawadi@gmail.com

	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import re
from xml.dom import minidom
import py2exe
sowar=[u"الفاتحة",u"البقرة",u"آل عمران",u"النساء",u"المائدة",u"الأنعام",u"الأعراف",u"الأنفال",u"التوبة",u"يونس",u"هود",u"يوسف",u"الرعد",u"إبراهيم",u"الحجر",u"النحل",u"الإسراء",
u"الكهف",u"مريم",u"طه",u"الأنبياء",u"الحج",u"المؤمنون",u"النور",u"الفرقان",u"الشعراء",u"النمل",u"القصص",u"العنكبوت",u"الروم",u"لقمان",u"السجدة",u"الأحزاب",u"سبأ",u"فاطر",
u"يس",u"الصافات",u"ص",u"الزمر",u"غافر",u"فصلت",u"الشوري",u"الزخرف",u"الدخان",u"الجاثية",u"الأحقاف",u"محمد",u"الفتح",u"الحجرات",u"ق",u"الذاريات",u"الطور",u"النجم",u"القمر",
u"الرحمن",u"الواقعة",u"الحديد",u"المجادلة",u"الحشر",u"الممتحنة",u"الصف",u"الجمعة",u"المنافقون",u"التغابن",u"الطلاق",u"التحريم",u"الملك",u"القلم",u"الحاقة",u"المعارج",
u"نوح",u"الجن",u"المزمل",u"المدثر",u"القيامة",u"الإنسان",u"المرسلات",u"النبأ",u"النازعات",u"عبس",u"التكوير",u"الانفطار",u"المطففين",u"الانشقاق",u"البروج",u"الطارق",u"الأعلي",
u"الغاشية",u"الفجر",u"البلد",u"الشمس",u"الليل",u"الضحي",u"الشرح",u"التين",u"العلق",u"القدر",u"البينة",u"الزلزلة",u"العاديات",u"القارعة",u"التكاثر",u"العصر",u"الهمزة",
u"الفيل",u"قريش",u"الماعون",u"الكوثر",u"الكافرون",u"النصر",u"المسد",u"الإخلاص",u"الفلق",u"الناس"]
swords=[u"وَابِلٌ",u"وَاحِدًا",u"وَاحِدَةً",u"وَاحِدَةٌ",u"وَاحِدَةٍ",u"وَاحِدٌ",u"وَاحِدٍ",u"وَادِيًا",u"وَادِ",u"وَادٍ",u"وَارِدُهَا",u"وَارِدَهُمْ",u"وَارِدُونَ",u"وَازِرَةٌ",u"وَاسِعًا",u"وَاسِعَةً",u"وَاسِعَةٌ",u"وَاسِعَةٍ",u"وَاسِعٌ",
u"وَاسِعُ",u"وَاصِبًا",u"وَاصِبٌ",u"وَاعَدْنَا",u"وَاعِيَةٌ",u"وَاقِعٌ",u"وَاقِعٍ",u"وَاقٍ",u"وَالٍ",u"وَبَالَ",u"وَبِيلًا",u"وَجَبَتْ",u"وَجَدَ",u"وُجِدَ",u"وَجِلَةٌ",u"وَجِلَتْ",u"وَجِلُونَ",u"وِجْهَةٌ",u"وَجْهَكَ",u"وَجْهِكَ",
u"وَجْهَهَا",u"وَجْهِهَا",u"وَجْهَهُ",u"وَجْهُهُ",u"وَجْهِهِ",u"وَجْهِيَ",u"وَجْهَ",u"وَجْهُ",u"وَجْهِ",u"وُجُوهًا",u"وُجُوهَكُمْ",u"وُجُوِهَكُمْ",u"وُجُوهَهُمُ",u"وُجُوهَهُمْ",u"وُجُوهُهُم",u"وُجُوهُهُمْ",u"وُجُوهِهِم",u"وُجُوهِهِمُ",u"وُجُوهِهِمْ",
u"وُجُوهٌ",u"وُجُوهُ",u"وُجُوهِ",u"وَجِيهًا",u"وَحْدَهُ",u"وَحْيًا",u"وَحْيُهُ",u"وَحْيٌ",u"وَدًّا",u"وُدًّا",u"وَدَّتْ",u"وَدَّعَكَ",u"وَرَاءَكُمْ",u"وَرَاءَهُمْ",u"وَرَائِكُمْ",u"وَرَائِهِ",u"وَرَاءَهُ",u"وَرَاءِ",u"وَرَاءَ",
u"وَرَائِهِمْ",u"وَرَائِي",u"وَرَثَةِ",u"وَرِثُوا",u"وِرْدًا",u"وَرْدَةً",u"وَرَدُوهَا",u"وَرَدَ",u"وَرَقَةٍ",u"وَرَقِ",u"وَزَرْعٌ",u"وِزْرَكَ",u"وَزَرَ",u"وِزْرَ",u"وَزْنًا",u"وَّزَنُوهُمْ",u"وَزِيرًا",u"وَسَطًا",u"وَسِعَتْ",u"وَسِعْتَ",u"وُسْعَهَا",
u"وَسَقَ",u"وَصَّاكُم",u"وَصَّاكُمُ",u"وَصَّاكُمْ",u"وَصْفَهُمْ",u"وَصَّلْنَا",u"وَصَّى",u"وَصَّىٰ",u"وَصِيَّةً",u"وَصِيَّةٍ",u"وَصِيلَةٍ",u"وَصَّيْنَا",u"وَطْئًا",u"وَطَرًا",u"وِعَاء",u"وَعْدًا",u"وَعَدْتَنَا",u"وَعَدْتَهُمْ",u"وَعَدَكُمُ",u"وَعَدَكُمْ",u"وَعْدَكَ",
u"وَعَدْنَاهُمْ",u"وَعَدْنَاهُ",u"وَعَدَنَا",u"وُعِدْنَا",u"وَعَدَهَا",u"وَعْدَهُ",u"وَعْدُهُ",u"وَعْدِهِ",u"وَعَدُوهُ",u"وَعَدَ",u"وَعْدٌ",u"وَعْدَ",u"وَعْدُ",u"وُعِدَ",u"وِفَاقًا",u"وَفْدًا",u"وَفَّىٰ",u"وَقَارًا",u"وَقَبَ",u"وَقْرًا",u"وِقْرًا",
u"وَقْرٌ",u"وَقَعَتِ",u"وَقَعَ",u"وُقِفُوا",u"وَقُودُهَا",u"وَقُودُ",u"وَكَّلْنَا",u"وُكِّلَ",u"وَكِيلًا",u"وَكِيلٌ",u"وِلْدَانٌ",u"وَلَدًا",u"وُلِدْتُ",u"وَلَدْنَهُمْ",u"وَلَدِهِ",u"وَلَدٌ",u"وَلَدٍ",u"وَلَدَ",u"وُلِدَ",u"وَلَّوْا",u"وَلَّوْاْ",
u"وَلَّيْتُمْ",u"وَلِيجَةً",u"وَلِيدًا",u"وَلِيُّكُمُ",u"وَلِيُّهُ",u"وَلِيِّي",u"وَلِيِّيَ",u"وَلِيٌّ",u"وَلِيٍّ",u"وَلِيُّ",u"وَهَّاجًا",u"وَهَبَتْ",u"وَهَبْنَا",u"وَهَبَ",u"وَهَبْ",u"وَهْنًا",u"وَهَنُوا",u"وَهَنَ",u"وَهْنٍ",u"وَيْكَأَنَّهُ",u"وَيْكَأَنَّ",
u"وَيْلَتَنَا",u"وَيْلَتَىٰ",u"وَيْلَكُمْ",u"وَيْلَكَ",u"وَيْلَنَا",u"وَيْلٌ",u"وَالِدِهِ",u"وَالِدٌ",u"وَالِدَةٌ"]


hq=minidom.parse('quran-simple.xml').lastChild
hh=[]
for i in range(1,len(hq.childNodes),2):
	sur=hq.childNodes[i]
	sua=[]
	for j in range(1,len(sur.childNodes),2):
		sua.append(sur.childNodes[j].attributes['text'].value.split(' '))
	hh.append(sua)
	
wrds={}
for i0 in range(len(hh)):
	for i1 in range(len(hh[i0])):
		for i2,i3 in enumerate(hh[i0][i1]):
			cwrd=i3
			if not cwrd[0] in map(unichr,range(0x620,0x63b))+map(unichr,range(0x641,0x64b)):
				cwrd=cwrd[1:]
			if cwrd[0]==u'و' and not cwrd in swords:
				cwrd=cwrd[1:]
				if not cwrd[0] in map(unichr,range(0x620,0x63b))+map(unichr,range(0x641,0x64b)):
					cwrd=cwrd[1:]
			if cwrd in wrds:
				if sowar[i0] in wrds[cwrd]:
					wrds[cwrd][sowar[i0]].append(i1+1)
				else:
					wrds[cwrd][sowar[i0]]=[i1+1]
			else:
				wrds[cwrd]={sowar[i0]:[i1+1]}
def sorting(wrd):
	w0=''
	w1=''
	for i in wrd:
		if i in map(unichr,range(0x620,0x63b))+map(unichr,range(0x641,0x64b)):
			w0+=i
		else:
			w1+=i
	return w0+'0000000000000'+w1
kk=wrds.keys()
kk.sort(key=sorting)

import gtk as Gtk

class HH(Gtk.HBox):
	def __init__(self,word,rf,arr=None):
		Gtk.HBox.__init__(self,homogeneous=False)
		self.word=word
		self.rf=rf
		if arr==None:
			self.mw=mainword = Gtk.ToggleButton(word)
			wdict=wrds[word]
		else:
			self.mw=mainword = Gtk.ToggleButton(' ')
			wdict=arr
		mainword.connect("toggled", self.maintoggle)
		self.pack_end(mainword, False, False,0)
		swr=wdict.keys()
		swr.sort(key=lambda x: sowar.index(x))
		self.act=[]
		self.wrds=[]
		self.wrdt=[]
		self.finished=1
		for i in swr:
			self.wrds.append(Gtk.ToggleButton(i))
			self.wrds[-1].connect("toggled", self.stoggle,len(self.wrdt))
			self.pack_end(self.wrds[-1], False, False,0)
			self.wrdt.append([])
			for j in wdict[i]:
				self.wrdt[-1].append(Gtk.ToggleButton(str(j)))
				self.wrdt[-1][-1].connect("toggled", self.toggle,sowar.index(i),j)
				self.pack_end(self.wrdt[-1][-1], False, False,0)
	def maintoggle(self,wid):
		fin=0
		if self.finished:
			fin=1
			self.finished=0
		if wid.get_active():
			for i in self.wrds:
				i.set_active(True)
		else:
			for i in self.wrds:
				i.set_active(False)
		if fin:
			self.finished=1
			self.rf()
	def stoggle(self,wid,a):
		fin=0
		if self.finished:
			fin=1
			self.finished=0
		if wid.get_active():
			for i in self.wrdt[a]:
				i.set_active(True)
		else:
			for i in self.wrdt[a]:
				i.set_active(False)
		if fin:
			self.finished=1
			self.rf()
	def toggle(self,wid,a,b):
		if wid.get_active():
			self.act.append((a,b))
		else:
			del self.act[self.act.index((a,b))]
		if self.finished:
			self.rf()
class Main(Gtk.Window):	
	def __init__(self):
		#Gtk.Window.__init__(self, title="Hello World")
		Gtk.Window.__init__(self)
		self.set_title('Qurans Search by:mielawadi@gmail.com')
		self.maximize()
		box0=Gtk.VBox(homogeneous=False)
		self.add(box0)
		
		self.text = Gtk.Entry()
		self.text.connect("activate", self.search,self.text)
		box0.pack_start(self.text, False, False, 0)
		bt=Gtk.Button("إبحث")
		bt.connect("clicked", self.search,self.text)
		box0.pack_start(bt, False, False, 0)
		bt=Gtk.ToggleButton("عرض")
		bt.connect("toggled", self.togall)
		box0.pack_start(bt, False, False, 0)
		
		paned=Gtk.VPaned()
		box0.pack_start(paned, True, True, 0)
		
		self.sw1=scrolledwindow1 = Gtk.ScrolledWindow()
		scrolledwindow1.set_placement(Gtk.CORNER_TOP_RIGHT)
		self.vb=Gtk.Viewport()
		self.vb.set_direction(Gtk.TEXT_DIR_RTL)
		self.res=Gtk.VBox()
		self.vb.add(self.res)
		scrolledwindow1.add(self.vb)
		paned.pack1(scrolledwindow1, False, False)
				
		scrolledwindow2 = Gtk.ScrolledWindow()
		scrolledwindow2.set_placement(Gtk.CORNER_TOP_RIGHT)
		self.textview = textview0 = Gtk.TextView()
		textview0.set_wrap_mode(Gtk.WRAP_WORD)
		textview0.set_editable(False)
		textview0.set_left_margin(5)
		textview0.set_right_margin(5)
		textview0.set_can_focus(True)
		textview0.set_pixels_above_lines(8)
		textview0.set_pixels_below_lines(8)
		self.text = textview0.get_buffer()
		scrolledwindow2.add(textview0)
		paned.pack2(scrolledwindow2, False, False)
		
		self.boxes=[]
	def togall(self,wid):
		
			for i in self.boxes:
				i.finished=0
				i.mw.set_active(wid.get_active())
				i.finished=1
			self.refresh()
	def getres(self,sr):
		resarr=[]
		for i in kk:
			tn=0
			for j in sr:
				if not j in i[tn:]:
					break
				else:
					tn+=i[tn:].index(j)+1
			else:
				resarr.append(i)
		return resarr
	def flatten(self,resarr):
		tarr=set()
		for k in resarr:
			for i in wrds[k]:
				for j in wrds[k][i]:
					tarr|=set([(sowar.index(i),j)])
		return tarr
	def unflatten(self,resarr):
		tarr={}
		for k in resarr:
			if sowar[k[0]] in tarr:
				tarr[sowar[k[0]]].append(k[1])
			else:
				tarr[sowar[k[0]]]=[k[1]]
		return tarr
	def search(self,asd,win):
		self.res.destroy()
		self.boxes=[]
		self.res=Gtk.VBox()
		self.vb.add(self.res)
		sr=win.get_text().decode('utf-8').strip()
		res=None
		if sr=='':
			pass
		if ' ' in sr:
			sr=sr.split()
			for i in sr:
				resarr=self.getres(i)
				res1=self.flatten(resarr)
				if res==None:
					res=res1
				else:
					res=res&res1
			res=self.unflatten(res)
			keys=res.keys()
			keys.sort(key=lambda x: sowar.index(x))
			for i in keys:
				self.boxes.append(HH(i,self.refresh,arr={i:res[i]}))
				self.res.pack_start(self.boxes[-1], False, False, 0)
			self.res.show_all()
		else:

			resarr=self.getres(sr)		
			for i in resarr:
				self.boxes.append(HH(i,self.refresh))
				self.res.pack_start(self.boxes[-1], False, False, 0)
			self.res.show_all()
	def refresh(self):
		a=''
		for i in self.boxes:
			for j in sorted(i.act):
				a+='%s:%i: '%(sowar[j[0]],j[1])+' '.join(hh[j[0]][j[1]-1])+'\n'
		self.text.set_text(a)
if __name__ == "__main__":
	main1=Main()
	main1.connect("delete-event", Gtk.main_quit)
	main1.show_all()
	Gtk.main()

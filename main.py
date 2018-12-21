
import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout

#untuk close calculator
Builder.load_string(""" 
<MyWidget>:
    BoxLayout:
        Button:
            text: "Close"
            on_release: app.stop()
""")

        

class Calculator(BoxLayout): #tata letak kotak

	def backward(self, express): # berfungsi untuk menghapus 
		if express:
			self.display.text = express[:-1]

	def calculate(self, express):# berfungsi untuk melakukan semua operasi yang ada di kalkulator
		if not express: return

		try:
			self.display.text = str( eval(express) )
		except Exception:# apabila operator di klik dengan sembarangan maka akan muncul tulisan eror
			self.display.text = 'error'


class CalculatorApp(App):
	title = 'calculator' #judul app
	icon = 'icon.png' #gambar / icon app

	def build(self):#untuk menampilkan boxlayout
		return Calculator()

	def on_pause(self):
		return True
	



if __name__ in ('__main__', '__android__'):# berfungsi untuk menjalankan class calculatorApp
	CalculatorApp().run()

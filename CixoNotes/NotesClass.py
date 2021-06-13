'''	
	Modul z klasa notatki w aplikacji
	Przechowuje notatke oraz jej date
	Wymaga konfiguracji przed rozpoczeciem uzywania
	config to klasa z pliku konfiguracyjnego, natomiast language to klasa Language
	funkcje robia to, na co wskazuje ich nazwa
	 * setConfig - ustawia konfiguracje klasy
	 * setDate - ustawia date notatki, mozna ta date podac jako obiekt
				 date time, w tedy as_string=False, lub jako string (domyslnie)
				 w tedy podajemy ja jako string w formacie z pliku konfiguracyjnego
	 * getDate - podobnie jak set date, z ta roznica ze wzraca obiekt lub (domyslnie) string
	 * display - wyswietla na ekranie notatke przechowywana w obiekcie
	 * setText - ustawia tekst notatki na ten z parametru
	 * addText - dodaje do tekstu notatki kolejny element z parametru
	 * getText - wzraca tekst notatki
'''

from . import *

class NotesClass:
	config = None
	language = None
	
	def setConfig(new_config, new_language) -> None:
		__class__.config = new_config
		__class__.language = new_language
	
	def __init__(self):
		self.date = None
		self.text = None
		
	def setDate(self, new_date : datetime, as_string = True) -> None:
		if as_string:
			self.date = datetime.strptime(new_date, self.config.DATE_FORMAT).date()
		else:
			self.date = new_date
		
	def getDate(self, as_string : bool = True):
		if as_string:
			return self.date.strftime(self.config.DATE_FORMAT)
		else:
			return self.date
		
	def setText(self, new_text : str) -> None:
		self.text = new_text if new_text is not None and new_text.split() != [] else None
		
	def addText(self, new_text : str) -> None:
		self.text = self.text + "\n" + new_text
		
	def getText(self) -> str:
		return self.text
		
	def display(self) -> None:
		print (\
			self.language.DISPLAY_TEMPLATE.format(\
				date = self.getDate(),\
				text = self.text if self.text is not None else self.language.NO_NOTES_TEXT\
			)\
		)

'''	
	Modul z klasa notatki w aplikacji
	Przechowuje notatke oraz jej date
	Wymaga konfiguracji przed rozpoczeciem uzywania
	config to klasa z pliku konfiguracyjnego, natomiast language to klasa Language
	funkcje robia to, na co wskazuje ich nazwa
	 * set_config - ustawia konfiguracje klasy
	 * set_date - ustawia date notatki, mozna ta date podac jako obiekt
				 date time, w tedy as_string=False, lub jako string (domyslnie)
				 w tedy podajemy ja jako string w formacie z pliku konfiguracyjnego
	 * get_date - podobnie jak set date, z ta roznica ze wzraca obiekt lub (domyslnie) string
	 * display - wyswietla na ekranie notatke przechowywana w obiekcie
	 * set_text - ustawia tekst notatki na ten z parametru
	 * add_text - dodaje do tekstu notatki kolejny element z parametru
	 * get_text - wzraca tekst notatki
'''

from datetime import datetime

class notes_class:
	config = None
	language = None
	
	def set_config(new_config, new_language) -> None:
		__class__.config = new_config
		__class__.language = new_language
	
	def __init__(self):
		self.date = None
		self.text = None
		
	def set_date(self, new_date : datetime, as_string = True) -> None:
		if as_string:
			self.date = datetime.strptime(new_date, self.config.get("cixo-notes", "DATE_FORMAT")).date()
		else:
			self.date = new_date
		
	def get_date(self, as_string : bool = True):
		if as_string:
			return self.date.strftime(self.config.get("cixo-notes", "DATE_FORMAT"))
		else:
			return self.date
		
	def set_text(self, new_text : str) -> None:
		self.text = new_text if new_text is not None and new_text.split() != [] else None
		
	def add_text(self, new_text : str) -> None:
		self.text = self.text + "\n" + new_text
		
	def get_text(self) -> str:
		return self.text
		
	def display(self) -> None:
		print (\
			self.language.get("cixo-notes", "DISPLAY_TEMPLATE").format(\
				date = self.get_date(),\
				text = "\n" + (self.text if self.text is not None else self.language.get("cixo-notes", "NO_NOTES_TEXT"))\
			)\
		)

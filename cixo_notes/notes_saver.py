'''
	Modul z klasa odpowiadajaca za zapis i odczyt notatek w systemie plikow
	Funckje jakie rezlizuje to:
	 * odczyt notatki
	 * zapis notatki
	 * kasowanie notatki
	 * modyfikacja notatki
	Realizuje to poprzez nastepujace funkcje:
	 * __init__ - resetuje klase tworzac nowy pusty obiekt
	 * read_notes - odczytuje notatke z systemu pliko
	 * write_notes - tworzy nowa notatke
	 * add_to_notes - dodaje nowa tresc do notatki
	 * save_changes - zapisuje zmiany do systemu plikow
	 * drop_notes - kasuje notatke
	 * set_notes - ustawia obiekt notatki jaki przechowuje na ten z argumentu
	 * set_path - ustawia sciezke do pliku z notatka
	 * reset - zmienia wewnatrzny obiekt notatki na pusty
'''

import os
from pathlib import Path
from datetime import datetime
from .notes_class import notes_class

class notes_saver:
	def __init__(self):
		self.reset();
	
	def read_notes(self) -> None:
		if self.file_path.exists():
			try:
				with self.file_path.open("r") as notes_file:
					self.notes.set_text(notes_file.read())
			except:
				print(self.notes.language.get("cixo-notes", "FILE_READWRITE_ERROR"))
	
	def write_notes(self) -> None:
		if self.notes.get_text() is not None:
			if input(self.notes.language.get("cixo-notes", "NOTES_EXIST")) != self.notes.language.get("cixo-notes", "CONFIRM_LETTER"):
				return 
			self.notes.set_text(None)
		
		while self.notes.get_text() is None:	
			self.notes.set_text(input(self.notes.language.get("cixo-notes", "CREATE_NEW_NOTE")))
			
		self.save_changes()
		
	def add_to_notes(self) -> None:
		if self.notes.get_text() is None:
			print(self.notes.language.get("cixo-notes", "NOTES_NOTEXIST"))
			self.write_notes()
			return
			
		self.notes.add_text(input(self.notes.language.get("cixo-notes", "ADD_TO_NOTE")))
		self.save_changes()
			
	def save_changes(self) -> None:
		if self.notes.get_text() is not None:
			try:
				with self.file_path.open("w") as notes_file:
					notes_file.write(self.notes.get_text())
			except:
				print(self.notes.language.get("cixo-notes", "FILE_READWRITE_ERROR"))
		else:
			try:
				self.file_path.unlink()
			except:
				print(self.notes.language.get("cixo-notes", "NO_NOTES_TEXT"))
				
	def drop_notes(self) -> None:
		if input(self.notes.language.get("cixo-notes", "WANT_TO_DELETE")) == self.notes.language.get("cixo-notes", "CONFIRM_LETTER"):
			self.notes.set_text(None)
			self.save_changes()
			
	def set_path(self) -> None:
		self.file_path = Path(self.notes.config.get("cixo-notes", "NOTES_DIRECTORY"), self.notes.get_date())
			
	def set_notes(self, new_notes) -> None:
		self.notes = new_notes
	
	def reset(self) -> None:
		self.file_path = Path()
		self.set_notes(notes_class())

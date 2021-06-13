'''
	Modul z klasa odpowiadajaca za zapis i odczyt notatek w systemie plikow
	Funckje jakie rezlizuje to:
	 * odczyt notatki
	 * zapis notatki
	 * kasowanie notatki
	 * modyfikacja notatki
	Realizuje to poprzez nastepujace funkcje:
	 * __init__ - resetuje klase tworzac nowy pusty obiekt
	 * readNotes - odczytuje notatke z systemu pliko
	 * writeNotes - tworzy nowa notatke
	 * addToNotes - dodaje nowa tresc do notatki
	 * saveChanges - zapisuje zmiany do systemu plikow
	 * dropNotes - kasuje notatke
	 * setNotes - ustawia obiekt notatki jaki przechowuje na ten z argumentu
	 * reset - zmienia wewnatrzny obiekt notatki na pusty
'''

from . import *

class NotesSaver:
	def __init__(self):
		self.reset();
	
	def readNotes(self) -> None:
		if os.path.isfile(self.notes.config.NOTES_DIRECTORY + self.notes.getDate()):
			try:
				notes_file = open(self.notes.config.NOTES_DIRECTORY + self.notes.getDate(), 'r')
				self.notes.setText(notes_file.read())
				notes_file.close()
			except:
				print(self.notes.language.FILE_READWRITE_ERROR)
	
	def writeNotes(self) -> None:
		if self.notes.getText() is not None:
			if input(self.notes.language.NOTES_EXIST) != self.notes.language.CONFIRM_LETTER:
				return 
			self.notes.setText(None)
		
		while self.notes.getText() is None:	
			self.notes.setText(input(self.notes.language.CREATE_NEW_NOTE))
			
		self.saveChanges()
		
	def addToNotes(self) -> None:
		if self.notes.getText() is None:
			print(self.notes.language.NOTES_NOTEXIST)
			self.writeNotes()
			return
			
		self.notes.addText(input(self.notes.language.ADD_TO_NOTE))
		self.saveChanges()
			
	def saveChanges(self) -> None:
		if self.notes.getText() is not None:
			try:
				notes_file = open(self.notes.config.NOTES_DIRECTORY + self.notes.getDate(), "w")
				notes_file.write(self.notes.getText())
				notes_file.close()
			except:
				print(self.notes.language.FILE_READWRITE_ERROR)
		else:
			try:
				os.remove(self.notes.config.NOTES_DIRECTORY + self.notes.getDate())
			except:
				print(self.notes.language.NO_NOTES_TEXT)
				
	def dropNotes(self) -> None:
		if input(self.notes.language.WANT_TO_DELETE) == self.notes.language.CONFIRM_LETTER:
			self.notes.setText(None)
			self.saveChanges()
			
	def setNotes(self, new_notes) -> None:
		self.notes = new_notes
	
	def reset(self) -> None:
		self.setNotes(NotesClass())

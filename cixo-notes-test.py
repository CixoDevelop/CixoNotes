'''
	Testy jednostkowe dla notes_class i notes_saver
	
	Program testow wymaga podawania danych z klawiatury
	z powodu harakteru klasu notes_saver, dziala ona w strumieniu 
	i wymaga ingerencji uzytkownika, mimo to wszyskie jej funckje sa tutaj
	wywolane
'''

import unittest
from configparser import ConfigParser
import cixo_notes

#tworzy sztuczny plik konfiguracji
cixo_notes.config = ConfigParser()
cixo_notes.config.add_section("cixo-notes")
cixo_notes.config.set("cixo-notes", "DATE_FORMAT", "%%Y-%%m-%%d")
cixo_notes.config.set("cixo-notes", "NOTES_DIRECTORY", "./")

class _cixo_notes_testcase(unittest.TestCase):
	def runTest(self):
		self.test_notes_class_clearmake()
		self.test_notes_class_setconfig()
		self.test_notes_class_date()
		self.test_notes_class_text()
		self.test_notes_class_display()
		
		self.test_notes_saver_write()
		self.test_notes_saver_read()
		self.test_notes_saver_add()
		self.test_notes_saver_read()
		self.test_notes_saver_drop()
	
	def test_notes_class_clearmake(self):
		test_notes = cixo_notes.notes_class()
		if test_notes.text is not None or test_notes.date is not None:
			self.fail("Klasa po stworzeniu nie jest pusta")
			
	def test_notes_class_setconfig(self):
		cixo_notes.notes_class.set_config(cixo_notes.config, cixo_notes.language)
		if cixo_notes.notes_class.config is None or cixo_notes.notes_class.language is None:
			self.fail("Ustawianie konfiguracji nie działa")
			
	def test_notes_class_date(self):
		test_notes = cixo_notes.notes_class()
		test_notes.set_date("2020-02-22")
		
		if test_notes.get_date() != "2020-02-22":
			self.fail("Operacje na datach nie działają")
			
			
	def test_notes_class_text(self):
		test_notes = cixo_notes.notes_class()
		test_notes.set_text("UwU")
		if test_notes.get_text() != "UwU":
			self.fail("Nie da się wstawić tekstu")
			
		test_notes.add_text("OwO")
		if test_notes.get_text() != "UwU\nOwO":
			self.fail("Nie da się dodać tekstu")
			
		test_notes.set_text("")
		if test_notes.get_text() is not None:
			self.fail("Brak tekstu to nie None")
			
	def test_notes_class_display(self):
		test_notes = cixo_notes.notes_class()
		test_notes.set_date("2020-02-20")
		test_notes.set_text("UwU")
		test_notes.display()
		
		if input("Czy treść jest wyświetlona poprawnie? (Y/n):") != "Y":
			self.fail("Nie działa wyświetlanie")
			
	def test_notes_saver_write(self):
		test_saver = cixo_notes.notes_saver()
		test_saver.notes.set_date("2020-02-20")
		test_saver.set_path()
		test_saver.read_notes()
		print("Zapisz 'UwU'")
		test_saver.write_notes()
	
	def test_notes_saver_read(self):
		test_saver = cixo_notes.notes_saver()
		test_saver.notes.set_date("2020-02-20")
		test_saver.set_path()
		test_saver.read_notes()	
		test_saver.notes.display()
		
		if input("Czy treść jest wyświetlona poprawnie? (Y/n):") != "Y":
			self.fail("Nie działa zapis/odczyt")
			
	def test_notes_saver_add(self):
		test_saver = cixo_notes.notes_saver()
		test_saver.notes.set_date("2020-02-20")
		test_saver.set_path()
		test_saver.read_notes()	
		print("Zapis 'OwO'")
		test_saver.add_to_notes()
		
	def test_notes_saver_drop(self):
		test_saver = cixo_notes.notes_saver()
		test_saver.notes.set_date("2020-02-20")
		test_saver.set_path()
		test_saver.read_notes()	
		test_saver.drop_notes()
			
_cixo_notes_testcase().runTest()

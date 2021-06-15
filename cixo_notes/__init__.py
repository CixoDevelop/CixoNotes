'''
	Modul importujacy wszyskie moduly w cixo_notes
	jednoczesnie laduje plik konfiguracyjny z tekstami do language
	jak i proboje zaladowac konfiguracje uzytkownika do config
'''

import os, sys

from pathlib import Path
from configparser import ConfigParser
from datetime import datetime
from .notes_class import notes_class
from .notes_saver import notes_saver

language = ConfigParser()
language.read(str(Path(Path(__file__).parents[0], "language.ini")))

config = ConfigParser()
config.read(str(Path(Path.home(), ".config/cixo-notes.ini")))


#jak plik nie jest plawidlowy to usun go
if not "cixo-notes" in config.sections():
	config = None

import datetime



class Notes:
    notesList = []

    def __init__(self):
        Notes.notesList.append(dict(noteid='id', txt='Заметка', tag='Тэги', Notedt="Дата и время изменения"))

    def addNote(txt, tag=None):
        noteid = len(Notes.notesList)
        if tag is None:
            tag = []
        else:
            tag = list(map(lambda x: x.strip(), tag.split(',')))
        d = dict(noteid=noteid, txt=txt, tag=tag, Notedt=Notes.getDT())

        Notes.notesList.append(d)

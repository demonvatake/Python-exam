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


    def listNotes():
        for c in Notes.notesList:
            print(*c.values(), sep='   ')

    def getDT():
        dt_now = datetime.datetime.now()
        dt_string = dt_now.strftime('%d/%m/%y %H:%M:%S')
        return dt_string

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

    def editNotes(noteid):
        for i in range(1, len(Notes.notesList)):
            if int(Notes.notesList[i]['noteid']) == noteid:
                break
        print("Введите, что будем редактировать: текст заметки(1), теги(2) ", end='')
        chid = int(input().strip())
        match chid:
            case 1:
                print("Введите текст заметки: ", end='')
                Notes.notesList[i]['txt'] = input().strip()
                Notes.notesList[i]['Notedt'] = Notes.getDT()

                print("Текст заметки изменен")
            case 2:
                print("Введите теги через запятую: ", end='')

                Notes.notesList[i]['tag'] = list(Notes.notesList[i]['tag'])
                Notes.notesList[i]['tag'] = list(map(lambda x: x.strip(), input().split(',')))
                Notes.notesList[i]['Notedt'] = Notes.getDT()

                print("Тэги изменены")
            case _:
                print("Неверная команда")


    def delNotes(noteid):
        for i in range(1, len(Notes.notesList)):
            if int(Notes.notesList[i]['noteid']) == noteid:
                del Notes.notesList[i]
                print("Удалено успешно")
                break
from os import system
import json

class StudentGrades:
    data = []
    studrec = {}
    def __init__(self):
        try:
            self.UploadGrades()
        except:
            self.data = []
        self.MainMenu()
    def MainMenu(self):
        while True:
            self.ClearScreen()
            # display options
            #
            choice = input('''
                M A I N   M E N U
                -----------------
                [A] Input Grades
                [B] Display Grades
                [C] Student List
                [X] Exit
                -----------------
                Choose: ''')

            if choice in ['A', 'a']:
                self.InputGrades()
            elif choice in ['B', 'b']:
                self.DisplayGrades()
            elif choice in ['C', 'c']:
                self.StudentList()
            elif choice in ['X', 'x']:
                self.SaveGrades()
                break
    def InputGrades(self):
        self.ClearScreen()
        self.showHeading('GRADE INPUT SCREEN')
        while True:
            studrec = {}
            idno = ''
            i_rec = True
            while i_rec == True:
                idno = input('Enter student ID: ')
                if idno == 'x' or idno == 'X':
                    break
                elif idno[:4].isdigit() == False or idno[5:10].isdigit() == False or idno[4] != "-" or idno[10:] != "" or len(idno) != 10:
                    i_rec = True
                else:
                    i_rec = False
            if idno == 'x' or idno == 'X':
                break
            # check if ID is already existing
            foundID = False
            recno = 0
            for rec in self.data:
                if rec['idnum'] == idno:
                    studrec = rec
                    foundID = True
                    grades = rec['grades']
                    break
                recno += 1               
            if not foundID:
                studrec['idnum'] = idno
                if input != 'x' or input != 'X':
                    studrec['name'] = input('Enter student name: ')
                elif input == 'x' or input == 'X':
                    break
                grades = {}
            # input grades
            while True:
                try:
                    sg = str(input('Enter subject & grade separated by space: '))
                    if sg == 'x' or sg == 'X':
                        break
                    lsg = sg.split(' ')
                    grades.update({str(lsg[0]): float(lsg[1])})
                except:
                    print('\t\t\tINVALID ENTRY')
            studrec['grades'] = grades
            if foundID:
                self.data[recno] = studrec
            else:
                self.data.append(studrec)
    def DisplayGrades(self):
        self.ClearScreen()
        self.showHeading('GRADES DISPLAY SCREEN')
        if len(self.data) == 0:
            print('\t\t\tTHERE IS NO RECORD !')
        else:
            id = input('enter student no.: ')
            for i in range(len(self.data)):
                if id == self.data[i]['idnum']:
                    print(' Name: ', self.data[i]['name'], '\n', 'ID: ', self.data[i]['idnum'])
                    print('\tSubject', '    Grades')
                    #print('\t-----', '     -----')
                    if len(self.data[i]['grades']) == 0:
                        print('No Grades')
                    else:
                        for r in self.data[i]['grades']:
                           print('{0:9}{1:<10}{2:<20}'.format('', r, self.data[i]['grades'][r]))

        self.showMessage('Press enter key ...')
    def StudentList(self):
        self.ClearScreen()
        self.showHeading('STUDENT LIST SCREEN')
        print('{0:6}{1:<30}{2:<20}'.format('','NAME','ID NUMBER'))
        for i in range(len(self.data)):
            print('{0:3d}. {1:<30s} {2:<20s}'.format(i+1, self.data[i]['name'], self.data[i]['idnum']))
            #print(i+1,self.data[i]['name'],'\t\t',self.data[i]['idnum'])
        self.showMessage('Press enter key ...')
    def UploadGrades(self):
        fp = open('grades.json', 'r')
        self.data = json.load(fp)
        fp.close()
    def SaveGrades(self):
        fp = open('grades.json', 'w')
        fp.write(json.dumps(self.data, separators=(',', ' : '), indent = 2))
        fp.close()
    def ClearScreen(self):
        system('cls')
    def showMessage(self, msg):
        input(msg)
    def showHeading(self, heading):
        print(heading + '\n' + len(heading)* '-')

        
if __name__ == '__main__':
    sr = StudentGrades()
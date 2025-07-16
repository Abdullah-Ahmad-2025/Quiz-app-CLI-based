class Quiz:
    def __init__(self, NameP, SerialNoP, GradeP):
        self.__Name = NameP
        self.__SerialNo = SerialNoP
        self.__Grade = GradeP

    def OutName(self):
        return self.__Name

    def OutSerialNo(self):
        return self.__SerialNo

    def OutGrade(self):
        return self.__Grade


    def QuizAnswers(self, Answers):
        correct = 0

        if Answers[0] == 'B':
            correct += 1

        if Answers[1] == 'C':
            correct += 1

        if Answers[2] == 'C':
            correct += 1

        if Answers[3] == 'B':
            correct += 1

        if Answers[4] == 'B':
            correct += 1

        if Answers[5] == 'A':
            correct += 1

        if Answers[6] == 'B':
            correct += 1

        if Answers[7] == 'C':
            correct += 1

        if Answers[8] == 'B':
            correct += 1

        if Answers[9] == 'A':
            correct += 1

        return correct


    def saveResults(self, Candidate, corrects):

        with open('StudentFile.txt','w') as f:
            f.writelines('Name : ' + Candidate.OutName())
            f.write('\n')

            print('Name : ' + Candidate.OutName())

            f.writelines('Serial Number : ' + str(Candidate.OutSerialNo()))
            f.write('\n')

            print('Serial Number : ' + str(Candidate.OutSerialNo()))

            f.writelines('Grade : ' + str(Candidate.OutGrade()))
            f.write('\n')

            print('Grade : ' + str(Candidate.OutGrade()))

            f.writelines('\n')

            line = 'You answered ' + str(corrects) +' correctly out of 10 !\n'

            f.writelines(line)
            print(line)

            percen = ( corrects / 10 ) * 100
            line2 = 'You got '+ str(percen)+'%\n'

            f.writelines(line2)
            print(line2)

            if percen >= 80.0:
                f.write('Excellent performance!')
                print('Excellent performance!')
            elif percen >= 50.0:
                f.write('Great performance!')
                print('Great performance!')
            else:
                f.write('Poor performance')
                print('Poor performance!')

            print('---------------------------------------------------------------------------------------------------------------------')
            print('All your records are saved on the file named StudentFile.txt, If you want to track your performance head towards it!')


name = input('Enter your name : ')
serialNo = int(input('Enter your serial number : '))
grade = int(input('Enter your grade : '))

candidate = Quiz(name, serialNo, grade)

flag = False
answers = [''] * 10

while not flag:
    try:
        # CHANGE YOUR QUESTIONS FROM HERE, INSIDE THE STRING QUOTATIONS
        answers[0] = input(
            '1. What does CPU stands for? \nA) Central Processing Uniform  B) Central Processing Unit  C) Central Peripheral Unit\n').upper()
        print('')
        answers[1] = input('2. Who first stepped on the moon? \nA) Neil Bohr  B) Neil Michael  C) Neil Armstrong\n').upper()
        print('')
        answers[2] = input('3. Which is known as the fourth state of matter? \nA) Gas  B) Liquid  C) Plasma\n').upper()
        print('')
        answers[3] = input("4. 'Time is relative' is said by who? \nA) Newton  B) Einstein  C) Dirac\n").upper()
        print('')
        answers[4] = input('5. Our Universe is ? \nA) Contracting  B) Expanding  C) None\n').upper()
        print('')
        answers[5] = input(
            '6. Internal energy increases with increase in? \nA) Temperature  B) Heat  C) Current \n').upper()
        print('')
        answers[6] = input(
            '7. Galaxies are moving away from us at what to speed of light? \nA) Slower than  B) Faster than  C) Same as\n').upper()
        print('')
        answers[7] = input('8. Time is absolute, said by? \nA) Einstein  B) Maxwell  C) Newton\n').upper()
        print('')
        answers[8] = input('9. Entropy always \nA) Decreases  B) Increases  C) Stays Same\n').upper()
        print('')
        answers[9] = input('10. Photons move at the speed of? \nA) Light  B) Current  C) Human\n').upper()
        print('')

        inp = input('Are these your final answers so that your score may be calculated Y/N ?\n').upper()
        print('')

        if inp == 'Y':
            flag = True

        else:
            flag = False

    except:
        print('Error, please enter valid options. Quiz is halted, please try again !')


correctAnswers = candidate.QuizAnswers(answers)

candidate.saveResults(candidate, correctAnswers)







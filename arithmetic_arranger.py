import re

def arithmetic_arranger(problems, displayAnswer = False):
    line1 = []
    line2 = []
    dashes = []
    answers = []

    if len(problems) > 5: return 'Error: Too many problems.'
    for problem in problems:
        tempList = problem.split()
        first = tempList[0]
        operator = tempList[1]
        second = tempList[2]
        gap = '     '
        dash = '-------'
        if operator != "+" and operator !="-": return "Error: Operator must be '+' or '-'."
        if re.search('[^\d\s+-]', problem): return 'Error: Numbers must only contain digits.'

        if len(first) > 4 or len(second) > 4: return 'Error: Numbers cannot be more than four digits.'

        spacer = gap[0:abs(len(first)-len(second))]

        if(len(first)-len(second) >= 0):
            line1.append('  '+ first)
            line2.append(operator + " " + spacer + second)
            line3 = dash[0:len(first)+2]
            dashes.append(line3)
        else:
            line1.append('  '+spacer+ first)
            line2.append(operator + " " + second)
            line3 = dash[0:len(second)+2]
            dashes.append(line3)


        if operator == "+": 
            answer = str(int(first) + int(second))
        else:
            answer = str(int(first) - int(second))

        answerLine = gap[0:len(line3)-len(answer)] + answer
        answers.append(answerLine)
                        
    formatted = "    ".join(line1) + "\n" +"    ".join(line2) + "\n" + "    ".join(dashes)
    if displayAnswer == True: formatted += "\n" + "    ".join(answers)

    return formatted
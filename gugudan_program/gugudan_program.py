''' 구구단 프로그램 '''

factor1 = 1
factor2 = 1

while factor2 <= 9 and factor1 <= 9:
    string1 = str(factor1)
    string2 = str(factor2)
    if factor2 == 1 and factor1 <= 9:
       print("----------" + string1 + "단" + "----------")
    expression = str(factor1) + " x " + string2 + " = "
    result = (factor1 * factor2)
    stringresult = str(result)
    print(expression + stringresult)
    factor2 = factor2 + 1
    if factor2 == 10:
       factor1 = factor1 + 1
       factor2 = 1
    
print("Done!")
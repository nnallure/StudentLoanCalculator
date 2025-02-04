typeStud = []

loan_amount= []

subRate = []

unsubRate = []

done = False

time = 0

years = []

 

with open('assignment_out.txt','w') as f:

    while done == False:

 

        while True:

            try:

                _typeStud = input("Enter I for Independent or D for Dependent student for this school year: ")

                if _typeStud.upper() != "I" and _typeStud.upper() != "D":

                    raise ValueError

                break

            except ValueError:

                continue

            typeStud.append(_typeStud)

            f.write("Enter I for Independent or D for Dependent student for this school year: %s\n"%_typeStud)

        while True:

            if (time== 0 and typeStud == "D" and loan_amount <= 5500): break

            elif (time == 0 and typeStud == "I" and loan_amount<= 9500): break

        #year 2

            if (time == 1 and typeStud == "D" and loan_amount <= 6500): break

            elif (time == 1 and typeStud == "I" and loan_amount<= 10500): break

        #year3

            if (time >= 2 and typeStud == "D" and loan_amount <= 7500): break

            elif (time >= 2 and typeStud == "I" and loan_amount<= 12500): break

            try:

                _loan_amount = float(input("What is the total loan amount for this school year: "))

                loan_amount.append(_loan_amount)

                f.write("What is the total loan amount for this school year: %d\n"%_loan_amount)

 

                break

            except ValueError:

                continue

        while True:

            try:       

                _subRate = float(input("What is the subsidized loan interest rate: "))

                subRate.append(_subRate)

                f.write("What is the subsidized loan interest rate: %d\n" %_subRate)

                break

            except ValueError:

                continue

        while True:   

            try:

                _unsubRate = float(input("What is the unsubsidized loan interest rate: "))

                unsubRate.append(_unsubRate)

 

                f.write("What is the unsubsidized loan interest rate: %d\n" %_unsubRate)

                break

            except ValueError:

                continue

        while True:

            try:   

                _years = input("Are you attending another year of undergraduate college Y or N: ")

                if _years.upper() != "Y" and _years.upper() != "N":

                    raise ValueError

                if _years == "N":

                        done = True

                if _years == "n":

                        done = True

                years.append(time)

                f.write("Are you attending another year of undergraduate college Y or N:  %d\n" %time)  

                break

            except ValueError:

                continue

        time += 1

   

    subLoanLimit = [3500, 4500, 5500]

 

    totalOwed = 0

    loansList, rateList = [], [] # for part C

 

    for count in years:

        #temp index

        if count < 2:

            ind = count

        else:

            ind = min(2, count)

 

        #calculate unsubsidized loan amt

        unsubAmt = loan_amount[count] - subLoanLimit[ind]

 

        #charge interest on "unsubAmt"

        annual_unsubRate = unsubRate[count]

        monthly_unsubRate = annual_unsubRate/12/100

 

        #month count

        month_count = (4 - count) * 12 +3

 

        for m in range(month_count):

            unsubAmt *= (1 + monthly_unsubRate)

 

       

        totalOwed = totalOwed + unsubAmt + subLoanLimit[ind]

 

        # for part C

        loansList.append(unsubAmt)

        loansList.append(subLoanLimit[ind])

 

        rateList.append(unsubRate[count])

        rateList.append(subRate[count])

 

    print ("Total ammount owed after six months of leaving college: ", "%.2f\n" %(totalOwed))

    f.write("Total ammount owed after six months of leaving college: %.2f\n" %(totalOwed))

    ##########

 

    debtDict = {0: 10,

                7500: 12,

                10000: 15,

                20000: 20,

                40000: 25,

                60000: 30}

 

    for i in debtDict:

        if totalOwed >= i:

            term = debtDict[i]

            break

 

    debtTotal = totalOwed

    interestTotal = 0

 

    for loanList, rate in zip (loansList, rateList):

        interestTotal += loanList *(rate/100)

   

    newRate = interestTotal /debtTotal

    print("Consolidated interest rate is: ", f'{newRate*100:.2f}''%')

    f.write("Consolidated interest rate is: %.2f\n"%newRate*100)

    # !pip install numpy_financial

    import numpy_financial as npf

    payment = npf.pmt(newRate/12, term * 12, totalOwed)* -1

    print('Monthly payment after consolidation:$', f'{payment:.2f}')

    f.write("Monthly payment after consolidation: %.2f\n"%payment)

   

    print("Loan payments continue for this many years: ", term)

    f.write("Loan payments continue for this many years: %d\n"%term)
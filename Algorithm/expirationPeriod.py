import datetime

def solution(today, terms, privacies):
    newToday = datetime.date(int(today.split('.')[0]), int(today.split('.')[1]), int(today.split('.')[2]))
    terms_split = [i.split(' ') for i in terms]
    privacies_split = [j.split(' ') for j in privacies]

    answer = []
    for privacies_value in range(len(privacies_split)):
        for terms_value in range(len(terms_split)):
            
            privacy = privacies_split[privacies_value][1]
            term = terms_split[terms_value][0]
            privacyTime = privacies_split[privacies_value][0].split('.')
            calTerm = int(terms_split[terms_value][1])
            
            if privacy == term:
                privacies_year = int(privacyTime[0])
                privacies_month = int(privacyTime[1])
                privacies_day = int(privacyTime[2])
                
                calMonth = calTerm  + privacies_month
                
                if calMonth > 12:
                    finYear = privacies_year + (calMonth // 12)
                    finMonth = calMonth % 12
                    finDay = privacies_day
                    
                else:
                    finYear = privacies_year
                    finMonth = calMonth
                    finDay = privacies_day
                    
                finDate = datetime.date(finYear, finMonth, finDay)
                    
                if newToday >= finDate:
                    answer.append(privacies_value + 1)

    return answer


# test1
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

# test2
today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

# result
res = solution(today, terms, privacies)
print(res)

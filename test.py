from day0411 import func
# 47,Self-emp-inc,109832,HS-grad,9,Divorced,Exec-managerial,Not-in-family,White,Male,0,0,60,United-States,<=50K
#n  = [[47,'Private' ,'Prof-school', 'Prof-specialty' ,'White' ,'Female', 60,'<=50K']]
# a = func.adult_d(47,'Self-emp-inc','Prof-school','Prof-specialty','White','Female',60,'<=50K')
# print(a)
# workclass, education, occupation, race, sex = func.getDomain()
# print(workclass)
# print(education)
# print(occupation)
# print(race)
# print(sex)
# domain = func.getDomain()
# print(domain[0])

d = func.adult_d(47,'Self-emp-inc','Prof-school','Prof-specialty','White','Female',60)
print(d)
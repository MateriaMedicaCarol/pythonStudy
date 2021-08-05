score=float(input('请输入成绩'))
if score>100:
    print('输入错误')
elif score==100:
    print('奖励一辆bmw')
elif (score>=80) and (score<=99):
    print("奖励电话手表")
elif (score >= 60) and (score <=79):
    print(('奖励书一本'))
elif score<0:
    print("输入错误")
else:
    print('罚站一小时')

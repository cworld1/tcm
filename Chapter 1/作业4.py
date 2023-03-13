car = 5750000
person = 21140000

rel15Gram = car * 15000 * 150
rel15Ton = rel15Gram / 10**6
perIntake = rel15Gram / person

print('北京2015年全年机动车排放废气', rel15Ton, '吨')
print('平均每人吸人废气', perIntake, '克')

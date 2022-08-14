# part 11 from 97
# project 1
# convert km to mile

kms = input('How many KMs do you want to convert? ')
miles = float(kms) / 1.60934
miles = round(miles, 3)

print(f'{kms}km is {miles} miles.')
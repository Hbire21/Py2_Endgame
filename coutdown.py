import datetime


days_left = ((datetime.datetime(2020,1,1) - datetime.datetime.now()).days) - 3
# print (days_left )
months_left = days_left / 30
# print(months_left)
string_form = repr(months_left)
splitted = string_form.split('.')
result = float ("0."+ splitted [1]) 
print(string_form[0],"months and", int (result * 30),"days is left for python2 endgame")


January = 'January'
February = 'February'
March = 'March'
April = 'April'
May = 'May'
June = 'June'
July = 'July'
August = 'August'
September = 'September'
October = 'October'
November = 'November'
December = 'December'
 
def function(month, day):
    if month == January:
            month = September
            day = day + 7
            if day <= 30:
                ed_day = day 
            else:
                month = October
                ed_day = 30 - day  
#Feb 
    elif month == February:
       month = October 
       day = day + 7
       if day < 31:
            ed_day = day 
       else :
            month = November
            ed_day = 30 - day
#Mar            
    elif month == March:
       month = November
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = December
            day = day - 1
            ed_day = 31 - day 
#Apr            
    elif month == April:
       month = December 
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = January
            ed_day = 31 - day
#May
    elif month == May:
       month = February 
       day = day + 7
       if day <= 28:
            ed_day = day 
       else :
            month = March
            day = day - 1           
            ed_day = 31 - day 
#June            
    elif month == June:
       month = March 
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = April
            day = day - 1
            ed_day = 30 - day 
#July            
    elif month == July:
       month = April
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = May
            day = day - 1
            ed_day = 31 - day
#August
    elif month == August:
       month = May
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = June
            ed_day = 30 - day
#Sept            
    elif month == September:
       month = June
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = July
            day = day - 1
            ed_day = 31 - day
#Oct
    elif month == October:
       month = July 
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = August
            ed_day = 30 - day
#Nov           
    elif month == November:
       month = August
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = September
            day = day - 1
            ed_day = 31 - day
#Dec
    elif month == December:
       month = September
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = October
            ed_day = 31 - day
    print("Congratulations!! The Expected date of your baby's delivery is " + str(day)+ ' ' + str(month) + ' :)')
    return "Congratulations!! The Expected date of your baby's delivery is " + str(day)+ ' ' + str(month) + ' :)'
     
# print('Please write full name of the month in which you had your last menstrual period, starting with a capitol letter (e.g January, March, June etc.)')           
# m = input('--> ')
# print('Please write the day of the month (e.g 14, 16, 22 etc)')
# d = input()
# d = int(d)
# function(m, d)
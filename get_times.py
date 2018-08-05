def get_times(time):
    """Turn a digital time (eg. 20:13) to all the various ways this might be represented.
		INPUT: A digital time
		FUNCTION: get(time)
		OUTPUT: A list of all the times
        Time taken: quick, quick"""
    numbers = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '15': 'fifteen', '18': 'eighteen', '20':'twenty', '30':'thirty', '40':'forty', '50':'fifty'}
    temp = time.split(':')
    mtemp = temp[1]
    htemp = temp[0]
    
    time2check = [time, htemp + '.' + mtemp, htemp + mtemp + ' h', htemp + mtemp + 'h']
    if htemp == '00':
        time2check.append(str(int(htemp)) + ':' + mtemp)
        time2check.append(str(int(htemp)) + '.' + mtemp)
        time2check.append(str(int(htemp) + 12) + ':' + mtemp)
        time2check.append(str(int(htemp) + 12) + '.' + mtemp)
    elif int(htemp) > 12:
        time2check.append(str(int(htemp) - 12) + ':' + mtemp)
        time2check.append(str(int(htemp) - 12) + '.' + mtemp)
    elif int(htemp) < 10:
        time2check.append(str(int(htemp)) + ':' + mtemp)
        time2check.append(str(int(htemp)) + '.' + mtemp)
    # Minutes before the half hour
    if int(mtemp) == 0:
        minutes = [" o'clock"]
    elif int(mtemp) == 30:
        minutes = ["half past ", "half-past ", numbers[mtemp] + ' past ', numbers[mtemp] + ' minutes past ']
        minutes = minutes + [numbers[mtemp] + ' after ', numbers[mtemp] + ' minutes after ']
    elif int(mtemp) == 1:
        minutes = [numbers[mtemp[1]] + ' past ', numbers[mtemp[1]] + ' minute past ', mtemp[1] + ' minute past ', mtemp[1] + ' past ']
        minutes = minutes + [numbers[mtemp[1]] + ' after ', numbers[mtemp[1]] + ' minute after ', mtemp[1] + ' minute after ', mtemp[1] + ' after ']
    elif int(mtemp) <= 9:
        minutes = [numbers[mtemp[1]] + ' past ', numbers[mtemp[1]] + ' minutes past ', mtemp[1] + ' minutes past ', mtemp[1] + ' past ']
        minutes = minutes + [numbers[mtemp[1]] + ' after ', numbers[mtemp[1]] + ' minutes after ', mtemp[1] + ' minutes after ', mtemp[1] + ' after ']
    elif int(mtemp) <= 13:
        minutes = [numbers[mtemp] + ' past ', numbers[mtemp] + ' minutes past ', mtemp + ' minutes past ', mtemp + ' past ']
        minutes = minutes + [numbers[mtemp] + ' after ', numbers[mtemp] + ' minutes after ', mtemp + ' minutes after ', mtemp + ' after ']
    elif int(mtemp) in [15]:
        minutes = ['quarter past ', 'quarter-past ', numbers[mtemp] + ' past ', numbers[mtemp] + ' minutes past ', mtemp + ' minutes past ', mtemp + ' past ']
        minutes = minutes + ['quarter after ', numbers[mtemp] + ' after ', numbers[mtemp] + ' minutes after ', mtemp + ' minutes after ', mtemp + ' after ']
    elif int(mtemp) in [18,20,40,50]:
        minutes = [numbers[mtemp] + ' past ', numbers[mtemp] + ' minutes past ', mtemp + ' minutes past ', mtemp + ' past ']
        minutes = minutes + [numbers[mtemp] + ' after ', numbers[mtemp] + ' minutes after ', mtemp + ' minutes after ', mtemp + ' after ']
    elif int(mtemp) <= 19:
        minutes = [numbers[mtemp[1]] + 'teen past ', numbers[mtemp[1]] + 'teen minutes past ', mtemp + ' minutes past ', mtemp + ' past ']
        minutes = minutes + [numbers[mtemp[1]] + 'teen after ', numbers[mtemp[1]] + 'teen minutes after ', mtemp + ' minutes after ', mtemp + ' after ']
    elif int(mtemp) <= 59:
        minutes = [numbers[mtemp[0] + '0'] + '-' + numbers[mtemp[1]] + ' past ', numbers[mtemp[0] + '0'] + '-' + numbers[mtemp[1]] + ' minutes past ', mtemp + ' minutes past ', mtemp + ' past ']
        minutes = minutes + [numbers[mtemp[0] + '0'] + '-' + numbers[mtemp[1]] + ' after ', numbers[mtemp[0] + '0'] + '-' + numbers[mtemp[1]] + ' minutes after ', mtemp + ' minutes after ', mtemp + ' after ']
    else:
        print "This is not a time!", time
    
    # Hours before the half hour
    if int(htemp) == 0:
        hours = ['midnight', 'twelve', '12', 'noon']
    elif int(htemp) <= 9:
        hours = [numbers[htemp[1]], htemp[1]]
    elif int(htemp) <= 11:
        hours = [numbers[htemp], htemp]
    elif int(htemp) == 12:
        hours = ['twelve', '12', 'noon']
    elif int(htemp) <= 23:
        hours = [numbers[str(int(htemp)-12)], htemp, str(int(htemp)-12)]
    else:
         print "This is not a time!", time
     
    # OK add to the lookup
    for hour in hours:
        for minute in minutes:
            if minute != " o'clock":
                time2check.append(minute + hour)
            else:
                if hour in ['midnight', 'noon']:
                    time2check.append(' ' + hour)
                else:
                    time2check.append(hour + minute)
                
    # Minutes after the half hour
    to_the_minute = str(60 - int(mtemp))
    if int(to_the_minute) <= 29:
        if int(to_the_minute) == 1:
            minutes = [numbers[to_the_minute] + ' minute to ', numbers[to_the_minute] + ' to ', to_the_minute + ' minute to ', to_the_minute + ' to ']
            minutes = minutes + [numbers[to_the_minute] + ' minute before ', numbers[to_the_minute] + ' before ', to_the_minute + ' minute before ', to_the_minute + ' before ']
        elif int(to_the_minute) <= 9:
            minutes = [numbers[to_the_minute] + ' minutes to ', numbers[to_the_minute] + ' to ', to_the_minute + ' minutes to ', to_the_minute + ' to ',]
            minutes = minutes + [numbers[to_the_minute] + ' minutes before ', numbers[to_the_minute] + ' before ', to_the_minute + ' minutes before ', to_the_minute + ' before ',]
        elif int(to_the_minute) <= 13:
            minutes = [numbers[to_the_minute] + ' minutes to ', numbers[to_the_minute] + ' to ', to_the_minute + ' minutes to ', to_the_minute + ' to ']
            minutes = minutes + [numbers[to_the_minute] + ' minutes before ', numbers[to_the_minute] + ' before ', to_the_minute + ' minutes before ', to_the_minute + ' before ']
        elif int(to_the_minute) in [15]:
            minutes = ['quarter to ', numbers[to_the_minute] + ' minutes to ', numbers[to_the_minute] + ' to ', to_the_minute + ' minutes to ', to_the_minute + ' to ']
            minutes = minutes + ['quarter before ', numbers[to_the_minute] + ' minutes before ', numbers[to_the_minute] + ' before ', to_the_minute + ' minutes before ', to_the_minute + ' before ']
        elif int(to_the_minute) in [18,20]:
            minutes = [numbers[to_the_minute] + ' minutes to ', numbers[to_the_minute] + ' to ', to_the_minute + ' minutes to ', to_the_minute + ' to ']
            minutes = minutes + [numbers[to_the_minute] + ' minutes before ', numbers[to_the_minute] + ' before ', to_the_minute + ' minutes before ', to_the_minute + ' before ']
        elif int(to_the_minute) <= 19:
            minutes = [numbers[to_the_minute[1]] + 'teen minutes to ', numbers[to_the_minute[1]] + 'teen to ', to_the_minute + ' minutes to ', to_the_minute + ' to ']
            minutes = minutes + [numbers[to_the_minute[1]] + 'teen minutes before ', numbers[to_the_minute[1]] + 'teen before ', to_the_minute + ' minutes before ', to_the_minute + ' before ']
        elif int(to_the_minute) <= 29:
            minutes = [numbers[to_the_minute[0] + '0'] + '-' + numbers[to_the_minute[1]] + ' minutes to ', numbers[to_the_minute[0] + '0'] + '-' + numbers[to_the_minute[1]] + ' to ', to_the_minute + ' minutes to ', to_the_minute + ' to ']
            minutes = minutes + [numbers[to_the_minute[0] + '0'] + '-' + numbers[to_the_minute[1]] + ' minutes before ', numbers[to_the_minute[0] + '0'] + '-' + numbers[to_the_minute[1]] + ' before ', to_the_minute + ' minutes before ', to_the_minute + ' before ']
        else:
            print "This is not a time!", time
        
        # Hours after the half hour
        to_the_hour = str(int(htemp) + 1)
        if int(to_the_hour) == 24:
            hours = ['midnight', 'twelve']
        elif int(to_the_hour) == 12:
            hours = [numbers[to_the_hour], to_the_hour, 'noon']
        elif int(to_the_hour) <= 12:
            hours = [numbers[to_the_hour], to_the_hour]
        elif int(to_the_hour) <= 23:
            hours = [numbers[str(int(to_the_hour)-12)], str(int(to_the_hour)-12)]
        else:
             print "This is not a time!", time
    
        # OK add to the lookup
        for hour in hours:
            for minute in minutes:
                time2check.append(minute + hour)
            
    # The harder times
    ## First up - words
    # Minutes
    if int(mtemp) == 0:
        minutes = [""]
    elif int(mtemp) == 30:
        minutes = [numbers[mtemp]]
    elif int(mtemp) <= 9:
        minutes = ['oh ' + numbers[mtemp[1]], 'zero ' + numbers[mtemp[1]]]
    elif int(mtemp) <= 13:
        minutes = [numbers[mtemp]]
    elif int(mtemp) in [15,18,20,40,50]:
        minutes = [numbers[mtemp]]
    elif int(mtemp) <= 19:
        minutes = [numbers[mtemp[1]] + 'teen']
    elif int(mtemp) <= 59:
        minutes = [numbers[mtemp[0] + '0'] + '-' + numbers[mtemp[1]]]
    else:
        print "This is not a time!", time

    # Hours
    if int(htemp) == 0:
        hours = ['twelve', '12']
    elif int(htemp) <= 9:
        hours = [numbers[htemp[1]], str(htemp[1])]
    elif int(htemp) <= 12:
        hours = [numbers[htemp], str(htemp[1])]
    elif int(htemp) <= 23:
        hours = [numbers[str(int(htemp)-12)], str(int(htemp)-12)]
    else:
         print "This is not a time!", time
 
    # Together
    for hour in hours:
        for minute in minutes:
            if minute == '':
                time2check.append(hour)
            else:
                time2check.append(hour + ' ' + minute)
                time2check.append(hour + '-' + minute)
    
    temp_to_add = []
    for instance in time2check:
        if instance[0].isalpha():
            temp_to_add.append(instance[0].upper() + instance[1:])
            temp_to_add.append("".join(c.upper() if c.islower() else c.lower() for c in instance))
        else:
            for i in instance[1:]:
                if i.isalpha():
                    temp_to_add.append("".join(c.upper() if c.islower() else c.lower() for c in instance))
                    break
    
    time2check += temp_to_add
    
    return(time2check)
    
def nuance(key):
    """Give the time just before and after a time
		INPUT: a time
		FUNCTION: nuance(key)
		OUTPUT: times
        Time taken: quick, quick"""
    temp = key.split(':')
    if temp[1] == '00':
        am = 59
        ah = int(temp[0]) - 1
        pm = 1
        ph = int(temp[0])
    elif temp[1] == '59':
        am = '58'
        ah = int(temp[0])
        pm = '00'
        ph = int(temp[0]) + 1
    else:
        am = int(temp[1]) - 1
        ah = int(temp[0])
        pm = int(temp[1]) + 1
        ph = int(temp[0])
        
    if ah == 24:
        ah = 0
    elif ah == -1:
        ah = 23
    if ph == 24:
        ph = 0
    elif ph == -1:
        ph = 23
        
    if ah < 10:
        if am < 10:
            just_before = '0' + str(ah) + ':0' + str(am)
        else:
            just_before = '0' + str(ah) + ':' + str(am)
    else:
        if am < 10:
            just_before = str(ah) + ':0' + str(am)
        else:
            just_before = str(ah) + ':' + str(am)
        
    if ph < 10:
        if pm < 10:
            just_after = '0' + str(ph) + ':0' + str(pm)
        else:
            just_after = '0' + str(ph) + ':' + str(pm)
    else:
        if pm < 10:
            just_after = str(ph) + ':0' + str(pm)
        else:
            just_after = str(ph) + ':' + str(pm)
        
    return([just_before, just_after])
    
def digit2word(digit):
    """Turn a digital number (eg. 13) into word
		INPUT: digits
		FUNCTION: digit2word(digit)
		OUTPUT: words
        Time taken: quick, quick"""
    
    numbers = {'0': 'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '15': 'fifteen', '18': 'eighteen', '20':'twenty', '30':'thirty', '40':'forty', '50':'fifty'}
    
    # Digit to word
    if digit <= 13:
        word = numbers[str(digit)]
    elif digit in [15,18,20,30,40,50]:
        word = numbers[str(digit)]
    elif digit <= 19:
        word = numbers[str(digit)[1]] + 'teen'
    elif digit <= 59:
        word = numbers[str(digit)[0] + '0'] + '-' + numbers[str(digit)[1]]
    else:
        print "This is not a time!", digit
            
    return(word)
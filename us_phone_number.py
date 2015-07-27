import re
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print (test_string + ' is a valid US local phone number')
    else:
        print (test_string + ' is rejected')

for test_string in [' user.user.user-user u@example.com',' user.user.user-@example.com',' user@example.com']:
    if not  re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$',test_string):
        print(test_string + ' is a valid email')   
    else:
        print (test_string + ' is rejected')

for test_string in ['user.user.user-user u@examp.le.com','user.user.user-@example.com','user@example.com']:
    if not  re.match(r'^[A-Za-z0-9\.]@[A-Za-z0-9]\.[a-zA-Z]*$',test_string):
        print(test_string + ' is a valid email')   
    else:
        print (test_string + ' is rejected')

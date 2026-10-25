# Take input for the student that he can attend the exam or not
medical_cause=input('Do you have a medical condition:').strip().upper()

# Checking the user input and predictiong output accordingly
if medical_cause=='Y':#Condition 1
    print('You are allowed')

else:
    
    atten=int(input('Enter the attendance of student:')) 
    if atten>=75: #Condition 2
        print('Allowed')
    else:
        print('Not allowed')
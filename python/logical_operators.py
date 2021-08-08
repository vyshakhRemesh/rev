has_high_income=True
has_good_credit=True
has_criminal_record=False

if has_high_income and has_good_credit:  #both conditions should be true
    print("eligible for loan ")

if has_good_credit or has_high_income:  #atleast one condition true
    print("welcome")

if has_good_credit and not has_criminal_record: # Not inverses any boolean value
    print("good citizen")

if not has_good_credit and not has_criminal_record:
    print('not eligible')

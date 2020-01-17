is_hot = True

if is_hot:
    print("It's a hot day")
print("Enjoy your day")

is_hot = False

if is_hot:
    print("It's a hot day")
print("Enjoy your day")

is_hot = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
   print("It's a lovely day")
print("Enjoy your day")

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
   print("It's a lovely day")
print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_pyment = 0.1 * price
else:
    down_pyment = 0.2 * price
print(f"Down payment: {down_pyment}")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_pyment = 0.1 * price
else:
    down_pyment = 0.2 * price
print(f"Down payment: ${down_pyment}")

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
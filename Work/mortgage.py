# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal>0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    principal = principal + principal * rate / 12 - payment
    total_paid = total_paid + payment
    month += 1

print(round(total_paid,1),month-1)

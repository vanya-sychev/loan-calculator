import argparse
import sys
import math


class LoanCalculator:
    @staticmethod
    def number_of_payments(loan_principal, monthly_payment, loan_interest):
        i = loan_interest / (12 * 100)
        n = math.ceil(math.log((monthly_payment
                                / (monthly_payment - i * loan_principal)), 1 + i))

        if n % 12 == 0:
            return f"It will take {n // 12} years to repay this loan!\n" \
                   f"Overpayment = {monthly_payment * n - loan_principal}"
        else:
            return f"It will take {n // 12} years and {n % 12} " \
                   f"months to repay this loan!\n" \
                   f"Overpayment = {monthly_payment * n - loan_principal}"

    @staticmethod
    def annuity_payment(loan_principal, n_of_periods, loan_interest):
        i = loan_interest / (12 * 100)
        a = loan_principal * (i / (1 - (1 + i) ** -n_of_periods))

        return f"Your annuity payment = {math.ceil(a)}!\n" \
               f"Overpayment = {math.ceil(a) * n_of_periods - loan_principal}"

    @staticmethod
    def loan_principal(annuity_payment, n_of_periods, loan_interest):
        i = loan_interest / (12 * 100)
        p = annuity_payment / (i / (1 - (1 + i) ** -n_of_periods))

        return f"Your loan principal = {math.floor(p)}!\n" \
               f"Overpayment = " \
               f"{math.floor(annuity_payment * n_of_periods - math.floor(p))}"

    @staticmethod
    def differentiated_payment(loan_principal, n_of_periods, loan_interest):
        i = loan_interest / (12 * 100)

        amount = 0
        for m in range(1, n_of_periods + 1):
            d = ((loan_principal / n_of_periods) + i
                 * (loan_principal - (loan_principal * (m - 1)) / n_of_periods))
            amount += math.ceil(d)
            print(f"Month {m}: payment is {math.ceil(d)}")

        print(f"\nOverpayment = {round(amount - loan_principal)}")

    def launch(self):
        print('What do you want to calculate?')
        print('type "n" for number of monthly payments,')
        print('type "a" for annuity monthly payment amount,')
        print('type "p" for loan principal,')
        print('type "d" for differentiated payment:')

        answer = input()

        if answer == "n":
            loan_principal = int(input("Enter the loan principal:\n"))
            monthly_payment = int(input("Enter the monthly payment:\n"))
            loan_interest = float(input("Enter the loan interest:\n"))
            print(self.number_of_payments(loan_principal, monthly_payment,
                                          loan_interest))
        elif answer == "a":
            loan_principal = int(input("Enter the loan principal:\n"))
            n_of_periods = int(input("Enter the number of periods:\n"))
            loan_interest = float(input("Enter the loan interest:\n"))
            print(self.annuity_payment(loan_principal, n_of_periods,
                                       loan_interest))
        elif answer == "p":
            annuity_payment = float(input("Enter the annuity payment:\n"))
            n_of_periods = int(input("Enter the number of periods:\n"))
            loan_interest = float(input("Enter the loan interest:\n"))
            print(self.loan_principal(annuity_payment, n_of_periods,
                                      loan_interest))
        elif answer == "d":
            loan_principal = float(input("Enter the loan interest:\n"))
            n_of_periods = int(input("Enter the number of periods:\n"))
            loan_interest = float(input("Enter the loan interest:\n"))
            self.differentiated_payment(loan_principal, n_of_periods,
                                        loan_interest)


person = LoanCalculator()

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if len(sys.argv) > 1:
    if args.type == "diff" and args.principal is not None \
            and args.periods is not None \
            and args.interest is not None:
        person.differentiated_payment(float(args.principal),
                                      int(args.periods), float(args.interest))
    elif args.type == "annuity" and args.payment is not None \
            and args.periods is not None \
            and args.interest is not None:
        print(person.loan_principal(float(args.payment),
                                    int(args.periods), float(args.interest)))
    elif args.type == "annuity" and args.principal is not None \
            and args.payment is not None \
            and args.interest is not None:
        print(person.number_of_payments(int(args.principal),
                                        int(args.payment),
                                        float(args.interest)))
    elif args.type == "annuity" and args.principal is not None \
            and args.periods is not None \
            and args.interest is not None:
        print(person.annuity_payment(int(args.principal),
                                     int(args.periods), float(args.interest)))
    else:
        print("Incorrect parameters")
else:
    person.launch()

import sys
import argparse
import math

def createParser ():
parser = argparse.ArgumentParser()
parser.add_argument ('--types', '--type')
parser.add_argument ('--payment', type = float, default = -1)
parser.add_argument ('--principal', type = float, default = -1)
parser.add_argument ('--periods', type = float, default = -1)
parser.add_argument ('--interest', type = float, default = -1)
return parser

if __name__ == '__main__':
parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
overpayment = 0
if namespace.payment == -1 and namespace.types == 'diff' and namespace.principal >= 0 and namespace.periods >= 0 and namespace.interest >= 0:
i = namespace.interest / (100 * 12)
for j in range(1, int(namespace.periods) + 1):
d = int(math.ceil(namespace.principal / namespace.periods + i * namespace.principal * (1 - (j - 1) / namespace.periods)))
print(f'Month {j}: paid out {d}')
overpayment += d
print()
overpayment = int(overpayment - namespace.principal)
print(f'Overpayment = {overpayment}')
elif namespace.payment == -1 and namespace.types == 'annuity' and namespace.principal >= 0 and namespace.periods >= 0 and namespace.interest >= 0:
i = namespace.interest / (100 * 12)
A = int(math.ceil(namespace.principal * (i * pow(1 + i, namespace.periods)) / (pow(1 + i, namespace.periods) - 1)))
print(f'Your annuity payment = {A}!')
overpayment = A * namespace.periods
overpayment = int(overpayment - namespace.principal)
print(f'Overpayment = {overpayment}')
elif namespace.principal == -1 and namespace.types == 'annuity' and namespace.payment >= 0 and namespace.periods >= 0 and namespace.interest >= 0:
i = namespace.interest / (100 * 12)
P = int(math.ceil(namespace.payment / ((i * pow(1 + i, namespace.periods)) / (pow(1 + i, namespace.periods) - 1))))
print(f'Your credit principal = {P}!')
overpayment = namespace.payment * namespace.periods
overpayment = int(overpayment - P)
print(f'Overpayment = {overpayment}')
elif namespace.periods == -1 and namespace.types == 'annuity' and namespace.principal >= 0 and namespace.payment >= 0 and namespace.interest >= 0:
i = namespace.interest / (100 * 12)
n = math.ceil(math.log(namespace.payment / (namespace.payment - i * namespace.principal), 1 + i))
years = int(n // 12)
months = int(n % 12)
if months == 0 and years == 1:
print(f'You need 1 year to repay this credit!')
elif months == 1 and years == 0:
print(f'You need 1 month to repay this credit!')
elif months == 0:
print(f'You need {years} years to repay this credit!')
elif years == 0:
print(f'You need {months} months to repay this credit!')
elif months == 1 and years == 1:
print(f'You need 1 year and 1 month to repay this credit!')
elif months == 1:
print(f'You need {years} years and 1 month to repay this credit!')
elif years == 1:
print(f'You need 1 year and {months} months to repay this credit!')
else:
print(f'You need {years} years and {months} months to repay this credit!')
overpayment = namespace.payment * n
overpayment = int(overpayment - namespace.principal)
print(f'Overpayment = {overpayment}')
else:
print('Incorrect parameters.')
income = 100000.12
single_person_tax_allowance = 36800
taxible_at_20_percent = income - single_person_tax_allowance
taxible_at_40_percent = income - taxible_at_20_percent
percent_tax_20 = taxible_at_20_percent * .2
percent_tax_40 = taxible_at_40_percent * .4
total_tax = percent_tax_20 + percent_tax_40

print(round(total_tax, 2) )
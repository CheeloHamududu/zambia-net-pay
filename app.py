def calculate_napsa(gross_pay):
    """Calculates NAPSA at 5% with the 2017 ceiling of K796.60."""
    napsa_rate = 0.05
    napsa_ceiling = 796.60
    contribution = gross_pay * napsa_rate
    return min(contribution, napsa_ceiling)

def calculate_paye(taxable_income):
    """Calculates PAYE based on the 2017 Zambian Tax Bands."""
    tax = 0
    if taxable_income <= 3300:
        tax = 0
    elif taxable_income <= 4100:
        tax = (taxable_income - 3300) * 0.25
    elif taxable_income <= 6200:
        tax = (800 * 0.25) + (taxable_income - 4100) * 0.30
    else:
        tax = (800 * 0.25) + (2100 * 0.30) + (taxable_income - 6200) * 0.375
    return tax

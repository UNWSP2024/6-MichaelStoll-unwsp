#title: taxes
#author: michael stoll
#date: 2/28/25

def retail_tax():
    sales = float(input('Enter total sales:'))
    county_tax = sales * 0.025
    state_tax = sales * 0.05
    total_tax = county_tax + state_tax
    print('County tax:', f'{county_tax:0.2f}')
    print('State tax', f'{state_tax:0.2f}')
    print('Total tax:', f'{total_tax:0.2f}')
    
retail_tax()
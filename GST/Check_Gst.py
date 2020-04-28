# Check your product GST percent
# Taking user input to enter product name
category=input('Enter your product category line food,hotel and hose hold etc :')
tax=0
if category.lower() in ('food','hotel','entertainment','transportion','house hold','mobile','phone'):
    # nested loop 
    product_name=input('Please enter your product name ex milk,tea etc :')
    if product_name.lower() in ('vegetable','grain','milk','newpaper'):
        tax=0
    elif product_name.lower() in ('coffe','tea','lpg','medicine','coal','sugar'):
        tax=5
    elif product_name.lower() in ('butter','juice','bicycle','leather','candle'):
        tax=12
    elif product_name.lower() in ('toothpaste','ice cream','corn flakes'):
        tax=18
    elif product_name.lower() in('race','cinema','movie','refrigerator','car','bike','air conditions','makeup','fax machine','beauty aid'):
        tax=28
    else:
        print('Not available in our system')
    print(str(tax)+'%')
else:
    print('Category are not available in list.')

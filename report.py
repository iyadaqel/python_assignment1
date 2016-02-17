def build_cash_report(dailySales):
    cash_sales = 0
    cc_sales = 0
    for sale in dailySales:
        if('Cash' in sale.keys()):
            cash_sales = cash_sales + sale['price']
        else:
            cc_sales = cc_sales + sale['price']

    report= {'cash_sales':cash_sales , 'cc_sales':cc_sales}
    return(report)


def build_customer_report(dailySales):
    crmReport = {}
    keys = crmReport.keys()
    for sale in dailySales:
        if sale['customerID'] in keys:
            crmReport[(sale['customerID'])] = crmReport[(sale['customerID'])] + int(sale['price'])
        else:
            crmReport[(sale['customerID'])] = 0 + int(sale['price'])


    return(crmReport)

#print(build_customer_report([{'SKU': '00001', 'customerID': 5, 'price': 20, 'CC': '123ABC'}, {'SKU': '00001', 'customerID': 5, 'price': 10, 'CC': '123ABC'}, {'SKU': '00001', 'customerID': 6, 'price': 10, 'CC': '123ABC'}]

#[{'SKU': '00001', 'customerID': 5, 'price': 10, 'CC': '123ABC'}, {'SKU': '00001', 'customerID': 0, 'price': 10, 'CC': '123ABC'}, {'SKU': '00001', 'customerID': 6, 'price': 10, 'CC': '123ABC'}]

'''
def build_report(customers,items,method) :
    report={}
    #for CUSTOMERS:
    customer=customer[0]
    i=0
    customerFirst = [customers[i]]
    for customers in customers[1:]:
        if len(customers) == len(customerFirst[i]):
            customers.append(customers)
            i+=1  
    report["CustomerID:"]=customer
    #for ITEMS:
    items=items[0]
    j=0
    itemsFirst= [items[i]]
    for items in items(items[1:]):
        if len(items) == len(itemsFirst[j]):
            items.append(items)
        else:
            break
    report["ItemsID:"]=items
    #SALES 
    method=method[0]
    amount=amount[0]
    total=total[0]
    totalCredit=totalCredit[0]
    totalCash=totalCash[0]
    k=0
    totalCredit=0
    totalCash=0
    total=0
    for method in method[1:]:
        if method[k]==1:
            totalCredit[k]=totalCredit[k]+amount[k]
            totalCash[k]=totalCash[k]
            total=total+totalCredit
            if len(total)==len(total[k]):
                total.append(total)
                totalCredit.append(totalCredit)
                totalCash.append(totalCash)
        elif method[k]==0:
            totalCash=totalCash+amount[k]
            totalCredit=totalCredit[k]
            total=total[k]+totalCash[k]
            if len(total)==total[k]:
                total.append(total)
                totalCredit.append(totalCredit)
                totalCash.append(totalCash)
    k+=1    
    report["Total amount:"]=total
    report["Total amount in cash:"]=totalCash
    report["Total amount with credit card:"]=totalCredit
    return report
'''
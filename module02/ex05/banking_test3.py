from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    acc_valid_1 = Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=1000.0)
    acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None)
    
    acc_invalid_4 = Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42)
    acc_invalid_1 = Account("Adam",
                            value=42,
                            zip='0',
                            addr='Somewhere')
    acc_invalid_2 = Account("Bender Bending Rodríguez",
                            zip='1',
                            addr='Mexico',
                            value=42)
    acc_invalid_3 = Account("Charlotte",
                            zip='2',
                            addr='Somewhere in the Milky Way',
                            value=42)
    acc_invalid_5 = Account("Edouard",
                            zip='3',
                            addr='France',
                            value=42)
    
    bank.add(acc_valid_1)
    bank.add(acc_valid_2)
    bank.add(acc_invalid_4)
    bank.add(acc_invalid_1)
    bank.add(acc_invalid_2)
    bank.add(acc_invalid_3)
    bank.add(acc_invalid_5)

    print("Before transfer")
    print(acc_valid_1.__dict__)
    print(acc_invalid_4.__dict__)
    if bank.transfer('Sherlock Holmes', 'Douglass', 1000.0) is False:
        print('Failed')
        bank.fix_account('Sherlock Holmes')
        bank.fix_account('Douglass')
    # ...
    print("After transfer")
    print(acc_valid_1.__dict__)
    print(acc_invalid_4.__dict__)
    if bank.transfer('Sherlock Holmes', 'Douglass', 1000.0) is False:
       print('Failed')
    else:
       print('Success')

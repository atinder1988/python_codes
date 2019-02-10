def adding_report(arg):
    print('Input an integer to add to the total or "Q" to quit')
    items = ""
    sum = 0
    while True:
        num_str = input('Enter an integer or "Q": ')
        if num_str.isdigit():
            num_int = int(num_str)
            items = items+num_str+"\n"
            sum = sum+num_int
            continue
        elif num_str.upper() == "Q" and arg == "A":
            print("\n\nItems\n"+items+"\n\n"+"Total\n"+str(sum))
            break
        elif num_str.upper() == "Q" and arg == "T":
            print("\n\nTotal\n"+str(sum))
            break
        else:
            print(num_str,"is invalid input")
    
print('Report types include All items ("A") or Total Only ("T")')
while True:
    report_type = input('Choose Report Type ("A" or "T"): ')
    if report_type.upper()== "A" or report_type.upper() == "T":
        adding_report(report_type.upper())
        break
    else:
        print(report_type,"is invalid input")
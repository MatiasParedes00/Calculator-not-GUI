def decorator1 (text):
    print ("=" * len (text))
    print (text + "\n")

def decorator2 (text):
    print (text)
    print ("=" * len (text))

def print_result (result):
    if result:
        print (result)
    else:
        print ("The operation is imvalid")

# exceptions management

def division(x=1,y=1):
    o = -1
    try: 
        o = x/y
        # a specified type of exception catches also all its subtypes
    except ArithmeticError as err:
        report_str = 'Error ({})!'.format(err)
        print(report_str)
        # use the information about the exception.
        # For example, save a log file
        f = open('log.txt', 'w+')
        if(f.writable()):
            f.write(report_str)
        f.close()
        # and then we launch another exception to stop the program,
        # BUT it is taken into account only if 'finally' block isn't present
        raise Exception('We propagate the exception')
    else:
        o = x/y
    finally:
        return o

# the block of code in 'else' is done only if the exception block does not catch the exception
# the block of code in 'finally' is done in all the cases: catched exception or not

# for the computation of 'out' variable,
# note that the operation which launches the exception didn't go well.
# So, the returned value was not overwritten (it has the value -1 which is its starting value)
out = division(10,0)
out2 = division(0,10)

print(out)
print(out2)
    

from decreasing_counter import DecreasingCounter
 
def main():
    counter = DecreasingCounter(10)
 
    counter.print_value()
 
    counter.decrement()
    counter.print_value()
 
    counter.decrement()
    counter.print_value()
    
if __name__ == '__main__':
    main()

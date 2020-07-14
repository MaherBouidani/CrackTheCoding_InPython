
items = [1,2,3,4,5,6,7,8,2,10]

def return_check(items): 
    current = 0 
    while current <= 9:
        print("current outside:", current)
        runner_pointer = current+1
        while runner_pointer <=9:
            if items[current] == items[runner_pointer]:
                        return items[current]
                        

            print("runner pointer inside:", runner_pointer) 
            runner_pointer = runner_pointer + 1
            
                    
        current = current + 1
        


print(return_check(items))
    # -*- coding: utf-8 -*-
    """
    Created on Mon Feb 17 17:09:54 2020
    
    @author: hp
    """
    
    """
    The multiprocessing library uses separate memory space, multiple CPU cores. 
    
    """
    
    import os
    import multiprocessing
    
    
    def fun(number):
        print("inside fun ")
        print("parent preocess ID : ", os.getppid())
        print("fun process ID ", os.getpid())
        
        for i in range(number):
            print(i)
            
        
        
    def gun(number):
        print("inside gun ")
        print("parent process ID : ", os.getppid())
        print("gun process ID : ", os.getpid())
        
        for i in range(number):
            print(i)
            
            
    def main():
        
        
        print("Total cores available : ", multiprocessing.cpu_count())
        
        print("parent process ID of Main : ", os.getppid())
        print("process ID of main : ", os.getpid())    
        
        number = 5
        #fun(5)
        #gun(5)
        
        process_1 = multiprocessing.Process(target = fun, args = (number,))
        process_2 = multiprocessing.Process(target = gun, args = (number,))
        
        process_1.start()
        process_2.start()
        
        process_1.join()
        process_2.join()
        
    
    
    if __name__ == "__main__":
        main()
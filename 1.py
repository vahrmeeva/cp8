while True:
    try:
        a = int(input('Введите положительное десятичное число:'))
        if a <= 0 :
            raise Exception() 
    except:
        print('Введено неположительное днсятичное число:')
        continue
    
    else:
        try:
            b = int(input('Введите целевую систему счисления:'))
            if b != 2 and b !=8:
                raise Exception()
        except:
            print('Введена не та система счисления')
            continue
        else:         
            def to_bin(a):
                r2 = ''
                while a>=b :
                    q1 = a%b
                    r2= str(q1)+r2 
                    a= a//b
                if a>=0:
                    r2 = str(a) +r2  
                    k = '0'+r2
                    return k   
            print (to_bin(a))
        
   
     
       
   
           
                
                
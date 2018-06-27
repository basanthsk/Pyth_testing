import  time
import  threading

def cal_sqr(num):
    print('Calculate square')
    for n in num:
        time.sleep(0.2)
        print('sqr: ',n*n)

def cal_cube(num):
    print('calculate cube')
    for n in num:
        time.sleep(0.2)
        print('cube:',n*n*n)


arr=[2,3,8,9]

t=time.time()
t1=threading.Thread(target=cal_sqr,args=(arr,))
t2=threading.Thread(target=cal_cube,args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()

print('done in:',time.time()-t)

print('Well done')

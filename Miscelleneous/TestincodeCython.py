import MyfirstCython
import time
number =10
start = time.time()
MyfirstCython.test(number)
end = time.time()
print("CythoTime:",end-start)
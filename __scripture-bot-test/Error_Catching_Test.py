from time import asctime,gmtime
from time import time as epochtime
import sys
def time():
	time=str(asctime(gmtime(epochtime())))
	return time
def error_test(test_func):
		try:
				test_func()
		except BaseException as err:
				print(err)
				print(str(err)+" occured at "+str(time()))
def bad_var():
	bad_var=1+'aa'
	return bad_var
def bad_mult():
	bad_var=1/0
	return bad_var
error_test(bad_mult)
error_test(bad_var)

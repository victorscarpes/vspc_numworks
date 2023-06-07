def __jury_aux(coeffs,N):
	B=coeffs;N=len(B)
	if N<=0:return()
	A=list(B);C=[A[0]*A[B]-A[N]*A[N-B]for B in range(N)];return tuple(C)
def jury_test(*C):
	A=list(C);B=len(C)-1
	if sum(A)<=0:return False
	if sum((D*(-1)**(B+C)for(C,D)in enumerate(A)))<=0:return False
	if abs(A[0])>=abs(A[-1]):return False
	while B>2:
		D=__jury_aux(A,B);B-=1
		if abs(D[0])<=abs(D[-1]):return False
	return True
print(jury_test(-0.02916,0.2511,0.522,-1.12,-0.6,1))
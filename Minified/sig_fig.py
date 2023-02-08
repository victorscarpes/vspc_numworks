_D='NaN'
_C='-j'
_B='inf'
_A='.'
import math as mt
_si_prefix={-30:' q',-27:' r',-24:' y',-21:' z',-18:' a',-15:' f',-12:' p',-9:' n',-6:' μ',-3:' m',0:' ',3:' k',6:' M',9:' G',12:' T',15:' P',18:' E',21:' Z',24:' Y',27:' R',30:' Q'}
def _round_sci(x,n=5,unit=''):
	J='×10^';I='×10';C=unit
	if C!='':C=' '+C
	if n==0:return''
	if x<0:return'-'+_round_sci(x=abs(x),n=n,unit=C)
	if mt.isinf(x):return _B+C
	if mt.isnan(x):return _D
	if x==0:
		B='0.'+(n-1)*'0'
		if B[-1]==_A:B=B[:-1]
		return B+C
	D=mt.floor(mt.log10(x));K=x/10**D;E,F=str(K).split(_A);B=E+F
	if len(B)==n:
		if D==0:return E+_A+F+C
		elif D==1:return E+_A+F+I+C
		else:return E+_A+F+J+str(D)+C
	elif len(B)<n:B+=(n-len(B)+1)*'0'
	A=[int(A)for A in B];L=A[n-1];H=A[n]
	if H>5:A[n-1]+=1
	elif H==5:
		if set(A[n:]).intersection(set([1,2,3,4,5,6,7,8,9])):A[n-1]+=1
		elif L%2==1:A[n-1]+=1
	A=A[:n];G=len(A)-1
	while G>0:
		M=A[G]
		if M>9:A[G]-=10;A[G-1]+=1
		G-=1
	if A[0]>9:D+=1;A[0]-=10;A=[1]+A
	A=A[:n];B=''.join([str(B)for B in A]);E=B[:1];F=B[1:]
	if D==0:return E+_A+F+C
	elif D==1:return E+_A+F+I+C
	else:return E+_A+F+J+str(D)+C
def _round_fix(x,n=5,unit=''):
	C=unit
	if C!='':C=' '+C
	if n==0:return''
	if mt.isnan(x):return _D
	if x<0:return'-'+_round_fix(x=abs(x),n=n,unit=C)
	if mt.isinf(x):return _B+C
	D=_round_sci(x=x,n=n,unit='')
	if'×'not in D:return D+C
	if'^'not in D:E=1
	else:E=int(D.split('^')[1])
	A=D.split('×')[0]
	if _A not in A:A+=_A
	while E!=0:
		B=A.index(_A);G=len(A)
		if E>0:
			if B==G-1:A=A[:-1]+'0'+_A
			else:H=A[B+1];A=A[:B]+H+_A+A[B+2:]
			E-=1
		else:
			if B==0:A='.0'+A[1:]
			elif B==1:F=A[0];A='0.'+F+A[2:]
			else:F=A[B-1];A=A[:B-2]+_A+F+A
			E+=1
	if A[-1]==_A:A=A[:-1]
	return A+C
def _round_eng(x,n=5,unit=''):
	D=unit
	if n==0:return''
	if x<0:return'-'+_round_eng(x=abs(x),n=n,unit=D)
	if mt.isinf(x):
		if D=='':return _B
		else:return'inf '+D
	if mt.isnan(x):return _D
	if x==0:
		A='0.'+(n-1)*'0'
		if A[-1]==_A:A=A[:-1]
		if D=='':return A
		else:return A+' '+D
	G=3*mt.floor(mt.log10(x)/3);K=x/10**G;C,H=str(K).split(_A);E=len(C);A=C+H
	if len(A)==n:return C+_A+H+_si_prefix[G]+D
	elif len(A)<n:A+=(n-len(A)+1)*'0'
	B=[int(B)for B in A];L=B[n-1];I=B[n]
	if I>5:B[n-1]+=1
	elif I==5:
		if set(B[n:]).intersection(set([1,2,3,4,5,6,7,8,9])):B[n-1]+=1
		elif L%2==1:B[n-1]+=1
	B=B[:n];F=len(B)-1
	while F>0:
		M=B[F]
		if M>9:B[F]-=10;B[F-1]+=1
		F-=1
	if B[0]>9:E+=1;B[0]-=10;B=[1]+B
	if E>3:G+=3;E-=3
	A=''.join([str(A)for A in B]);J=len(A)
	if J<E:A+=(E-J)*'0'
	A=A[:E]+_A+A[E:];C,H=A.split(_A)
	if len(C)>=n:A=C
	else:N=n-len(C);A=C+_A+H[:N]
	return A+_si_prefix[G]+D
def _complex_round_sci(z,n=5,unit=''):
	B=unit
	if B!='':B=' '+B
	C=complex(z).real;A=complex(z).imag
	if mt.isinf(C)or mt.isinf(A):return _B+B
	if C==0 and A==0:return _round_sci(x=0,n=n,unit=B)
	if A==0:return _round_sci(x=C,n=n,unit=B)
	if C==0 and A>0:return'j'+_round_sci(abs(A),n=n)
	elif C==0 and A<0:return _C+_round_sci(abs(A),n=n)
	if A<0:D=_C+_round_sci(abs(A),n=n)
	else:D='+j'+_round_sci(abs(A),n=n)
	E=_round_sci(x=C,n=n)
	if B=='':return E+D
	return'('+E+D+')'+B
def _complex_round_fix(z,n=5,unit=''):
	B=unit
	if B!='':B=' '+B
	C=complex(z).real;A=complex(z).imag
	if mt.isinf(C)or mt.isinf(A):return _B+B
	if C==0 and A==0:return _round_fix(x=0,n=n,unit=B)
	if A==0:return _round_fix(x=C,n=n,unit=B)
	if C==0 and A>0:return'j'+_round_fix(abs(A),n=n)
	elif C==0 and A<0:return _C+_round_fix(abs(A),n=n)
	if A<0:D=_C+_round_fix(abs(A),n=n)
	else:D='+j'+_round_fix(abs(A),n=n)
	E=_round_fix(x=C,n=n)
	if B=='':return E+D
	return'('+E+D+')'+B
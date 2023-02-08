_E='Unable to allocate memory'
_D='deg'
_C='blue'
_B='Hz'
_A='-'
import polynomial as pl,math as mt
from cmath import phase
import sig_fig as sf,matplotlib.pyplot as plt
pi=mt.pi
a1,a2,b1,b2,c1,c2,d1,d2=0,0,0,0,0,0,0,0
freqs=[]
poles=[]
zeros=[]
def _H(p):
	A=0
	if(a1,b1,c1)==(0,0,0):A=d1
	elif(a1,b1)==(0,0):A=c1
	elif a1==0:A=b1
	else:A=a1
	B=0
	if(a2,b2,c2)==(0,0,0):B=d2
	elif(a2,b2)==(0,0):B=c2
	elif a2==0:B=b2
	else:B=a2
	for C in zeros:A=A*(p-C)
	for C in poles:B=B*(p-C)
	return A/B
def H(f):
	B=_H(complex(0,2*pi*f));A=phase(B)*180/pi;print(43*_A)
	try:C=20*mt.log10(abs(B));print(sf._round_eng(C,unit='dB'))
	except:print('-inf dB')
	if abs(A)<1:print(sf._round_sci(A,unit=_D))
	else:print(sf._round_eng(A,unit=_D))
	print(43*_A)
def _is_equal(z1,z2,n=5):
	A=pl._real(z1)
	if A!=0:Q=mt.floor(mt.log10(abs(A)));I=A/10**Q;I=round(I,n-1);A=I*10**Q
	B=pl._imag(z1)
	if B!=0:R=mt.floor(mt.log10(abs(B)));J=B/10**R;J=round(J,n-1);B=J*10**R
	C=abs(z1)
	if C!=0:S=mt.floor(mt.log10(abs(C)));K=C/10**S;K=round(K,n-1);C=K*10**S
	D=phase(z1)
	if D!=0:T=mt.floor(mt.log10(abs(D)));L=D/10**T;L=round(L,n-1);D=L*10**T
	E=pl._real(z2)
	if E!=0:U=mt.floor(mt.log10(abs(E)));M=E/10**U;M=round(M,n-1);E=M*10**U
	F=pl._imag(z2)
	if F!=0:V=mt.floor(mt.log10(abs(F)));N=F/10**V;N=round(N,n-1);F=N*10**V
	G=abs(z2)
	if G!=0:W=mt.floor(mt.log10(abs(G)));O=G/10**W;O=round(O,n-1);G=O*10**W
	H=phase(z2)
	if H!=0:X=mt.floor(mt.log10(abs(H)));P=H/10**X;P=round(P,n-1);H=P*10**X
	return(A,B)==(E,F)or(C,D)==(G,H)
def coeffs():
	G='d = ';F='c = ';E='b = ';D='a = ';C='ap^3+bp^2+cp+d';global a1,b1,c1,d1;global a2,b2,c2,d2;global freqs;global poles,zeros;global H;print('Enter numerator coefficients');print(C);a1=float(input(D));b1=float(input(E));c1=float(input(F));d1=float(input(G));print('\nEnter denominator coefficients');print(C);a2=float(input(D));b2=float(input(E));c2=float(input(F));d2=float(input(G));zeros=list(pl._cubic(a1,b1,c1,d1));poles=list(pl._cubic(a2,b2,c2,d2))
	for A in poles[:]:
		for B in zeros[:]:
			if _is_equal(A,B):poles.remove(A);zeros.remove(B)
	freqs=[]
	for A in poles+zeros:I=abs(A/(2*pi));freqs.append(I)
	freqs.sort()
def pole_values():
	H='\np';G='f';B=' = ';print(43*_A)
	if len(poles)==0:print('No poles')
	else:
		print('Poles:');A=1
		for C in poles:D=abs(C/(2*pi));E=-mt.cos(phase(C));F=1/(2*E);print(H+str(A)+B+sf._complex_round_fix(C));print(G+str(A)+B+sf._round_eng(D,unit=_B));print('m'+str(A)+B+sf._round_sci(E));print('Q'+str(A)+B+sf._round_sci(F));A+=1
	print(43*_A)
	if len(zeros)==0:print('No zeros')
	else:
		print('Zeros:');A=1
		for C in zeros:D=abs(C/(2*pi));E=-mt.cos(phase(C));F=1/(2*E);print(H+str(A)+B+sf._complex_round_fix(C));print(G+str(A)+B+sf._round_eng(D,unit=_B));print('m'+str(A)+B+sf._round_sci(E));print('Q'+str(A)+B+sf._round_sci(F));A+=1
	print(43*_A);print('Corner frequencies:\n');A=1
	for D in freqs:print(G+str(A)+B+sf._round_eng(D,unit=_B));A+=1
def root_locust_plot():
	A=0;B=0
	if len(poles)!=0:C=[pl._real(A)for A in poles];D=[pl._imag(A)for A in poles];A=max([A]+[abs(A)for A in C]);B=max([B]+[abs(A)for A in D]);plt.scatter(C,D,color='orange')
	if len(zeros)!=0:E=[pl._real(A)for A in zeros];F=[pl._imag(A)for A in zeros];A=max([A]+[abs(A)for A in E]);B=max([B]+[abs(A)for A in F]);plt.scatter(E,F,color=_C)
	if A==0:A=1
	else:A*=1.1
	if B==0:B=1
	else:B*=1.1
	plt.axis((-A,A,-B,B));plt.show()
def mag_plot(fmin=0,fmax=0):
	C=fmax;B=fmin;A=500
	while A>0:
		try:
			if B<=0 or C<=0 or C<=B:D=(A for A in freqs if A!=0);E=mt.log10(min(D)/100);D=(A for A in freqs if A!=0);G=mt.log10(max(D)*100)
			else:E=mt.log10(B);G=mt.log10(C)
			J=G-E;H=[J*B/(A-1)+E for B in range(A)];K=(complex(0,2*pi*10**A)for A in H);F=[]
			for I in K:
				try:F.append(20*mt.log10(abs(_H(I))))
				except:F.append(20*mt.log10(abs(_H(I+complex(0,1e-10)))))
			plt.plot(H,F,color=_C);break
		except:A-=10
	else:print(_E);return
	plt.show()
def phase_plot(fmin=0,fmax=0):
	D=fmax;C=fmin;A=500
	while A>0:
		try:
			if C<=0 or D<=0 or D<=C:E=(A for A in freqs if A!=0);F=mt.log10(min(E)/100);E=(A for A in freqs if A!=0);I=mt.log10(max(E)*100)
			else:F=mt.log10(C);I=mt.log10(D)
			K=I-F;J=[K*B/(A-1)+F for B in range(A)];L=(complex(0,2*pi*10**A)for A in J);B=[phase(_H(A))*180/pi for A in L]
			for G in range(1,A):
				H=B[G]-B[G-1]
				if abs(H)>150:B[G]-=mt.copysign(mt.ceil(abs(H)/180)*180,H)
			plt.plot(J,B,color=_C);break
		except:A-=10
	else:print(_E);return
	plt.show()
def nyquist_plot(fmin=0,fmax=0):
	C=fmax;B=fmin;A=500
	while A>0:
		try:
			if B<=0 or C<=0 or C<=B:D=(A for A in freqs if A!=0);E=mt.log10(min(D)/100);D=(A for A in freqs if A!=0);F=mt.log10(max(D)*100)
			else:E=mt.log10(B);F=mt.log10(C)
			J=F-E;K=[J*B/(A-1)+E for B in range(A)];L=(complex(0,2*pi*10**A)for A in K);G=[];H=[]
			for I in L:G.append(pl._real(_H(I)));H.append(pl._imag(_H(I)))
			plt.scatter(-1,0,color='black');plt.plot(G,H,color=_C);break
		except:A-=10
	else:print(_E);return
	plt.show()
def nichols_plot(fmin=0,fmax=0):
	E=fmax;D=fmin;B=500
	while B>0:
		try:
			if D<=0 or E<=0 or E<=D:F=(A for A in freqs if A!=0);G=mt.log10(min(F)/100);F=(A for A in freqs if A!=0);K=mt.log10(max(F)*100)
			else:G=mt.log10(D);K=mt.log10(E)
			L=K-G;M=[L*A/(B-1)+G for A in range(B)];N=(complex(0,2*pi*10**A)for A in M);A=[];H=[]
			for C in N:
				try:H.append(20*mt.log10(abs(_H(C))));A.append(phase(_H(C))*180/pi)
				except:H.append(20*mt.log10(abs(_H(C+complex(0,1e-10)))));A.append(phase(_H(C+complex(0,1e-10)))*180/pi)
			for I in range(1,B):
				J=A[I]-A[I-1]
				if abs(J)>150:A[I]-=mt.copysign(mt.ceil(abs(J)/180)*180,J)
			plt.scatter(-180,0,color='black');plt.plot(A,H,color=_C);break
		except:B-=10
	else:print(_E);return
	plt.show()
def stab(tol=0.0001,iter=500):
	P='Phase margin: ';K='Not able to find margins';A=min(freqs)/100
	if A==0:A=1
	B=100*A;C=mt.sqrt(A*B);H=abs(_H(complex(0,2*pi*A)));I=abs(_H(complex(0,2*pi*C)));J=abs(_H(complex(0,2*pi*B)));D=0
	while H>1 and J>1:
		if D>=iter:print(K);return
		A*=10;B*=10;C=mt.sqrt(A*B);H=abs(_H(complex(0,2*pi*A)));I=abs(_H(complex(0,2*pi*C)));J=abs(_H(complex(0,2*pi*B)));D+=1
	D=0
	while H<1 and J<1:
		if D>=iter:print(K);return
		A*=0.1;B*=0.1;C=mt.sqrt(A*B);H=abs(_H(complex(0,2*pi*A)));I=abs(_H(complex(0,2*pi*C)));J=abs(_H(complex(0,2*pi*B)));D+=1
	D=0
	while abs(H-1)>tol:
		if D>=iter:print(K);return
		C=mt.sqrt(A*B);H=abs(_H(complex(0,2*pi*A)));I=abs(_H(complex(0,2*pi*C)));J=abs(_H(complex(0,2*pi*B)))
		if I>1 and J<1:A=C
		elif H>1 and I<1:B=C
		elif I<1 and J>1:A=C
		elif H<1 and I>1:B=C
		D+=1
	N=A;A=min(freqs)/100
	if A==0:A=1
	B=100*A;C=mt.sqrt(A*B);E=phase(_H(complex(0,2*pi*A)))
	if E>=0:E-=2*pi
	F=phase(_H(complex(0,2*pi*C)))
	if F>=0:F-=2*pi
	G=phase(_H(complex(0,2*pi*B)))
	if G>=0:G-=2*pi
	D=0
	while E>-pi and G>-pi:
		if D>=iter:print(K);return
		A*=10;B*=10;C=mt.sqrt(A*B);E=phase(_H(complex(0,2*pi*A)))
		if E>=0:E-=2*pi
		F=phase(_H(complex(0,2*pi*C)))
		if F>=0:F-=2*pi
		G=phase(_H(complex(0,2*pi*B)))
		if G>=0:G-=2*pi
		D+=1
	D=0
	while E<-pi and G<-pi:
		if D>=iter:print(K);return
		A*=0.1;B*=0.1;C=mt.sqrt(A*B);E=phase(_H(complex(0,2*pi*A)))
		if E>=0:E-=2*pi
		F=phase(_H(complex(0,2*pi*C)))
		if F>=0:F-=2*pi
		G=phase(_H(complex(0,2*pi*B)))
		if G>=0:G-=2*pi
		D+=1
	D=0
	while abs(E/pi+1)>tol:
		if D>=iter:print(K);return
		C=mt.sqrt(A*B);E=phase(_H(complex(0,2*pi*A)))
		if E>=0:E-=2*pi
		F=phase(_H(complex(0,2*pi*C)))
		if F>=0:F-=2*pi
		G=phase(_H(complex(0,2*pi*B)))
		if G>=0:G-=2*pi
		if F>-pi and G<-pi:A=C
		elif E>-pi and F<-pi:B=C
		elif F<-pi and G>-pi:A=C
		elif E<-pi and F>-pi:B=C
		D+=1
	O=A;L=phase(_H(complex(0,2*pi*N)))
	if L>=0:L-=2*pi
	M=180+L*180/pi;Q=-20*mt.log10(abs(_H(complex(0,2*pi*O))));print(43*_A)
	if abs(M)<1:print(P+sf._round_sci(M,unit=_D))
	else:print(P+sf._round_eng(M,unit=_D))
	print('Gain margin: '+sf._round_eng(Q,unit='dB'));print('\nPhase crossover: '+sf._round_eng(O,unit=_B));print('Gain crossover: '+sf._round_eng(N,unit=_B));print(43*_A)
coeffs()
import polynomial as pl,math as mt
from math import pi
from cmath import phase
import sig_fig as sf,matplotlib.pyplot as plt
_a1,_a2,_b1,_b2,_c1,_c2,_d1,_d2=0,0,0,0,0,0,0,0
_freqs=[]
_poles=[]
_zeros=[]
def _H(p):
	A=0
	if(_a1,_b1,_c1)==(0,0,0):A=_d1
	elif(_a1,_b1)==(0,0):A=_c1
	elif _a1==0:A=_b1
	else:A=_a1
	B=0
	if(_a2,_b2,_c2)==(0,0,0):B=_d2
	elif(_a2,_b2)==(0,0):B=_c2
	elif _a2==0:B=_b2
	else:B=_a2
	for C in _zeros:A=A*(p-C)
	for C in _poles:B=B*(p-C)
	return A/B
def H(f):
	A=_H(2*pi*f);B=phase(A)*180/pi;print(43*'-')
	try:C=20*mt.log10(abs(A));print(sf._round_fix(C,unit='dB'))
	except:print('-inf dB')
	print(sf._round_fix(B,unit='deg'));print(43*'-')
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
	global _a1,_b1,_c1,_d1;global _a2,_b2,_c2,_d2;global _freqs;global _poles,_zeros;print('Enter numerator coefficients');print('ap^3+bp^2+cp+d');_a1=float(input('a = '));_b1=float(input('b = '));_c1=float(input('c = '));_d1=float(input('d = '));print('\nEnter denominator coefficients');print('ap^3+bp^2+cp+d');_a2=float(input('a = '));_b2=float(input('b = '));_c2=float(input('c = '));_d2=float(input('d = '));_zeros=list(pl._cubic(_a1,_b1,_c1,_d1));_poles=list(pl._cubic(_a2,_b2,_c2,_d2))
	for A in _poles[:]:
		for B in _zeros[:]:
			if _is_equal(A,B):_poles.remove(A);_zeros.remove(B)
	_freqs=[abs(A/(2*pi))for A in _poles+_zeros];_freqs.sort()
def pole_values():
	print(43*'-')
	if len(_poles)==0:print('No poles')
	else:
		print('Poles:')
		for A in range(len(_poles)):print('\np'+str(A+1)+' = '+sf._complex_round_fix(_poles[A]));print('f'+str(A+1)+' = '+sf._round_eng(abs(_poles[A]/(2*pi)),unit='Hz'));print('m'+str(A+1)+' = '+sf._round_fix(-mt.cos(phase(_poles[A]))));print('Q'+str(A+1)+' = '+sf._round_fix(-1/(2*mt.cos(phase(_poles[A])))))
	print(43*'-')
	if len(_zeros)==0:print('No zeros')
	else:
		print('Zeros:')
		for A in range(len(_zeros)):print('\nz'+str(A+1)+' = '+sf._complex_round_fix(_zeros[A]));print('f'+str(A+1)+' = '+sf._round_eng(abs(_zeros[A]/(2*pi)),unit='Hz'));print('m'+str(A+1)+' = '+sf._round_fix(-mt.cos(phase(_zeros[A]))));print('Q'+str(A+1)+' = '+sf._round_fix(-1/(2*mt.cos(phase(_zeros[A])))))
	print(43*'-');print('Corner frequencies:\n')
	for A in range(len(_freqs)):print('f'+str(A+1)+' = '+sf._round_eng(_freqs[A],unit='Hz'))
def root_locust_plot():
	A=0;B=0
	if len(_poles)!=0:C=[pl._real(A)for A in _poles];D=[pl._imag(A)for A in _poles];A=max([A]+[abs(A)for A in C]);B=max([B]+[abs(A)for A in D]);plt.scatter(C,D,color='orange')
	if len(_zeros)!=0:E=[pl._real(A)for A in _zeros];F=[pl._imag(A)for A in _zeros];A=max([A]+[abs(A)for A in E]);B=max([B]+[abs(A)for A in F]);plt.scatter(E,F,color='blue')
	if A==0:A=1
	else:A*=1.1
	if B==0:B=1
	else:B*=1.1
	plt.axis((-A,A,-B,B));plt.show()
def mag_plot(fmin=0,fmax=0):
	D=fmax;C=fmin;B=500
	while B>0:
		try:
			if C<=0 or D<=0 or D<=C:A=(B for B in A if B!=0);E=mt.log10(min(A)/100);A=(B for B in A if B!=0);G=mt.log10(max(A)*100)
			else:E=mt.log10(C);G=mt.log10(D)
			J=G-E;H=[J*A/(B-1)+E for A in range(B)];K=(2*pi*10**A for A in H);F=[]
			for I in K:
				try:F.append(20*mt.log10(abs(_H(I))))
				except:F.append(20*mt.log10(abs(_H(I+1e-10))))
			plt.plot(H,F,color='blue');break
		except:B-=10
	else:print('Unable to allocate memory');return
	plt.show()
def phase_plot(fmin=0,fmax=0):
	E=fmax;D=fmin;A=500
	while A>0:
		try:
			if D<=0 or E<=0 or E<=D:B=(A for A in B if A!=0);F=mt.log10(min(B)/100);B=(A for A in B if A!=0);I=mt.log10(max(B)*100)
			else:F=mt.log10(D);I=mt.log10(E)
			K=I-F;J=[K*B/(A-1)+F for B in range(A)];L=(2*pi*10**A for A in J);C=[phase(_H(A))*180/pi for A in L]
			for G in range(1,A):
				H=C[G]-C[G-1]
				if abs(H)>150:C[G]-=mt.copysign(mt.ceil(abs(H)/180)*180,H)
			plt.plot(J,C,color='blue');break
		except:A-=10
	else:print('Unable to allocate memory');return
	plt.show()
def nyquist_plot(fmin=0,fmax=0):
	D=fmax;C=fmin;B=500
	while B>0:
		try:
			if C<=0 or D<=0 or D<=C:A=(B for B in A if B!=0);E=mt.log10(min(A)/100);A=(B for B in A if B!=0);F=mt.log10(max(A)*100)
			else:E=mt.log10(C);F=mt.log10(D)
			J=F-E;K=[J*A/(B-1)+E for A in range(B)];L=(2*pi*10**A for A in K);G=[];H=[]
			for I in L:G.append(pl._real(_H(I)));H.append(pl._imag(_H(I)))
			plt.scatter(-1,0,color='black');plt.plot(G,H,color='blue');break
		except:B-=10
	else:print('Unable to allocate memory');return
	plt.show()
def nichols_plot(fmin=0,fmax=0):
	F=fmax;E=fmin;B=500
	while B>0:
		try:
			if E<=0 or F<=0 or F<=E:C=(A for A in C if A!=0);G=mt.log10(min(C)/100);C=(A for A in C if A!=0);K=mt.log10(max(C)*100)
			else:G=mt.log10(E);K=mt.log10(F)
			L=K-G;M=[L*A/(B-1)+G for A in range(B)];N=(2*pi*10**A for A in M);A=[];H=[]
			for D in N:
				try:H.append(20*mt.log10(abs(_H(D))));A.append(phase(_H(D))*180/pi)
				except:H.append(20*mt.log10(abs(_H(D+1e-10))));A.append(phase(_H(D+1e-10))*180/pi)
			for I in range(1,B):
				J=A[I]-A[I-1]
				if abs(J)>150:A[I]-=mt.copysign(mt.ceil(abs(J)/180)*180,J)
			plt.scatter(-180,0,color='black');plt.plot(A,H,color='blue');break
		except:B-=10
	else:print('Unable to allocate memory');return
	plt.show()
def stab(tol=0.0001,iter=500):
	A=min(_freqs)/100
	if A==0:A=1
	B=100*A;C=mt.sqrt(A*B);H=abs(_H(2*pi*A));I=abs(_H(2*pi*C));J=abs(_H(2*pi*B));D=0
	while H>1 and J>1:
		if D>=iter:print('Not able to find margins');return
		A*=10;B*=10;C=mt.sqrt(A*B);H=abs(_H(2*pi*A));I=abs(_H(2*pi*C));J=abs(_H(2*pi*B));D+=1
	D=0
	while H<1 and J<1:
		if D>=iter:print('Not able to find margins');return
		A*=0.1;B*=0.1;C=mt.sqrt(A*B);H=abs(_H(2*pi*A));I=abs(_H(2*pi*C));J=abs(_H(2*pi*B));D+=1
	D=0
	while abs(H-1)>tol:
		if D>=iter:print('Not able to find margins');return
		C=mt.sqrt(A*B);H=abs(_H(2*pi*A));I=abs(_H(2*pi*C));J=abs(_H(2*pi*B))
		if I>1 and J<1:A=C
		elif H>1 and I<1:B=C
		elif I<1 and J>1:A=C
		elif H<1 and I>1:B=C
		D+=1
	M=A;A=min(_freqs)/100
	if A==0:A=1
	B=100*A;C=mt.sqrt(A*B);E=phase(_H(2*pi*A))
	if E>=0:E-=2*pi
	F=phase(_H(2*pi*C))
	if F>=0:F-=2*pi
	G=phase(_H(2*pi*B))
	if G>=0:G-=2*pi
	D=0
	while E>-pi and G>-pi:
		if D>=iter:print('Not able to find margins');return
		A*=10;B*=10;C=mt.sqrt(A*B);E=phase(_H(2*pi*A))
		if E>=0:E-=2*pi
		F=phase(_H(2*pi*C))
		if F>=0:F-=2*pi
		G=phase(_H(2*pi*B))
		if G>=0:G-=2*pi
		D+=1
	D=0
	while E<-pi and G<-pi:
		if D>=iter:print('Not able to find margins');return
		A*=0.1;B*=0.1;C=mt.sqrt(A*B);E=phase(_H(2*pi*A))
		if E>=0:E-=2*pi
		F=phase(_H(2*pi*C))
		if F>=0:F-=2*pi
		G=phase(_H(2*pi*B))
		if G>=0:G-=2*pi
		D+=1
	D=0
	while abs(E/pi+1)>tol:
		if D>=iter:print('Not able to find margins');return
		C=mt.sqrt(A*B);E=phase(_H(2*pi*A))
		if E>=0:E-=2*pi
		F=phase(_H(2*pi*C))
		if F>=0:F-=2*pi
		G=phase(_H(2*pi*B))
		if G>=0:G-=2*pi
		if F>-pi and G<-pi:A=C
		elif E>-pi and F<-pi:B=C
		elif F<-pi and G>-pi:A=C
		elif E<-pi and F>-pi:B=C
		D+=1
	N=A;K=phase(_H(2*pi*M))
	if K>=0:K-=2*pi
	L=180+K*180/pi;O=-20*mt.log10(abs(_H(2*pi*N)));print(43*'-')
	if abs(L)<1:print('Phase margin: '+sf._round_sci(L,unit='deg'))
	else:print('Phase margin: '+sf._round_eng(L,unit='deg'))
	print('Gain margin: '+sf._round_eng(O,unit='dB'));print('\nPhase crossover: '+sf._round_eng(N,unit='Hz'));print('Gain crossover: '+sf._round_eng(M,unit='Hz'));print(43*'-')
coeffs()
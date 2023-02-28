_A=False
import math as mt,cmath as cm
from math import pi as _pi
_j=complex(0,1)
_inf=complex('inf')
_nan=complex('nan')
def _isnan(z):A=complex(z).real;B=complex(z).imag;return mt.isnan(A)or mt.isnan(B)
def _isinf(z):
	if _isnan(z):return _A
	A=complex(z).real;B=complex(z).imag;return mt.isinf(A)or mt.isinf(B)
def _isfinite(z):return not _isinf(z)and not _isnan(z)
def _dB(z):
	if z==0:return-_inf.real
	if _isinf(z):return _inf.real
	return 10*mt.log10(abs(z))
def _real(z):return complex(z).real
def _imag(z):return complex(z).imag
def _conj(z):A=_real(z);B=_imag(z);return complex(A,-B)
def _pol(r,theta):return r*cm.exp(_j*theta)
def _z_to_s(Z,Z0=50):
	if Z+Z0==0:return _inf
	if _isinf(Z):return 1
	return(Z-Z0)/(Z+Z0)
def _s_to_z(gamma,Z0=50):
	A=gamma
	if A==1:return _inf
	if _isinf(A):return-Z0
	return Z0*(1+A)/(1-A)
def _source_stab_circle(S):
	C=S[0];I=S[1];J=S[2];K=S[3];H=C*K-J*I;D=_conj(C-H*_conj(K));E=abs(C)**2-abs(H)**2;A:0
	if D==0 and E==0:A=_nan
	elif D!=0 and E==0:A=_inf
	elif _isinf(E)and _isinf(D):A=_nan
	else:A=D/E
	F=abs(J*I);G=abs(abs(C)**2-abs(H)**2);B:0
	if F==0 and G==0:B=_nan.real
	elif F!=0 and G==0:B=_inf.real
	elif _isinf(G)and _isinf(F):B=_nan.real
	else:B=F/G
	return A,B
def _load_stab_circle(S):
	I=S[0];J=S[1];K=S[2];C=S[3];H=I*C-K*J;D=_conj(C-H*_conj(I));E=abs(C)**2-abs(H)**2;A:0
	if D==0 and E==0:A=_nan
	elif D!=0 and E==0:A=_inf
	elif _isinf(E)and _isinf(D):A=_nan
	else:A=D/E
	F=abs(K*J);G=abs(abs(C)**2-abs(H)**2);B:0
	if F==0 and G==0:B=_nan.real
	elif F!=0 and G==0:B=_inf.real
	elif _isinf(G)and _isinf(F):B=_nan.real
	else:B=F/G
	return A,B
def _input_reflection(S,gammaL):
	A=gammaL;E=S[0];B=S[1];C=S[2];D=S[3]
	if 1-D*A==0 and B*C*A!=0:return _inf
	if 1-D*A==0 and B*C*A==0:return _nan
	return E+B*C*A/(1-D*A)
def _output_reflection(S,gammaS):
	A=gammaS;B=S[0];C=S[1];D=S[2];E=S[3]
	if 1-B*A==0 and 1-B*A!=0:return _inf
	if 1-B*A==0 and 1-B*A==0:return _nan
	return E+C*D*A/(1-B*A)
def _rollet(S):
	C=S[0];D=S[1];E=S[2];F=S[3];G=C*F-E*D;A=1+abs(G)**2-abs(C)**2-abs(F)**2;B=2*abs(E)*abs(D)
	if B==0 and A>0:return _inf.real
	if B==0 and A<0:return-_inf.real
	if B==0 and A==0:return _nan.real
	return A/B
def _mu_stab(S):
	A=S[0];C=S[1];D=S[2];B=S[3];K=A*B-D*C;E=1-abs(B)**2;F=abs(A-_conj(B)*K)+abs(C*D)
	if F==0 and E!=0:G=_inf.real
	elif F==0 and E==0:G=_nan.real
	else:G=E/F
	H=1-abs(A)**2;I=abs(B-_conj(A)*K)+abs(C*D)
	if I==0 and H!=0:J=_inf.real
	elif I==0 and H==0:J=_nan.real
	else:J=H/I
	return G,J
def _gain_transducer(S,gammaS,gammaL):
	C=gammaL;B=gammaS;E=S[0];D=S[1];F=S[2];G=S[3]
	if D==0:return 0
	H=(1-abs(B)**2)*abs(D)**2*(1-abs(C)**2);A=abs((1-E*B)*(1-G*C)-F*D*C*B)**2
	if A==0 and A!=0:return _inf.real
	if A==0 and A==0:return _nan.real
	return H/A
def _gain_unilateral(S,gammaS,gammaL):
	C=gammaL;B=gammaS;E=S[0];D=S[1];F=S[3]
	if D==0:return 0
	G=(1-abs(B)**2)*abs(D)**2*(1-abs(C)**2);A=abs((1-E*B)*(1-F*C))**2
	if A==0 and A!=0:return _inf.real
	if A==0 and A==0:return _nan.real
	return G/A
def _gain_max_unilateral(S):
	C=S[0];D=S[1];E=S[3];A=abs(D)**2;B=abs((1-abs(C)**2)*(1-abs(E)**2))
	if A==0 and B==0 or _isinf(A)and _isinf(B):return _nan.real
	if A!=0 and B==0:return _inf.real
	return A/B
def _gain_availabe(S,gammaS):
	B=gammaS;D=S[0];C=S[1]
	if C==0:return 0
	E=_output_reflection(S,B);F=(1-abs(B)**2)*abs(C)**2;A=(1-abs(E)**2)*abs(1-D*B)**2
	if A==0 and A!=0:return _inf.real
	if A==0 and A==0:return _nan.real
	return F/A
def _gain_operating(S,gammaL):
	B=gammaL;C=S[1];D=S[3]
	if C==0:return 0
	E=_input_reflection(S,B);F=(1-abs(B)**2)*abs(C)**2;A=(1-abs(E)**2)*abs(1-D*B)**2
	if A==0 and A!=0:return _inf.real
	if A==0 and A==0:return _nan.real
	return F/A
def _gain_maximum(S):
	A=S[1];B=S[2];C=_rollet(S)
	if C<=1:return _nan.real
	if A==0:return 0
	if B==0:return _gain_max_unilateral(S)
	if _isinf(A)and _isinf(B):return _nan.real
	if _isfinite(A)and B==0:return _inf.real
	return abs(A/B)/(C+mt.sqrt(C**2-1))
def _gain_maximum_stable(S):
	A=S[1];B=S[2];C=_rollet(S)
	if _isnan(C):return _nan.real
	if C>=1:return _nan.real
	if A==0:return 0
	if B==0 and A==0:return _nan.real
	if _isinf(B)and _isinf(A):return _nan.real
	if _isinf(B)and _isfinite(A):return _inf.real
	return abs(A/B)
def _unilateral_test(S):
	F=S[0];H=S[1];I=S[2];G=S[3];A:0;B=abs(I*H*F*G);C=(1-abs(F)**2)*(1-abs(G)**2)
	if B==0 and C==0 or _isinf(B)and _isinf(C):A=_nan.real
	elif B!=0 and C==0:A=_inf.real
	else:A=B/C
	D:0;E:0
	if A==-1:D=_inf.real
	else:D=1/(1+A)**2
	if A==1:E=_inf.real
	else:E=1/(1-A)**2
	return A,D,E
def _x_to_lc(x,f):
	if x*f==0 or _isinf(x*f):return _nan.real
	if x>0:return x/(2*_pi*abs(f))
	return 1/(2*_pi*abs(f)*x)
def _l_matching_network(ZS,ZL,f,block_DC=_A):
	D=block_DC
	if _isnan(ZS)or _isnan(ZL):return _nan.real,_nan.real,_nan.real,_A
	A=_real(1/ZS);J=_imag(1/ZS);B=_real(ZL);K=_imag(ZL)
	if A<0 or B<0:return _nan.real,_nan.real,_nan.real,_A
	if A*B>1:E:0;F:0;G:0;F,E,G=_l_matching_network(ZS=ZL,ZL=ZS,f=f,block_DC=D)[:3];return E,F,G,_A
	C=mt.sqrt(1/(A*B)-1);H=C*A;I=C*B
	if D:H*=-1;I*=-1
	L=H-J;M=I-K;N=_x_to_lc(-1/L,f);O=_x_to_lc(M,f);return N,O,C,True
def _two_port_match(S):
	F=S[0];H=S[1];I=S[2];E=S[3];G=F*E-I*H;B=1+abs(F)**2-abs(E)**2-abs(G)**2;C=F-G*_conj(E)
	if C==0 and B==0:return _nan,_nan
	if C==0 and B!=0:return 0,_conj(E)
	A=(B+cm.sqrt(B**2-4*abs(C)**2))/(2*C);D=_conj(_output_reflection(S,A))
	if abs(A)<1 and abs(D)<1:return A,D
	A=(B-cm.sqrt(B**2-4*abs(C)**2))/(2*C);D=_conj(_output_reflection(S,A))
	if abs(A)<1 and abs(D)<1:return A,D
	return _nan,_nan
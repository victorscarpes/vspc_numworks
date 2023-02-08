import cmath as cm,math as mt
def _imag(z):return complex(z).imag
def _real(z):return complex(z).real
def _linear(a,b):
	if a==0:return()
	return complex(-b/a),
def _quadratic(a,b,c):
	if a==0:return _linear(b,c)
	A=b**2-4*a*c;B=(-b-cm.sqrt(A))/(2*a)+complex(0,0);C=(-b+cm.sqrt(A))/(2*a)+complex(0,0);return B,C
def _cubic(a,b,c,d):
	if a==0:return _quadratic(b,c,d)
	L=(3*c/a-b**2/a**2)/3;A=(2*b**3/a**3-9*b*c/a**2+27*d/a)/27;B=A**2/4+L**3/27
	if L==0 and A==0 and B==0:
		if d/a>=0:E=-(d/a)**(1/3)+complex(0,0)
		else:E=(-d/a)**(1/3)+complex(0,0)
		return E,E,E
	elif _real(B)<=0:M=mt.sqrt(A**2/4-B);N=M**(1/3);F=mt.acos(-(A/(2*M)));O=-N;P=mt.cos(F/3);Q=mt.sqrt(3)*mt.sin(F/3);R=-b/(3*a);G=2*N*mt.cos(F/3)-b/(3*a)+complex(0,0);H=O*(P+Q)+R+complex(0,0);I=O*(P-Q)+R+complex(0,0);return G,H,I
	elif _real(B)>0:
		J=mt.sqrt(B)-A/2
		if J>=0:C=J**(1/3)
		else:C=(-J)**(1/3)*-1
		K=-A/2-mt.sqrt(B)
		if K>=0:D=K**(1/3)
		else:D=(-K)**(1/3)*-1
		G=C+D-b/(3*a)+complex(0,0);H=-(C+D)/2-b/(3*a)+(C-D)*mt.sqrt(3)*complex(0,1/2)+complex(0,0);I=-(C+D)/2-b/(3*a)-(C-D)*mt.sqrt(3)*complex(0,1/2)+complex(0,0);return G,H,I
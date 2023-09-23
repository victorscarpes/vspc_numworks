import kandinsky
def mandelbrot(N_iteration=100):
	D=N_iteration
	for E in range(320):
		for F in range(222):
			A=complex(0,0);G=complex(3.5*E/319-2.5,-2.5*F/221+1.25);B=0
			while B<D and abs(A)<2:B=B+1;A=A*A+G
			C=int(255*B/D);H=kandinsky.color(int(C),int(C*.75),int(C*.25));kandinsky.set_pixel(E,F,H)
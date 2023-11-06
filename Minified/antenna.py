import sig_fig as sf
c=29979e4
print('Enter operating frequency in GHz.')
str_in=input('f: ')
f=eval(str_in)*1e9
print('\nEnter relative permittivity.')
str_in=input('ε_r: ')
Er=eval(str_in)
print('\nEnter substrate thickness in mm.')
str_in=input('h: ')
h=eval(str_in)*.001
W=c/(2*f)*(2/(Er+1))**.5
Eeff=.5*(Er+1)+.5*(Er-1)*(1+12*h/W)**-.5
dL=.412*h*((Eeff+.3)*(.264+W/h)/((Eeff-.258)*(.8+W/h)))
lambda_g=c/(f*Eeff**.5)
L=lambda_g/2-2*dL
Zin=90*(Er**2/(Er-1))*(L/W)**2
print('\nW = '+sf._round_eng(W,unit='m'))
print('ε_eff = '+sf._round_fix(Eeff))
print('ΔL = '+sf._round_eng(dL,unit='m'))
print('λ_g = '+sf._round_eng(lambda_g,unit='m'))
print('L = '+sf._round_eng(L,unit='m'))
print('Z_in = '+sf._round_eng(Zin,unit='Ω'))
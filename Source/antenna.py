import sig_fig as sf

c = 2.9979e8

print("Enter operating frequency in GHz.")
str_in: str = input("f: ")
f: float = eval(str_in)*1e9

print("\nEnter relative permittivity.")
str_in: str = input("ε_r: ")
Er: float = eval(str_in)

print("\nEnter substrate thickness in mm.")
str_in: str = input("h: ")
h: float = eval(str_in)*1e-3

W = (c/(2*f))*(2/(Er+1))**0.5
Eeff = 0.5*(Er+1) + 0.5*(Er-1)*(1+12*h/W)**-0.5
dL = 0.412*h*(((Eeff+0.3)*(0.264+W/h))/((Eeff-0.258)*(0.8+W/h)))
lambda_g = c/(f*Eeff**0.5)
L = lambda_g/2 - 2*dL
Zin = 90*((Er**2)/(Er-1))*(L/W)**2

print("\nW = "+sf._round_eng(W, unit="m"))
print("ε_eff = "+sf._round_fix(Eeff))
print("ΔL = "+sf._round_eng(dL, unit="m"))
print("λ_g = "+sf._round_eng(lambda_g, unit="m"))
print("L = "+sf._round_eng(L, unit="m"))
print("Z_in = "+sf._round_eng(Zin, unit="Ω"))

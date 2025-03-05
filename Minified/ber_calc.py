import math as mt,sig_fig as sf
def _erf(x):a=.147;return mt.copysign(1,x)*mt.sqrt(1-mt.exp(-x**2*(4/mt.pi+a*x**2)/(1+a*x**2)))
def _erfinv(x):a=.147;k1=2/(a*mt.pi)+.5*mt.log(1-x**2);k2=1/a*mt.log(1-x**2);return mt.copysign(1,x)*mt.sqrt(mt.sqrt(k1**2-k2)-k1)
def _Q(x):return .5-.5*_erf(x/mt.sqrt(2))
def _Qinv(x):return mt.sqrt(2)*_erfinv(1-2*x)
def _BER_func(EbN0,M):gamma=10**(EbN0/10);return 4/mt.log2(M)*_Q(mt.sqrt(3*gamma*mt.log2(M)/(M-1)))
def _EbN0_func(BER,M):gamma=(M-1)/(3*mt.log2(M))*_Qinv(mt.log2(M)*BER/4)**2;return 10*mt.log10(gamma)
continue_flag=True
while continue_flag:
	print('======================================');print('==== M-QAM performance calculator ====');print('======================================\n');print('0 - Exit');print('1 - BER given Eb/N0');print('2 - Eb/N0 given BER\n');input_str=input('Choose an option: ');print('')
	if input_str=='0':print('Exiting program');continue_flag=False;break
	elif input_str=='1':M=int(input('M = '));Eb_N0=eval(input('Eb/N0(dB) = '));Pe=_BER_func(EbN0=Eb_N0,M=M);print('BER = '+sf._round_sci(Pe))
	elif input_str=='2':M=int(input('M = '));Pe=eval(input('BER = '));Eb_N0=_EbN0_func(BER=Pe,M=M);print('Eb/N0 = '+sf._round_fix(Eb_N0,unit='dB'))
	else:print('Invlid option')
	input_str=input('\nPress enter to continue or 0 to exit: ')
	if input_str=='0':continue_flag=False
	print('')
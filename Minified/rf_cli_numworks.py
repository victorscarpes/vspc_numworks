_a='\nIn parallel with load:'
_Z='\nIn series with load:'
_Y='\nIn series with amp output:'
_X='\nIn parallel with amp output:'
_W='\nIn parallel with amp input:'
_V='\nIn series with amp input:'
_T='\nIn series with source:'
_R='\nIn parallel with source:'
_Q='stable.'
_P='G_TU_max = '
_O='G_TU = '
_N='Q = '
_M='Ω'
_L='Unable to match network.'
_J='deg'
_I='F'
_H='C = '
_G='H'
_F='L = '
_E='dB'
_D='\nPress [ENTER] to continue.'
_C='-'
_B='\n'
_A=','
import cmath as cm,sig_fig as sf,rf_active_tools as rf
from math import pi
print('Enter operating frequency in MHz.')
_str_in=input('f: ')
_f=eval(_str_in)*1e6
print('\nEnter S parameters as linear magnitude and')
print('phase in degrees separated by comma with no')
print('spaces. If a single value is entered')
print('without any comma, it is considered as the')
print('magnitude and the phase defaults to zero.')
_str_in=input('\nS_11: ')
_s11_mag_str=_str_in
_s11_deg_str='0'
if _A in _str_in:_s11_mag_str=_str_in.split(_A)[0];_s11_deg_str=_str_in.split(_A)[1]
_s11_mag=eval(_s11_mag_str)
_s11_rad=eval(_s11_deg_str)*pi/180
_S11=rf._pol(_s11_mag,_s11_rad)
del _s11_mag,_s11_mag_str,_s11_rad,_s11_deg_str
_str_in=input('S_12: ')
_s12_mag_str=_str_in
_s12_deg_str='0'
if _A in _str_in:_s12_mag_str=_str_in.split(_A)[0];_s12_deg_str=_str_in.split(_A)[1]
_s12_mag=eval(_s12_mag_str)
_s12_rad=eval(_s12_deg_str)*pi/180
_S12=rf._pol(_s12_mag,_s12_rad)
del _s12_mag,_s12_mag_str,_s12_rad,_s12_deg_str
_str_in=input('S_21: ')
_s21_mag_str=_str_in
_s21_deg_str='0'
if _A in _str_in:_s21_mag_str=_str_in.split(_A)[0];_s21_deg_str=_str_in.split(_A)[1]
_s21_mag=eval(_s21_mag_str)
_s21_rad=eval(_s21_deg_str)*pi/180
_S21=rf._pol(_s21_mag,_s21_rad)
del _s21_mag,_s21_mag_str,_s21_rad,_s21_deg_str
_str_in=input('S_22: ')
_s22_mag_str=_str_in
_s22_deg_str='0'
if _A in _str_in:_s22_mag_str=_str_in.split(_A)[0];_s22_deg_str=_str_in.split(_A)[1]
_s22_mag=eval(_s22_mag_str)
_s22_rad=eval(_s22_deg_str)*pi/180
_S22=rf._pol(_s22_mag,_s22_rad)
del _s22_mag,_s22_mag_str,_s22_rad,_s22_deg_str
_S=_S11,_S21,_S12,_S22
print('\nEnter reference, load and source impedances')
print('in ohms. Values default to 50 Ω when not')
print('specified.')
_str_in=input('\nZ_0: ')
_Z0=complex(50)
if _str_in!='':_Z0=eval(_str_in)
_str_in=input('Z_S: ')
_ZS=complex(50)
if _str_in!='':_ZS=eval(_str_in)
_str_in=input('Z_L: ')
_ZL=complex(50)
if _str_in!='':_ZL=eval(_str_in)
_gammaS=rf._z_to_s(_ZS,_Z0)
_gammaL=rf._z_to_s(_ZL,_Z0)
_Gt=rf._gain_transducer(_S,_gammaS,_gammaL)
_Ga=rf._gain_availabe(_S,_gammaS)
_Go=rf._gain_operating(_S,_gammaL)
_Gmax=rf._gain_maximum(_S)
_Gstab=rf._gain_maximum_stable(_S)
_Gtu=rf._gain_unilateral(_S,_gammaS,_gammaL)
_Gtumax=rf._gain_max_unilateral(_S)
_K=rf._rollet(_S)
_delta=_S11*_S22-_S12*_S21
_muL:0
_muS:0
_muS,_muL=rf._mu_stab(_S)
_Ocs:0
_rs:0
_Ocs,_rs=rf._source_stab_circle(_S)
_Ocl:0
_rl:0
_Ocl,_rl=rf._load_stab_circle(_S)
_U:0
_lim_inf:0
_lim_sup:0
_U,_lim_inf,_lim_sup=rf._unilateral_test(_S)
_gain_error=100*max(abs(1-_lim_inf),abs(1-_lim_sup))
_gammaS_match:0
_gammaL_match:0
_gammaS_match,_gammaL_match=rf._two_port_match(_S)
_ZS_match=rf._s_to_z(_gammaS_match,_Z0)
_ZL_match=rf._s_to_z(_gammaL_match,_Z0)
_gamma_in=rf._input_reflection(_S,_gammaL)
_gamma_out=rf._output_reflection(_S,_gammaS)
_Zin=rf._s_to_z(_gamma_in,_Z0)
_Zout=rf._s_to_z(_gamma_out,_Z0)
_Zin_opt=rf._conj(_ZS_match)
_Zout_opt=rf._conj(_ZL_match)
_LC1_in_lp:0
_LC2_in_lp:0
_Q_in_lp:0
_source_parallel_lp:0
_LC1_in_lp,_LC2_in_lp,_Q_in_lp,_source_parallel_lp=rf._l_matching_network(_ZS,_Zin_opt,_f)
_LC1_in_hp:0
_LC2_in_hp:0
_Q_in_hp:0
_source_parallel_hp:0
_LC1_in_hp,_LC2_in_hp,_Q_in_hp,_source_parallel_hp=rf._l_matching_network(_ZS,_Zin_opt,_f,True)
_LC1_out_lp:0
_LC2_out_lp:0
_Q_out_lp:0
_amp_parallel_lp:0
_LC1_out_lp,_LC2_out_lp,_Q_out_lp,_amp_parallel_lp=rf._l_matching_network(_Zout_opt,_ZL,_f)
_LC1_out_hp:0
_LC2_out_hp:0
_Q_out_hp:0
_amp_parallel_hp:0
_LC1_out_hp,_LC2_out_hp,_Q_out_hp,_amp_parallel_hp=rf._l_matching_network(_Zout_opt,_ZL,_f,True)
_loop_flag=True
while _loop_flag:
	print(_B+43*_C);print('0 - Gain metrics');print('1 - Unilaterality metrics');print('2 - Stability metrics');print('3 - Stability circles');print('4 - Simultaneous matching');print('5 - Input low-pass L network');print('6 - Input high-pass L network');print('7 - Output low-pass L network');print('8 - Output high-pass L network');print('9 - Input and output impedances');print('\nEnter operation or press [ENTER] to end');str_in=input('the program: ')
	if str_in=='0':
		print(_B+43*_C);print('G_T = '+sf._round_fix(rf._dB(_Gt),unit=_E));print('G_A = '+sf._round_fix(rf._dB(_Ga),unit=_E));print('G_OP = '+sf._round_fix(rf._dB(_Go),unit=_E));print(_O+sf._round_fix(rf._dB(_Gtu),unit=_E));print(_P+sf._round_fix(rf._dB(_Gtumax),unit=_E))
		if _K>1 and abs(_delta)<1:print('G_max = '+sf._round_fix(rf._dB(_Gmax),unit=_E))
		elif abs(_K)<1:print('G_stab = '+sf._round_fix(rf._dB(_Gstab),unit=_E))
		input(_D)
	elif str_in=='1':print(_B+43*_C);print(_O+sf._round_fix(rf._dB(_Gtu),unit=_E));print(_P+sf._round_fix(rf._dB(_Gtumax),unit=_E));print('U = '+sf._round_fix(_U));print(sf._round_fix(_lim_inf)+' < G_T/G_TU < '+sf._round_fix(_lim_sup));print('Δ% = '+sf._round_fix(_gain_error)+'%');input(_D)
	elif str_in=='2':
		print(_B+43*_C);print('K = '+sf._round_fix(_K));print('|Δ| = '+sf._round_fix(abs(_delta)));print('arg(Δ) = '+sf._round_fix(cm.phase(_delta)*180/pi,unit=_J));print('μ_S = '+sf._round_fix(_muS));print('μ_L = '+sf._round_fix(_muL))
		if abs(_K)==1:print('\nNetwork is unmatchable.')
		elif _K>1 and abs(_delta)<1:print('\nNetwork is matchable and unconditionally');print(_Q)
		elif _K>1 and abs(_delta)>1:print('\nNetwork is matchable and conditionally');print(_Q)
		elif _K<-1:print('\nNetwork is unmatchable and unconditionally');print('unstable.')
		input(_D)
	elif str_in=='3':print(_B+43*_C);print('|O_S| = '+sf._round_fix(abs(_Ocs)));print('arg(O_S) = '+sf._round_fix(cm.phase(_Ocs)*180/pi,unit=_J));print('r_S = '+sf._round_fix(_rs));print('\n|O_L| = '+sf._round_fix(abs(_Ocl)));print('arg(O_L) = '+sf._round_fix(cm.phase(_Ocl)*180/pi,unit=_J));print('r_L = '+sf._round_fix(_rl));input(_D)
	elif str_in=='4':
		print(_B+43*_C)
		if rf._isnan(_gammaS_match)or rf._isnan(_gammaL_match):print(_L)
		else:print('|Γ_S| = '+sf._round_fix(abs(_gammaS_match)));print('arg(Γ_S) = '+sf._round_fix(cm.phase(_gammaS_match)*180/pi,unit=_J));print('\n|Γ_L| = '+sf._round_fix(abs(_gammaL_match)));print('arg(Γ_L) = '+sf._round_fix(cm.phase(_gammaL_match)*180/pi,unit=_J));print('\nZ_S = '+sf._complex_round_fix(_ZS_match,unit=_M));print('Z_L = '+sf._complex_round_fix(_ZL_match,unit=_M))
		input(_D)
	elif str_in=='5':
		print(_B+43*_C)
		if rf._isnan(_Q_in_lp)or rf._isnan(_LC1_in_lp)or rf._isnan(_LC2_in_lp):print(_L)
		else:
			print(_N+sf._round_fix(_Q_in_lp))
			if _source_parallel_lp:print(_R)
			else:print(_T)
			if _LC1_in_lp>0:print(_F+sf._round_eng(_LC1_in_lp,unit=_G))
			else:print(_H+sf._round_eng(-_LC1_in_lp,unit=_I))
			if _source_parallel_lp:print(_V)
			else:print(_W)
			if _LC2_in_lp>0:print(_F+sf._round_eng(_LC2_in_lp,unit=_G))
			else:print(_H+sf._round_eng(-_LC2_in_lp,unit=_I))
		input(_D)
	elif str_in=='6':
		print(_B+43*_C)
		if rf._isnan(_Q_in_hp)or rf._isnan(_LC1_in_hp)or rf._isnan(_LC2_in_hp):print(_L)
		else:
			print(_N+sf._round_fix(_Q_in_hp))
			if _source_parallel_hp:print(_R)
			else:print(_T)
			if _LC1_in_hp>0:print(_F+sf._round_eng(_LC1_in_hp,unit=_G))
			else:print(_H+sf._round_eng(-_LC1_in_hp,unit=_I))
			if _source_parallel_hp:print(_V)
			else:print(_W)
			if _LC2_in_hp>0:print(_F+sf._round_eng(_LC2_in_hp,unit=_G))
			else:print(_H+sf._round_eng(-_LC2_in_hp,unit=_I))
		input(_D)
	elif str_in=='7':
		print(_B+43*_C)
		if rf._isnan(_Q_out_lp)or rf._isnan(_LC1_out_lp)or rf._isnan(_LC2_out_lp):print(_L)
		else:
			print(_N+sf._round_fix(_Q_out_lp))
			if _amp_parallel_lp:print(_X)
			else:print(_Y)
			if _LC1_out_lp>0:print(_F+sf._round_eng(_LC1_out_lp,unit=_G))
			else:print(_H+sf._round_eng(-_LC1_out_lp,unit=_I))
			if _amp_parallel_lp:print(_Z)
			else:print(_a)
			if _LC2_out_lp>0:print(_F+sf._round_eng(_LC2_out_lp,unit=_G))
			else:print(_H+sf._round_eng(-_LC2_out_lp,unit=_I))
		input(_D)
	elif str_in=='8':
		print(_B+43*_C)
		if rf._isnan(_Q_out_hp)or rf._isnan(_LC1_out_hp)or rf._isnan(_LC2_out_hp):print(_L)
		else:
			print(_N+sf._round_fix(_Q_out_hp))
			if _amp_parallel_hp:print(_X)
			else:print(_Y)
			if _LC1_out_hp>0:print(_F+sf._round_eng(_LC1_out_hp,unit=_G))
			else:print(_H+sf._round_eng(-_LC1_out_hp,unit=_I))
			if _amp_parallel_hp:print(_Z)
			else:print(_a)
			if _LC2_out_hp>0:print(_F+sf._round_eng(_LC2_out_hp,unit=_G))
			else:print(_H+sf._round_eng(-_LC2_out_hp,unit=_I))
		input(_D)
	elif str_in=='9':print(_B+43*_C);print('|Γ_in| = '+sf._round_fix(abs(_gamma_in)));print('arg(Γ_in) = '+sf._round_fix(cm.phase(_gamma_in)*180/pi,unit=_J));print('\n|Γ_out| = '+sf._round_fix(abs(_gamma_out)));print('arg(Γ_out) = '+sf._round_fix(cm.phase(_gamma_out)*180/pi,unit=_J));print('\nZ_in = '+sf._complex_round_fix(_Zin,unit=_M));print('Z_out = '+sf._complex_round_fix(_Zout,unit=_M));input(_D)
	else:_loop_flag=False
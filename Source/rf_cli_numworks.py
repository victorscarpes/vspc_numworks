# optmize_ram
import cmath as cm
import sig_fig as sf
import rf_active_tools as rf
from math import pi

print("Enter operating frequency in MHz.")

_str_in: str = input("f: ")
_f: float = eval(_str_in)*1e6

print("\nEnter S parameters as linear magnitude and")
print("phase in degrees separated by comma with no")
print("spaces. If a single value is entered")
print("without any comma, it is considered as the")
print("magnitude and the phase defaults to zero.")

_str_in = input("\nS_11: ")
_s11_mag_str: str = _str_in
_s11_deg_str: str = "0"
if "," in _str_in:
    _s11_mag_str = _str_in.split(",")[0]
    _s11_deg_str = _str_in.split(",")[1]
_s11_mag: float = eval(_s11_mag_str)
_s11_rad: float = eval(_s11_deg_str)*pi/180
_S11: complex = rf._pol(_s11_mag, _s11_rad)
del _s11_mag, _s11_mag_str, _s11_rad, _s11_deg_str

_str_in = input("S_12: ")
_s12_mag_str: str = _str_in
_s12_deg_str: str = "0"
if "," in _str_in:
    _s12_mag_str = _str_in.split(",")[0]
    _s12_deg_str = _str_in.split(",")[1]
_s12_mag: float = eval(_s12_mag_str)
_s12_rad: float = eval(_s12_deg_str)*pi/180
_S12: complex = rf._pol(_s12_mag, _s12_rad)
del _s12_mag, _s12_mag_str, _s12_rad, _s12_deg_str

_str_in = input("S_21: ")
_s21_mag_str: str = _str_in
_s21_deg_str: str = "0"
if "," in _str_in:
    _s21_mag_str = _str_in.split(",")[0]
    _s21_deg_str = _str_in.split(",")[1]
_s21_mag: float = eval(_s21_mag_str)
_s21_rad: float = eval(_s21_deg_str)*pi/180
_S21: complex = rf._pol(_s21_mag, _s21_rad)
del _s21_mag, _s21_mag_str, _s21_rad, _s21_deg_str

_str_in = input("S_22: ")
_s22_mag_str: str = _str_in
_s22_deg_str: str = "0"
if "," in _str_in:
    _s22_mag_str = _str_in.split(",")[0]
    _s22_deg_str = _str_in.split(",")[1]
_s22_mag: float = eval(_s22_mag_str)
_s22_rad: float = eval(_s22_deg_str)*pi/180
_S22: complex = rf._pol(_s22_mag, _s22_rad)
del _s22_mag, _s22_mag_str, _s22_rad, _s22_deg_str

_S = (_S11, _S21, _S12, _S22)


print("\nEnter reference, load and source impedances")
print("in ohms. Values default to 50 Ω when not")
print("specified.")

_str_in = input("\nZ_0: ")
_Z0: complex = complex(50)
if _str_in != "":
    _Z0 = eval(_str_in)

_str_in = input("Z_S: ")
_ZS: complex = complex(50)
if _str_in != "":
    _ZS = eval(_str_in)

_str_in = input("Z_L: ")
_ZL: complex = complex(50)
if _str_in != "":
    _ZL = eval(_str_in)

_gammaS: complex = rf._z_to_s(_ZS, _Z0)
_gammaL: complex = rf._z_to_s(_ZL, _Z0)

_Gt: float = rf._gain_transducer(_S, _gammaS, _gammaL)
_Ga: float = rf._gain_availabe(_S, _gammaS)
_Go: float = rf._gain_operating(_S, _gammaL)
_Gmax: float = rf._gain_maximum(_S)
_Gstab: float = rf._gain_maximum_stable(_S)
_Gtu: float = rf._gain_unilateral(_S, _gammaS, _gammaL)
_Gtumax: float = rf._gain_max_unilateral(_S)

_K: float = rf._rollet(_S)
_delta: complex = _S11*_S22 - _S12*_S21
_muL: float
_muS: float
_muS, _muL = rf._mu_stab(_S)

_Ocs: complex
_rs: float
_Ocs, _rs = rf._source_stab_circle(_S)

_Ocl: complex
_rl: float
_Ocl, _rl = rf._load_stab_circle(_S)

_U: float
_lim_inf: float
_lim_sup: float
_U, _lim_inf, _lim_sup = rf._unilateral_test(_S)
_gain_error: float = 100*max(abs(1-_lim_inf), abs(1-_lim_sup))

_gammaS_match: complex
_gammaL_match: complex
_gammaS_match, _gammaL_match = rf._two_port_match(_S)
_ZS_match: complex = rf._s_to_z(_gammaS_match, _Z0)
_ZL_match: complex = rf._s_to_z(_gammaL_match, _Z0)

_gamma_in: complex = rf._input_reflection(_S, _gammaL)
_gamma_out: complex = rf._output_reflection(_S, _gammaS)
_Zin: complex = rf._s_to_z(_gamma_in, _Z0)
_Zout: complex = rf._s_to_z(_gamma_out, _Z0)

_Zin_opt: complex = rf._conj(_ZS_match)
_Zout_opt: complex = rf._conj(_ZL_match)

_LC1_in_lp: float
_LC2_in_lp: float
_Q_in_lp: float
_source_parallel_lp: bool
_LC1_in_lp, _LC2_in_lp, _Q_in_lp, _source_parallel_lp = rf._l_matching_network(_ZS, _Zin_opt, _f)

_LC1_in_hp: float
_LC2_in_hp: float
_Q_in_hp: float
_source_parallel_hp: bool
_LC1_in_hp, _LC2_in_hp, _Q_in_hp, _source_parallel_hp = rf._l_matching_network(_ZS, _Zin_opt, _f, True)

_LC1_out_lp: float
_LC2_out_lp: float
_Q_out_lp: float
_amp_parallel_lp: bool
_LC1_out_lp, _LC2_out_lp, _Q_out_lp, _amp_parallel_lp = rf._l_matching_network(_Zout_opt, _ZL, _f)

_LC1_out_hp: float
_LC2_out_hp: float
_Q_out_hp: float
_amp_parallel_hp: bool
_LC1_out_hp, _LC2_out_hp, _Q_out_hp, _amp_parallel_hp = rf._l_matching_network(_Zout_opt, _ZL, _f, True)

_loop_flag: bool = True


while _loop_flag:
    print("\n"+43*"-")
    print("0 - Gain metrics")
    print("1 - Unilaterality metrics")
    print("2 - Stability metrics")
    print("3 - Stability circles")
    print("4 - Simultaneous matching")
    print("5 - Input low-pass L network")
    print("6 - Input high-pass L network")
    print("7 - Output low-pass L network")
    print("8 - Output high-pass L network")
    print("9 - Input and output impedances")

    print("\nEnter operation or press [ENTER] to end")
    str_in = input("the program: ")

    if str_in == "0":  # Gain metrics
        print("\n"+43*"-")
        print("G_T = "+sf._round_fix(rf._dB(_Gt), unit="dB"))
        print("G_A = "+sf._round_fix(rf._dB(_Ga), unit="dB"))
        print("G_OP = "+sf._round_fix(rf._dB(_Go), unit="dB"))
        print("G_TU = "+sf._round_fix(rf._dB(_Gtu), unit="dB"))
        print("G_TU_max = "+sf._round_fix(rf._dB(_Gtumax), unit="dB"))

        if _K > 1 and abs(_delta) < 1:
            print("G_max = "+sf._round_fix(rf._dB(_Gmax), unit="dB"))
        elif abs(_K) < 1:
            print("G_stab = "+sf._round_fix(rf._dB(_Gstab), unit="dB"))

        input("\nPress [ENTER] to continue.")

    elif str_in == "1":  # Unilaterality metrics
        print("\n"+43*"-")
        print("G_TU = "+sf._round_fix(rf._dB(_Gtu), unit="dB"))
        print("G_TU_max = "+sf._round_fix(rf._dB(_Gtumax), unit="dB"))
        print("U = "+sf._round_fix(_U))
        print(sf._round_fix(_lim_inf)+" < G_T/G_TU < "+sf._round_fix(_lim_sup))
        print("Δ% = "+sf._round_fix(_gain_error)+"%")

        input("\nPress [ENTER] to continue.")

    elif str_in == "2":  # Stability metrics
        print("\n"+43*"-")
        print("K = "+sf._round_fix(_K))
        print("|Δ| = "+sf._round_fix(abs(_delta)))
        print("arg(Δ) = "+sf._round_fix(cm.phase(_delta)*180/pi, unit="deg"))
        print("μ_S = "+sf._round_fix(_muS))
        print("μ_L = "+sf._round_fix(_muL))

        if abs(_K) == 1:
            print("\nNetwork is unmatchable.")
        elif _K > 1 and abs(_delta) < 1:
            print("\nNetwork is matchable and unconditionally")
            print("stable.")
        elif _K > 1 and abs(_delta) > 1:
            print("\nNetwork is matchable and conditionally")
            print("stable.")
        elif _K < -1:
            print("\nNetwork is unmatchable and unconditionally")
            print("unstable.")

        input("\nPress [ENTER] to continue.")

    elif str_in == "3":  # Stability circles
        print("\n"+43*"-")

        print("|O_S| = "+sf._round_fix(abs(_Ocs)))
        print("arg(O_S) = "+sf._round_fix(cm.phase(_Ocs)*180/pi, unit="deg"))
        print("r_S = "+sf._round_fix(_rs))

        print("\n|O_L| = "+sf._round_fix(abs(_Ocl)))
        print("arg(O_L) = "+sf._round_fix(cm.phase(_Ocl)*180/pi, unit="deg"))
        print("r_L = "+sf._round_fix(_rl))

        input("\nPress [ENTER] to continue.")

    elif str_in == "4":  # Simultaneous matching
        print("\n"+43*"-")

        if rf._isnan(_gammaS_match) or rf._isnan(_gammaL_match):
            print("Unable to match network.")

        else:
            print("|Γ_S| = "+sf._round_fix(abs(_gammaS_match)))
            print("arg(Γ_S) = "+sf._round_fix(cm.phase(_gammaS_match)*180/pi, unit="deg"))

            print("\n|Γ_L| = "+sf._round_fix(abs(_gammaL_match)))
            print("arg(Γ_L) = "+sf._round_fix(cm.phase(_gammaL_match)*180/pi, unit="deg"))

            print("\nZ_S = "+sf._complex_round_fix(_ZS_match, unit="Ω"))
            print("Z_L = "+sf._complex_round_fix(_ZL_match, unit="Ω"))

        input("\nPress [ENTER] to continue.")

    elif str_in == "5":  # Input low-pass L network
        print("\n"+43*"-")

        if rf._isnan(_Q_in_lp) or rf._isnan(_LC1_in_lp) or rf._isnan(_LC2_in_lp):
            print("Unable to match network.")
        else:
            print("Q = "+sf._round_fix(_Q_in_lp))

            if _source_parallel_lp:
                print("\nIn parallel with source:")
            else:
                print("\nIn series with source:")

            if _LC1_in_lp > 0:
                print("L = "+sf._round_eng(_LC1_in_lp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC1_in_lp, unit="F"))

            if _source_parallel_lp:
                print("\nIn series with amp input:")
            else:
                print("\nIn parallel with amp input:")

            if _LC2_in_lp > 0:
                print("L = "+sf._round_eng(_LC2_in_lp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC2_in_lp, unit="F"))

        input("\nPress [ENTER] to continue.")

    elif str_in == "6":  # Input high-pass L network
        print("\n"+43*"-")

        if rf._isnan(_Q_in_hp) or rf._isnan(_LC1_in_hp) or rf._isnan(_LC2_in_hp):
            print("Unable to match network.")
        else:
            print("Q = "+sf._round_fix(_Q_in_hp))

            if _source_parallel_hp:
                print("\nIn parallel with source:")
            else:
                print("\nIn series with source:")

            if _LC1_in_hp > 0:
                print("L = "+sf._round_eng(_LC1_in_hp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC1_in_hp, unit="F"))

            if _source_parallel_hp:
                print("\nIn series with amp input:")
            else:
                print("\nIn parallel with amp input:")

            if _LC2_in_hp > 0:
                print("L = "+sf._round_eng(_LC2_in_hp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC2_in_hp, unit="F"))

        input("\nPress [ENTER] to continue.")

    elif str_in == "7":  # Output low-pass L network
        print("\n"+43*"-")

        if rf._isnan(_Q_out_lp) or rf._isnan(_LC1_out_lp) or rf._isnan(_LC2_out_lp):
            print("Unable to match network.")
        else:
            print("Q = "+sf._round_fix(_Q_out_lp))

            if _amp_parallel_lp:
                print("\nIn parallel with amp output:")
            else:
                print("\nIn series with amp output:")

            if _LC1_out_lp > 0:
                print("L = "+sf._round_eng(_LC1_out_lp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC1_out_lp, unit="F"))

            if _amp_parallel_lp:
                print("\nIn series with load:")
            else:
                print("\nIn parallel with load:")

            if _LC2_out_lp > 0:
                print("L = "+sf._round_eng(_LC2_out_lp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC2_out_lp, unit="F"))

        input("\nPress [ENTER] to continue.")

    elif str_in == "8":  # Output high-pass L network
        print("\n"+43*"-")

        if rf._isnan(_Q_out_hp) or rf._isnan(_LC1_out_hp) or rf._isnan(_LC2_out_hp):
            print("Unable to match network.")
        else:
            print("Q = "+sf._round_fix(_Q_out_hp))

            if _amp_parallel_hp:
                print("\nIn parallel with amp output:")
            else:
                print("\nIn series with amp output:")

            if _LC1_out_hp > 0:
                print("L = "+sf._round_eng(_LC1_out_hp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC1_out_hp, unit="F"))

            if _amp_parallel_hp:
                print("\nIn series with load:")
            else:
                print("\nIn parallel with load:")

            if _LC2_out_hp > 0:
                print("L = "+sf._round_eng(_LC2_out_hp, unit="H"))
            else:
                print("C = "+sf._round_eng(-_LC2_out_hp, unit="F"))

        input("\nPress [ENTER] to continue.")

    elif str_in == "9":  # Input and output impedances
        print("\n"+43*"-")

        print("|Γ_in| = "+sf._round_fix(abs(_gamma_in)))
        print("arg(Γ_in) = "+sf._round_fix(cm.phase(_gamma_in)*180/pi, unit="deg"))

        print("\n|Γ_out| = "+sf._round_fix(abs(_gamma_out)))
        print("arg(Γ_out) = "+sf._round_fix(cm.phase(_gamma_out)*180/pi, unit="deg"))

        print("\nZ_in = "+sf._complex_round_fix(_Zin, unit="Ω"))
        print("Z_out = "+sf._complex_round_fix(_Zout, unit="Ω"))

        input("\nPress [ENTER] to continue.")

    else:  # End program
        _loop_flag = False

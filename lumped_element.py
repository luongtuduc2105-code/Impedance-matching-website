import cmath
import math

def lumped_element_matching_method(Z_l, Z_0, f, e_r):
    # Input values:
    wave_length=((3*10**8)/(f))*(1/(e_r**0.5))
    omega=f*2*math.pi
    beta=(2*math.pi)/(wave_length)

    # Calculate reflection coeff value:
    Delta=(Z_l-Z_0)/(Z_l+Z_0)
    theta_r_rad=cmath.phase(Delta) # theta_r angle is currently in rad
    abs_delta=abs(Delta)
    if abs(Delta) < 1e-12:
        return {
            "matched": True,
            "message": "The load is matched to the line, no matching element needed."
        }

    # Calculate the value of theta'
    theta_1=math.acos(-(abs_delta))
    theta_2=-theta_1

    # Calculate case 1
    d1=(theta_r_rad-theta_1)/(2*beta)
    d1 = d1 % (wave_length / 2)
    bs1=(2*abs_delta*math.sin(theta_1))/((1+abs_delta*math.cos(theta_1))**2 + (abs_delta)**2 * (math.sin(theta_1)**2))
    y_s1=1j*bs1
    z_s1=1/(y_s1)
    Z_s1=Z_0*z_s1
    if Z_s1.imag > 0:
        L1=(Z_s1.imag)/(omega)
        kq1=f"Method 1: We need to place an inductor with an inductance of: {L1} and at a distance from the load of: {d1}"
    else:
        C1=-1/(omega*Z_s1.imag)
        kq1=f"Method 1: We need to place a capacitor with a capacitance of: {C1} and at a distance from the load of: {d1}"

    # Calculate case 2
    d2=(theta_r_rad-theta_2)/(2*beta)
    d2 = d2 % (wave_length / 2) # Automatically add 1/2 wavelength if d2 is negative
    bs2=(2*abs_delta*math.sin(theta_2))/((1+abs_delta*math.cos(theta_2))**2 + (abs_delta)**2 * (math.sin(theta_2)**2))
    y_s2=1j*bs2
    z_s2=1/(y_s2)
    Z_s2=Z_0*z_s2
    if Z_s2.imag > 0:
        L2=(Z_s2.imag)/(omega)
        kq2=f"Method 2: We need to place an inductor with an inductance of: {L2} and at a distance from the load of: {d2}"
    else:
        C2=-1/(omega*Z_s2.imag)
        kq2=f"Method 2: We need to place a capacitor with a capacitance of: {C2} and at a distance from the load of: {d2}"
    return f"{kq1}\n\n{kq2}"
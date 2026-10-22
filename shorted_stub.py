import cmath
import math

def shorted_stub_matching_method(Z_l, Z_0, f, e_r):
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
    if abs(bs1) < 1e-12:
        beta_l1 = math.pi / 2
    else:
        beta_l1 = math.atan(-1 / bs1)
        beta_l1 = beta_l1 % math.pi
    y_s1=1j*bs1
    l1=beta_l1/beta
    kq1=f"Method 1: We need to place a shorted stub with a length of l={l1} and at a distance from the load of: {d1}"

    # Calculate case 2
    d2=(theta_r_rad-theta_2)/(2*beta)
    d2 = d2 % (wave_length / 2) # Automatically add 1/2 wavelength if d2 is negative
    bs2=(2*abs_delta*math.sin(theta_2))/((1+abs_delta*math.cos(theta_2))**2 + (abs_delta)**2 * (math.sin(theta_2)**2))
    if abs(bs2) < 1e-12:
        beta_l2 = math.pi / 2
    else:
        beta_l2 = math.atan(-1 / bs2)
        beta_l2 = beta_l2 % math.pi
    y_s2=1j*bs2
    l2=beta_l2/beta
    kq2=f"Method 2: We need to place a shorted stub with a length of l={l2} and at a distance from the load of: {d2}"
    return f"{kq1}\n\n{kq2}"
import cmath
import math

def quarter_wavelength_matching_method(Z_l, Z_0, f, e_r):
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


    # Determine d_max and d_min
    if theta_r_rad<0:
        d_max=((theta_r_rad*wave_length)/(4*math.pi))+(wave_length/2)
    else:
        d_max=((theta_r_rad*wave_length)/(4*math.pi))

    if d_max<(wave_length/4):
        d_min=d_max+(wave_length/4)
    else:
        d_min=d_max-(wave_length/4)

    # When placing a transformer at a distance of d_max or d_min from the load, both the input impedance and the reflection coefficient are real numbers

    # Position 1: At a distance d_max from the load
    Z_d_max=Z_0*((1+abs_delta)/(1-abs_delta)) # Impedance value at a distance d_max from the load
    Z_02_max=math.sqrt(Z_0*Z_d_max)
    kq1=f"Method 1: Place a lambda/4 transformer with an impedance of: {Z_02_max} and a distance to the load of: {d_max}"

    # Position 2: At a distance d_min from the load
    Z_d_min=Z_0*((1-abs_delta)/(1+abs_delta)) # Impedance value at a distance d_min from the load
    Z_02_min=math.sqrt(Z_0*Z_d_min)
    kq2=f"Method 2: Place a lambda/4 transformer with an impedance of: {Z_02_min} and a distance to the load of: {d_min}"
    return f"{kq1}\n\n{kq2}"
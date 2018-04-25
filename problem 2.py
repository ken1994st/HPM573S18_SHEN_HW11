# transition matrix without treatment
TRANS_MATRIX = [
    [None,  0.0136,   0.0,    0.0015,  0.0178],   # Well
    [0.0,     None,    52.14,    0.0,  0.0],   # Stroke
    [0,     0.00208,   None,   0.00052,  0.0178],   # Post-Stroke
    [0.0,   0.0,    0.0,    0.0,  None],   # Dead
    ]

# transition matrix with treatment
TRANS_MATRIX_TREAT = [
     [None,  0.0136,   0.0,    0.0015,  0.0178],   # Well
    [0.0,     None,    52.14,    0.0,  0.0],   # Stroke
    [0,     0.00156,   None,   0.00052,  0.0178],   # Post-Stroke
    [0.0,   0.0,    0.0,  0.0,  None],   # Dead
    ]

print("the rate of non stroke-associated is -ln(1-(18/1000-36.2/100000))*105%", 0.0187)
print("the annual rate of transition from state Post-Stroke to Stroke is 25% lower", 0.00156)

### Implementing and simulating multiplexers in PyRTL ###

from ast import BitAnd
import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
# < add your code here >
a = pyrtl.Input(bitwidth=3, name='a')
b = pyrtl.Input(bitwidth=3, name='b')
c = pyrtl.Input(bitwidth=3, name='c')
d = pyrtl.Input(bitwidth=3, name='d')
e = pyrtl.Input(bitwidth=3, name='e')

# Declare control inputs
s_0 = pyrtl.Input(bitwidth=3, name='s_0')
s_1 = pyrtl.Input(bitwidth=3, name='s_1')
s_2 = pyrtl.Input(bitwidth=3, name='s_2')

# Declare outputs 
# < add your code here >
o = pyrtl.Output(bitwidth=3, name='o')

# Describe your 5:1 MUX implementation
# < add your code here >

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >

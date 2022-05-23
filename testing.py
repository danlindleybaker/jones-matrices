from jones_matrices import calculate_polarisation #type:ignore

input_polarisation = 'Linear 45 Degrees'
optics_list = ['Quarter Wave Plate, Slow Axis Horizontal']


output, string = calculate_polarisation(optics_list,input_polarisation)

print(output)
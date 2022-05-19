"""

Jones matrices calculations

"""



import numpy as np

H_Polariser = np.array(([1,0],[0,0]))
V_Polariser = np.array(([0,0],[0,1]))

Lin_Polariser_45 = 0.5*np.array([[1,1],[1,1]])
Lin_Polariser_minus45 = 0.5*np.array(([1,-1],[-1,1]))

#QWP_H = np.exp(1j*np.pi/4)*np.array(([1,0],[0,-1*1j]))
#QWP_V = np.exp(1j*np.pi/4)*np.array(([1,0],[0,1j]))

QWP_H = np.array(([1,0],[0,-1*1j]))
QWP_V = np.array(([1,0],[0,1j]))

h_lin_pol = np.array([[1, 0]]).T
v_lin_pol = np.array([[0, 1]]).T

lin_pol_45 = (1/np.sqrt(2))*np.array([[1,1]]).T
lin_pol_minus45 = (1/np.sqrt(2))*np.array([[1,-1]]).T

right_circ_pol = (1/np.sqrt(2))*np.array([[1,-1*1j]]).T
left_circ_pol = (1/np.sqrt(2))*np.array([[1,1j]]).T

HWP_H = QWP_H.dot(QWP_H)
HWP_V = QWP_V.dot(QWP_V)

polarisation_dict = {'Linear Horizontal': h_lin_pol, 
                     'Linear Vertical': v_lin_pol, 
                     'Linear 45 Degrees': lin_pol_45,
                     'Linear -45 Degrees': lin_pol_minus45,
                    'Right Circular': right_circ_pol,
                    'Left Circular': left_circ_pol,}

optical_element_dict = {'Horizontal Linear Polariser': H_Polariser,
                        'Vertical Linear Polariser': V_Polariser,
                        'Linear Polariser at 45 Degrees': Lin_Polariser_45,
                        'Linear Polariser at -45 Degrees': Lin_Polariser_minus45,
                        'Quarter Wave Plate, Slow Axis Horizontal': QWP_H,
                        'Quarter Wave Plate, Slow Axis Vertical': QWP_V,
                        'Half Wave Plate, Slow Axis Horizontal': HWP_H,
                        'Half Wave Plate, Slow Axis Vertical': HWP_V,}



def calculate_polarisation(optics_list,input_polarisation):
   if len(optics_list) > 0:
    for i,element in enumerate(optics_list):
        if i == 0:
            polarisation = optical_element_dict[element].dot(polarisation_dict[input_polarisation])

        else:
            polarisation = optical_element_dict[element].dot(polarisation)

    
    #if np.size(polarisation) == 2:
    #   for i,x in enumerate(polarisation): 
    #      if x!=0:
    #         polarisation[i]=1
           
             


    for key in polarisation_dict:
        comparison = polarisation_dict[key] == polarisation

        if comparison.all():

            return key
      
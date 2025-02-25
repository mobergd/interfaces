"""
 tests writing of projrot input
"""

import numpy as np
import projrot_io


# Set info for writing the file
GEOM = (('C', (-4.0048955763, -0.3439866053, -0.0021431734)),
        ('O', (-1.3627056155, -0.3412713280, 0.0239463418)),
        ('H', (-4.7435343957, 1.4733340928, 0.7491098889)),
        ('H', (-4.7435373042, -1.9674678465, 1.1075144307)),
        ('H', (-4.6638955748, -0.5501793084, -1.9816675556)),
        ('H', (-0.8648060003, -0.1539639444, 1.8221471090)))
GRAD = ((-4.0048955763, -0.3439866053, -0.0021431734),
        (-1.3627056155, -0.3412713280, 0.0239463418),
        (-4.7435343957, 1.4733340928, 0.7491098889),
        (-4.7435373042, -1.9674678465, 1.1075144307),
        (-4.6638955748, -0.5501793084, -1.9816675556),
        (-0.8648060003, -0.1539639444, 1.8221471090))
HESS = np.random.rand(33, 33)
AXIS = [5, 6]
GROUP = [7, 8, 9, 10, 11, 12]
COORD_PROJ = 'cartesian'


def test__writer():
    """ test projrot_io.writer.rotors_str and
        test projrot_io.writer.rpht_input
    """

    # Write the rotors string
    rotors_str = projrot_io.writer.rotors(AXIS, GROUP)

    # Write the string for the ProjRot input
    inp_str = projrot_io.writer.rpht_input(GEOM, GRAD, HESS,
                                           rotors_str=rotors_str,
                                           coord_proj=COORD_PROJ)

    # Print the string
    print(inp_str)


if __name__ == '__main__':
    test__writer()

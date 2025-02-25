""" test chemkin_io.mechparser.mechanism
"""

from __future__ import unicode_literals
from builtins import open
import os
import pandas
import automol
import chemkin_io.mechparser


def _read_file(file_name):
    with open(file_name, encoding='utf8', errors='ignore') as file_obj:
        file_str = file_obj.read()
    return file_str


PATH = os.path.dirname(os.path.realpath(__file__))
NATGAS_PATH = os.path.join(PATH, '../data/natgas')
HEPTANE_PATH = os.path.join(PATH, '../data/heptane')
SYNGAS_PATH = os.path.join(PATH, '../data/syngas')
TEST_PATH = os.path.join(PATH, '../data/test')

NATGAS_MECH_STR = _read_file(os.path.join(NATGAS_PATH, 'mechanism.txt'))

HEPTANE_MECH_STR = _read_file(os.path.join(HEPTANE_PATH, 'mechanism.txt'))
HEPTANE_TAB = pandas.read_csv(os.path.join(HEPTANE_PATH, 'species_smiles.csv'))
HEPTANE_TAB['inchi'] = list(map(automol.smiles.inchi, HEPTANE_TAB['smiles']))

SYNGAS_MECH_STR = _read_file(os.path.join(SYNGAS_PATH, 'mechanism.txt'))
SYNGAS_CSV_STR = _read_file(os.path.join(SYNGAS_PATH, 'smiles.csv'))

M3_MECH_STR = _read_file(os.path.join(TEST_PATH, 'm3.txt'))
M4_MECH_STR = _read_file(os.path.join(TEST_PATH, 'm4.txt'))


def test__species_block():
    """ test chemkin_io.mechparser.mechanism.species_block
    """

    mech_str = NATGAS_MECH_STR
    block_str = chemkin_io.mechparser.mechanism.species_block(mech_str)
    assert len(block_str.splitlines()) == 131


def test__reaction_block():
    """ test chemkin_io.mechparser.mechanism.reaction_block
    """

    mech_str = NATGAS_MECH_STR
    block_str = chemkin_io.mechparser.mechanism.reaction_block(mech_str)
    assert len(block_str.splitlines()) == 1834


def test__thermo_block():
    """ test chemkin_io.mechparser.mechanism.thermo_block
    """

    mech_str = NATGAS_MECH_STR
    block_str = chemkin_io.mechparser.mechanism.thermo_block(mech_str)
    assert len(block_str.splitlines()) == 522


def test__reaction_units():
    """ test chemkin_io.mechparser.mechanism.reaction_units
    """
    mech1_str = NATGAS_MECH_STR
    units1 = chemkin_io.mechparser.mechanism.reaction_units(mech1_str)
    mech2_str = SYNGAS_MECH_STR
    units2 = chemkin_io.mechparser.mechanism.reaction_units(mech2_str)
    mech3_str = HEPTANE_MECH_STR
    units3 = chemkin_io.mechparser.mechanism.reaction_units(mech3_str)
    mech4_str = M3_MECH_STR
    units4 = chemkin_io.mechparser.mechanism.reaction_units(mech4_str)
    mech5_str = M4_MECH_STR
    units5 = chemkin_io.mechparser.mechanism.reaction_units(mech5_str)
    print(units1)
    print(units2)
    print(units3)
    print(units4)
    print(units5)


def test__name_inchi_dct():
    """ test chemkin_io.mechparser.species.name_inchi_dct
    """
    name_inchi_dct = chemkin_io.mechparser.mechanism.species_name_inchi_dct(
        SYNGAS_CSV_STR)
    for key, val in name_inchi_dct.items():
        print(key)
        print(val)


def test__inchi_name_dct():
    """ test chemkin_io.mechparser.species.inchi_name_dct
    """
    inchi_name_dct = chemkin_io.mechparser.mechanism.species_inchi_name_dct(
        SYNGAS_CSV_STR)
    for key, val in inchi_name_dct.items():
        print(key)
        print(val)


if __name__ == '__main__':
    # test__species_block()
    # test__reaction_block()
    # test__thermo_block()
    test__reaction_units()
    # test__name_inchi_dct()
    # test__inchi_name_dct()

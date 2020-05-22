# -*- coding: utf-8 -*-
"""
Blackmagic Log Encodings
========================

Defines the *Blackmagic Log* encodings:

-   :func:`colour.models.log_encoding_BMDFilm`
-   :func:`colour.models.log_decoding_BMDFilm`
-   :func:`colour.models.log_encoding_BMD4KFilm`
-   :func:`colour.models.log_decoding_BMD4KFilm`
-   :func:`colour.models.log_encoding_BMD46KFilm`
-   :func:`colour.models.log_decoding_BMD46KFilm`
-   :func:`colour.models.log_encoding_BMDPocket4KFilmV4`
-   :func:`colour.models.log_decoding_BMDPocket4KFilmV4`
-   :func:`colour.models.log_encoding_BMDPocket6KFilmV4`
-   :func:`colour.models.log_decoding_BMDPocket6KFilmV4`

References
----------
-   :cite:`Blackmagic2020a` : Blackmagic Design. (2020). DaVinci Resolve
    CIE Chromaticity Plot.
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.models.rgb.transfer_functions import full_to_legal, legal_to_full
from colour.utilities import (as_float, domain_range_scale, from_range_1,
                              to_domain_1)
from colour.utilities.deprecation import handle_arguments_deprecation

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'log_encoding_BMDFilm', 'log_decoding_BMDFilm', 'log_encoding_BMD4KFilm',
    'log_decoding_BMD4KFilm', 'log_encoding_BMD46KFilm',
    'log_decoding_BMD46KFilm', 'log_encoding_BMDPocket4KFilmV4',
    'log_decoding_BMDPocket4KFilmV4', 'log_encoding_BMDPocket6KFilmV4',
    'log_decoding_BMDPocket6KFilmV4'
]

def interp(x, table, invert=False):
    domain = np.linspace(0, 1, len(table))
    if invert:
        return np.interp(x, table, domain)
    else:
        return np.interp(x, domain, table)

BMDFILM_LUT = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
BMD4KFILM_LUT = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
BMD46KFILM_LUT = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
BMDPOCKET4KFILM_LUT = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
BMDPOCKET6KFILM_LUT = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

def log_encoding_BMDFilm(x):
    """
    Defines the *Blackmagic Film* log encoding curve / opto-electronic transfer
    function.

    Parameters
    ----------
    x : numeric or array_like
        Linear data :math:`x`.

    Returns
    -------
    numeric or ndarray
        *Blackmagic Film* non-linear data.

    References
    ----------
    :cite:`Blackmagic2020a`

    Notes
    -----

    +---------------+-----------------------+---------------+
    | **Domain**    | **Scale - Reference** | **Scale - 1** |
    +===============+=======================+===============+
    | ``x``         | [0, 1]                | [0, 1]        |
    +---------------+-----------------------+---------------+

    +---------------+-----------------------+---------------+
    | **Range**     | **Scale - Reference** | **Scale - 1** |
    +===============+=======================+===============+
    | ``bmdfilm``   | [0, 1]                | [0, 1]        |
    +---------------+-----------------------+---------------+

    Examples
    --------
    >>> log_encoding_BMDFilm(0.18) # doctest: +ELLIPSIS
    0.3835615...
    """

    x = to_domain_1(x)

    with domain_range_scale('ignore'):
        bmdfilm = interp(x, BMDFILM_LUT, invert=True)

    return as_float(from_range_1(bmdfilm))


def log_decoding_BMDFilm(bmdfilm):
    """
    Defines the *Blackmagic Film* log decoding curve / electro-optical transfer
    function.

    Parameters
    ----------
    bmdfilm : numeric or array_like
        *Blackmagic Film* non-linear data.

    Returns
    -------
    numeric or ndarray
        Linear data :math:`x`.

    Notes
    -----

    +---------------+-----------------------+---------------+
    | **Domain**    | **Scale - Reference** | **Scale - 1** |
    +===============+=======================+===============+
    | ``bmdfilm``         | [0, 1]                | [0, 1]        |
    +---------------+-----------------------+---------------+

    +---------------+-----------------------+---------------+
    | **Range**     | **Scale - Reference** | **Scale - 1** |
    +===============+=======================+===============+
    | ``x``         | [0, 1]                | [0, 1]        |
    +---------------+-----------------------+---------------+

    References
    ----------
    :cite:`Blackmagic2020a`

    Examples
    --------
    >>> log_decoding_BMDFilm(0.3835615)  # doctest: +ELLIPSIS
    0.17999999...
    """

    bmdfilm = to_domain_1(bmdfilm)

    x = interp(bmdfilm, BMDFILM_LUT, invert=False)

    return as_float(from_range_1(x))

def log_encoding_BMD4KFilm(x):
    return interp(x, BMD4KFILM_LUT, invert=True)

def log_decoding_BMD4KFilm(y):
    return interp(y, BMD4KFILM_LUT, invert=False)

def log_encoding_BMD46KFilm(x):
    return interp(x, BMD4KFILM_LUT, invert=True)

def log_decoding_BMD46KFilm(y):
    return interp(y, BMD4KFILM_LUT, invert=False)

def log_encoding_BMDPocket4KFilmV4(x):
    return interp(x, BMDPOCKET4KFILM_LUT, invert=True)

def log_decoding_BMDPocket4KFilmV4(y):
    return interp(y, BMDPOCKET4KFILM_LUT, invert=False)

def log_encoding_BMDPocket6KFilmV4(x):
    return interp(x, BMDPOCKET6KFILM_LUT, invert=True)

def log_decoding_BMDPocket6KFilmV4(y):
    return interp(y, BMDPOCKET4KFILM_LUT, invert=False)

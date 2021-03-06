"""
Image, time-frequency map and spectrogram objects
=================================================

Use and control image, time-frequency maps and spectrogram.

.. image:: ../../picture/picobjects/ex_imtfspec_obj.png
"""
import numpy as np
from visbrain.objects import (ImageObj, TimeFrequencyObj, ColorbarObj,
                              SceneObj)

CBAR_STATE = dict(cbtxtsz=12, txtsz=10., width=.2, rect=(-0.2, -2., 1., 4.))
sc = SceneObj(size=(1200, 1000))

"""Create a 2-D image
"""
n = 10
time = np.r_[np.arange(n - 1), np.arange(n)[::-1]]
time = time.reshape(-1, 1) + time.reshape(1, -1)
time[np.diag_indices_from(time)] = 30.

print("""
# =============================================================================
#                              Basic image
# =============================================================================
""")
im_basic = ImageObj('im', time)
sc.add_to_subplot(im_basic, row=0, col=0, title='Basic image')

print("""
# =============================================================================
#                           Interpolated image
# =============================================================================
""")
im_interp = ImageObj('im', time, interpolation='bicubic')
sc.add_to_subplot(im_interp, row=0, col=1, title='Interpolated image')

print("""
# =============================================================================
#                         Custom color properties
# =============================================================================
""")
im_color = ImageObj('im', time, interpolation='bicubic', cmap='Spectral_r',
                    vmin=5., vmax=20., under='gray', over='darkred')
sc.add_to_subplot(im_color, row=0, col=2, title='Custom colors')
cb_im_color = ColorbarObj(im_color, cblabel='Image data', **CBAR_STATE)
sc.add_to_subplot(cb_im_color, row=0, col=3, width_max=150)

"""Define a 25hz sine
"""
n, sf = 512, 256
time = np.arange(n) / sf  # time vector
data = np.sin(2 * np.pi * 25. * time) + np.random.rand(n)

print("""
# =============================================================================
#                                Spectrogram
# =============================================================================
""")
spec = TimeFrequencyObj('spec', data, sf, cmap='RdBu_r')
sc.add_to_subplot(spec, row=1, col=0, title='Spectrogram')

print("""
# =============================================================================
#                             Time-frequency map
# =============================================================================
""")
tf = TimeFrequencyObj('tf', data, sf, method='wavelet')
sc.add_to_subplot(tf, row=1, col=1, title='Time-frequency map')

print('\n-> Compute time-frequency map with windows')
print("""
# =============================================================================
#                                 Multi-taper
# =============================================================================
""")
tf_mt = TimeFrequencyObj('mt', data, sf, method='multitaper', overlap=.7,
                         interpolation='bicubic', cmap='Spectral_r')
sc.add_to_subplot(tf_mt, row=1, col=2, title='Multi-taper')
cb_tf_win = ColorbarObj(tf_mt, cblabel='Power', **CBAR_STATE)
sc.add_to_subplot(cb_tf_win, row=1, col=3, width_max=150)

sc.preview()

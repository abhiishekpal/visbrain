"""
Connectivity object
===================

Illustration of the main functionalities and inputs of the connctivity object.

.. image:: ../../picture/picobjects/ex_connect_obj.png
"""
import numpy as np

from visbrain.objects import ConnectObj, SceneObj, SourceObj, BrainObj
from visbrain.io import download_file

arch = np.load(download_file('phase_sync_delta.npz'))
nodes, edges = arch['nodes'], arch['edges']

sc = SceneObj(bgcolor=(.1, .1, .1))

print("""
# =============================================================================
#                       Color by connectivity strength
# =============================================================================
""")
c_default = ConnectObj('default', nodes, edges, select=edges > .7,
                       cmap='Spectral_r', line_width=2.)
s_obj = SourceObj('sources', nodes, color='#ab4642', radius_min=15.)
sc.add_to_subplot(c_default, title='Color by connectivity strength')
sc.add_to_subplot(s_obj)
sc.add_to_subplot(BrainObj('B1'), use_this_cam=True)

print("""
# =============================================================================
#                    Color by number of connections per node
# =============================================================================
""")
c_count = ConnectObj('default', nodes, edges, select=edges > .7,
                     color_by='count', antialias=True, line_width=4.,
                     dynamic=(.1, 1.))
s_obj_c = SourceObj('sources', nodes, color='olive', radius_min=10.,
                    symbol='square')
sc.add_to_subplot(c_count, row=0, col=1,
                  title='Color by number of connections per node')
sc.add_to_subplot(s_obj_c, use_this_cam=True, row=0, col=1)
sc.add_to_subplot(BrainObj('B3'), use_this_cam=True, row=0, col=1)

print("""
# =============================================================================
#                                 Custom colors
# =============================================================================
""")
edges_copy = edges.copy()
edges_copy[edges_copy >= .85] = 3.1
edges_copy[np.logical_and(edges_copy >= .8, edges_copy < .9)] = 2.7
edges_copy[np.logical_and(edges_copy >= .75, edges_copy < .8)] = 1.5
ccol = {1.5: 'red', 2.7: 'blue', 3.1: 'orange', None: 'lightgray'}
c_cuscol = ConnectObj('default', nodes, edges_copy, select=edges > .7,
                      custom_colors=ccol)
s_obj_cu = SourceObj('sources', nodes, color='slategray', radius_min=10.,
                     symbol='ring')
sc.add_to_subplot(c_cuscol, row=0, col=2, title='Custom colors')
sc.add_to_subplot(s_obj_cu, row=0, col=2)
sc.add_to_subplot(BrainObj('white'), use_this_cam=True, row=0, col=2)

sc.preview()

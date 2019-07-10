# coding: utf-8

import os
import mne
import time
import matplotlib.pyplot as plt

''' ==============================================================
Function : Setup enviroments
Outputs  : subjects_dir, subject, trans, epochs_dir, epoch_path, info
self.subjects_dir = subjects_dir in freesurfer style
self.subject = subject_id in freesurfer style
self.trans = trans made by mne coreg
self.epochs_dir = dir of epochs
self.epoch_path = path of THE EPOCH
self.info = info of THE EPOCH

-------------------------------------------------------------- '''
print('#:', time.ctime(), 'Setup environments starts.')

subjects_dir = 'd:\\freesurfer\\subjects'
subject = 's02_bem'
trans = os.path.join(subjects_dir, subject, 's02-trans.fif')

epochs_dir = 'D:\\RSVP_MEG_experiment\\epochs_saver\\epochs_freq_0.5_30_crop_n0.2_p1.1'
epoch_path = os.path.join(epochs_dir, 'meg_S02_epochs_4-epo.fif')
info = mne.io.read_info(epoch_path)
print(info)

print('#:', time.ctime(), 'Setup environments done.')


''' ==============================================================
Function : Plot bem
Outputs  : None
self.None = None

-------------------------------------------------------------- '''
print('#:', time.ctime(), 'Plot bem starts.')

mne.viz.plot_bem(subject=subject, subjects_dir=subjects_dir,
                 brain_surfaces='white', orientation='coronal',
                 show=False)

print('#:', time.ctime(), 'Plot bem done.')


''' ==============================================================
Function : Compute source space and plot
Outputs  : src
self.src = source space as triangles

-------------------------------------------------------------- '''
print('#:', time.ctime(), 'Compute source space and plot starts.')

src = mne.setup_source_space(subject, spacing='oct6',
                             subjects_dir=subjects_dir, add_dist=False)
print(src)
mne.viz.plot_bem(subject=subject, subjects_dir=subjects_dir,
                 src=src,
                 brain_surfaces='white', orientation='coronal',
                 show=False)

print('#:', time.ctime(), 'Compute source space and plot done.')


''' ==============================================================
Function : Compute source space (defined with a grid) and plot
Outputs  : vol_src
self.vol_src = source space in triangles, defined with a grid

-------------------------------------------------------------- '''
print('#:', time.ctime(),
      'Compute source space [defined with a grid] and plot starts.')

surface = os.path.join(subjects_dir, subject, 'bem', 'inner_skull.surf')
vol_src = mne.setup_volume_source_space(subject, subjects_dir=subjects_dir,
                                        surface=surface)
print(vol_src)

mne.viz.plot_bem(subject=subject, subjects_dir=subjects_dir,
                 src=vol_src,
                 brain_surfaces='white', orientation='coronal',
                 show=False)
print(time.ctime(),
      'Compute source space [defined with a grid] and plot done.')

print('#:', time.ctime(),
      'Compute source space [defined with a grid] and plot done.')


plt.show()


'''
# These code is to show surface, however they do not work in win10

import numpy as np  # noqa
import matplotlib.pyplot as plt  # noqa
from mayavi import mlab  # noqa
from surfer import Brain  # noqa

brain = Brain(subject, 'lh', 'inflated', alpha=0.5,
              interaction='terrain', subjects_dir=subjects_dir)
surf = brain.geo['lh']

vertidx = np.where(src[0]['inuse'])[0]

mlab.points3d(surf.x[vertidx], surf.y[vertidx],
              surf.z[vertidx], color=(1, 1, 0), scale_factor=1.5)

a = input('Press any key to quit.')
'''

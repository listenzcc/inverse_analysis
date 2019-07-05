# coding: utf-8

import os
import mne

subjects_dir = os.path.join(
    'd:\\', 'RSVP_MEG_experiment', 'inverse_analysis', 'freesurfer_subjects')
subject = 's02'

mne.viz.plot_bem(subject=subject, subjects_dir=subjects_dir,
                 brain_surfaces='white', orientation='coronal')

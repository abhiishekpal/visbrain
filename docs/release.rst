.. _Release:

Changelog
=========

.. contents:: Contents
   :local:
   :depth: 1

0.4.1
-----

New features
~~~~~~~~~~~~

* You can now :ref:`replace_detection` using the :class:`visbrain.Sleep.replace_detections` method.
* Add activations (:class:`visbrain.objects.CrossSecObj.set_activation`) and highlight multiple sources (:class:`visbrain.objects.CrossSecObj.highlight_sources`) inside the :class:`visbrain.objects.CrossSecObj`
* Plot MNE sources :class:`visbrain.mne.mne_plot_source_space`

Improvements
~~~~~~~~~~~~

* :class:`visbrain.objects.CrossSecObj` : much faster + colormap computed onto the GPU + superposition of multiple mask + keyboard interactions

Bug fixes
~~~~~~~~~

* :class:`visbrain.objects.BrainObj.parcellize` using nibabel >= 2.3
* colorbar control of :class:`visbrain.objects.Picture3DObj` object
* add multiple objects to the :class:`visbrain.objects.SceneObj` with *row_span* and / or *col_span* > 1 
* path to brain templates
* loading hypnogram with spaces instead of tabs
* Fix :class:`visbrain.mne.mne_plot_source_estimation` with left and right hemispheres
* Fix activations that disappear using :class:`visbrain.Brain.brain_control`
* Fix x and y axis update inside :class:`visbrain.Signal`
* Reading Nifti files with NaN values

0.4.0
-----

New features
~~~~~~~~~~~~

* Plot MNE estimated sources :class:`visbrain.mne.mne_plot_source_estimation`

Improvements
~~~~~~~~~~~~

* JSON saving for configuration file

Bug fixes
~~~~~~~~~

* visbrain installation (no requirements file)
* compatibility with numpy and pip
* broken examples + templates/ folder
* Hypnogram is now exported as a .txt file with stage-duration encoding.
* .xlsx and EDF+ are now supported for hypnogram
* units when loading with MNE
* warning in UTF-8 file loading
* compatibility with numpy and pip


0.3.8
-----


New features
~~~~~~~~~~~~

* Multitaper-based spectrogram (require `lspopt <https://github.com/hbldh/lspopt>`_ package, see doc) 

Improvements
~~~~~~~~~~~~

* Added logging
* Code improvements: PEP8 and flake8
* automatic spindles detection
* Simplified and improved Sleep GUI
* Removed drag-and-drop method for hypnogram scoring

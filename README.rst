
Legendre Memory Units: Continuous-Time Representation in Recurrent Neural Networks
----------------------------------------------------------------------------------

`Paper <https://papers.nips.cc/paper/9689-legendre-memory-units-continuous-time-representation-in-recurrent-neural-networks.pdf>`_

We propose a novel memory cell for recurrent neural networks that dynamically maintains information across long windows of time using relatively few resources. The Legendre Memory Unit (LMU) is mathematically derived to orthogonalize its continuous-time history – doing so by solving d coupled ordinary differential equations (ODEs), whose phase space linearly maps onto sliding windows of time via the Legendre polynomials up to degree d − 1 (example d=12, shown below).


.. image:: https://i.imgur.com/Uvl6tj5.png
   :target: https://i.imgur.com/Uvl6tj5.png
   :alt: Legendre polynomials


A single ``LMUCell`` expresses the following computational graph in Keras as an RNN layer, which couples the optimal linear memory (\ ``m``\ ) with a nonlinear hidden state (\ ``h``\ ):


.. image:: https://i.imgur.com/IJGUVg6.png
   :target: https://i.imgur.com/IJGUVg6.png
   :alt: Computational graph


The discretized ``(A, B)`` matrices are initialized according to the LMU's mathematical derivation with respect to some chosen window length, θ. Backpropagation can be used to learn this time-scale, or fine-tune ``(A, B)``\ , if necessary. By default the coupling between the hidden state (\ ``h``\ ) and the memory vector (\ ``m``\ ) is trained via backpropagation, while the dynamics of the memory remain fixed (\ `see paper for details <https://papers.nips.cc/paper/9689-legendre-memory-units-continuous-time-representation-in-recurrent-neural-networks.pdf>`_\ ).

This repository includes a pre-trained Keras/TensorFlow model, located at ``models/psMNIST-standard.hdf5``\ , which obtains the current best-known psMNIST result (using an RNN) of **97.15%**. Note, the network is using fewer internal state-variables and neurons than there are pixels in the input sequence.

----

We recommend Python 3.6+ and a computer with:


* At least 32GB of RAM
* A powerful GPU
* GPU install of ``tensorflow>=1.12.0``

To reproduce all experiments / training / figures:

.. code-block::

   git clone --recurse-submodules https://github.com/abr/neurips2019 lmu
   cd lmu
   pip install -e .
   python figures/legendre-basis.py
   python figures/poisson-performance.py
   jupyter notebook

And then run the notebooks:


* ``experiments/capacity.ipynb``
* ``experiments/psMNIST-standard.ipynb``
* ``experiments/psMNIST-phased-lstm.ipynb``
* ``experiments/mackey-glass.ipynb``

Models will be saved to the ``models`` directory and figures to the ``figures`` directory.

A neuromorphic example deployed on Loihi is located at ``neuromorphic/loihi_lmu.py``. This requires running ``pip install -r neuromorphic/requirements.txt``. If a Loihi board is connected to your computer then it should be automatically detected and used. Otherwise, a detailed hardware emulator is run in software. 

Nengo Examples
--------------


* `Spiking LMUs in Nengo (with online learning) <https://www.nengo.ai/nengo/examples/learning/lmu.html>`_
* `Spiking LMUs in Nengo Loihi (with online learning) <https://www.nengo.ai/nengo-loihi/examples/lmu.html>`_
* `LMUs in NengoDL (reproducing SotA on psMNIST) <https://www.nengo.ai/nengo-dl/examples/lmu.html>`_

Citation
--------

.. code-block::

   @inproceedings{voelker2019lmu,
     title={Legendre Memory Units: Continuous-Time Representation in Recurrent Neural Networks},
     author={Aaron R. Voelker and Ivana Kaji\'c and Chris Eliasmith},
     booktitle={Advances in Neural Information Processing Systems},
     pages={15544--15553},
     year={2019}
   }

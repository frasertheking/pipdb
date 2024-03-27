Installation
=====

How to
------------
With the package cloned to your local system, the pipdb package can be installed by following these steps:

1. cd into the pipdb directory:

.. code-block:: bash

    cd package_dir/pipdb

2. Create a conda environment, and install the required package dependencies using conda:

.. code-block:: bash

    conda env create -f pipdb.yml

3. Activate the pipdb environment:

.. code-block:: bash

    conda activate pipdb

4. Install the package so you can use it anywhere on your system:

.. code-block:: bash

    python setup.py install

With the steup.py file run, you should now be able to access the pipdb API from your other project locations.

Importing
----------------
If everything was downloaded and installed properly, you should now be able to use the API in your projects by importing pipdb:

.. code-block:: bash

    import pipdb


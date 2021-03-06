
The purpose of CLiC
===================

The CLiC webapp provides an easy, mobile-friendly user interface that enables users to explore
literary texts using corpus linguistics. 

It comes with a pre-defined set of literary texts. The app can be used at ``clic.bham.ac.uk``. 

The code is written in Python and Javascript.

Installing CLiC
===============

Quick start
-----------

To deploy a local or public CLiC server, one needs:
     - Docker
     - the CLiC Docker image
     - the pre-processed cheshire3 indexes (for the Concordance, Clusters, and Keywords)
     - a selection of pre-processed text files (for the Subsets, Patterns, and the User Annotation)


Test the installation:


CLiC for developers
-------------------

Cf. the Dockerfile
on a vanilla ubuntu version

Cheshire3 uses a number of packages that are no longer updated. That makes a simple
 ``pip install`` impossible (or, let's say, complex at the least).


Description of the repository
=============================




Cheshire3: The underlying database
==================================

It is not the purpose of these docs to provide a comprehensive intro to cheshire3. For more information 
on cheshire3, cf. ``cheshire3.readthedocs.org``



TODO
====

* Add new texts: Alice in Wonderland
* Package CLiC so a setup.py install is possible
* Auto-sphinx docx

## JupterLab Install Guide

**Prerequisites:**

* [Anaconda Install](AnacondaInstallGuide.md)

This guide walks through the installation and configuration process for JupyterLab.

* Verify that the Anaconda dev environment is activated

* Install JupyterLab

* Launch JupyterLab

### Install JupyterLab

1. Update the Anaconda environment to ensure the latest packages are installed.

  ```shell
  conda update conda
  conda update anaconda
  ```

2. Activate the Anaconda dev environment.

  ```shell
  conda activate dev
  ```

3. Install JupyterLab using the `conda install` command. `conda install` will connect to the JupyterLab GitHub repository, named `conda-forge`, and download the JupyterLab package.

  ```shell
  conda install -c conda-forge jupyterlab
  ```

### Launch JupyterLab

1. Execute the JupyterLab launch command from the Anaconda terminal.

  ```shell
  jupyter lab
  ```

2. The JupyterLab UI should open automatically. If it does not, copy and paste the URL provided in the Anaconda terminal into an internet browser.

  ![Jupyter_Lab_Web_Url.png](Images/Jupyter_Lab_Web_Url.png)

### Explore JupyterLab

Take note of the following components of the JupyterLab interface:

  * File Explorer

  * Launcher

  * Python Notebook

  * Terminal

  * Text File Kernel

## Intel oneAPI Series - Deep Dive (Live Demo and Hands-on): oneAPI and DPC++ on Intel DevCloud

The Intel oneAPI Toolkits based on Data Parallel C++ (DPC++) - modern C++ and SYCL - allows developers to develop, optimize, and deploy algorithms for accelerated computing across XPU architectures (CPU, GPU, FPGA, and other accelerators).

## What will you learn:

* Articulate how oneAPI can help to solve the challenges of programming in a heterogeneous world.
* Understand the DPC++ language and programming model.
* Profile a DPC++ application using Intel VTune Profiler on Intel DevCloud.
* Learn how to migrate CUDA code to Data Parallel C++ using the Intel DPC++ Compatibility tool.

## Agenda 

* Overview of Intel oneAPI and Data Parallel C++ 
* Introduction to the Intel DevCloud
* Setup of Intel DevCloud and JupyterLab Environment
* DPC++ Program Structure 
* Demonstration of Intel VTune Profiler on Intel DevCloud 
* Demonstration of Intel DPC++ Compatibility Tool on Intel DevCloud 

## Get 120 days of Free access (extensions available) of Intel DevCloud - a free development sandbox with access to the latest hardware from Intel and Intel oneAPI software.

[Create an Intel DevCloud Account](https://software.intel.com/devcloud/oneapi)

[Connect with Linux/macOS SSH Client](https://devcloud.intel.com/oneapi/documentation/connect-with-ssh-linux-macos)

[Launch Jupyterlab on your Intel DevCloud account](https://jupyter.oneapi.devcloud.intel.com)

## Clone this Repo for Hands-on Lab

```
git clone https://github.com/mkhpc/oneAPI-Deep-Dive.git
```
| Notebook Name | Description |
|---|---|
|[oneAPI_and_DPCPP_Intro](oneAPI_and_DPCPP_Intro)| * Introduction and Motivation for oneAPI and DPC++ <br>* DPC++ __Hello World__<br>* Compiling DPC++ and __DevCloud__ Usage<br>* ___Lab Excercise___: Vector Increment to Vector Add |
|[DPCPP_Program_Structure](DPCPP_Program_Structure)| * __Classes__ - device, device_selector, queue, basic kernels and ND-Range kernels, Buffers-Accessor memory model<br>* DPC++ __Code Anotomy__<br>* Implicit __Dependency__ with Accessors, __Synchronization__ with Host Accessor and Buffer Destruction<br>* Creating __Custom__ Device Selector<br>* ___Lab Exercise___: Complex Multiplication |
|[Intel_VTune_Profiler](06_Intel_VTune_Profiler)| * Intel VTune™ Profiler usage __in Intel DevCloud__ environment using command-line options<br>* ___Lab Excercise___: VTune Profiling by collecting __gpu_hotspots__ for __iso3dfd__ hotspots sample application. |
|[DPCT_Intro](DPCT_Intro)| * Intel® DPC++ Compatibility Tool Introduction <br>* ___Lab Exercise___: Use the Intel® DPC++ Compatibility Tool to quickly assist in the migration of simple user CUDA* code to DPC++ code |

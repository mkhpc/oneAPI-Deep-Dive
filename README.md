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

"__Get 120 days of Free access (extensions available) of Intel DevCloud - a free development sandbox with access to the latest hardware from Intel and Intel oneAPI software.__"

[Create an Intel DevCloud Account](https://consumer.intel.com/intelcorpb2c.onmicrosoft.com/B2C_1A_UnifiedLogin_SISU_CML_SAML/api/SelfAsserted/confirmed?csrf_token=TFRTTkRGSFBpWStFRlgxQ0U3c2NOOUpLKzZ3d1d1N3dSN2xEREdaS3RjN3lJL3RMM3JuM3YvSDZmWElDVUE2UDMwZ0c4LzBia0dFdGN4anBzL29Rbmc9PTsyMDIzLTA1LTE2VDA3OjU3OjU1LjY5NDk4MjJaO2FXaUxEekFQTVhFTVpQclJORFNaVWc9PTt7IlRhcmdldEVudGl0eSI6IlJlYWRTZXNzaW9uIiwiT3JjaGVzdHJhdGlvblN0ZXAiOjN9&tx=StateProperties=eyJUSUQiOiI2NDQyY2IzMC0wZTI2LTQyZDktYWNiMy0zYWVkZGI1MWNiY2MifQ&p=B2C_1A_UnifiedLogin_SISU_CML_SAML&diags=%7B%22pageViewId%22%3A%2297fbe78b-abd3-4083-a26f-7f9fe235db58%22%2C%22pageId%22%3A%22SelfAsserted%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1684223873%2C%22acD%22%3A10%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fconsumer.intel.com%2Fsignin_username.html%22%2C%22acST%22%3A1684223873%2C%22acD%22%3A32%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1684223873%2C%22acD%22%3A7%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1684223873%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1684223874%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1684223874%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1684223874%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1684223875%2C%22acD%22%3A181%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1684223876%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1684223875%2C%22acD%22%3A183%7D%5D%7D)

[Launch Jupyterlab on your Intel DevCloud account](https://jupyter.oneapi.devcloud.intel.com/hub/login)

[Connect with Linux/macOS SSH Client](https://devcloud.intel.com/oneapi/documentation/connect-with-ssh-linux-macos)

## Clone this Repo for Hands-on Lab

```
git clone https://github.com/mkhpc/oneAPI-Deep-Dive.git
```
| Notebook Name | Description |
|---|---|
|[oneAPI_and_DPCPP_Intro](oneAPI_and_DPCPP_Intro)| * Introduction and Motivation for oneAPI and DPC++ <br>* DPC++ __Hello World__<br>* Compiling DPC++ and __DevCloud__ Usage<br>* ___Lab Excercise___: Vector Increment to Vector Add |
|[DPCPP_Program_Structure](DPCPP_Program_Structure)| * __Classes__ - device, device_selector, queue, basic kernels and ND-Range kernels, Buffers-Accessor memory model<br>* DPC++ __Code Anotomy__<br>* Implicit __Dependency__ with Accessors, __Synchronization__ with Host Accessor and Buffer Destruction<br>* Creating __Custom__ Device Selector<br>* ___Lab Exercise___: Complex Multiplication |
|[Intel_VTune_Profiler](06_Intel_VTune_Profiler)| * Intel VTune™ Profiler usage __in Intel DevCloud__ environment using command-line options<br>* ___Lab Excercise___: VTune Profiling by collecting __gpu_hotspots__ for __iso3dfd__ hotspots sample application. |
|[DPCT_Intro](DPCT_Intro)| * Introduction  of Intel® DPC++ Compatibility Tool <br>* ___Lab Exercise___: Use the Intel® DPC++ Compatibility Tool to quickly assist in the migration of simple user CUDA* code to DPC++ code |

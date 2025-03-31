# RHINO
**RHINO: A Native Serverless Container System for Efficient Small-Scale HPC Applications**

This repository contains experimental scripts, datasets, and analysis results related to the RHINO system. Each subfolder corresponds to a specific set of experiments or analysis presented in the paper.

---

## Folder Overview

### `/build-test`
Experiments to compare the runtime size of HPC applications built using the **Two-Step Adaptive Build strategy** versus other container build methods.  
**Related Figure:** *Table I* in the paper.

### `/cluster`
Scripts and configurations for submitting and running HPC jobs on **AWS ParallelCluster**.  
Used as a baseline to compare RHINO's performance and cost.

### `/cold-start`
Experiments evaluating the **cold start time** of different HPC applications on **AWS Fargate**.  
Includes the impact analysis of the **Two-Step Adaptive Build strategy** on HPC applications’ cold start latency and turnaround time.  
**Related Figures:** *Fig. 3* and *Fig. 8*.

### `/Mustang`
Data analysis and visualization scripts based on **LANL Mustang traces**, used to profile and characterize small-scale HPC workloads.  
**Related Figure:** *Fig. 1*.

### `/perf-cost`
Experiments evaluating the **performance and cost efficiency** of RHINO.  
Includes analysis of how different VM types affect RHINO's performance and cost.  
**Related Figures:** *Fig. 5*, *Fig. 6*, *Fig. 7*.

### `/scale`
Experiments comparing the **scalability and performance** of **RHINO** and traditional **VM-based clusters** when executing large-scale HPC workloads.  
**Related Figure:** *Fig. 10*.

### `/schedule`
Evaluation of different **scheduling strategies** in RHINO and their impact on overall performance and cost.  
**Related Figure:** *Fig. 9*.

---

## Quick Start (In Progress)

Currently, deploying and running RHINO requires several manual configuration steps, including:
	•	Setting up AWS Fargate services and associated IAM roles
	•	Configuring the networking environment and task definitions
	•	Preparing the container images with the Two-Step Adaptive Build strategy
	•	Manually configuring scheduler parameters and resource mappings

We are actively working on developing automated deployment scripts and configuration templates to simplify this process.
A fully automated one-click deployment guide will be released in future updates.

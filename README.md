# RHINO 🦏
**RHINO: An Efficient Serverless Container System for Small-Scale HPC Applications**


## 📄 Overview

**RHINO** (seRverless HIgh performaNce cOmputing) is a cloud-native serverless system specifically designed for **small-scale HPC applications**. Traditional HPC clusters suffer from long job queuing times, resource over/under-provisioning, and management complexity, particularly for short-running or small-scale workloads. RHINO addresses these challenges by integrating **serverless computing paradigms** with HPC execution models.

RHINO introduces:
- **Two-Step Adaptive Build strategy** to package MPI-based HPC applications into lightweight, scalable serverless containers, significantly reducing cold start latency.
- A **Rhino Function Execution Model (RFEM)** that decouples HPC applications from underlying hardware, enabling dynamic scaling and efficient MPI communication in a serverless environment.
- An **Auto-scaling Engine** with a **heuristic scheduling algorithm** to balance execution performance and cost, solving the Rhino Function Placement (RFP) problem.

Deployed on AWS Fargate, RHINO offers an **elastic, pay-as-you-go alternative to traditional HPC clusters**, achieving up to **30% performance improvement** and over **40% cost reduction** for small-scale HPC applications compared to VM-based clusters.

---

## 📂 Folder Structure

| Folder         | Description                                                                                 | Related Figures/Table |
|--------------|---------------------------------------------------------------------------------------------|----------------------:|
| `/build-test` | Experiments comparing container image build strategies, including the **Two-Step Adaptive Build** strategy. | Table I |
| `/cluster`    | Scripts and configurations for submitting and running HPC jobs on **AWS ParallelCluster** (used as baseline). | — |
| `/cold-start` | Experiments evaluating the **cold start time** and turnaround latency of HPC apps on Fargate. | Fig. 3, Fig. 8 |
| `/Mustang`    | Scripts for analyzing **LANL Mustang traces** to profile small-scale HPC workloads.        | Fig. 1 |
| `/perf-cost`  | Experiments measuring **performance and cost-efficiency** of RHINO across different VM types. | Fig. 5, Fig. 6, Fig. 7 |
| `/scale`      | Scalability and performance comparison of **RHINO** and VM-based clusters on large-scale workloads. | Fig. 10 |
| `/schedule`   | Evaluation of RHINO's **scheduling strategies** and their impact on cost and performance.  | Fig. 9 |

---

## 🚀 Quick Start (In Progress)

At present, deploying and running RHINO requires several **manual configuration steps**, including:
- Setting up **AWS Fargate** services and required **IAM roles**
- Configuring **networking environments**, task definitions, and log streams
- Preparing container images using the **Two-Step Adaptive Build strategy**
- Manually configuring **scheduler parameters** and resource mappings

We are actively developing **automated deployment scripts and configuration templates** to streamline this process.  
A **fully automated, one-click deployment guide** will be released in future updates.
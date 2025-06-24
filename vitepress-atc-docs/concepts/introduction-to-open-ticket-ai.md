---
title: Introduction to Open Ticket AI
description: Understand the problem Open Ticket AI solves and its solution.
---

# Introduction

## Problem Statement

Most organizations receive large volumes of text-based tickets (email, chat, forms) that require manual queue assignment and prioritization—an error-prone and time-consuming process. Without 24/7 staffing, critical tickets can sit unattended, breaching SLAs and risking customer satisfaction.

## Solution Overview

Open Ticket AI uses fine-tuned transformer models to automatically:

- Predict **Queue** (which team or department should handle it)
- Predict **Priority** (how urgently it must be processed)
- Optionally **answer** simple tickets via a built-in chatbot

All processing runs **on-premise**, ensuring no sensitive data leaves your environment.

## Prerequisites

- Linux server (Debian/Ubuntu/CentOS)
- Docker & Docker Compose
- Python 3.8+
- A Hugging Face token (for model downloads and custom models)

## Supported Ticket Systems

Open Ticket AI provides out-of-the-box adapters for:

- **OTOBO** (including Znuny / OTRS-derivatives)
- **Zammad**
- **Other REST-based systems** (Jira, ServiceNow, custom APIs)

Adapters use each system’s REST API to fetch, update and move tickets between queues.

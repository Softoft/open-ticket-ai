---
description: Boost support efficiency with ATC Community Edition, a free, on-premise
  tool for automated ticket classification. Installs easily with Docker and integrates
  seamlessly with OTOBO to improve accuracy and ensure data security.
title: ATC Community Edition Overview
---
# ATC Community Edition Overview

## Introduction

The ATC (Automated Ticket Classification) Community Edition is an advanced solution for automated classification of support tickets. It is free, on-premise, and can be installed on any operating system that supports Docker. This documentation provides a comprehensive overview of ATC’s features and use cases.

## Main Features

### Simple Installation

ATC can be quickly and easily installed on your server using Docker containers. By leveraging Docker, deployment and management of the application are simplified, enabling rapid startup.

### Powerful API

ATC offers a robust HTTP REST API through which users can send data for processing, initiate model training, and retrieve classification results. The API is designed to provide high flexibility and seamless integration into existing systems.

### Data Transfer and Training

Users can send training data or CSV files to ATC via the REST API. Model training can also be triggered through the API, automating the entire workflow of data processing and model optimization.

### Automated Classification

Once trained, ATC can automatically classify incoming support tickets. Classification is based on the patterns learned during training, ensuring consistent and accurate ticket assignment.

### OTOBO Integration

ATC provides a dedicated add-on for the OTOBO ticketing system, enabling seamless integration. This add-on collects data from OTOBO and uses ATC for automated ticket classification, significantly improving efficiency and accuracy in ticket handling.

### High Security

Data security and customer privacy are top priorities. All data processing occurs locally on the server, with no external storage or processing. This ensures full compliance with data protection requirements.

### Flexibility and Customizability

ATC offers high flexibility through customizable configurations. Users can tailor the settings to their specific needs to achieve optimal results.

## Installation and Usage

### Docker Installation

ATC can be easily installed on your server using Docker. Follow these steps to install:

1. **Install Docker**:

   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

2. **Run the ATC Container**:

   ```bash
   docker run -d -p 8080:80
   ```

### API Usage

After installation, you have HTTP REST access to the ATC API. You can send data to the API to start training and retrieve classification results.

#### Sending Training Data

Send your training data or a CSV file to the ATC REST API:

```bash
curl -X POST http://your-server:8080/api/train \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

#### Starting Training

Trigger model training:

```bash
curl -X POST http://your-server:8080/api/start-training
```

#### Classifying Tickets

After training, send tickets to the API for classification and receive the corresponding labels:

```bash
curl -X POST http://your-server:8080/api/classify \
     -H "Content-Type: application/json" \
     -d '{"ticket_data": "Your ticket content"}'
```

## Future Extensions

We plan to provide additional integration add-ons for various systems in the future. Stay tuned for the latest updates.

## Summary

The ATC Community Edition is a powerful, free solution for automated support ticket classification. With a user-friendly API, simple Docker installation, and seamless OTOBO integration, ATC offers a flexible and scalable way to optimize your support processes and boost your team’s efficiency.

For more information, visit our website: [SoftOft](https://softoft.de/otobo/docs)

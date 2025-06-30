---
description: Discover how to easily install ATC using Docker and utilize its REST
  API for automated support ticket classification. This guide provides step-by-step
  instructions on sending training data, initiating model training, and classifying
  new tickets to streamline your support workflow.
title: Installation and Usage of ATC
---
-----------------------------------------------------------------------------------------------------

# Installation of ATC

ATC can be easily installed on your server using Docker. Follow the steps below to perform the installation:

## Step 1: Install Docker

First, you need to install Docker on your server. Run the following commands to install Docker:

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Step 2: Run the ATC Container

After Docker is installed, you can run the ATC container. Use the following command to start the container:

```bash
docker run -d -p 8080:80 your-docker-repo/atc:latest
```

This command pulls the latest ATC Docker image from your repository and starts it on port 8080.

# Using the ATC API

After installation, you have HTTP REST access to the ATC API. Here are some basic commands to use the API:

## Sending Training Data

To send training data or a CSV file to the ATC REST API, use the following command:

```bash
curl -X POST http://your-server:8080/api/train \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

This command sends the file `yourfile.csv` to the API for use in training.

## Starting Training

To start the model training, use this command:

```bash
curl -X POST http://your-server:8080/api/start-training
```

This command initiates the training process based on the previously sent data.

## Classifying Tickets

After successful training, you can send ticket data to the API for classification and receive the corresponding labels:

```bash
curl -X POST http://your-server:8080/api/classify \
     -H "Content-Type: application/json" \
     -d '{"ticket_data": "Your ticket content"}'
```

This command sends the ticket content for classification and returns the classification labels.

# Summary

With these steps, you can install ATC on your server and use the basic API functions. ATC offers a powerful, flexible solution for automated support ticket classification that is easy to install and use.

This section describes the installation of ATC and the basic API commands in detail. You can adapt and extend it to include additional information or specific instructions.

# Azure Telephony AI Voice Agent

AI Voice agent built with Azure Communication Services and GPT-4o-realtime.


## Prerequisites
- Azure Communication Services (with phone number deployed)
- Azure OpenAI with gpt-4o-realtime model

## Local development

1. Clone the repository
1. Start the DevContainer

### Login to Azure CLI

This project leverages identity-based authentication, for example with Azure CLI. To login, run the following command:

```bash
az login
```

### Create DevTunnel (one-time only)

The DevTunnel CLI is a tool that allows you to create a secure tunnel to your local development environment. This allows you to expose your local development environment to Azure Communication Services without having to deploy your code to a public server.

```bash
devtunnel login # or devtunnel login -g
devtunnel create -a
devtunnel port create -p 5000
devtunnel host
```

Set your HOSTNAME in the `.env` file to the hostname provided by DevTunnel.

### Start DevTunnel

```bash
devtunnel host
```

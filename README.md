# Azure Telephony AI Voice Agent

AI Voice agent built with Azure Communication Services and GPT-4o-realtime.


## Prerequisites
- Azure Communication Services [(with a phone number deployed)](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/telephony/get-phone-number?tabs=linux&pivots=platform-azp)
- Azure OpenAI with gpt-4o-realtime model

## Local development

1. Clone the repository
1. Start the DevContainer

### Configure environment variables

Copy the `.env.example` file, rename it to `.env` and fill in the values.

### Login to Azure CLI

This project leverages identity-based authentication, for example with Azure CLI. To login, run the following command:

```bash
az login
```

### Create DevTunnel (first time only)

The DevTunnel CLI is a tool that allows you to create a secure tunnel to your local development environment. This allows you to expose your local development environment to Azure Communication Services without having to deploy your code to a public server.

```bash
devtunnel login # or devtunnel login -g
devtunnel create -a
devtunnel port create -p 5000
```

Set your HOSTNAME in the `.env` file to the hostname provided by DevTunnel.

### Start existing DevTunnel

```bash
devtunnel host
```

### Start the application

```bash
uv run app.py
```

(or run the application from the VS Code debugger)

### Configure Azure Communication Services resource

1. [Subscribe to voice and video calling events using web hooks](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/voice-video-calling/handle-calling-events)
    * Set the subscriber endpoint to `https://{{your_hostname}}/api/incomingCall`

### Test the application

* Make a call to your phone number.

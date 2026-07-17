---
title: Add document RAG, browser search, and proactive cron workflows
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a synthetic household document

Create a small text file on your computer with the following public tutorial content:

```text
Household heating maintenance notes

Inspect the boiler every October.
Clean the heating filter on the first Saturday of every third month.
Keep the service reference number with the maintenance record.
```

Save the file as `household-maintenance.txt` and upload it to the Telegram bot with this caption:

```text
/knowledge
```

OpenClaw saves the file to the local workspace, indexes it with the memory watcher, and writes its chunks to `personal_knowledge_base`.

{{% notice Note %}}
In v1.2, supported Telegram uploads are indexed after they are saved. The review-first upload workflow is planned but is not part of this release.
{{% /notice %}}

After the bot reports the document identifier, ask a document-scoped question. Replace `<document-id>` with the returned identifier:

```text
/rag doc:<document-id> When should the heating filter be cleaned?
```

The answer should mention the first Saturday of every third month.

Confirm the knowledge collection from the host:

```bash
curl http://127.0.0.1:6333/collections/personal_knowledge_base
```

## Search the web with the local browser worker

Send an explicit search command:

```text
/search Find current public guidance for reducing household heating energy use.
```

The request path is:

```text
Telegram
  -> browser_search_agent
  -> local Playwright worker
  -> public search pages
  -> local LLM summary
  -> Telegram
```

The browser runs locally, but the query and page requests leave the host. The resulting page content is summarized by the local model rather than a public cloud LLM API.

## Create a proactive reminder

Choose a time a few minutes in the future using the runtime timezone configured by `OPENCLAW_CRON_TIMEZONE`. Create a daily tutorial reminder:

```text
/cron add daily 19:30 Heating check :: Remind the household to review the heating maintenance notes.
```

Replace `19:30` with your test time. List the job:

```text
/cron list
```

The job runs only inside the configured due-time window. Creating the job must not execute it immediately.

To test without waiting, copy the job ID from `/cron list` and run:

```text
/cron run <job-id>
```

The result should be delivered as a Telegram push message.

## Inspect cron from the Gateway dashboard

The Gateway dashboard listens on localhost. If you are working directly on the DGX Spark desktop, open:

```text
http://127.0.0.1:18789/
```

If DGX Spark is remote, create an SSH tunnel from your laptop:

```bash
ssh -L 18789:127.0.0.1:18789 <user>@<dgx-spark-host>
```

Then open `http://127.0.0.1:18789/` locally and enter the `OPENCLAW_GATEWAY_TOKEN` stored in the private `.env` file.

Confirm that the dashboard and Telegram show the same cron job and run history.

{{% notice Warning %}}
Keep the Gateway and its admin RPC endpoint behind localhost, an SSH tunnel, or a trusted private network. Do not expose the dashboard directly to the public internet.
{{% /notice %}}

## Review the complete household workflow

You have now exercised four different runtime paths:

| User goal | OpenClaw path |
|---|---|
| Remember a household fact | Telegram -> memory skill -> Ollama -> Qdrant |
| Answer from a household document | Telegram -> RAG skill -> Qdrant -> local LLM |
| Find current public information | Telegram -> Playwright -> local LLM |
| Send a proactive reminder | Cron -> OpenClaw skill -> Telegram push |

This is what distinguishes the runtime from a local chatbot. The LLM is replaceable, while the surrounding memory, tools, schedules, and interaction paths remain part of the application.

## What you've learned and what's next

You have created a document-backed, web-enabled, proactive household assistant on DGX Spark and verified its local and external data paths.

Next, you will move the same OpenClaw workflows to a CPU-only Armv9 system.

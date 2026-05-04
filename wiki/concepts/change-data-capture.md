---
type: concept
title: "Change Data Capture"
aliases: ["CDC"]
tags: [data-engineering]
sources: [sources/data-engineering-projects]
last_updated: 2026-04-14
---

# Change Data Capture

## Definition

Change Data Capture (CDC) is a pattern for identifying and tracking incremental changes in source data (inserts, updates, deletes) rather than reprocessing entire datasets. It enables efficient, near-real-time data synchronization between systems.

## How It Works

- Monitor source system for changes (database logs, timestamps, triggers)
- Capture only the changed records
- Apply changes to the target system incrementally
- Avoids full table scans — processes only deltas

## Why It Matters

- Dramatically more efficient than full [[concepts/etl]] reloads for large datasets
- Enables near-real-time data freshness
- Essential for event-driven architectures and [[concepts/streaming-processing]]

## Related Concepts

- [[concepts/etl]] -- CDC is an incremental alternative to full ETL
- [[concepts/streaming-processing]] -- CDC often feeds streaming pipelines
- [[concepts/data-quality]] -- validating incremental changes

## Source References

- [[sources/data-engineering-projects]] -- "Build a CDC Tracker" project

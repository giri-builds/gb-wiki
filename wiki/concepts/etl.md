---
type: concept
title: "ETL"
aliases: ["extract transform load", "ELT"]
tags: [data-engineering]
sources: [sources/data-engineering-projects]
last_updated: 2026-04-14
---

# ETL

## Definition

ETL (Extract, Transform, Load) is the foundational data engineering pattern for moving data from source systems to a target data store. Data is extracted from sources, transformed (cleaned, enriched, restructured), and loaded into a destination like a data warehouse or data lake.

## How It Works

1. **Extract**: read data from source systems (APIs, databases, files)
2. **Transform**: clean, validate, deduplicate, reshape, aggregate
3. **Load**: write to target system (warehouse, lake, database)

Modern variant **ELT** loads raw data first and transforms in-place using the target system's compute (common with cloud warehouses like [[entities/snowflake]]).

## Why It Matters

- Foundation of all data engineering work
- Every data pipeline is some form of ETL/ELT
- Understanding ETL is prerequisite for more advanced patterns like [[concepts/change-data-capture]] and [[concepts/streaming-processing]]

## Related Concepts

- [[concepts/data-orchestration]] -- scheduling and managing ETL pipelines
- [[concepts/change-data-capture]] -- incremental alternative to full ETL
- [[concepts/data-quality]] -- validation during the transform step
- [[concepts/dimensional-modeling]] -- common target schema for ETL output

## Source References

- [[sources/data-engineering-projects]] -- "Build a Simple ETL Script" project

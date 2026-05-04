---
type: source
title: "Data Engineering Learning Projects"
source_file: "Data Engineering.md"
source_type: md
date_ingested: 2026-04-14
tags: [data-engineering, project-ideas]
---

# Data Engineering Learning Projects

## Summary

A curated list of 20 hands-on projects for aspiring data engineers, organized by progressive complexity. Each project targets a specific data engineering concept — from basic file format conversion to building mini versions of production tools like dbt and orchestrators. The emphasis is on learning by building rather than passive study.

## Key Points

- **Fundamentals**: CSV to Parquet converter (columnar storage), log parser pipeline (data cleaning), simple ETL script
- **Data Quality & Modeling**: data quality checker (validation, null handling, schema enforcement), CDC tracker (change data capture), star schema from raw JSON (dimensional modeling)
- **Orchestration & Streaming**: simple orchestrator (task dependencies, DAG logic), streaming word counter (producers, consumers, real-time), database migration tool (schema versioning, rollbacks)
- **Integration & SCD**: REST API to SQL bridge (API to warehouse), SCD handler (Type 1 and Type 2 logic), data lake file organizer (partitioning strategies)
- **Advanced Tooling**: simple scheduler (cron, retries), metadata catalog (lineage, discoverability), mini dbt clone (SQL transformations, dependency graphs)
- **Production Patterns**: dead letter queue (failed record handling), backfill script (historical reprocessing without duplicates), data diff tool (row-by-row comparison), config-driven pipeline (YAML/JSON configs)
- **Serving**: mini dashboard backend (aggregated data serving to frontend)

## Entities Mentioned

- [[entities/dbt]] -- SQL transformation tool (referenced as "mini dbt clone" project)
- [[entities/parquet]] -- columnar file format

## Concepts Covered

- [[concepts/etl]] -- extract, transform, load pipelines
- [[concepts/change-data-capture]] -- tracking data changes incrementally
- [[concepts/dimensional-modeling]] -- star schema, fact/dimension tables
- [[concepts/slowly-changing-dimensions]] -- SCD Type 1 and Type 2 logic
- [[concepts/data-orchestration]] -- task dependencies, DAG-based scheduling
- [[concepts/streaming-processing]] -- real-time producers and consumers
- [[concepts/data-lake]] -- partitioning and folder structure strategies
- [[concepts/data-quality]] -- validation, schema enforcement, null handling
- [[concepts/data-lineage]] -- metadata catalog, discoverability

## Notable Quotes or Data

- 20 projects total, progressing from basic (CSV conversion) to advanced (mini dbt clone)
- Learning philosophy: "the best way to learn is by doing"

## Related Sources

- [[sources/ai-engineer-requirements]] -- notes convergence of data engineering and AI engineering

---
type: concept
title: "Dimensional Modeling"
aliases: ["star schema", "fact and dimension tables"]
tags: [dimensional-modeling, data-engineering]
sources: [sources/data-engineering-projects]
last_updated: 2026-04-14
---

# Dimensional Modeling

## Definition

Dimensional modeling is a data warehouse design technique that organizes data into fact tables (measurements/events) and dimension tables (descriptive context). The star schema is the most common implementation, with a central fact table connected to surrounding dimension tables.

## How It Works

- **Fact tables**: contain quantitative measurements (sales amount, click count) and foreign keys to dimensions
- **Dimension tables**: contain descriptive attributes (customer name, product category, date)
- **Star schema**: fact table at center, dimension tables radiating outward
- [[concepts/slowly-changing-dimensions]] handle attributes that change over time

## Why It Matters

- Standard approach for data warehouse design
- Enables efficient analytical queries (aggregations, slicing, dicing)
- Foundation for BI reporting and dashboards

## Related Concepts

- [[concepts/slowly-changing-dimensions]] -- handling changing dimension attributes
- [[concepts/etl]] -- process that populates dimensional models
- [[concepts/data-quality]] -- schema enforcement for dimension/fact tables

## Source References

- [[sources/data-engineering-projects]] -- "Build a Star Schema from Raw JSON" project

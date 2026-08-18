# Northstar Retail - Automatic Retry & Exponential Backoff

## Project Overview

This project implements an automatic retry mechanism for temporary
warehouse network failures.

The system retries a failed operation up to 3 times using exponential
backoff.

## Retry Pattern

The delay increases after each failed attempt:

- First retry: 1 second
- Second retry: 2 seconds
- Third attempt: final attempt

The pattern is:

1s → 2s → 4s → ...

## Why It Matters

Northstar Retail receives inventory updates from warehouse systems.
Temporary network failures should not cause inventory updates to be
lost immediately.

The retry mechanism gives the network request another opportunity to
succeed before reporting a permanent failure.

## Files

```text
northstar-retry-backoff/
│
├── retry.py
├── test_retry.py
└── README.md

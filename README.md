# Panther-Analysis-Enrichment
Enrichment and Lookup Tables Automation with Gitub Actions

The github action worflows run on configurable schedules. 

## Okta Enrichment Action
Description: To Add

.github/workflows/okta_users.yml


Configuration: Set `OKTA_DOMAIN` and `OKTA_API_TOKEN` as Github Secrets. 
See Upload to Panther with PAT for required Panther secrets

## AWS IP Ranges Action
Description: To Add

.github/workflows/aws_ip_ranges.yml

See Upload to Panther with PAT for required Panther secrets

## GCP IP Ranges Action
Description: To Add

.github/workflows/gcp_ip_ranges.yml

See Upload to Panther with PAT for required Panther secrets


## Upload to Panther with PAT
Description: To Add

Configuration: Set `PANTHER_HOST` and `PANTHER_API_TOKEN` as Github Secrets.
Ex:  
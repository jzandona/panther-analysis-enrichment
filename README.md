# Panther-Analysis-Enrichment
Enrichment and Lookup Tables Automation with Gitub Actions

The github action worflows run on configurable schedules. 

1. Runs on a cron schedule
2. Checks to make sure needed variables/secrets are set before continuing
3. Checkouts out repo
4. cURLS the endpoint
5. Does any cleanup of the json response to get it into a format we can use as a LUT
6. Downloads PAT
7. Uploads lookup table using `pat upload`

Note: Custom schemas need to be configured in Panther before the pat upload will succeed. 

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
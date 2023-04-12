# Panther-Analysis-Enrichment
Enrichment and Lookup Tables Automation with Gitub Actions

The github action worflows run on configurable schedules. 

1. Runs on a cron schedule
2. Checks to make sure needed variables/secrets are set before continuing
3. Checkouts out repo
4. cURLs the endpoint
5. Does any cleanup of the json response to get it into a format we can use as a LUT
6. Downloads PAT
7. Uploads lookup table using `pat upload`

Note: Custom schemas need to be configured in Panther before the pat upload will succeed. 

## Okta Enrichment Action
This action retrieves the user list from Okta's /api/v1/users endpoint. 

Set `OKTA_DOMAIN` and `OKTA_API_TOKEN` as Github secrets. 
See Upload to Panther with PAT for required Panther secrets. 

Workflow can be found at .github/workflows/okta_users.yml

## AWS IP Ranges Action
The AWS IP ranges action retrieves the IP ranges published by AWS from https://ip-ranges.amazonaws.com/ip-ranges.json. 
Using `jq` it combines IPv4 and IPv6 records to a `ipPrefix` key. In a small amount of cases, a range may have multiple records, combining them on `ipPrefix` with `service` as an array.

> See Upload to Panther with PAT for required Panther secrets.


Example Output:

``{"ipPrefix":"99.87.8.0/21","region":"ap-south-2","network_border_group":"ap-south-2","service":["AMAZON"]}``

.github/workflows/aws_ip_ranges.yml


## GCP IP Ranges Action
The GCP IP ranges action retrieves the IP ranges published by Google from https://www.gstatic.com/ipranges/cloud.json. 
Using `jq` it combines IPv4 and IPv6 records to a `ipPrefix` key.

> See Upload to Panther with PAT for required Panther secrets.


Example Output:

``{"ipPrefix":"35.219.128.0/18","service":"Google Cloud","scope":"us-west4"}``

.github/workflows/gcp_ip_ranges.yml


## Upload to Panther with PAT
To be able to upload to Panther, set `PANTHER_HOST` and `PANTHER_API_TOKEN` as Github Secrets. Refer to the Panther [docs](https://docs.panther.com/panther-developer-workflows/ci-cd/deployment-workflows/pat#creating-an-api-token) for more information on creating an API token.

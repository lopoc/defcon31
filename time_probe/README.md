
<img src="timeprobe.png" alt="Image Description" width="300">

# TIMEPROBE

## AWS Lambda Latency Measurement Function

This AWS Lambda function is designed to measure the latency between the data center where the Lambda function is executed and a target URL. The latency is determined using the Time To First Byte (TTFB) metric, providing insights into the network performance.

## Configuration

Configuration**: Modify the `aws_data.py` file to include the AWS region data relevant to your use case. This data is used to map AWS regions to countries and coordinates.

## Deploy Lambda Function

Use the AWS CLI or the graphical interface to deploy the Lambda function to your AWS account.
deploy it on different zones and manage them from a single point (eg. using an api gateway)

## Results
The function will return a JSON response containing information about the AWS region, country, coordinates, and the calculated TTFB latency.

```json
{
  "aws_region": "eu-west-3",
  "country": "FR",
  "coordinates": [
    48.864716,
    2.349014
  ],
  "TTFB": 0.096719
```
---

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess

import aws_data


def timeprobe(target_url, ntimes=1):
    data = []
    for i in range(ntimes):
        res = subprocess.run([
            'curl',
            '-s',
            '-I',
            '-o',
            '/dev/null',
            '-w',
            '%{time_pretransfer},%{time_starttransfer}',
            target_url,
            ], capture_output=True, shell=False)
        (time_pretransfer, time_starttransfer) = \
            eval(res.stdout.decode())
        data.append(time_starttransfer - time_pretransfer)
    return min(data)


def lambda_handler(event, context):
    aws_region = os.getenv('AWS_REGION')
    try:
        ttfb = timeprobe(event['target_url'])
        return {
            'aws_region': aws_region,
            'country': aws_data.aws_regions[aws_region].get('country'),
            'coordinates': aws_data.aws_regions[aws_region].get('coords'
                    ),
            'TTFB': ttfb,
            }
    except:
        return {
            'aws_region': aws_region,
            'country': aws_data.aws_regions[aws_region].get('country'),
            'coordinates': aws_data.aws_regions[aws_region].get('coords'
                    ),
            'TTFB': None,
            }

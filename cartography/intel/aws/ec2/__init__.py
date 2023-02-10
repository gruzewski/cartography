import logging
from typing import List

import boto3

from cartography.util import timeit

logger = logging.getLogger(__name__)


@timeit
def get_ec2_regions(boto3_session: boto3.session.Session, aws_endpoint: str) -> List[str]:
    client = boto3_session.client('ec2', endpoint_url=aws_endpoint)
    result = client.describe_regions()
    return [r['RegionName'] for r in result['Regions']]

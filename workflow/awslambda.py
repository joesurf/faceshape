import json
from main import pipeline
import asyncio
from readCsv import getResult


async def lambda_handler(event, context):
    # TODO implement

    await pipeline()
    # time.sleep()

    prediction = ""

    # Read lastest casting predictions csv file
    result = getResult()
    if result:
        prediction = result[2]

    print(prediction)

    return {
        'statusCode': 200,
        'body': json.dumps(prediction)
    }


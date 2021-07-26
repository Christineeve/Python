import boto3
#rds = boto3.client('rds')
rds = boto3.client('rds', region_name='us-west-2')
my_session = boto3.session.Session()
my_region = my_session.region_name
print(my_session)
print(my_region)
# rds = boto3.setup_default_session(region_name='us-west-2')
# rds = boto3.client('rds')
# # print(rds) 
# # print(my_region)


# # Get the service resource.
# dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='devTestDDB',
#       AttributeDefinitions=[
#         {
#             'AttributeName': 'guid',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'ingestdate',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'emailid',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'subject',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'content',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'createdate',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'creator',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'id',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'recipient',
#             'AttributeType': 'S'
#         },
#     ],
#     KeySchema=[
#         {
#             'AttributeName': 'guid',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'ingestdate',
#             'KeyType': 'RANGE'
#         }
#     ],
#     # GlobalSecondaryIndexes=[
#     #     {
#     #         'IndexName': 'guid',
#     #         'KeySchema': [
#     #             {
#     #                 'AttributeName': 'guid',
#     #                 'KeyType': 'HASH'
#     #             },
#     #         ],
#     #         'Projection': {
#     #             'ProjectionType': 'ALL'
#     #         },
#     #         'ProvisionedThroughput' :{
#     #             'ReadCapacityUnits': 1,
#     #             'WriteCapacityUnits': 1,
#     #         }
#     #     }
#     # ],

#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# Wait until the table exists.
# table.meta.client.get_waiter('table_exists').wait(TableName='devTestDDB')

# # Print out some data about the table.
# print(table.item_count)

#import boto3
#from boto3.dynamodb.conditions import Key
#dynamodb = boto3.resource('dynamodb')
#table = dynamodb.Table('bulkemail')

#table.update_item(
#    Key={
#        'emailid': 2,
#        'ingestdate': 20210219
#    },
#    UpdateExpression='SET bulkdata = :val1',
#    ExpressionAttributeValues={
#        ':val1': "Null"
#    }
#)
#response = table.get_item(
#S    Key={
#        'emailid': 2,
#        'ingestdate': 20210219
#    }
#)
#item = response['Item']
#print(item)

'''
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('bulkemail')

response = table.query(
    KeyConditionExpression=Key('emailid').eq(8)
)

for i in response['Items']:
    print(i['emailid'], ":", i['bulkdata'])

'''

#import boto3
# Get the service resource.
#dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
#table = dynamodb.Table('bulkemail')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
#print(table.creation_date_time) 

# import boto3
# from boto3.dynamodb.conditions import Key
# dynamodb = boto3.resource('dynamodb')


# #Get the service resource.
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('testDevDDB')
# #database = 'devTestDDB'
# guid = '8'
# ingestdate = '2021072601'
# subject  = 'testing a new test table for artifacts'
# content  = '[{"Component 1": "Y component: Quantization table 0, Sampling factors 2 horiz/2 vert", "Component 2": "Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Component 3": "Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Compression Type": "Baseline", "Content-Type": "image/jpeg", "Data Precision": "8 bits", "File Modified Date": "Fri Jan 22 10:49:27 -05:00 2021", "File Name": "apache-tika-2326026356302560937.tmp", "File Size": "104692 bytes", "Image Height": "720 pixels", "Image Width": "1280 pixels", "Number of Components": "3", "Number of Tables": "4 Huffman tables", "Resolution Units": "none", "Thumbnail Height Pixels": "0", "Thumbnail Width Pixels": "0", "X Resolution": "1 dot", "X-Parsed-By": "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.jpeg.JpegParser", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "4", "Y Resolution": "1 dot", "resourceName": "b'"samplejpg.jpg'"', "tiff:BitsPerSample": "8", "tiff:ImageLength": "720", "tiff:ImageWidth": "1280", "content": "No Text Content"}, {"Author": "dst1", "Content-Type": "application/pdf", "Creation-Date": "2021-01-17T18:57:21Z", "Last-Modified": "2021-01-17T18:57:21Z", "Last-Save-Date": "2021-01-17T18:57:21Z", "X-Parsed-By":"org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.pdf.PDFParser", "X-TIKA:content_handler": "ToTextContentHandler", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "10", "access_permission:assemble_document": "true", "access_permission:can_modify": "true", "access_permission:can_print": "true", "access_permission:can_print_degraded": "true", "access_permission:extract_content": "true", "access_permission:extract_for_accessibility": "true", "access_permission:fill_in_form": "true", "access_permission:modify_annotations": "true", "created": "2021-01-17T18:57:21Z", "creator": "dst1", "date": "2021-01-17T18:57:21Z", "dc:creator": "dst1", "dc:format": "application/pdf; version=1.7", "dc:title": "Microsoft Word - Document1", "dcterms:created": "2021-01-17T18:57:21Z", "dcterms:modified": "2021-01-17T18:57:21Z", "meta:author": "dst1", "meta:creation-date": "2021-01-17T18:57:21Z", "meta:save-date": "2021-01-17T18:57:21Z", "modified": "2021-01-17T18:57:21Z", "pdf:PDFVersion": "1.7", "pdf:charsPerPage": "27", "pdf:docinfo:created": "2021-01-17T18:57:21Z", "pdf:docinfo:creator": "dst1", "pdf:docinfo:modified": "2021-01-17T18:57:21Z", "pdf:docinfo:producer": "Microsoft: Print To PDF", "pdf:docinfo:title": "Microsoft Word - Document1", "pdf:encrypted": "false", "pdf:hasMarkedContent": "false", "pdf:hasXFA": "false", "pdf:hasXMP": "false", "pdf:unmappedUnicodeCharsPerPage": "0", "producer": "Microsoft: Print To PDF", "resourceName": "b''samplepdf.pdf'", "'"title": "Microsoft Word - Document1", "xmpTPg:NPages": "1""}{"Component 1": "Y component: Quantization table 0, Sampling factors 2 horiz/2 vert", "Component 2": "Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Component 3": "Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Compression Type": "Baseline", "Content-Type": "image/jpeg", "Data Precision": "8 bits", "File Modified Date": "Fri Jan 22 10:49:27 -05:00 2021", "File Name": "apache-tika-2326026356302560937.tmp", "File Size": "104692 bytes", "Image Height": "720 pixels", "Image Width": "1280 pixels", "Number of Components": "3", "Number of Tables": "4 Huffman tables", "Resolution Units": "none", "Thumbnail Height Pixels": "0", "Thumbnail Width Pixels": "0", "X Resolution": "1 dot", "X-Parsed-By": "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.jpeg.JpegParser", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "4", "Y Resolution": "1 dot", "resourceName": "b'"samplejpg.jpg'"', "tiff:BitsPerSample": "8", "tiff:ImageLength": "720", "tiff:ImageWidth": "1280", "content": "No Text Content"}, {"Author": "dst1", "Content-Type": "application/pdf", "Creation-Date": "2021-01-17T18:57:21Z", "Last-Modified": "2021-01-17T18:57:21Z", "Last-Save-Date": "2021-01-17T18:57:21Z", "X-Parsed-By":"org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.pdf.PDFParser", "X-TIKA:content_handler": "ToTextContentHandler", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "10", "access_permission:assemble_document": "true", "access_permission:can_modify": "true", "access_permission:can_print": "true", "access_permission:can_print_degraded": "true", "access_permission:extract_content": "true", "access_permission:extract_for_accessibility": "true", "access_permission:fill_in_form": "true", "access_permission:modify_annotations": "true", "created": "2021-01-17T18:57:21Z", "creator": "dst1", "date": "2021-01-17T18:57:21Z", "dc:creator": "dst1", "dc:format": "application/pdf; version=1.7", "dc:title": "Microsoft Word - Document1", "dcterms:created": "2021-01-17T18:57:21Z", "dcterms:modified": "2021-01-17T18:57:21Z", "meta:author": "dst1", "meta:creation-date": "2021-01-17T18:57:21Z", "meta:save-date": "2021-01-17T18:57:21Z", "modified": "2021-01-17T18:57:21Z", "pdf:PDFVersion": "1.7", "pdf:charsPerPage": "27", "pdf:docinfo:created": "2021-01-17T18:57:21Z", "pdf:docinfo:creator": "dst1", "pdf:docinfo:modified": "2021-01-17T18:57:21Z", "pdf:docinfo:producer": "Microsoft: Print To PDF", "pdf:docinfo:title": "Microsoft Word - Document1", "pdf:encrypted": "false", "pdf:hasMarkedContent": "false", "pdf:hasXFA": "false", "pdf:hasXMP": "false", "pdf:unmappedUnicodeCharsPerPage": "0", "producer": "Microsoft: Print To PDF", "resourceName": "b''samplepdf.pdf'", "'"title": "Microsoft Word - Document1", "xmpTPg:NPages": "1"}]"'
# createdate = '07262021'
# creator ='christine lee'
# id = '01'
# recipient = 'whitney mallicoat'

# table.put_item(
#     Item={
#          'guid': guid,
#          'ingestdate': ingestdate,
#          'subject': subject,
#          'content': content,
#          'createdate': createdate,
#          'creator': creator,
#          'id': id,
#          'recipient': recipient,
#      }
#  )

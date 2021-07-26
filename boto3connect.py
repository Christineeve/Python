import boto3
#Get the service resource.
dynamodb = boto3.resource('dynamodb')

# # Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='bulkemail',
    KeySchema=[
        {
            'AttributeName': 'emailid',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'ingestdate',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'emailid',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'ingestdate',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'bulkdata',
            'AttributeType': 'S'
        },
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'bulkdata',
            'KeySchema': [
                {
                    'AttributeName': 'bulkdata',
                    'KeyType': 'HASH'
                },
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput' :{
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1,
            }
        }
    ],

    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='bulkemail')

# # Print out some data about the table.
# print(table.item_count)
 
#import boto3

# def delete_movie_table(dynamodb=None):
#     if not dynamodb:
#         dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

#     table = dynamodb.Table('bst_bulkemail')
#     table.delete()


# if __name__ == '__main__':
#     delete_movie_table()
#     print("Movies table deleted.")
# print(delete_a_table_from_database("bulkemail","bulkdata"))




# import boto3

# dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
# table = dynamodb.Table('bulkemail')

# with table.batch_writer() as batch:
#      # Iterate through table until it's fully scanned
#     while scan is None or 'LastEvaluatedKey' in scan:
#         if scan is not None and 'LastEvaluatedKey' in scan:
#             scan = table.scan(
#                 ProjectionExpression='emailid', # Replace with your actual Primary Key
#                 ExclusiveStartKey=scan['LastEvaluatedKey'],
#             )
#         else:
#             scan = table.scan(ProjectionExpression='emailid')

#         for item in scan['Items']:
#             batch.delete_item(Key={'emailid': item['emailid']})


# from boto3.dynamodb.conditions import Attr
# import boto3

# attr = Attr('emailid').attribute_type('S')
#     response = table.scan(FilterExpression = attr)
#     items = response['Items']

#     while 'LastEvaluatedKey' in response:
#         response = table.scan(FilterExpression = attr, ExclusiveStartKey = response['LastEvaluatedKey'])
#         items.extend(response['Items'])




#   rds = boto3.client('rds', region_name='us-west-2')
#   my_session = boto3.session.Session()
#  my_region = my_session.region_name
# # print(my_session)
# # print(my_region)
#  rds = boto3.setup_default_session(region_name='us-west-2')
#  rds = boto3.client('rds')
# #print(rds) 
# # #print(my_region)


# # # Get the service resource.
#  dynamodb = boto3.resource('dynamodb')

#  # # Create the DynamoDB table.
#  table = dynamodb.create_table(
#      TableName='bulkemail',
#      KeySchema=[
#         {
#             'AttributeName': 'emailid',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'ingestdate',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'emailid',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'ingestdate',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'bulkdata',
#             'AttributeType': 'S'
#         },
#     ],
#     GlobalSecondaryIndexes=[
#         {
#             'IndexName': 'bulkdata',
#             'KeySchema': [
#                 {
#                     'AttributeName': 'bulkdata',
#                     'KeyType': 'HASH'
#                 },
#             ],
#             'Projection': {
#                 'ProjectionType': 'ALL'
#             },
#             'ProvisionedThroughput' :{
#                 'ReadCapacityUnits': 5,
#                 'WriteCapacityUnits': 5,
#             }
#         }
#     ],

#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# # # Wait until the table exists.
# table.meta.client.get_waiter('table_exists').wait(TableName='bulkemail')

# # # Print out some data about the table.
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
# table = dynamodb.Table('bulkemail')

# #Get the service resource.
# database = 'bulkemail'
# emailid = 8
# ingestdate = 2021223
# dynamodb = boto3.resource('dynamodb')
# bulkdata  = '[{"Component 1": "Y component: Quantization table 0, Sampling factors 2 horiz/2 vert", "Component 2": "Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Component 3": "Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Compression Type": "Baseline", "Content-Type": "image/jpeg", "Data Precision": "8 bits", "File Modified Date": "Fri Jan 22 10:49:27 -05:00 2021", "File Name": "apache-tika-2326026356302560937.tmp", "File Size": "104692 bytes", "Image Height": "720 pixels", "Image Width": "1280 pixels", "Number of Components": "3", "Number of Tables": "4 Huffman tables", "Resolution Units": "none", "Thumbnail Height Pixels": "0", "Thumbnail Width Pixels": "0", "X Resolution": "1 dot", "X-Parsed-By": "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.jpeg.JpegParser", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "4", "Y Resolution": "1 dot", "resourceName": "b'"samplejpg.jpg'"', "tiff:BitsPerSample": "8", "tiff:ImageLength": "720", "tiff:ImageWidth": "1280", "content": "No Text Content"}, {"Author": "dst1", "Content-Type": "application/pdf", "Creation-Date": "2021-01-17T18:57:21Z", "Last-Modified": "2021-01-17T18:57:21Z", "Last-Save-Date": "2021-01-17T18:57:21Z", "X-Parsed-By":"org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.pdf.PDFParser", "X-TIKA:content_handler": "ToTextContentHandler", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "10", "access_permission:assemble_document": "true", "access_permission:can_modify": "true", "access_permission:can_print": "true", "access_permission:can_print_degraded": "true", "access_permission:extract_content": "true", "access_permission:extract_for_accessibility": "true", "access_permission:fill_in_form": "true", "access_permission:modify_annotations": "true", "created": "2021-01-17T18:57:21Z", "creator": "dst1", "date": "2021-01-17T18:57:21Z", "dc:creator": "dst1", "dc:format": "application/pdf; version=1.7", "dc:title": "Microsoft Word - Document1", "dcterms:created": "2021-01-17T18:57:21Z", "dcterms:modified": "2021-01-17T18:57:21Z", "meta:author": "dst1", "meta:creation-date": "2021-01-17T18:57:21Z", "meta:save-date": "2021-01-17T18:57:21Z", "modified": "2021-01-17T18:57:21Z", "pdf:PDFVersion": "1.7", "pdf:charsPerPage": "27", "pdf:docinfo:created": "2021-01-17T18:57:21Z", "pdf:docinfo:creator": "dst1", "pdf:docinfo:modified": "2021-01-17T18:57:21Z", "pdf:docinfo:producer": "Microsoft: Print To PDF", "pdf:docinfo:title": "Microsoft Word - Document1", "pdf:encrypted": "false", "pdf:hasMarkedContent": "false", "pdf:hasXFA": "false", "pdf:hasXMP": "false", "pdf:unmappedUnicodeCharsPerPage": "0", "producer": "Microsoft: Print To PDF", "resourceName": "b''samplepdf.pdf'", "'"title": "Microsoft Word - Document1", "xmpTPg:NPages": "1""}{"Component 1": "Y component: Quantization table 0, Sampling factors 2 horiz/2 vert", "Component 2": "Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Component 3": "Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Compression Type": "Baseline", "Content-Type": "image/jpeg", "Data Precision": "8 bits", "File Modified Date": "Fri Jan 22 10:49:27 -05:00 2021", "File Name": "apache-tika-2326026356302560937.tmp", "File Size": "104692 bytes", "Image Height": "720 pixels", "Image Width": "1280 pixels", "Number of Components": "3", "Number of Tables": "4 Huffman tables", "Resolution Units": "none", "Thumbnail Height Pixels": "0", "Thumbnail Width Pixels": "0", "X Resolution": "1 dot", "X-Parsed-By": "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.jpeg.JpegParser", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "4", "Y Resolution": "1 dot", "resourceName": "b'"samplejpg.jpg'"', "tiff:BitsPerSample": "8", "tiff:ImageLength": "720", "tiff:ImageWidth": "1280", "content": "No Text Content"}, {"Author": "dst1", "Content-Type": "application/pdf", "Creation-Date": "2021-01-17T18:57:21Z", "Last-Modified": "2021-01-17T18:57:21Z", "Last-Save-Date": "2021-01-17T18:57:21Z", "X-Parsed-By":"org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.pdf.PDFParser", "X-TIKA:content_handler": "ToTextContentHandler", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "10", "access_permission:assemble_document": "true", "access_permission:can_modify": "true", "access_permission:can_print": "true", "access_permission:can_print_degraded": "true", "access_permission:extract_content": "true", "access_permission:extract_for_accessibility": "true", "access_permission:fill_in_form": "true", "access_permission:modify_annotations": "true", "created": "2021-01-17T18:57:21Z", "creator": "dst1", "date": "2021-01-17T18:57:21Z", "dc:creator": "dst1", "dc:format": "application/pdf; version=1.7", "dc:title": "Microsoft Word - Document1", "dcterms:created": "2021-01-17T18:57:21Z", "dcterms:modified": "2021-01-17T18:57:21Z", "meta:author": "dst1", "meta:creation-date": "2021-01-17T18:57:21Z", "meta:save-date": "2021-01-17T18:57:21Z", "modified": "2021-01-17T18:57:21Z", "pdf:PDFVersion": "1.7", "pdf:charsPerPage": "27", "pdf:docinfo:created": "2021-01-17T18:57:21Z", "pdf:docinfo:creator": "dst1", "pdf:docinfo:modified": "2021-01-17T18:57:21Z", "pdf:docinfo:producer": "Microsoft: Print To PDF", "pdf:docinfo:title": "Microsoft Word - Document1", "pdf:encrypted": "false", "pdf:hasMarkedContent": "false", "pdf:hasXFA": "false", "pdf:hasXMP": "false", "pdf:unmappedUnicodeCharsPerPage": "0", "producer": "Microsoft: Print To PDF", "resourceName": "b''samplepdf.pdf'", "'"title": "Microsoft Word - Document1", "xmpTPg:NPages": "1"}]"'
# #bulkdata = '[{"Component 1": "Y component: Quantization table 0, Sampling factors 2 horiz/2 vert", "Component 2": Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Component 3": "Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Compression Type": "Baseline", "Content-Type": "image/jpeg", "Data Precision": "8 bits", "File Modified Date": "Fri Jan 22 10:49:27 -05:00 2021", "File Name": "apache-tika-2326026356302560937.tmp", "File Size": "104692 bytes", "Image Height": "720 pixels", "Image Width": "1280 pixels", "Number of Components": "3", "Number of Tables": "4 Huffman tables", "Resolution Units": "none", "Thumbnail Height Pixels": "0", "Thumbnail Width Pixels": "0", "X Resolution": "1 dot", "X-Parsed-By": "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.jpeg.JpegParser", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "4", "Y Resolution": "1 dot", "resourceName": "b'"samplejpg.jpg'," "tiff:BitsPerSample":"" "8",""" "tiff:ImageLength"': "720", "tiff:ImageWidth": "1280", "content": "No Text Content"}, {"Author": "dst1", "Content-Type": "application/pdf", "Creation-Date": "2021-01-17T18:57:21Z", "Last-Modified": "2021-01-17T18:57:21Z", "Last-Save-Date": "2021-01-17T18:57:21Z", "X-Parsed-By": "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.pdf.PDFParser", "X-TIKA:content_handler": "ToTextContentHandler", "X-TIKA:embedded_depth": "0", "X-TIKA:parse_time_millis": "10", "access_permission:assemble_document": "true", "access_permission:can_modify": "true", "access_permission:can_print": "true", "access_permission:can_print_degraded": "true", "access_permission:extract_content": "true", "access_permission:extract_for_accessibility": "true", "access_permission:fill_in_form": "true", "access_permission:modify_annotations": "true", "created": "2021-01-17T18:57:21Z", "creator": "dst1", "date": "2021-01-17T18:57:21Z", "dc:creator": "dst1", "dc:format": "application/pdf; version=1.7", "dc:title": "Microsoft Word - Document1", "dcterms:created": "2021-01-17T18:57:21Z", "dcterms:modified": "2021-01-17T18:57:21Z", "meta:author": "dst1", "meta:creation-date": "2021-01-17T18:57:21Z", "meta:save-date": "2021-01-17T18:57:21Z", "modified": "2021-01-17T18:57:21Z", "pdf:PDFVersion": "1.7", "pdf:charsPerPage": "27", "pdf:docinfo:created": "2021-01-17T18:57:21Z", "pdf:docinfo:creator": "dst1", "pdf:docinfo:modified": "2021-01-17T18:57:21Z", "pdf:docinfo:producer": "Microsoft: Print To PDF", "pdf:docinfo:title": "Microsoft Word - Document1", "pdf:encrypted": "false", "pdf:hasMarkedContent": "false", "pdf:hasXFA": "false", "pdf:hasXMP": "false", "pdf:unmappedUnicodeCharsPerPage": "0", "producer": "Microsoft: Print To PDF", "resourceName": "b'"samplepdf.pdf'", "title": "Microsoft Word - Document1"', "xmpTPg:NPages": "1", "content": '"b'"'"Microsoft Word - Document1\\n\\n\\nPlease please please work! \\n\\n\\n'"}, '{"'Application-Name": "Microsoft Office PowerPoint", "Application-Version": "16.0000", "Author": "Whitney Mallicoat", "Content-Type": "application/vnd.openxmlformats-officedocument.presentationml.presentation", "image/jpeg", "Creation-Date": "2021-01-18T19:05:01Z", "Last-Author": "Whitney Mallicoat", "Last-Modified": "2021-01-18T19:06:01Z", "Last-Save-Date": "2021-01-18T19:06:01Z", "Paragraph-Count": "1", "Presentation-Format": "Widescreen", "Revision-Number": "1", "Slide-Count": "1", "Word-Count": "6", "X-Parsed-By": "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.microsoft.ooxml.OOXMLParser", "org.apache.tika.parser.DefaultParser", "org.apache.tika.parser.jpeg.JpegParser", "X-TIKA:content_handler": "ToTextContentHandler", "ToTextContentHandler", "X-TIKA:embedded_depth": "0", "1", "X-TIKA:parse_time_millis": "44", "4", "cp:revision": "1", "creator": "Whitney Mallicoat", "date": "2021-01-18T19:06:01Z", "dc:creator": "Whitney Mallicoat", "dc:title": "PowerPoint Presentation", "/docProps/thumbnail.jpeg", "dcterms:created": "2021-01-18T19:05:01Z", "dcterms:modified": "2021-01-18T19:06:01Z", "extended-properties:AppVersion": "16.0000", "extended-properties:Application": "Microsoft Office PowerPoint", "extended-properties:PresentationFormat": "Widescreen", "meta:author": "Whitney Mallicoat", "meta:creation-date": "2021-01-18T19:05:01Z", "meta:last-author": "Whitney Mallicoat", "meta:paragraph-count": "1", "meta:save-date": "2021-01-18T19:06:01Z", "meta:slide-count": "1", "meta:word-count": "6", "modified": "2021-01-18T19:06:01Z", "resourceName": "b''samplepptx.pptx'", '"'/docProps/thumbnail.jpeg", "title": "PowerPoint Presentation", "/docProps/thumbnail.jpeg", "xmpTPg:NPages": "1", "Component 1": "Y component: Quantization table 0, Sampling factors 2 horiz/2 vert", "Component 2": "Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Component 3": "Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert", "Compression Type": "Baseline", "Data Precision": "8 bits", "File Modified Date": "Fri Jan 22 10:49:27 -05:00 2021", "File Name": "apache-tika-3283484519910092972.tmp", "File Size": "1483 bytes", "Image Height": "144 pixels", "Image Width": "256 pixels", "Number of Components": "3", "Number of Tables": "4 Huffman tables", "Resolution Units": "inch", "Thumbnail Height Pixels": "0", "Thumbnail Width Pixels": "0", "X Resolution": "96 dots", "X-TIKA:embedded_resource_path": "/thumbnail.jpeg", "Y Resolution": "96 dots", "embeddedRelationshipId": "/docProps/thumbnail.jpeg", "tiff:BitsPerSample": "8", "tiff:ImageLength": "144", "tiff:ImageWidth": "256", "content": "b''\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\nPowerPoint Presentation\\n\\nSample .ppt text for testing\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n/docProps/thumbnail.jpeg\\n\\n'"},' {"'Author": "Gregory Thomas <gregawscsa@gmail.com>", "Content-Type": ["message/rfc822", "application/pdf"], "Creation-Date": ["2021-01-22T02:36:33Z", "2014-12-02T16:27:13Z"], "Message-From": "Gregory Thomas <gregawscsa@gmail.com>", "Message-To": "test@admin.iwc-mail.com", "Message:From-Email": "gregawscsa@gmail.com", "Message:From-Name": "Gregory Thomas", "Message:Raw-Header:Authentication-Results": "amazonses.com; spf=pass (spfCheck: domain of _spf.google.com designates 209.85.208.173 as permitted sender) client-ip=209.85.208.173; envelope-from=gregawscsa@gmail.com; helo=mail-lj1-f173.google.com; dkim=pass header.i=@gmail.com; dmarc=pass header.from=gmail.com;", "Message:Raw-Header:DKIM-Signature": "v=1; a=rsa-sha256; c=relaxed/relaxed;        d=gmail.com; s=20161025;        h=mime-version:from:date:message-id:subject:to;        bh=fwCn5xKJThG/lrOlIbl2Sw/PY3BQc7Jct36B8rgRfLs=;        b=YESlF3RLyiLSS3xgjBA14F8JGFe3ldMPud6tNz3cuWuh7MJoje3TKUnD7Z3He2oz2A         D9DVJtvi8YLxi4kxh2rPMbCVYF+OZASWCWeyCQwuP7TLfVjYc3X1AvG+EYhnT1vlKK0d         5KkYtrcgf/449TtUmLX7SCzKj5nfXV4ZUpTMWZ89oWVYmXcFRK76PErhRmttuXyGE5e4         QNXyXna6o6X9Dm+FQ04QRwhOHX9Ed8qvGyeggDHnpo9ejYq7gLb/bMltjS525Y3gpd74         lY11DVeM44MoifkgnrFxf6ypRTftpGckWzNXTPv4gn2vUl1Jm739pJ3mRZxHyv4/bmRu         0ZFw==", "Message:Raw-Header:MIME-Version": "1.0", "Message:Raw-Header:Message-ID": "<CAAaOrRgC86-0OEeHfW2ZPVefwFJwVy2oteZ3W+fzuOGzO_Yx1w@mail.gmail.com>", "Message:Raw-Header:Received": ["from mail-lj1-f173.google.com (mail-lj1-f173.google.com [209.85.208.173]) by inbound-smtp.us-west-2.amazonaws.com with SMTP id viin6r4joh0cr3imf3nnro2l3rvr8714noa8fe81 for test@admin.iwc-mail.com; Fri, 22 Jan 2021 02:36:48 +0000 (UTC)", "by mail-lj1-f173.google.com with SMTP id i17so4885812ljn.1        for <test@admin.iwc-mail.com>; Thu, 21 Jan 2021 18:36:47 -0800 (PST)"], "Message:Raw-Header:Received-SPF": "pass (spfCheck: domain of _spf.google.com designates 209.85.208.173 as permitted sender) client-ip=209.85.208.173; envelope-from=gregawscsa@gmail.com; helo=mail-lj1-f173.google.com;", "Message:Raw-Header:Return-Path": "<gregawscsa@gmail.com>", "Message:Raw-Header:X-Gm-Message-State": "AOAM532DTfuSpO7tyqjv2J+74nmdddl/usDesDnX2O+hxVRVwZOzpJVe\tyTp+A/MsxeX2E3GawFXQHrVGy5t+4sWMEUWhxJA+DSJ8rzU=", "Message:Raw-Header:X-Google-DKIM-Signature": "v=1; a=rsa-sha256; c=relaxed/relaxed;        d=1e100.net; s=20161025;        h=x-gm-message-state:mime-version:from:date:message-id:subject:to;        bh=fwCn5xKJThG/lrOlIbl2Sw/PY3BQc7Jct36B8rgRfLs=;        b=gBS6YzElBjz2rQzYcvqO14YTA5339CtC1ZlR/UtoXvuXBeTEWUDYQhROGEhLY8PXLo         RNTK50nOH2IGJx2/A1X6/c5vtDhy5HHkahCZ5graQBXDqs6Rh9QqMUJ2A5lihBPWsgot         0DH/w3Vpy0U3YS/tWNelTiy7krXVC2yqd9x42SwEpCcWmyKv0VcskrC9Qn3PWfe3n/vz         H1mlxTWk2pS854Xr+S6CDMiEgePWzKuG6KXUByD5AVhY+dYZoinbEHMyvN0hhNLUA0Tv         MKJJvN1G5/Ds/RTz19dCr723oPrPmrzFC8KQ1u4fAYzCWr4eQ4YWI0eWeaSqdLynxej3         F/4w==", "Message:Raw-Header:X-Google-Smtp-Source": "ABdhPJzINQ8YXutPGtSbOZ+bmYYY2Bkzf5Lkw66W2usU3Vzw9FPqz8PTdeV3zUORS3LgMKlblrJlqFSYKe0FjlFUAng=", "Message:Raw-Header:X-Received": "by 2002:a2e:94d:: with SMTP id 74mr211246ljj.104.1611283005217; Thu, 21 Jan 2021 18:36:45 -0800 (PST)", "Message:Raw-Header:X-SES-DKIM-SIGNATURE": "a=rsa-sha256; q=dns/txt; b=HO7iz/9yDl9kPdk9CYRXAne22DBbE161yg9HSrAKgZUBrvIg/Ud1UlEcPP8W2xRo9tNtezniCS4+49Uj+xm1BLU12fdGRBItInsRpP73bIv6W+fqKCydqt9qLpNtXXledG8YNYwrS/NsRQ0h6CobxusXnMob4r2fWTA0CfmVh3Q=; c=relaxed/simple; s=hsbnp7p3ensaochzwyq5wwmceodymuwv; d=amazonses.com; t=1611283009; v=1; bh=RDcE2CpOa...""}""]'

# table = dynamodb.Table(database)

# table.put_item(
#     Item={
#          'emailid': emailid,
#          'ingestdate': ingestdate,
#          'bulkdata': bulkdata
#      }
#  )

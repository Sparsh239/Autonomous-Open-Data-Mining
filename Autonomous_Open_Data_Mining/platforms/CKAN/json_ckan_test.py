# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:47:29 2020

@author: skans
"""
import requests
import pandas as pd
import json


# url = 'http://data.louisvilleky.gov/api/3/action/package_list'

# r = requests.get(url)
# print(r.text)
# load_json_data = json.loads(r.text)
# dataframe_json = pd.DataFrame(load_json_data)
# dataframe_json['result'] = 'http://data.louisvilleky.gov/api/3/action/package_show?id='+ dataframe_json['result']
# dataset_information = []
# for row in dataframe_json.itertuples():
#     link = getattr(row, 'result')
#     r_link = requests.get(link)
#     json_link_data = json.loads(r_link.text)
#     dataset_information.append(json_link_data)



link_json_data = [{
  'help': 'Return the metadata of a dataset (package) and its resources. :param id: the id or name of the dataset :type id: string',
  'success': True,
  'result': [
    {
      'id': 'f1472350-9094-4e4e-8ff8-dcdc5ac1952a',
      'name': 'metro-parks-program-registration-list',
      'title': 'Metro Parks Program Registration List',
      'maintainer': 'Louisville Metro Open Data',
      'maintainer_email': 'opendata@louisvilleky.gov',
      'url': 'https://data.louisvilleky.gov/dataset/metro-parks-program-registration-list',
      'state': 'Active',
      'log_message': "Update to resource 'Metro Parks Program Registration List'",
      'private': True,
      'revision_timestamp': 'Mon, 03/25/2019 - 12:13',
      'metadata_created': 'Thu, 06/09/2016 - 09:57',
      'metadata_modified': 'Mon, 03/25/2019 - 12:13',
      'creator_user_id': '833fff9d-2f9d-4ad2-9c5a-40305b0d0ee1',
      'type': 'Dataset',
      'resources': [
        {
          'id': '0e9c04df-78c3-4679-806c-a84bc832086a',
          'revision_id': '',
          'url': 'https://data.louisvilleky.gov/sites/default/files/Parks_Program_Registration_0.csv',
          'description': '',
          'format': 'csv',
          'state': 'Active',
          'revision_timestamp': 'Tue, 01/16/2018 - 16:31',
          'name': 'Metro Parks Program Registration List',
          'mimetype': 'text/csv',
          'size': '3.76 MB',
          'created': 'Tue, 02/21/2017 - 08:45',
          'resource_group_id': '612b627b-aaf2-412f-ad09-20d59dcf97f2',
          'last_modified': 'Date changed  Tue, 01/16/2018 - 16:31'
        }
      ],
      'groups': [
        {
          'description': '<p>Metro Parks was established in 1968, combining the Louisville City Parks Department (founded in 1888) and the Jefferson County Parks Department (founded in the mid-1940s). The agency became a department of Louisville/Jefferson County Metro Government when the City of Louisville and Jefferson County governments merged on January 6, 2003.</p>\n<p><a href="https://louisvilleky.gov/government/parks">Website</a></p>\n',
          'id': '612b627b-aaf2-412f-ad09-20d59dcf97f2',
          'image_display_url': 'https://data.louisvilleky.gov/sites/default/files/lpr_logo_color_vert.jpg',
          'title': 'Parks and Recreation',
          'name': 'group/metro-parks'
        }
      ]
    }
  ]
},{
  'help': 'Return the metadata of a dataset (package) and its resources. :param id: the id or name of the dataset :type id: string',
  'success': True,
  'result': [
    {
      'id': 'a05805f8-7442-4f80-ad85-61fd80eb7e9c',
      'name': 'suburban-fire-districts',
      'title': 'Suburban Fire Districts',
      'maintainer': 'Louisville Metro Open Data',
      'maintainer_email': 'opendata@louisvilleky.gov',
      'notes': '<p>Fire District boundaries for Louisville Metro Suburban areas.</p>\n',
      'url': 'https://data.louisvilleky.gov/dataset/suburban-fire-districts',
      'state': 'Active',
      'log_message': "Update to resource 'Suburban Fire Districts'",
      'private': True,
      'revision_timestamp': 'Mon, 03/25/2019 - 12:13',
      'metadata_created': 'Thu, 06/09/2016 - 09:59',
      'metadata_modified': 'Mon, 03/25/2019 - 12:13',
      'creator_user_id': '833fff9d-2f9d-4ad2-9c5a-40305b0d0ee1',
      'type': 'Dataset',
      'resources': [
        {
          'id': '7e7aed6f-0c4c-42e8-b060-a19e09f3bf7e',
          'revision_id': '',
          'url': 'https://data.louisvilleky.gov/sites/default/files/Suburban_Fire_Districts.zip',
          'description': '',
          'format': 'arcgis shp',
          'state': 'Active',
          'revision_timestamp': 'Tue, 01/16/2018 - 16:28',
          'name': 'Suburban Fire Districts',
          'mimetype': 'application/zip',
          'size': '207.23 KB',
          'created': 'Tue, 06/21/2016 - 19:20',
          'resource_group_id': '268f62f6-006b-4429-b80b-454ff47e6ff7',
          'last_modified': 'Date changed  Tue, 01/16/2018 - 16:28'
        }
      ],
      'groups': [
        {
          'description': '<p>The Louisville Division of Fire, commonly known as the Louisville Fire Department or Louisville Fire &amp; Rescue (abbreviated LFD or LFR), is the sole fire suppression agency for the former city of Louisville, Kentucky and is one of nineteen fire departments within the Louisville-Jefferson County, Kentucky metropolitan area. The Louisville Division of Fire is the second largest fire department in Kentucky.</p>\n',
          'id': '268f62f6-006b-4429-b80b-454ff47e6ff7',
          'image_display_url': 'https://data.louisvilleky.gov/sites/default/files/MASvert2c.ai_0013_firevert2c.png',
          'title': 'Louisville Fire',
          'name': 'group/louisville-fire'
        }
      ]
    }
  ]
}
]

dataframe_list = []
for link_data in link_json_data:
    results = link_data['result']
    dataset_information_list = []
    for dataset_information in results:
        dataset_id = dataset_information['id']
        location_link = dataset_information['url']
        dataset_title = dataset_information['title']
        dataset_state = dataset_information['state']
        dataset_creation_date = dataset_information['metadata_created']
        dataset_metadata_modified = dataset_information['metadata_modified']
        dataset_information_list.extend([dataset_id,location_link,dataset_title,dataset_state,
                                        dataset_creation_date,dataset_metadata_modified])
        resources = dataset_information['resources']
        groups = dataset_information['groups']
        resource_information_list = []
        groups_information_list = []
        for resource in resources:
            dataset_link = resource['url']
            dataset_format = resource['format']
            dataset_size = resource['size']
            resource_information_list.extend([dataset_link,dataset_format,dataset_size])
            dataset_information_list.extend(resource_information_list)
        for group in groups:
            description = group['description']
            groups_information_list.append(description)
            dataset_information_list.extend(groups_information_list)
    dataframe_list.append(dataset_information_list)
    
print(dataframe_list)
louville = pd.DataFrame(dataframe_list)
louville.columns = ["ID","Location Link","Title", "State","Creation Date", "Metadata Modification Date",
                    'Dataset URL',"Dataset Format","Size","Description"]
louville.to_csv("louville.csv")

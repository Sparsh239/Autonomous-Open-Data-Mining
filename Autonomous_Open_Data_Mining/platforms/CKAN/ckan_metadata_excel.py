# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 00:50:22 2020

@author: skans
"""

import requests
import pandas as pd
import json

class Ckan:
    def __init__(self, ckan_dataset):
        self.ckan_dataset = ckan_dataset

    def add_specific_characters(self):
        for index,row in self.ckan_dataset.iterrows():
            website_link = getattr(row, "website_url")
            if website_link[-1] == "/":
                updated_link = website_link + "api/3/action/package_list"
                self.ckan_dataset.loc[index, "api_website_url"] = updated_link
            else:
                website_link = website_link + "/"
                updated_link = website_link + "api/3/action/package_list"
                self.ckan_dataset.loc[index, "website_url"] = website_link
                self.ckan_dataset.loc[index, "api_website_url"] = updated_link # Required to access the api functionality
        return self.ckan_dataset   
    
    def ckan_dataset_information(self):
        ckan_dataset = self.add_specific_characters()
        all_datasets = []
        for index,row in ckan_dataset.iterrows():
            api_website_url = getattr(row, "api_website_url")
            website_link = getattr(row,"website_url")
            r = requests.get(api_website_url)
            if r.status_code == requests.codes.OK:
                print("Everything Worked")
                continue 
            elif r.status_code == requests.code.BAD:
                print("Something went Wrong!")
                continue
            elif r.status_code == requests.code.NOT_FOUND:
                print("Ther server could not find this URL")
                continue
            elif r.status_code == requests.code.NOT_ALLOWED:
                print("You are not allowed to access this!")
                continue
                

    
# def ckan_metadat_excel(ckan_dataset):
#     ckan_dataset_updated = add_specific_characters(ckan_dataset)
#     collection_of_all_datasets = []
#     for index,row in ckan_dataset_updated.iterrows():
#         api_website_link  = getattr(row, "api_website_link")
#         website_link = getattr(row, "website_url")
#         print(website_link)
#         r = requests.get(api_website_link)
#         json_data = json.loads(r.text)
#         dataframe_data = pd.DataFrame(json_data)
#         dataframe_data['result'] = website_link + "api/3/action/package_show?id=" + dataframe_data['result']
#         information_list = []
#         for row in dataframe_data.itertuples():
#             final_call_link= getattr(row, 'result')
#             r_final_call_link = requests.get(final_call_link)
#             json_data = json.loads(r_final_call_link.text)
#             information_list.append(json_data)
#         print(information_list)
#         # dataframe_list = []
#         # for link_data in information_list:
#         #     results = link_data['result']
#         #     if isinstance(results, list):
#         #         print("The results is a list, thus normal code")
#         #     else:
#         #         print("The results column of the dictionary is not a list - CHECK 2 (False)")
#         #         intermediary_list_creation = [results]
#         #         dataset_information_list = []
#         #         for dataset_information in results:
#         #             dataset_id = dataset_information['id']
#         #             dataset_state = dataset_information['state']
#         #             dataset_creation_date = dataset_information['metadata_created']
#         #             dataset_metadata_modified = dataset_information['metadata_modified']
#         #             dataset_information_list.extend([dataset_id,dataset_state,
#         #                                              dataset_creation_date,dataset_metadata_modified])
#         #             resources = dataset_information['resources']
#         #             resources_list_information = []
#         #             if instance(resources, list):
#         #                 print("\n The Resources is a list - CHECK 2 (True)")
#         #                 if len(resources)>1:
#         #                     for subresource in resources:
#         #                         subresource_dict = {}
#         #                         subresource_dict['name'] = subresource['name']
#         #                         subresource_dict['url'] = subresource['url']
#         #                         subresource_dict['format'] = subresource['format']
#         #                         subresource_dict['id'] = subresource['id']
#         #                         subresource_dict['description'] = subresource['description']
#         #                         resources_list_information.append(subresource_dict)
#         #                     dataset_information_list.extend(resources_list_information)
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
#         #         #     groups = dataset_information['groups']
#         #         #     resource_information_list = []
#         #         #     groups_information_list = []
#         #         #     for resource in resources:
#         #         #         dataset_link = resource['url']
#         #         #         dataset_format = resource['format']
#         #         #         dataset_size = resource['size']
#         #         #         resource_information_list.extend([dataset_link,dataset_format,dataset_size])
#         #         #         dataset_information_list.extend(resource_information_list)
#         #         #     for group in groups:
#         #         #         description = group['description']
#         #         #         groups_information_list.append(description)
#         #         #         dataset_information_list.extend(groups_information_list)
#         #         # dataframe_list.append(dataset_information_list)
            
                
                
                
                
                
                
                
                
                
#         #         # dataset_information_list = []
#         #         # for dataset_information in results:
#         #         #     dataset_id = dataset_information['id']
#         #         #     location_link = dataset_information['url']
#         #         #     dataset_title = dataset_information['title']
#         #         #     dataset_state = dataset_information['state']
#         #         #     dataset_creation_date = dataset_information['metadata_created']
#         #         #     dataset_metadata_modified = dataset_information['metadata_modified']
#         #         #     dataset_information_list.extend([dataset_id,location_link,dataset_title,dataset_state,
#         #         #                                     dataset_creation_date,dataset_metadata_modified])
#         #         #     resources = dataset_information['resources']
#         #         #     groups = dataset_information['groups']
#         #         #     resource_information_list = []
#         #         #     groups_information_list = []
#         #         #     for resource in resources:
#         #         #         dataset_link = resource['url']
#         #         #         dataset_format = resource['format']
#         #         #         dataset_size = resource['size']
#         #         #         resource_information_list.extend([dataset_link,dataset_format,dataset_size])
#         #         #         dataset_information_list.extend(resource_information_list)
#         #         #     for group in groups:
#         #         #         description = group['description']
#         #         #         groups_information_list.append(description)
#         #         #         dataset_information_list.extend(groups_information_list)
#         #         # dataframe_list.append(dataset_information_list)
            
    
    
                
            
    
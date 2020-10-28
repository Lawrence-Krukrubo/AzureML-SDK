# tutorial/01-create-workspace.py
from azureml.core import Workspace

ws = Workspace.create(name='azure-sdk', # provide a name for your workspace
                      subscription_id='87447ba1-18dc-40e1-9a5d-0a2dfd160f16', # provide your subscription ID
                      resource_group='azure_ml_and_data_sci', # provide a resource group name
                      create_resource_group=True,
                      location='South Central US') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')
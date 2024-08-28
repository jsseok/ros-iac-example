import os
import json

class LONParser:

    # init parser
    def __init__(self, file_path: str):

        self.file_path = file_path
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
    # 
    def get_nodes(self, package_name: str) -> list[str]:
        node_list = self.data.get(package_name, [])
        return [f"{node['node_name']} = {package_name}.{node['node_name']}.main:main" for node in node_list]

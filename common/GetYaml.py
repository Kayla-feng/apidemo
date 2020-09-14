import logging

import yaml


class GetYaml:


    @classmethod
    def get_yaml(self,path):

        try:
            with open(path,'r',encoding='utf-8') as f:
                file_data = f.read()

            data = yaml.load(file_data,Loader=yaml.FullLoader)
            return data
        except Exception as msg:
            logging.debug("yaml文件加载失败，报错信息：%s" % msg)



if __name__ == "__main__":
    print(GetYaml().get_yaml(r'D:\CrmApiProject\data\kind.yml')["create_kind"])
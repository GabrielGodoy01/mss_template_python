from decimal import Decimal
from typing import List

from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.user_dynamo_dto import UserDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class UserRepositoryDynamo(IUserRepository):

    @staticmethod
    def partition_key_format(id) -> str:
        return f"user#{id}"

    @staticmethod
    def sort_key_format(id: int) -> str:
        return f"{id}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)
    def get_user(self, id: int) -> User:
        user_data = self.dynamo.get_item(partition_key=self.partition_key_format(id), sort_key=self.sort_key_format(id))                    
        
        if 'Item' not in user_data:
            return None

        user = UserDynamoDTO.from_dynamo(user_data.get("Item")).to_entity()

        return user

    def get_all_user(self) -> List[User]:
        resp = self.dynamo.get_all_items()
        users = []
        for item in resp['Items']:
            if 'id' in item:
                users.append(UserDynamoDTO.from_dynamo(item).to_entity())

        return users


    def create_user(self, new_user: User) -> User:
        item = UserDynamoDTO.from_entity(user=new_user).to_dynamo()
        resp = self.dynamo.put_item(
            partition_key=self.partition_key_format(new_user.id),
            sort_key=self.sort_key_format(id=new_user.id),
            item=item,
            is_decimal=True
        )
        return new_user

    def delete_user(self, id: int) -> User:
        resp = self.dynamo.delete_item(partition_key=self.partition_key_format(id), sort_key=self.sort_key_format(id))

        if "Attributes" not in resp:
            raise NoItemsFound("id")

        return UserDynamoDTO.from_dynamo(resp['Attributes']).to_entity()

    def update_user(self, id: int, new_name: str) -> User:

        response = self.dynamo.update_item(
            partition_key=self.partition_key_format(id),
            sort_key=self.sort_key_format(id),
            update_dict={'name': new_name})

        if "Attributes" not in response:
            return None

        return UserDynamoDTO.from_dynamo(response["Attributes"]).to_entity()

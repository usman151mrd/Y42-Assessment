import os
from abc import abstractmethod
from enum import Enum
from uuid import uuid4


class Type(Enum):
    """
    Data can be divided into two major categories 1) Text, 2) Binary
    """

    Text = 1
    Binary = 2


class Model:
    """
    model class used to assign unique id to each model entity class and used to implement
    to_dict function so that all class members mapped into any format
    """

    def __init__(self):
        self.__id = uuid4().int

    @property
    def id(self):
        """
        :return:
        """
        return self.__id

    @abstractmethod
    def to_dict(self) -> dict:
        """
        :return
        """
        pass


class Product(Model):
    """
    this class is used for product entity and can be extended by a subclass
    """

    def __init__(self, title: str, category: str, price: int, description: str):
        """
        :param title:
        :param category:
        :param price:
        :param description:
        """
        super().__init__()
        self.__title: str = title
        self.__category: str = category
        self.__price: int = price
        self.__description: str = description

    @property
    def title(self) -> str:
        """
        :return:
        """
        return self.__title

    @property
    def category(self) -> str:
        """
        :return:
        """
        return self.__category

    @property
    def price(self) -> int:
        """

        :return:
        """
        return self.__price

    @property
    def description(self):
        """

        :return:
        """
        return self.__description

    @title.setter
    def title(self, value: str):
        self.__title = value

    @category.setter
    def category(self, value: str):
        self.__category = value

    @price.setter
    def price(self, value: int):
        self.__price = value

    @description.setter
    def description(self, value: str):
        self.__description = value

    def to_dict(self) -> dict:
        """

        :return:
        """
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "price": self.price,
            "description": self.description,
        }


class Storage:
    """
    Abstract class to manage storage operations
    """

    def __init__(self, type_: Type, file_name):
        self.__type = type_
        self.__filename = file_name

    @property
    def type(self) -> Type:
        """

        :return:
        """
        return self.__type

    @property
    def filename(self):
        """

        :return:
        """
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    @abstractmethod
    def dump(self, data: str, data_type: Type):
        """

        :param data:
        :param data_type:
        """
        pass

    @abstractmethod
    def load(self, data_type: Type):
        """

        :param data_type:
        """
        pass


class LocalStorage(Storage):
    """
    Implement local Storage concept using this class
    """

    def __init__(self, _type: Type, file_name: str):
        super().__init__(type_=_type, file_name=file_name)

    def dump(self, data: str, data_type: Type):
        """

        :param data:
        :param data_type:
        """
        op_type = "w" + "t" if data_type == Type.Text else "b"
        path = os.getcwd()
        with open(os.path.join(path, self.filename), op_type) as file:
            file.write(data)

    def load(self, data_type: Type):
        """

        :param data_type:
        :return:
        """
        op_type = "r" + "t" if data_type == Type.Text else "b"
        path = os.getcwd()
        with open(os.path.join(path, self.filename), op_type) as file:
            data = file.read()
        return data


class CloudStorage(Storage):
    """
    Mock class to implement Cloud storage
    """

    def __init__(self, file_name: str):
        super().__init__(type_=Type.Text, file_name=file_name)

    def dump(self, data: "Data", data_type: Type):
        """

        :param data:
        :param data_type:
        """
        pass

    def load(self, data_type: Type):
        """

        :param data_type:
        """
        pass


class Data:
    """
    Abstract class to handle difference operation w.r.t to a particular format
    """

    def __init__(self, designation: Storage, format_: str):
        self.__designation: Storage = designation
        self.__format = format_

    @property
    def designation(self) -> Storage:
        """

        :return:
        """
        return self.__designation

    @property
    def format(self) -> str:
        """

        :return:
        """
        return self.__format

    @designation.setter
    def designation(self, value: str):
        self.__designation = value

    @format.setter
    def format(self, value: str):
        self.__format = value

    @abstractmethod
    def insert(self, record: Model):
        """

        :param record:
        """
        pass

    @abstractmethod
    def batch_insert(self, records: [Model]):
        """

        :param records:
        """
        pass

    @abstractmethod
    def filter(self, **kwargs):
        """

        :param kwargs:
        """
        pass

    @abstractmethod
    def update(self, _id: uuid4().int, record: Model):
        """

        :param _id:
        :param record:
        """
        pass

    @abstractmethod
    def delete(self, _id):
        """

        :param _id:
        """
        pass


class JsonData(Data):
    """
    Extended from data and will be handled json format data
    """

    def __init__(self, designation: Storage):
        format_ = "json"
        super().__init__(designation=designation, format_=format_)

    def insert(self, record: Model):
        """

        :param record:
        :return:
        """
        # eval convert string to list of dict
        try:
            try:
                existing_data = eval(self.designation.load(self.designation.type))
            except FileNotFoundError:
                existing_data = []
            existing_data.append(record.to_dict())
            self.designation.dump(str(existing_data), self.designation.type)
            return True
        except Exception as e:
            print(e.args)
            return False

    def batch_insert(self, records: [Model]):
        """

        :param records:
        :return:
        """
        try:
            try:
                existing_data = eval(self.designation.load(self.designation.type))
            except FileNotFoundError:
                existing_data = []
            existing_data.extend([record.to_dict() for record in records])
            self.designation.dump(str(existing_data), self.designation.type)
            return True
        except Exception as e:
            print(e.args)
            return False

    def filter(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        filtered_records = []
        records = self.designation.load(self.designation.type)
        for record in eval(records):
            for key in kwargs.keys():
                if key in record.keys() and record[key] == kwargs[key]:
                    continue
                else:
                    break
            else:
                filtered_records.append(record)
        return filtered_records

    def update(self, _id, record: Model):
        """

        :param _id:
        :param record:
        :return:
        """
        try:
            record = record.to_dict()
            records = self.designation.load(self.designation.type)
            records = eval(records)
            for _record in records:
                if _record["id"] == _id:
                    for key in _record:
                        _record[key] = record[key]
                    break
            self.designation.dump(str(records), self.designation.type)
            return True
        except Exception as e:
            print(e.args)
            return False

    def delete(self, _id):
        """

        :param _id:
        """
        records = self.designation.load(self.designation.type)
        records = eval(records)
        counter = 0
        for record in records:
            if record["id"] == _id:
                break
            counter += 1
        del records[counter]
        self.designation.dump(str(records), self.designation.type)


class XMLData(Data):
    """
    Mock class to handle xml format data
    """

    def __init__(self, designation: Storage):
        format_ = "xml"
        super().__init__(designation=designation, format_=format_)

    def insert(self, record: Model):
        """

        :param record:
        """
        pass

    def batch_insert(self, records: [Model]):
        """

        :param records:
        """
        pass

    def filter(self, **kwargs):
        """

        :param kwargs:
        """
        pass

    def update(self, _id: uuid4().int, record: Model):
        """

        :param _id:
        :param record:
        """
        pass

    def delete(self, _id):
        """

        :param _id:
        """
        pass

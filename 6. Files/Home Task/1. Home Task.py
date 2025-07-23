#Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format

# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Private ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.

from datetime import datetime
from typing import final
import os
import text_cleaner
import shutil


class FeedItem:

    _instances = []

    def __init__(self) -> None:
        """
        Base function for class creation. Empty attributes will be populated by further functions, depending on user's choice.
        """

        self._title = ''
        self.title = 'placeholder'
        self.body = ''
        self.created_at = ''

    def get_info_manual(self) -> None:
        """
        Function for data input manually. Asks user about Feed title and body, and adds timestamp.
        Keeps track of created instances and stores it in a list.

        :return: Populates self title, body and created_at attributes. Record added to the list.
        """

        self.title = input('Please provide title for your Feed: ')
        self.body = input('Please provide message for your Feed: ')
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @property
    def title(self) -> str:
        """
        Creating setter for title.

        :return: Title string.
        """

        return self._title

    @title.setter
    def title(self, value:str) -> None:
        """
        Validating whether title is not empty. On empty raise error.

        :param value: Title string.
        :return: Error if title string is empty.
        """

        if not value.strip():
            raise ValueError('Title cannot be empty.')
        self._title = value.strip()

    @property
    def full_title(self) -> str:
        """
        Dynamically creates full title for a Feed using Class Name and user provided title.

        :return: Full title in standard format.
        """

        return f'{self.__class__.__name__} {self.title}'

    @classmethod
    def export_all_ads(cls, filepath = './feed_output.txt') -> None:
        """
        Saves summary of feeds in a file using full_title, body and additional_information keys of each instance.

        :param filepath: Path to file where the instance info will be stored.
        :return: File with summary of Feeds.
        """

        with open(filepath, 'w', encoding='utf8') as file:
            file.write(f'News feed: \n')
            for instance in cls._instances:
                file.write(f'{instance.full_title}\n')
                file.write(f'{vars(instance)["body"]}\n')
                file.write(f'{vars(instance)["additional_information"]}\n')
                file.write('\n')


@final
class NewsAd(FeedItem):
    def __init__(self) -> None:
        """
        Subclass for News Ad.
        """

        super().__init__()
        self.additional_information = ''

    def get_additional_info_manual(self) -> None:
        """
        Asks user about City, gets current date and creates standardized information for the Feed.

        :return: Populates additional_information attribute.
        """

        city = input('Please provide City location for your News Ad: ')
        self.additional_information = f'{city}, {datetime.today().strftime("%d/%m/%Y %H.%M")}'
        FeedItem._instances.append(self)

    def get_info_from_file(self, file_name: str) -> None:
        """
        Takes input from file. Reads file, splits by dot and populates attributes.
        :return: Populates additional_information attribute.
        """

        with open(f'./Files to process/{file_name}', 'r', encoding='utf8') as file:
            cleaned = text_cleaner.remove_non_ascii_string(file.read())
            trimmed = text_cleaner.trim_and_capitalize_text(cleaned).replace('.', '.\n')

            self.title = trimmed.splitlines()[0].strip()
            self.body = trimmed.splitlines()[1].strip()
            self.additional_information = f'{trimmed.splitlines()[2].strip().replace(".", "")}, {datetime.today().strftime("%d/%m/%Y %H.%M")}'
            FeedItem._instances.append(self)


class PrivateAd(FeedItem):
    def __init__(self) -> None:
        """
        Subclass for Private Ad.
        """
        super().__init__()
        self.additional_information = ''

    def get_additional_info_manual(self) -> None:
        """"
        Asks user for expiration date of the Ad and calculates days remaining and creates standardized information string for the Feed.

        :return: Populates additional_information attribute.
        """

        expiration = input('Please provide expiration date for your Private Ad (format dd/mm/YYYY): ')
        expiration_date = datetime.strptime(expiration, "%d/%m/%Y").date()
        today = datetime.today().date()
        days_left = (expiration_date - today).days
        self.additional_information = f'Actual until: {expiration}, {days_left} days left.'
        FeedItem._instances.append(self)

    def get_info_from_file(self, file_name: str) -> None:
        """
        Takes input from file. Reads file, splits by dot and populates attributes.
        :return: Populates additional_information attribute.
        """

        with open(f'./Files to process/{file_name}', 'r', encoding='utf8') as file:
            cleaned = text_cleaner.remove_non_ascii_string(file.read())
            trimmed = text_cleaner.trim_and_capitalize_text(cleaned).replace('.', '.\n')


            self.title = trimmed.splitlines()[0].strip()
            self.body = trimmed.splitlines()[1].strip()
            expiration = trimmed.splitlines()[2].strip().replace('.', '')

            expiration_date = datetime.strptime(expiration, "%d/%m/%Y").date()
            today = datetime.today().date()
            days_left = (expiration_date - today).days
            self.additional_information = f'Actual until: {expiration}, {days_left} days left.'
            FeedItem._instances.append(self)


class MatrimonialAd(FeedItem):
    def __init__(self) -> None:
        """
        Subclass for Matrimonial Ad.
        """

        super().__init__()
        self.additional_information = ''

    def get_additional_info_manual(self) -> None:
        """
        Asks user for gender, age and city and creates standardized information string for the Feed.

        :return: Populates additional_information attribute.
        """

        gender = input('Please provide your gender: ')
        age = input('Please provide your age: ')
        city = input('Please provide City: ')
        self.additional_information = f'Hot {gender}/{age} in area {city}!'
        FeedItem._instances.append(self)

    def get_info_from_file(self, file_name: str) -> None:
        """
        Takes input from file. Reads file, splits by dot and populates attributes.
        :return: Populates additional_information attribute.
        """

        with open(f'./Files to process/{file_name}', 'r', encoding='utf8') as file:
            cleaned = text_cleaner.remove_non_ascii_string(file.read())
            trimmed = text_cleaner.trim_and_capitalize_text(cleaned).replace('.', '.\n')

            self.title = trimmed.splitlines()[0].strip()
            self.body = trimmed.splitlines()[1].strip()

            gender = trimmed.splitlines()[2].strip().replace('.', '')
            age = trimmed.splitlines()[3].strip().replace('.', '')
            city  = trimmed.splitlines()[4].strip().replace('.', '')
            self.additional_information = f'Hot {gender}/{age} in area {city}!'
            FeedItem._instances.append(self)


def select_file(files_map: dict) -> str:
    """
    Helper function for create_feed().
    Lists available files and asks user to select one. Will validate user's choice and rerun the loop if choice is invalid

    :param files_map: Dictionary with number and file name.
    :return: File name of user's choice.
    """

    while True:
        print(f'Available files:')
        for key, file_name in files_map.items():
            print(f'{key} - {file_name}')

        file_choice = input(f'Please input file number: ')
        if file_choice in files_map:
            return files_map.get(file_choice)

        print(f'Invalid file, please select one of the below:\n')


def create_feed() -> FeedItem:
    """
    Main function which will trigger instance creation for specific class based on user's input. Will ask for input as long as user doesn't provide correct Feed type.
    Users can select Ad type they want to create, and either fill data manually or pull it from file.

    :return: Instance of subclass based on input, along with title and body for the Feed.
    """

    type_map = {
		'1': NewsAd,
		'2': PrivateAd,
		'3': MatrimonialAd
	}

    files_map = {str(index): file_name for index, file_name in enumerate(os.listdir('./Files to process'), start= 1)}


    while True:
        feed_type_choice = input('1 - News\n2 - Private Ad\n3 - Matrimonial Ad\nPlease input Feed type number: ')
        if feed_type_choice in type_map:
            print('')
            feed_class = type_map.get(feed_type_choice)

            while True:
                input_type = input('1 - Manual\n2 - From file\nPlease select Feed input type: ')
                print('')

                match input_type:
                    case '1':
                        new_feed = feed_class()
                        new_feed.get_info_manual()
                        new_feed.get_additional_info_manual()
                        return new_feed
                    case '2':
                        selected_file = select_file(files_map)
                        new_feed = feed_class()
                        new_feed.get_info_from_file(selected_file)
                        os.remove(f'./Files to process/{selected_file}')
                        return new_feed


                print(f'Invalid Input type, please select one of the below:\n')

        print(f'Invalid Feed type, please select one of the below:\n')


if __name__ == '__main__':

    # Copy sample files to processing folder

    for file in os.listdir('./Sample files'):
        shutil.copyfile(f'./Sample files/{file}', f'./Files to process/{file}')

    ads_num = int(input('How many ads do you want to create?: '))
    print('')
    for _ in range(ads_num):
        print(f'Adding Ad {_+1} out of {ads_num}.')
        feed = create_feed()
        print('')

FeedItem.export_all_ads()

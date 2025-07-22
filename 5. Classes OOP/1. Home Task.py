#Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format

# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Private ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.

from datetime import datetime
from typing import Callable

def i_am_out_of_ideas_at_this_hour_decorator(func: Callable) -> Callable:
    import time
    def wrapper():
        """
        Standard time-calculation wrapper as I'm running out of ideas :S

        :return: Function runtime duration
        """

        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Execution time is {(end_time - start_time):.04f} seconds.')
    return wrapper


class FeedItem:

    _instances = []

    def __init__(self, title: str, body: str) -> None:
        """
        Main function collects Feed title and body from user, passes it to subclass and then to this super class.
        Keeps track of created instances and stores it in a list.

        :param title: Feed title input by user.
        :param body: Feed message input by user.
        """

        self.title = title
        self.body = body
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        FeedItem._instances.append(self)

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


class NewsAd(FeedItem):
    def __init__(self, title: str, body: str) -> None:
        """
        Subclass for News Ad. Asks user about City and adds standardized information regarding City and current date for the News. Yes this could be one-liner but IMO it's a bit more clear if we break it down.

        :param title: Feed title input by user.
        :param body: Feed message input by user.
        """

        super().__init__(title, body)
        city = input('Please provide City location for your News Ad: ')
        self.additional_information = f'{city}, {datetime.today().strftime("%d/%m/%Y %H.%M")}'


class PrivateAd(FeedItem):
    def __init__(self, title: str, body: str) -> None:
        """
        Subclass for Private Ad. Asks user for expiration date of the Ad and calculates days remaining.

        :param title: Feed title input by user.
        :param body: Feed message input by user.
        """
        super().__init__(title, body)

        expiration = input('Please provide expiration date for your Private Ad (format dd/mm/YYYY): ')
        expiration_date = datetime.strptime(expiration, "%d/%m/%Y").date()
        today = datetime.today().date()
        days_left = (expiration_date - today).days
        self.additional_information = f'Actual until: {expiration}, {days_left} days left.'


class MatrimonialAd(FeedItem):
    def __init__(self, title: str, body: str) -> None:
        """
        Subclass for Matrimonial Ad. Asks user for gender, age and city.

        :param title: Feed title input by user.
        :param body: Feed message input by user.
        """

        super().__init__(title, body)

        gender = input('Please provide your gender: ')
        age = input('Please provide your age: ')
        city = input('Please provide City: ')
        self.additional_information = f'Hot {gender}/{age} in area {city}!'


@i_am_out_of_ideas_at_this_hour_decorator
def create_feed() -> FeedItem:
    """
    Main function which will trigger instance creation for specific class based on user's input. Will ask for input as long as user doesn't provide correct Feed type.

    :return: Instance of subclass based on input, along with title and body for the Feed.
    """
    type_map = {
		'1': NewsAd,
		'2': PrivateAd,
		'3': MatrimonialAd
	}

    while True:
        choice = input('1 - News\n2 - Private Ad\n3 - Matrimonial Ad\nPlease input feed type number: ')
        if choice in type_map:
            feed_class = type_map.get(choice)
            title = input('Please provide title for your feed: ')
            body = input('Please provide message for your feed: ')
            return feed_class(title, body)

        print(f'Invalid Choice, please select one of the below:')

if __name__ == '__main__':
    ads_num = int(input('How many ads do you want to create?: '))
    for _ in range(ads_num):
        print(f'Adding Ad {_+1} out of {ads_num}.')
        feed = create_feed()

FeedItem.export_all_ads()

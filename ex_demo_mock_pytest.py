import requests
import pytest
import responses
from prettyprinter import cpprint
from dataclasses import dataclass
from unittest import mock

import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

MOCK_USER = {
        'results': [{
            'email': 'stephane@wirtel.be',
            'name':dict(title='Monsieur', first='Stephane', last='Wirtel'),
             'login': dict(username='matrixise'),
           'gender': 'male',
        }]
    }

@dataclass
class User:
    gender: str
    title: str
    firstname: str
    lastname: str
    email: str
    username: str

    @classmethod
    def create_from_api(cls, result):
        record = result['results'][0]
        record_name = record['name']
        record_login = record['login']

        user = User(record['gender'], record_name['title'], record_name['first'],
                    record_name['last'], record['email'], record_login['username']
                    )
        return user

class APIUnreachableException(Exception):
    pass

class HttpNotFound(Exception):
    pass


def get_user():
    #import pdb;pdb.set_trace()


    try :
        response = requests.get('https://randomuser.me/api/')
        # print(response.status_code)
        logging.info('web service %d', response.status_code)
        if response.status_code == 404:
            raise HttpNotFound()
        return User.create_from_api(response.json())

        # result = response.json()
        # cpprint(result)
        # record = result['results'][0]


        # -- deplacement de ce code dans classmethod
        # record_name = record['name']
        # record_login = record['login']
        #
        # user = User(record['gender'], record_name['title'], record_name['first'],
        #             record_name['last'], record['email'], record_login['username']
        #             )
        # return user
    except requests.exceptions.ConnectionError as error:
        # print (error)
        raise APIUnreachableException()



class  GetUserTestCase(unittest.TestCase):
    # @unittest.skip('disable')
    @responses.activate
    def test_get_user_works(self):
        responses.add(responses.GET, 'https://randomuser.me/api/', json=MOCK_USER)
        user = get_user()
        self.assertIsInstance(user, User)
        self.assertEqual(user.firstname, 'Stephane')
        self.assertEqual(user.lastname, 'Wirtel')

    # @unittest.skip('disable')
    #@unittest.skip('in progress') # stopper ce test en cours
    @responses.activate
    def test_get_user_not_found(self):
        responses.add(responses.GET, 'https://randomuser.me/api/', status=404)
        with self.assertRaises(HttpNotFound):
            user = get_user()

    # @unittest.skip('disable')
    #@unittest.skip('in progress') # stopper ce test en cours
    @responses.activate
    def test_get_user_server_is_unreachable(self):
        with self.assertRaises(APIUnreachableException):
            user = get_user()

    @mock.patch('ex_demo_mock.get_user')
    def test(self, mock_get_user):
        # avec mock on ne passe pas dans get_user c'est redéfini
        mock_get_user.return_value = User.create_from_api(MOCK_USER)
        #print('essai=%s'%mock_get_user.return_value)
        user = get_user()
        self.assertEqual(user.firstname, 'Stephane')


def main():
    try:
        user = get_user()
        logging.debug(user)
    except APIUnreachableException:
        print ('le serveur est injoignable')
    except HttpNotFound:
        print ('Le serveur n''existe pas')

if __name__ == '__main__':
    # unittest.main()
    main()

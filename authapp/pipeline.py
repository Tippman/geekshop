import datetime
from collections import OrderedDict
from urllib.parse import urlunparse, urlencode

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    # api_url = f'https://api.vk.com/method/users.get/fields=bdate,about,sex&access_token={response["access_token"]}&v=5.92'

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'crop_photo')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['sex'] != 0:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about_me = data['about']

    if data['bdate']:
        bday = datetime.datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        age = timezone.now().year - bday.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social-core.backends.vk.VKOAuth2')
        user.birthday = bday

    user.email = response['email']
    user.save()

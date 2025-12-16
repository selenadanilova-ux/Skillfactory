from api import PetFriends

from settings import nonvalid_email, valid_password

import os

pf = PetFriends()

# Первый негативный тест

def test_get_api_key_for_nonvalid_email_user(email=nonvalid_email, password=valid_password):
    """ Проверяем, что запрос упадёт из-за невалидного email"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

# Второй негативный тест

from settings import valid_email, nonvalid_password

def test_get_api_key_for_nonvalid_password_user(email=valid_email, password=nonvalid_password):
    """ Проверяем, что запрос упадёт из-за невалидного пароля"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

# Третий негативный тест

from settings import empty_email, valid_password

def test_get_api_key_for_empty_email_user(email=empty_email, password=valid_password):
    """ Проверяем, что запрос упадёт из-за пустого email"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

# Четвертый негативный тест

from settings import valid_email, empty_password

def test_get_api_key_for_empty_password_user(email=valid_email, password=empty_password):
    """ Проверяем, что запрос упадёт из-за пустого пароля"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

# Пятый негативный тест

def test_get_all_pets_with_nonvalid_email_key(filter=''):
    """ Проверяем, что запрос упадёт из-за невалидного email."""

    _, auth_key = pf.get_api_key(nonvalid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

# Шестой негативный тест

def test_add_new_pet_with_negative_age_data(name='Барбоскин', animal_type='двортерьер',
                                     age='-4', pet_photo='images/cat1.jpg'):
    """Проверяем, что нельзя добавить питомца с отрицательным возрастом"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

# Седьмой негативный тест

def test_add_new_pet_with_empty_animal_type_data(name='Барбоскин', animal_type=' ',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем, что нельзя добавить питомца без типа животного"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

# Восьмой негативный тест

def test_add_new_pet_with_empty_name_data(name=' ', animal_type='кошка',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем, что нельзя добавить питомца без имени животного"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

# Девятый негативный тест

def test_successful_delete_self_pet_nonvalid_password():
    """Проверяем возможность удаления питомца с невалидным паролем пользователя"""

    _, auth_key = pf.get_api_key(valid_email, nonvalid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

# Десятый негативный тест

def test_successful_delete_self_pet_nonvalid_email():
    """Проверяем возможность удаления питомца с невалидным email пользователя"""

    _, auth_key = pf.get_api_key(nonvalid_email, valid_email)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()
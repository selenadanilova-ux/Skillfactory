import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()

# 1. Присутствуют все питомцы.

def test_all_pets_are_present(driver):
    driver.find_element(By.ID, 'email').send_keys('selenadan@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('l;fp2025')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

    stats = driver.find_element(By.XPATH, '//div[contains(@class, ".col-sm-4")]').text
    expected_count = int(stats.split('Питомцев:')[1].split()[0])

    pets = driver.find_elements(By.CSS_SELECTOR, '.table-hover tbody tr')
    actual_count = len(pets)

    assert actual_count == expected_count

# 2. Хотя бы у половины питомцев есть фото.

def test_half_pets_have_photos(driver):
    driver.find_element(By.ID, 'email').send_keys('selenadan@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('l;fp2025')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

    images = driver.find_elements(By.CSS_SELECTOR, '.table-hover img')

    num_photos = 0
    for img in images:
        if img.get_attribute('src') != '':
            num_photos += 1

    all_pets = driver.find_elements(By.CSS_SELECTOR, '.table-hover tbody tr')
    total_pets = len(all_pets)

    assert num_photos >= total_pets / 2

# 3. У всех питомцев есть имя, возраст и порода.

def test_all_pets_have_details(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'email'))).send_keys('selenadan@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('l;fp2025')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Мои питомцы"))).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table-hover tbody tr")))

    rows = driver.find_elements(By.CSS_SELECTOR, '.table-hover tbody tr')

    for i in range(len(rows)):
        cells = rows[i].find_elements(By.TAG_NAME, 'td')
        assert cells[1].text != ''
        assert cells[2].text != ''
        assert cells[3].text != ''
        assert len(cells[1].text) > 0
        assert len(cells[2].text) > 0
        assert len(cells[3].text) > 0

# 4. У всех питомцев разные имена.

def test_all_pets_have_different_names(driver):
    driver.find_element(By.ID, 'email').send_keys('selenadan@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('l;fp2025')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

    rows = driver.find_elements(By.CSS_SELECTOR, '.table-hover tbody tr')

    pet_names = []

    for i in range(len(rows)):
        cells = rows[i].find_elements(By.TAG_NAME, 'td')
        name = cells[1].text
        pet_names.append(name)

    assert len(pet_names) == len(set(pet_names))

# 5. В списке нет повторяющихся питомцев.

def test_no_duplicate_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('selenadan@mail.ru')
    driver.find_element(By.ID, 'pass').send_keys('l;fp2025')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

    rows = driver.find_elements(By.CSS_SELECTOR, '.table-hover tbody tr')

    list_all_pets = []

    for i in range(len(rows)):
        cells = rows[i].find_elements(By.TAG_NAME, 'td')
        pet_data = f"{cells[1].text} {cells[2].text} {cells[3].text}"
        list_all_pets.append(pet_data)

    assert len(list_all_pets) == len(set(list_all_pets))



import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('open_webpage')
class TestHomepage:

    def test_link_our_post(self):
        """
        Тест проверяет работоспособность ссылки "Наши отделения" на главной странице
        """
        button_our_post = '//*[@id="item-map-send"]/a'
        map_title_text = "//*[contains(text(), 'Найти отделение')]"
        correct_map_title = "Найти отделение"
        correct_url = 'https://boxberry.ru/find_an_office'
        # Кликаем на кнопку "Наши отделения"
        our_post = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_our_post))
        )
        our_post.click()
        current_url = self.driver.current_url
        # Сравниваем текущий урл с эталонным
        assert current_url == correct_url
        # Находим заголовок над картой
        map_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, map_title_text))
        )
        # Получаем текст заголовка над картой
        map_title = map_title.get_attribute("innerText")
        # Сравниваем полученный текст заголовка с эталонным
        assert map_title == correct_map_title

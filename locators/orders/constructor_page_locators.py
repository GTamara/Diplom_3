from selenium.webdriver.common.by import By


class ConstructorPageLocators:

    PAGE_HEADING = By.XPATH, '//h1[text()="Соберите бургер"]'
    # LOGIN_LINK = By.XPATH, '//a[@href="/login"]'

    BURGER_INGREDIENT = By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]'
    BURGER_INGREDIENTS_SECTION = By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]'


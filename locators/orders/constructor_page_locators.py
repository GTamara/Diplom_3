from selenium.webdriver.common.by import By


class ConstructorPageLocators:

    PAGE_HEADING = By.XPATH, '//h1[text()="Соберите бургер"]'

    BURGER_INGREDIENT = By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]'
    BURGER_INGREDIENT_IMAGE = By.XPATH, BURGER_INGREDIENT[1] + '/img'

    SPECIFIED_INGREDIENT_SECTION = By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]'
    INDEXED_CATEGORY_SECTION = By.XPATH, '//ul[contains(@class, "BurgerIngredients_ingredients__list")][{}]'

    SPECIFIED_CATEGORY_INGREDIENT_ITEM = \
        By.XPATH, INDEXED_CATEGORY_SECTION[1] + '//a[contains(@class, "BurgerIngredient_ingredient_")]'
    SPECIFIED_CATEGORY_INDEXED_INGREDIENT_ITEM = \
        By.XPATH, INDEXED_CATEGORY_SECTION[1] + '//a[contains(@class, "BurgerIngredient_ingredient_")][{}]'

    SPECIFIED_CATEGORY_INDEXED_INGREDIENT_ITEM_TITLE = \
        By.XPATH, SPECIFIED_CATEGORY_INDEXED_INGREDIENT_ITEM[1] + '/p[contains(@class, "BurgerIngredient_ingredient__text_")]'

    INGREDIENT_ITEM = By.XPATH, SPECIFIED_INGREDIENT_SECTION[1] + '//a[contains(@class, "BurgerIngredient_ingredient_")]'
    INDEXED_INGREDIENT_ITEM = By.XPATH, INGREDIENT_ITEM[1] + '[{}]'

    POPUP = By.XPATH, '//section[contains(@class, "Modal_modal_opened_")]'
    INGREDIENT_TITLE_WITHIN_POPUP = By.XPATH, POPUP[1] + '//p[contains(@class, "text_type_main")]'
    POPUP_CLOSE_BTN = By.XPATH, POPUP[1] + '//button[contains(@class, "_modal__close_")]'

    BURGER_CONSTRUCTOR_BUCKET = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket_")]'

    INDEXED_INGREDIENT_COUNTER = \
        By.XPATH, SPECIFIED_CATEGORY_INDEXED_INGREDIENT_ITEM[1] + '/div/p[contains(@class, "counter_counter__num_")]'

    CREATE_ORDER_BUTTON = By.XPATH, '//button[contains(text(), "Оформить заказ")]'

    NEW_ORDER_POPUP_ORDER_NUMBER = By.XPATH, POPUP[1] + '//h2[contains(@class, "ext_type_digits")]'
    NEW_ORDER_POPUP_ORDER_TITLE = By.XPATH, POPUP[1] + '//p[contains(text(), "идентификатор заказа")]'

    BURGER_INGREDIENTS_SECTION = By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]'


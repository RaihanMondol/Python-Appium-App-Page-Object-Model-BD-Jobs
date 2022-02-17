from selenium.webdriver.common.by import By


class LoginLocators():
    first_next_buton_id = (By.ID, 'com.bdjobs.app:id/btn_next')
    allow_button_id = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    signin_icon_id = (By.ID, 'com.bdjobs.app:id/profileIMGV')
    enter_username_textbox_id = (By.ID, 'com.bdjobs.app:id/usernameTIET')
    arrow_button_id = (By.ID, 'com.bdjobs.app:id/nextButtonFAB')
    enter_password_textbox_id = (By.ID, 'com.bdjobs.app:id/passwordTIET')
    click_fb_button_id = (By.ID, 'com.bdjobs.app:id/facebookLoginIMGV')
    accept_and_continue_button_id = (By.ID, 'com.android.chrome:id/terms_accept')
    no_thanks_button_id = (By.ID, 'com.android.chrome:id/negative_button')


class SearchJobLocators():
    search_button_id = (By.ID, 'com.bdjobs.app:id/searchIMGV')
    keyword_textbox_id = (By.ID, 'com.bdjobs.app:id/keywordET')
    general_category_id = (By.ID, 'com.bdjobs.app:id/generalCatET')
    experience_button_id = (By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.CompoundButton[1]')
    final_search_icon_id = (By.ID, 'com.bdjobs.app:id/searchBTN_fab')


class NavigationBarLocators():
    hotjobs_button_id = (By.ID, 'com.bdjobs.app:id/navigation_hotjobs')
    shortlisted_button_id = (By.ID, 'com.bdjobs.app:id/navigation_shortlisted_jobs')
    myBdjobs_button_id = (By.ID, 'com.bdjobs.app:id/navigation_mybdjobs')
    more_button_id = (By.ID, 'com.bdjobs.app:id/navigation_more')

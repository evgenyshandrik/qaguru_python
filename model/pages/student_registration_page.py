"""
Page object
"""
from selene import have, command
from selene.core.entity import Element
from selene.support.shared.jquery_style import s

from model.controls.contorls import Dropdown, Table, TagsInput, DatePicker
from util.resources import path


class StudentRegistrationForm(object):
    """
    Student registration form on page
    """

    def set_name(self, first_name: str, last_name: str):
        s('#firstName').type(first_name)
        s('#lastName').type(last_name)
        return self

    def set_email(self, value: str):
        s('#userEmail').type(value)
        return self

    def set_sex(self, value: str):
        gender_types = s('#genterWrapper')
        gender_types.all('.custom-radio').element_by(have.exact_text(value)).click()
        return self

    def set_phone_number(self, value: int):
        mobile_phone = '#userNumber'
        s(mobile_phone).type(value)
        return self

    def set_date_of_birthday(self, value: str):
        date_picker = DatePicker(s('#dateOfBirthInput'))
        date_picker.set_date(value)
        return self

    def set_subject(self, values):
        subjects = TagsInput(s('#subjectsInput'))
        for item in values:
            subjects.add(item)
        return self

    def set_hobby(self, values):
        hobbies_types = s('#hobbiesWrapper')
        for item in values:
            hobbies_types.all('.custom-checkbox').element_by(have.exact_text(item)).click()
        return self

    def set_avatar(self, path_value: str):
        s('#uploadPicture').send_keys(path(f'{path_value}'))
        return self

    def set_address(self, value: str):
        s('#currentAddress').type(value)
        return self

    def set_state(self, value: str):
        state_element = Dropdown(s('#state'))
        state_element.select(option=value)
        return self

    def set_city(self, value: str):
        city_element = Dropdown(s('#city'))
        city_element.autocomplete(option=value)
        return self

    @staticmethod
    def submit_form():
        s('#submit').perform(command.js.click)


class ModalResultingForm(object):
    """
    Modal resulting form on page
    """

    def __init__(self):
        self.result_table = Table(s('.modal-content .table'))

    def get_cells_by_index(self, index: int, label: str, expected_result: str):
        return self.result_table.cells_of_row(index).should(have.exact_texts(label, expected_result))
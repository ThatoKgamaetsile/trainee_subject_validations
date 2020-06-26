from django.test import TestCase
from edc_constants.constants import YES, NO
from ..form_validators import EducationQuestionnaireFormValidation
from django.core.exceptions import ValidationError


class TestEducationQuestionnaireForm(TestCase):

    def test_what_type_of_work_currently_working_required(self):
        '''ValidationError raised if not a citizen and not
        married to a citizen of botswana
        '''
        cleaned_data = {
            "currently_working": YES,
            "what_type_of_work": NO,
            }
        form_validator = EducationQuestionnaireFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError Not a citizen and not '
                      f'married to a citizen of Botswana. Got{e}')





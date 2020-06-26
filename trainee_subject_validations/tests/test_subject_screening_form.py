from django.test import TestCase
from edc_constants.constants import YES, NO
from ..form_validators import SubjectScreeningFormValidation
from django.core.exceptions import ValidationError


class TestSubjectScreeningForm(TestCase):

    def test_citizen_or_not_no(self):
        '''ValidationError raised if not a citizen and not
        married to a citizen of botswana
        '''
        cleaned_data = {
            "citizen_or_not": NO,
            "married_to_motswana": NO,
            }
        form_validator = SubjectScreeningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError Not a citizen and not '
                      f'married to a citizen of Botswana. Got{e}')
#            self.assertRaises(ValidationError, form_validator.validate)
#            self.assertIn('married_to_motswana', form_validator._errors)

    def test_marriage_certificate_proof_no(self):
        '''ValidationError raised if participant failed to
        produce marriage certificate proof
        '''
        cleaned_data = {
            "married_to_motswana": YES,
            "marriage_certificate_proof": NO,
            }
        form_validator = SubjectScreeningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError Participant cannot proceed without '
                      f'providing local marriage certificate proof. Got{e}')

    def test_marriage_certificate_proof_no_error(self):
        '''ValidationError raised if participant failed to
        produce marriage certificate proof
        '''
        cleaned_data = {
            "married_to_motswana": YES,
            "marriage_certificate_proof": YES,
            }
        form_validator = SubjectScreeningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_literate_or_illiterate(self):
        '''Assert raises if the person is illiterate
        and has no literate witness
        '''
        cleaned_data = {
            "literate_or_illiterate": NO,
            "literate_witness": NO,
            }
        form_validator = SubjectScreeningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError an illiterate person cant go on '
                      f'without a literate witness. Got{e}')

    def test_literate_or_illiterate_no_error(self):
        '''True if participant is literate
        '''
        cleaned_data = {
            "literate_or_illiterate": NO,
            "literate_witness": YES,
            }
        form_validator = SubjectScreeningFormValidation(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')



